var str = '';
resultadoMostrado = false;
const tela = document.getElementById("tela");

$(".opas").on("click", function() {
    str += this.id;
    tela.append(str.slice(-1));
});

$(".operacoes").on("click", function() {
    operacoes = ["+", "-", "*", "/", "%"];
    if (operacoes.includes(tela.textContent.slice(-1))){
        alert("nao pode");
    } else {
        str += this.id;
        tela.append(str.slice(-1));
    }
});

$("#igual").on("click", function() {
    if (!isNaN(tela.textContent.slice(-1))){

        $.ajax({
            url: `http://localhost:5000/conta/${str}`,
            method: "GET",
            error: function(resp){
                alert(resp.resultado);
            },
            success: function(resp){
                tela.append(resp.detalhes);
                console.log(resp)
            }
        });

        tela.innerHTML = "";
        str = '';
    } else {
        alert("nao pode");
    }
});

$("#limpar").on("click", function() {
    str = '';
    tela.innerHTML = "";
});