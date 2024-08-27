const btn = document.getElementById("btn");
const main1 = document.getElementById("main1")
const main2 = document.getElementById("main2")

btn.addEventListener("click",function(){
    main1.style.display = "none";
    main2.style.display = "block"

})