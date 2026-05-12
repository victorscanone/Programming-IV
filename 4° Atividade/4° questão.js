/*
4. Usando jQuery, escreva o código que:
• Aguarda a página carregar ($(document).ready)
• Ao clicar no botão #btn-detalhes, alterna a visibilidade do elemento #detalhes usando
.toggle()
• Ao clicar no botão #btn-limpar, remove o texto do elemento #mensagem usando .text("")
*/

$(document).ready(function() {
    $('#btn-detalhes').click(function() {
        $('#detalhes').toggle();
    });
    
    $('#btn-limpar').click(function() {
        $('#mensagem').text("");
    });
});