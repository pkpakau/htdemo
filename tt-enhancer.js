// ==UserScript==
// @name         tt-enhancer.js
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       khuparag@
// @match        http*://tt*.amazon.com*
// @include     http*://tt*.amazon.com*
// @grant        none
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==

var boost = "https://myday-website.bom.aws-border.com/";
var mobility = "https://mobility.amazon.com/";
var shiftReport = "https://bom-shift-report.corp.amazon.com/report";
    var boostBox = "<div style=\"text-align:center;margin-top: 10px\"><button type=\"button\" id=\"boost\" style=\"margin-right:5px\"><b>Boost</b></button><button type=\"button\" id=\"mobility\" style=\"margin-right:5px\"><b>Mobility</b></button> <button type=\"button\" id=\"shift-report\" style=\"margin-right:5px\"><b>Shift Report</b></button> </div> ";
    $(boostBox).insertBefore("#content");
    $("#boost").on("click",function(){
        window.open(boost);
    });
    $("#mobility").on("click",function(){
        window.open(mobility);
    });
$("#shift-report").on("click",function(){
        window.open(shiftReport);
    });

$(document).ready(function() {
var a = $("#context_bar > table > tbody > tr  td:first-child");
    var ticketNumber = a[0].baseURI.slice(22, );
    var mydayLink = a[0].baseURI= "https://myday-website.bom.aws-border.com/ticket/" + ticketNumber;
    $(a).on('click',a ,function() {
    //window.location.replace(mydayLink);
        window.location.href = mydayLink;
    });
});

var b = $("details_only").context.childNodes[0].nextSibling.innerText;
var assetId = b.slice(b.search("asset_id =")+10,b.search("asset_id =")+21);

if( $("#details_readonly > h2")[0].firstChild.data.search("CONSOLE") != -1)
{
    var dunkel = "https://tavern.corp.amazon.com/dunkel?host_id=" + assetId +"&con_ip=";
    var dunkelBox = "<button type=\"button\" id=\"dunkel\" style=\"margin-right:5px\"><b>Dunkel</b></button>  ";
    $(dunkelBox).insertBefore("#details_readonly");
    $("#dunkel").on("click",function(){
        window.open(dunkel);
    });
}

var ipa = "https://tavern.corp.amazon.com/ipa?host_id=" + assetId;
    var ipaBox = "<button type=\"button\" id=\"ipa\" style=\"margin-right:5px\"><b>IPA</b></button>  ";
    $(ipaBox).insertBefore("#details_readonly");
    $("#ipa").on("click",function(){
        window.open(ipa);
    });

var quad = "https://tavern.corp.amazon.com/quad?host_id=" + assetId;
    var quadBox = "<button type=\"button\" id=\"quad\" style=\"margin-right:5px\"><b>Quad</b></button>  ";
    $(quadBox).insertBefore("#details_readonly");
    $("#quad").on("click",function(){
        window.open(quad);
    });
