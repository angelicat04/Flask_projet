// Liste déroulante
document.addEventListener('DOMContentLoaded', function () {
    const domaineItems = document.querySelectorAll('.domaine-item');
  
    domaineItems.forEach(function (item) {
      item.addEventListener('click', function () {
        const subList = this.nextElementSibling;
        subList.classList.toggle('active');
      });
    });
  });
  
//Caroussel des actualités
document.getElementById('arrowLeft').addEventListener('click', function() {
    document.querySelector('.content').scrollLeft -= 200;
});

document.getElementById('arrowRight').addEventListener('click', function() {
    document.querySelector('.content').scrollLeft += 200;
});
