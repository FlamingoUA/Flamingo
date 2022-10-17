let intervalid;

document.querySelectorAll('.dropdown__inner').forEach(e => {
    e.addEventListener('click', e => {
        const menu = e.currentTarget.dataset.path;
        document.querySelectorAll('.dropdown__content').forEach(e => {
            if(!document.querySelector(`[data-target=${menu}]`).classList.contains('open')) {
                e.classList.remove('dropdown-active')
                e.classList.remove('open');
                document.querySelector(`[data-target=${menu}]`).classList.add('dropdown-active');
                intervalId = setTimeout(() => {
                    document.querySelector(`[data-target=${menu}]`).classList.add('open');
                }, 0);
            }

            if(document.querySelector(`[data-target=${menu}]`).classList.contains('open')) {
                clearTimeout(intervalid);
                document.querySelector(`[data-target=${menu}]`).classList.remove('dropdown-active');
                intervalId = setTimeout(() => {
                    document.querySelector(`[data-target=${menu}]`).classList.remove('open');
                }, 0);
            }

            window.onclick = e => {
                if (e.target == document.querySelector(`[data-target=${menu}]`) || e.target == document.querySelector(`[data-path=${menu}]`)) {
                    return;
                } else {
                    document.querySelector(`[data-target=${menu}]`).classList.remove('dropdown-active');
                    document.querySelector(`[data-target=${menu}]`).classList.remove('open');
                }
            };

        });
    });
});






























//    const dropDown = document.querySelector('.dropdown'),
//    dropDownI = dropDown.querySelector('.dropdown__inner'),
//    dropDownC = dropDown.querySelector('.dropdown__content');
//
//    let countries = ['Києв', 'Єгипет'];
//
//    function addCountry() {
//        countries.forEach(country => {
//            let li = `<li onclick='updateName(this)' class="dropdown__item">${country}</li>`;
//            dropDownC.insertAdjacentHTML('beforeend', li);
//        });
//    };
//    addCountry();
//
//    function updateName(selectedLi) {
//        dropDown.classList.remove('active');
//        dropDownI.firstElementChild.innerText = selectedLi.innerText;
//    };
//
//    dropDownI.addEventListener('click', () => {
//        dropDown.classList.toggle('active');
//    });















