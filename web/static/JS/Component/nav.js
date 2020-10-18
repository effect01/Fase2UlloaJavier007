// async function UserButton() {
  
//    const view = document.querySelectorAll('.userview');
//     view.forEach(view =>
//     !userState ? view.style = 'display : none':view.style = 'display : block'
//     );

// }

// const navLi = () => {
//     const navLi = document.querySelectorAll('nav li a');
//     navLi.forEach((li) =>
//     li.addEventListener('click', function (e) {
//         navLi.forEach((x) => (x.className = 'nav-link'));
//         document.querySelector(`nav li a[name="${e.target.name}"]`).className =
//         'nav-link active';
//     })
//     );
// };



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

const navLi2 = () => {
    let pathName = window.location.pathname
    pathName = pathName.substring(1 , pathName.length -1 ) 
    document.querySelector(`nav li a[name="${pathName}"]`).className =  'nav-link active';
};

window.addEventListener('load', () => {
    navLi2();
    collapserFix();
    // UserButton();
    // navLi();
});
