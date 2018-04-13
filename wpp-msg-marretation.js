/************** Usei esse código via Console do DevTools, no Chrome *******************/

// Seleciona as mensagens carregadas
var messageContainers = document.getElementsByClassName('vW7d1');
// Pega a primeira da lista e sobe até o elemento que contém o scroll e o joga pra zero
// Esse monte de parent aí é porque eu estava testando pra ver qual era o elemento...
console.log(messageContainers[0].parentElement.parentElement.scrollTop) = 0;


/************** ...esse também, mas quando já tinha chegado no topo das minhas mensagens *******************/
var spanElements = document.getElementsByTagName("span");
var messageArray = [];
var linkedInArray = []

// Filtra as spans com uma determinada classe
for (var i=0; i<spanElements.length; ++i) {
    if (spanElements[i].className === 'selectable-text invisible-space copyable-text') {
		messageArray.push(spanElements[i]);
	}
}
// Filtra os resultados anteriores pelo conteúdo da mensagem
for (var i=0; i<messageArray.length; ++i) {
    if (messageArray[i].innerText.includes('www.linkedin.com')) {
		linkedInArray.push(messageArray[i]);
	}
}
// Imprime no console o que achou
for (var i=0; i<linkedInArray.length; ++i) {
	console.log(linkedInArray[i].innerText);
}