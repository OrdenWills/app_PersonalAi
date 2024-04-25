const bg_btn = document.getElementById('theme-toggle-btn');


const body = document.body;
// console.log('doc body',body)

bg_btn.addEventListener('click', () => {
    body.classList.toggle('light');

    const currentText = bg_btn.querySelector('.chat_text__TkPfN').textContent;
    const newText = currentText === 'Dark Theme' ? 'Light Theme' : 'Dark Theme';
    bg_btn.querySelector('.chat_text__TkPfN').textContent = newText;
})


// resize the screen 

const home_resize_btn = document.getElementById('home_cont_btn');
const home_screen = document.getElementById('home_cont')

// console.log(home_screen)
home_resize_btn.addEventListener('click', () => {
    home_screen.classList.toggle('home_tight-container__ztaM7')
})

// chat settings

const chat_setting_btn = document.getElementById('')
