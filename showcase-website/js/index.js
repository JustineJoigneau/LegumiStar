var artistsData = [
    { id: 0, name: "Clémentine", edition: 2036, srcImage: "./img/apple-without-bg.png" },
    { id: 1, name: "Céline Dion", edition: 2035, srcImage: "./img/lemon-without-bg.png" },
    { id: 2, name: "Patrick Otato", edition: 2034, srcImage: "./img/potato-without-bg.png" },
    { id: 3, name: "Clément", edition: 2033, srcImage: "./img/sweet-potato-without-bg.png" },
    { id: 4, name: "Charline", edition: 2032, srcImage: "./img/zucchini-without-bg.png" },
    { id: 5, name: "Zoé", edition: 2031, srcImage: "./img/banana-without-bg.png" },
];

var opinionsData = [
    { id: 0, name: "M., fan de Patrick Otato" }
];

function buildCardsInCarousel() {
    var carouselInner = document.getElementById('carousel-homepage-inner');

    artistsData.forEach(function (artist, index) {
        var carouselItem = document.createElement('div');
        carouselItem.className = 'carousel-item' + (artist.id === 0 ? ' active' : '');

        var img = document.createElement('img');
        img.className = 'd-block';
        img.alt = artist.name;
        img.src = artist.srcImage;

        var captionBackground = document.createElement('div');
        captionBackground.className = 'carousel-caption-background d-none d-md-block';

        var caption = document.createElement('div');
        caption.className = 'carousel-caption d-none d-md-block';
        caption.innerHTML = '<h3>' + artist.name + '</h3>Gagnante de l\'édition ' + artist.edition;

        carouselItem.appendChild(img);
        carouselItem.appendChild(captionBackground);
        carouselItem.appendChild(caption);

        carouselInner.appendChild(carouselItem);
    });
}

function buildIndicatorsCarousel() {
    var carouselIndicators = document.getElementById('carousel-indicators-container');
    artistsData.forEach(function (artist, index) {
        var indicatorButton = document.createElement('button');
        indicatorButton.type = 'button';
        indicatorButton.setAttribute('data-bs-target', '#carousel-sample');
        indicatorButton.setAttribute('data-bs-slide-to', index.toString());
        indicatorButton.className = artist.id === 0 ? 'active' : '';
        carouselIndicators.appendChild(indicatorButton);
    });
}

function buildIndexJs() {
    buildCardsInCarousel();
    buildIndicatorsCarousel();
}

document.addEventListener('DOMContentLoaded', buildIndexJs);
