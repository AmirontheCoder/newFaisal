let dropdownMenu = document.getElementsByClassName("dropdown")
function dropdown2(){
    if(dropdownMenu[0].style.display == "block" ){
        dropdownMenu[0].style.display = "none"
    }else{
        dropdownMenu[0].style.display = "block"
    }
}


function dropdown3() {
    let accordionLinks = document.getElementById("question1");
    let dropdownMenu2 = document.getElementsByClassName("dropdown2");
      if (dropdownMenu2[0].style.display == "block") {
        dropdownMenu2[0].style.display = "none";
      } else {
        dropdownMenu2[0].style.display = "block";
      }
    }