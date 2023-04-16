const form = document.querySelector('#search-form');
const searchInput = document.querySelector('#search-input');
const resultsDiv = document.querySelector('#results');

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  const searchTerm = searchInput.value;
  const url = `https://api.tvmaze.com/search/shows?q=${searchTerm}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    resultsDiv.innerHTML = '';
    data.forEach(function(result) {
      const title = result.show.name;
      const url = result.show.url;
      const image = result.show.image?.medium;
      const summary = result.show.summary;
      const article = document.createElement('article');
      const titleEl = document.createElement('h2');
      const urlEl = document.createElement('a');
      const imgEl = document.createElement('img');
      const summaryEl = document.createElement('div');
      titleEl.textContent = title;
      urlEl.textContent = 'Details';
      urlEl.href = url;
      urlEl.target = '_blank';
      if (image) {
        imgEl.src = image;
        imgEl.alt = title;
      } else {
        imgEl.alt = 'No Image Available';
      }
      summaryEl.innerHTML = summary;
      article.appendChild(titleEl);
      article.appendChild(urlEl);
      article.appendChild(imgEl);
      article.appendChild(summaryEl);
      resultsDiv.appendChild(article);
    });
  } catch (error) {
    console.error(error);
  }
});
