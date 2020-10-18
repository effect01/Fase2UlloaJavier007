function RegLogState(bin) {
  this.state = bin;
}
let stat = new RegLogState(false);


const changeOnClick = (bin) => {
  stat.state = bin;
};

// invalid= { this.validationStr(this.state.displayName)  }  valid={ false}
const submitLogin = () => {
  stat.state;
};


const onchangg = (e) => {
  let trig
  if(e.name){
    switch (e.name) {
      case 'email'|| 'email1':
        trig = verify.emailCharacter(e.value)
        break;
      case 'username':
        trig = verify.lengthAndCharacter(e.value, 3, 25);
        break;
        case 'password' || 'password1':
        trig =  verify.cap(e.value) && verify.lengthAndCharacter(e.value, 5, 25) ? true:false;
        break;
      case 'password2':
        trig = verify.equalString(e.value, document.querySelector('input[name="password"]').value) === 0? true:false;
      break;
  default:
    console.log('name.error in input tag')
    }
    
    trig  ? (document.querySelector(`#id_'${e.name}']`).className = 'form-control is-valid')
    : (document.querySelector(`#id_'${e.name}']`).className =
        'form-control is-invalid');

  }

};


const fixedLogin = () =>{
  const listLabelNone = ['div_id_username', 'div_id_email', 'div_id_password', 'div_id_password1' , 'div_id_password2']

  listLabelNone.forEach(element => {

    if ( document.querySelector(`#${element}`)){

      document.querySelector(`#${element} label`).style.display = 'none';
      document.querySelector(`#${element}`).style.marginTop  = '20px';
      let nameIn = element.substring(7, element.length );
      let idIn = element.substring(4, element.length ) ;
      document.querySelector(`#${idIn}`).placeholder = nameIn.charAt(0).toUpperCase() + nameIn.substr(1, nameIn.length ) ;
      
      document.querySelector(`#${idIn}`).onchange = ()=> onchangg();

      };
  

    });

}


window.addEventListener('load', ()=>{
  fixedLogin();

})