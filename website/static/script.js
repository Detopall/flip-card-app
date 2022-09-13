"use strict";

document.addEventListener("DOMContentLoaded", init);

function init(){
	document.addEventListener("click", turnCard);
}

function turnCard(e){
	if (!e.target.closest("article")) return;
	const article = e.target.closest("article");
	if (article.classList.contains("turn-to-back")){
		showBack(article);
	} else {
		showFront(article);
	}
}

function showBack(article){
	const frontText = article.querySelector("p").innerHTML;
	const backText = article.getAttribute("data-back");
	let html = `
	<h2> ${frontText} </h2>
	<p> ${backText} </p>
	`;
	article.innerHTML = "";
	article.insertAdjacentHTML("beforeend", html);
	article.classList.remove("turn-to-back");
	article.classList.add("turn-to-front");
}

function showFront(article){
	const frontText = article.querySelector("h2").innerHTML;
	const descriptionText = article.getAttribute("data-description");
	let html = `
	<h2> ${descriptionText} </h2>
	<p> ${frontText} </p>
	`;
	article.innerHTML = "";
	article.insertAdjacentHTML("beforeend", html);
	article.classList.add("turn-to-back");
	article.classList.remove("turn-to-front");
}