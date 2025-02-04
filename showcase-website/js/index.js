var dataIndexPage = {
    artists: [
        { id: 0, name: "Clémentine", edition: "18 janvier 2036", srcImage: "./img/apple-without-bg.png" },
        { id: 1, name: "Céline Dion", edition: "15 janvier 2036", srcImage: "./img/lemon-without-bg.png" },
        { id: 2, name: "Patrick Otato", edition: "16 janvier 2036", srcImage: "./img/potato-without-bg.png" },
        { id: 3, name: "Clément", edition: "14 janvier 2036", srcImage: "./img/sweet-potato-without-bg.png" },
        { id: 4, name: "Charline", edition: "17 janvier 2036", srcImage: "./img/zucchini-without-bg.png" },
        { id: 5, name: "Zoé", edition: "12 janvier 2036", srcImage: "./img/banana-without-bg.png" },
    ],
    stars: [
        { id: 0, src: "./icon/star-solid.svg", alt: "star-full" },
        { id: 1, src: "./icon/star-half-stroke-regular.svg", alt: "star-mid" },
        { id: 2, src: "./icon/star-regular.svg", alt: "star-empty" },
    ],
    opinions: [
        {
            id: 0,
            name: "M., fan de Patrick Otato",
            comment: "g pa pu voire la cène... Tro naze...",
            fullStar: 2, midStar: 0, emptyStar: 3,
        },
        {
            id: 1,
            name: "T., rageux",
            comment: "Moz'Poire est mort pour cela ! L'original se retourne dans sa tombe... >-(",
            fullStar: 1, midStar: 0, emptyStar: 4,
        },
        {
            id: 2,
            name: "H.",
            comment: "Franchement, étant sourde, je n'ai pas tout compris, mais en tout cas il y avait une super ambiance! A bon entendeur, Michelle du Nord-Pas-de-Calais",
            fullStar: 4, midStar: 0, emptyStar: 1,
        },
        {
            id: 3,
            name: "Anonyme",
            comment: "A méditez.",
            fullStar: 2, midStar: 1, emptyStar: 2,
        },
        {
            id: 4,
            name: "B., hyper-méga-fan de Jean-Michel Poire",
            comment: "mOI J4AI TROP AIM2 MERCI A TOUS !!",
            fullStar: 5, midStar: 0, emptyStar: 0,
        },
    ],
};


function buildCardsInCarousel() {
    var carouselInner = document.getElementById('carousel-homepage-inner');

    dataIndexPage.artists.forEach(function (artist, index) {
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
        caption.innerHTML = '<h3>' + artist.name + '</h3>Gagnante de l\'édition du ' + artist.edition;

        carouselItem.appendChild(img);
        carouselItem.appendChild(captionBackground);
        carouselItem.appendChild(caption);

        carouselInner.appendChild(carouselItem);
    });
}

function buildIndicatorsCarousel() {
    var carouselIndicators = document.getElementById('carousel-indicators-container');
    dataIndexPage.artists.forEach(function (artist, index) {
        var indicatorButton = document.createElement('button');
        indicatorButton.type = 'button';
        indicatorButton.setAttribute('data-bs-target', '#carousel-sample');
        indicatorButton.setAttribute('data-bs-slide-to', index.toString());
        indicatorButton.className = artist.id === 0 ? 'active' : '';
        carouselIndicators.appendChild(indicatorButton);
    });
}

function buildOpinionCards() {
    var opinionHomepageContainer = document.getElementById('opinion-homepage-container');
    dataIndexPage.opinions.forEach(function (opinion, index) {
        var cardItem = document.createElement('div');
        cardItem.className = 'card opinion-homepage-card';
        var cardBody = document.createElement('div');
        cardBody.className = 'card-body';
        var h3 = document.createElement('h3');
        h3.className = 'card-title';
        h3.textContent = opinion.name;
        var containerStars = document.createElement('div');
        for (let i = 0; i < opinion.fullStar; i++) {
            var img = document.createElement('img');
            img.src = dataIndexPage.stars[0].src;
            img.alt = dataIndexPage.stars[0].alt;
            containerStars.appendChild(img);
        }
        for (let i = 0; i < opinion.midStar; i++) {
            var img = document.createElement('img');
            img.src = dataIndexPage.stars[1].src;
            img.alt = dataIndexPage.stars[1].alt;
            containerStars.appendChild(img);
        }
        for (let i = 0; i < opinion.emptyStar; i++) {
            var img = document.createElement('img');
            img.src = dataIndexPage.stars[2].src;
            img.alt = dataIndexPage.stars[2].alt;
            containerStars.appendChild(img);
        }
        h3.appendChild(containerStars);
        var comment = document.createElement('p');
        comment.className = 'text-secondary';
        comment.textContent = opinion.comment;
        cardBody.appendChild(h3);
        cardBody.appendChild(comment);
        cardItem.appendChild(cardBody);
        opinionHomepageContainer.appendChild(cardItem);
    });
}

function buildIndexJs() {
    buildCardsInCarousel();
    buildIndicatorsCarousel();
    buildOpinionCards();
}

document.addEventListener('DOMContentLoaded', buildIndexJs);
