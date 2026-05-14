/*3. Escreva uma função JavaScript chamada adicionarProduto que recebe o nome e o preco de
um produto e adiciona um novo <li> à lista #lista-produtos no formato: "NomeDoProduto
- R$ 99.90". Use createElement, textContent e appendChild.*/


const lista = document.querySelector("#lista-produtos");

function adicionarProduto(nome, preco) {
    const item = document.createElement('li');

    item.textContent = `${nome} - R$ ${preco.toFixed(2)}`;

    lista.appendChild(item);
}

adicionarProduto("Cadeira", 45.9);