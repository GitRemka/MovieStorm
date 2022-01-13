function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.content__wrap_content');
    div.innerHTML = output;
}

let html = '\
{{#movies}}\
    <div class="wrap__item">\
        <div class="movie_item item{{ id }}">\
            <img src="media/{{ poster }}" alt="Карточка" class="img_item">\
            <p class="card_description" align="center">\
                <span class="movie_card_header title">\
                    {{ title }}\
                    <i class="raiting_sub">\
                        {{ restriction }}\
                    </i>\
                </span>\
                <span class="movie_card_genre">\
                    {{ genres }}\
                </span>\
            </p>\
           <button class="card_btn">\
                <span class="card_btn__label">Подробности</span>\
            </button>\
        </div>\
    </div>\
{{/movies}}'