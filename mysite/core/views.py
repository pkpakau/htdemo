from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from mysite.core.forms import SignUpForm,ProfileForm
from mysite.core.tokens import account_activation_token


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
@permission_required('is_superuser')
def admin(request):
    users=User.objects.all()
    return render(request,'admin.html',{'users':users})

    
def signup(request):
    if request.method == 'POST':
        signupform=SignUpForm(request.POST)
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user = signupform.save(commit=False)
            user.is_active = False
            user.save()
            user.refresh_from_db()
            user.profile.dob=form.cleaned_data.get('dob')
            user.profile.gender=form.cleaned_data.get('gender')
            user.profile.mobile=form.cleaned_data.get('mobile')
            user.profile.aadhar_no=form.cleaned_data.get('aadhar_no')
            user.profile.acertificate=form.cleaned_data.get('acertificate')
            user.profile.address=form.cleaned_data.get('address')
            user.profile.bcertificate=form.cleaned_data.get('bcertificate')
            user.profile.experience=form.cleaned_data.get('experience')
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        signupform = SignUpForm()
        form=ProfileForm
    return render(request, 'signup.html', {'form': signupform,'profile_form':form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
