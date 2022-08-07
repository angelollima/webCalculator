var str = '';
const tela = document.getElementById("tela");

$(".opas").on("click", function() {
    str += this.id;
    tela.append(str.slice(-1));
});

$(".operacoes").on("click", function() {
    operacoes = ["+", "-", "*", "/", "%"];
    if (operacoes.includes(tela.textContent.slice(-1))){
        alert("burro");
    } else {
        str += this.id;
        tela.append(str.slice(-1));
    }
});

$("#igual").on("click", function() {
    if (!isNaN(tela.textContent.slice(-1))){
        $.ajax({
            method: "POST",
            url: "http://localhost:5000/conta/" + str
        });
        tela.innerHTML = "";
        str = '';
    } else {
        alert("burro");
    }
});

$("#limpar").on("click", function() {
    str = '';
    tela.innerHTML = "";
});

$.ajax({
    method: "POST",
    url: "http://localhost:5000/" + str
});