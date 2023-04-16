const form = document.querySelector("form");
const searchTermInput = document.querySelector("#search-term");
const resultsDiv = document.querySelector("#results");

form.addEventListener("submit", event => {
  event.preventDefault();
  const searchTerm = searchTermInput.value;
  const apiUrl = `https://api.chucknorris.io/jokes/search?query=${searchTerm}`;

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      resultsDiv.innerHTML = "";
      data.result.forEach(joke => {
        const article = document.createElement("article");
        const p = document.createElement("p");
        p.innerText = joke.value;
        article.appendChild(p);
        resultsDiv.appendChild(article);
      });
    })
    .catch(error => console.error(error));
});
