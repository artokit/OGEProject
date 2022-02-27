'use strict';
function clickRadio(elem) {
    let active = document.getElementsByClassName('radio_active')[0];
    let slider = document.getElementsByClassName('slider')[0];
    active.className = '';
    elem.className = 'radio_active';
    for (let i = 0; i < 5; i++) {
        if (document.getElementsByName('select')[i].className === 'radio_active') {
            slider.style.transition = '.3s';
            slider.style.transform = `translateX(-${300*i}px)`;
        }
    }
}