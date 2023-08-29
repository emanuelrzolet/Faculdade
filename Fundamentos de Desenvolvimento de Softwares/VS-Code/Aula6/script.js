let paragrafo = document.querySelector("#paragrafo1")

paragrafo.addEventListener("click",Mudaverde);

paragrafo.addEventListener("click",Mudavermelho);

function Mudaverde(){
    paragrafo.style.background="green"
}
function Mudavermelho(){
    paragrafo.style.background="red"
}