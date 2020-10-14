async function UserButton() {
    const userState = false;
    const userOnlineState = ` <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    !imagen! Pts 0 
    </a>
    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
    <a class="dropdown-item" onClick="openHtml('./views/profile.html','homes')" href="#">Perfil</a>
    <a class="dropdown-item" href="#">Configuracion</a>
    <a class="dropdown-item" href="#">Salir</a>
    </div>
    </li>`;
 
    const userOfflineState = `
    <a class="btn btn-outline-warning "  id='loginBtn'href='#' onclick="openHtml( ${urlLogin} ,'homes')" role="button">Iniciar Sesión</a>
    `;
   const view = document.querySelectorAll('.userview');
    view.forEach(view =>
    !userState ? view.style = 'display : none':view.style = 'display : block'
    );


    document.querySelector('div#navbarNavDropdown > ul').innerHTML += userState
    ? userOnlineState
    :userOfflineState ;
    
}

const navLi = () => {
    const navLi = document.querySelectorAll('nav li a');
    navLi.forEach((li) =>
    li.addEventListener('click', function (e) {
        navLi.forEach((x) => (x.className = 'nav-link'));
        document.querySelector(`nav li a[name="${e.target.name}"]`).className =
        'nav-link active';
    })
    );
};
//// si el collapser se abre, entonces el objecto [buscar] se alinia con un 'auto margin', para que tenga coherencia con los demas botones
const collapserFix = () => {
    let xe = document.querySelector('.show');
    /// xe ve el estado de collaparse, si esta clickeado
    
    if (!xe) {
        document.querySelector('#searchBtn').className = 'input-group m-auto';
    } else {
        console.log('fixer', xe);
        
        document.querySelector('#searchBtn').className = 'input-group';
    }
};

window.addEventListener('load', () => {
    document.querySelector(`nav li a[name="home"]`).className = 'nav-link active';
    UserButton();
    navLi();
});
