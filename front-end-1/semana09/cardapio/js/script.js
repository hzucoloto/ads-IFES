// Teste rápido: se esta frase aparecer no Console (F12), o script está conectado.
console.log("script.js carregado!");

// ============ 1. SELEÇÃO: pegar os elementos do DOM ============
// querySelector usa os mesmos seletores do CSS (#id, .classe, tag)
const corpo = document.body;
const btnTema = document.querySelector("#btn-tema");
const pratoDoDia = document.querySelector("#prato-do-dia");
const btnProximo = document.querySelector("#btn-proximo");
const btnPromos = document.querySelector("#btn-promos");

// querySelectorAll devolve uma LISTA (NodeList), não um elemento só
const promocoes = document.querySelectorAll(".promo");


// ============ 2. ESTADO: variáveis que guardam a situação atual ============
let escuro = false;                 // let: este valor vai mudar
const pratos = ["Moqueca capixaba", "Feijoada", "Torta capixaba"]; // const: a lista não é trocada
let indice = 0;                     // posição do prato mostrado agora


// ============ 3. FUNÇÕES que atualizam o DOM conforme o estado ============

// Modo noturno — mesmo padrão da lâmpada da apostila
function alternarTema() {
  escuro = !escuro;                 // inverte: false -> true -> false...
  corpo.classList.toggle("escuro"); // liga/desliga a classe (o visual está no CSS)

  if (escuro) {
    btnTema.textContent = "☀️ Modo claro";
  } else {
    btnTema.textContent = "🌙 Modo noturno";
  }
}

// Prato do dia — passa para o próximo item do array
function proximoPrato() {
  indice = indice + 1;

  // [complemento] pratos.length = quantidade de itens do array (aqui, 3).
  // Os índices vão de 0 a 2; ao chegar em 3, voltamos ao início.
  if (indice === pratos.length) {   // === compara valor E tipo
    indice = 0;
  }

  // Template literal (crase) para montar o texto com a variável dentro
  pratoDoDia.textContent = `${pratos[indice]}`;
  console.log(`Agora mostrando o prato ${indice}: ${pratos[indice]}`);
}

// Promoções — aplica a mudança em CADA item da lista
function destacarPromocoes() {
  // promocoes.classList.toggle(...) NÃO funcionaria: é uma lista, não um elemento.
  promocoes.forEach((item) => {
    item.classList.toggle("destaque");
  });
}


// ============ 4. EVENTOS: o clique dispara a função ============
// A apostila usa botao.onclick = funcao; addEventListener faz o mesmo
// e é o assunto da Semana 10 (e da Prática 9).
btnTema.addEventListener("click", alternarTema);
btnProximo.addEventListener("click", proximoPrato);
btnPromos.addEventListener("click", destacarPromocoes);
