function extend(){
    var accordionLinks = document.getElementById("question1");
    var ionIcon = document.getElementById("ao");

    if(accordionLinks.style.display == "block" ){
        accordionLinks.style.display = "none"
        ionIcon.style.transform = "rotate(0deg)";
    }else{
        accordionLinks.style.display = "block"
        ionIcon.style.transform = "rotate(135deg)";
    }

    
}

function extend1(){
    var accordionLinks = document.getElementById("question2");
    var ionIcon = document.getElementById("ao1");

    if(accordionLinks.style.display == "block" ){
        accordionLinks.style.display = "none"
        ionIcon.style.transform = "rotate(0deg)";
    }else{
        accordionLinks.style.display = "block"
        ionIcon.style.transform = "rotate(135deg)";
    }
}

function extend2(){
    var accordionLinks = document.getElementById("question3");
    var ionIcon = document.getElementById("ao2");

    if(accordionLinks.style.display == "block" ){
        accordionLinks.style.display = "none"
        ionIcon.style.transform = "rotate(0deg)";
    }else{
        accordionLinks.style.display = "block"
        ionIcon.style.transform = "rotate(135deg)";
    }
}

