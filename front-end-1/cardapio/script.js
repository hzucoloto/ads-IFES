// Guarda o elemento onde a resposta será exibida
const saida = document.querySelector('#saida');

// Faz uma requisição GET para "caminho" e mostra a resposta na tela
async function fazerPedido(caminho) {
  saida.textContent = `Enviando GET ${caminho}...`;

  try {
    const resposta = await fetch(caminho); // fetch faz GET por padrão
    const corpo = await resposta.text();   // lê o corpo da resposta como texto

    saida.textContent =
      `Status: ${resposta.status} ${resposta.statusText}\n` +
      `Content-Type: ${resposta.headers.get('Content-Type')}\n\n` +
      `Corpo:\n${corpo}`;
  } catch (erro) {
    // Cai aqui quando NÃO houve resposta HTTP nenhuma
    saida.textContent = `Falha na requisição: ${erro.message}`;
  }
}

// Liga cada botão a um pedido
document.querySelector('#btn-existe')
  .addEventListener('click', () => fazerPedido('pratos.json'));

document.querySelector('#btn-nao-existe')
  .addEventListener('click', () => fazerPedido('sobremesas.json'));