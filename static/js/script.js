var starter = document.querySelector("#timer-start");
var timecounter = document.getElementById("timecounter");
var currentindex = 0;
var score = 0;
var count;
let hours=3;
let startingminutes=60;
let time=60 * 180;
startingminutes--;
hours--;
var alert =document.getElementById("alert");
var info = document.getElementById("info");
// var addscore = document.getElementById("addscore");
// var submitresult = document.getElementById("submitresult");
startQuiz();

function startQuiz(){  
        setInterval(Starttimer,1000);
     setInterval(hou,360000);
     setInterval(sm,60000);
}
// Time set


function hou(){
    hours--;
}


function sm(){
    startingminutes--;
}

function hous(){
    hours--;
}


function sem(){
    startingminutes--;
}

function Starttimer(){
var starter = document.querySelector("#timer-start");
let seconds=time % 60;
    time--;
    if(startingminutes<=-1){
        startingminutes=59;
    }
    if(hours==0 && startingminutes==0 && seconds==1){
        starter.innerHTML="00hr:00m:00s";
        location.href("result.html");
    }
    var count=hours + "hrs:" + startingminutes + "m:" + seconds + "s";
    console.log(count);
    starter.innerHTML=hours + "hrs:" + startingminutes + "m:" + seconds + "s";
}



