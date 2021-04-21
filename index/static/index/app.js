// Side nav
    const menu = document.getElementById("menu");
    const fullDisplayNav = document.querySelector(".full-display-nav");
    const cross = document.querySelector(".cross-mark");

    menu.addEventListener('click', (e) => {
        fullDisplayNav.style.width='100%';    
    });

    cross.addEventListener('click', (e) => {
        fullDisplayNav.style.width='0%';    
    });
// 