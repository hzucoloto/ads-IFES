// [complemento] JavaScript é conteúdo das semanas 9 e 10.
// O formulário funciona sem este arquivo: aqui é só um "extra" de experiência.

// Contador de caracteres da mensagem
const mensagem = document.querySelector('#mensagem');
const contador = document.querySelector('#contador');

// O evento "input" dispara a cada letra digitada ou apagada
mensagem.addEventListener('input', () => {
  contador.textContent = `${mensagem.value.length}/500`;
});
