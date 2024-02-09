const carousel = document.getElementById('carousel');

//logique pour charger les articles similaires depuis votre base de données

// contenu statique pour le carrousel
const similarArticles = [
  { title: 'Article 1', image: 'img.jpeg' },
  { title: 'Article 2', image: 'img.jpeg' },
  { title: 'Article 3', image: 'img.jpeg' },
  { title: 'Article 3', image: 'img.jpeg' },
];

similarArticles.forEach(article => {
  const articleElement = document.createElement('article');
  articleElement.innerHTML = `<img src="${article.image}" alt="${article.title}"><h4>${article.title}</h4>`;
  carousel.appendChild(articleElement);
});
