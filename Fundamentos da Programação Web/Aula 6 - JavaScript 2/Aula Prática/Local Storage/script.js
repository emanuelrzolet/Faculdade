function enviar() {
	//Capturar os campos de input
	const nomeField = document.getElementById("nome").value;
	const cidadeField = document.getElementById("cidade").value;
	//Salva as informações no local Storage
	localStorage.setItem("nome", nomeField);
	localStorage.setItem("cidade", cidadeField);
	//Redireciona o Usuário
	window.location.href = "visualizador.html";

}
