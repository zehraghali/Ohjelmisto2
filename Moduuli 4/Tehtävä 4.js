const imageSrc = tvShow.image ? tvShow.image.medium : "https://via.placeholder.com/210x295?text=Not%20Found";
const imageElement = document.createElement("img");
imageElement.src = imageSrc;
imageElement.alt = tvShow.name;
articleElement.appendChild(imageElement);
