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
      case 'displayName':
        trig = verify.lengthAndCharacter(e.value, 3, 25);
        break;
        case 'password':
        trig =  verify.cap(e.value) && verify.lengthAndCharacter(e.value, 5, 25) ? true:false;
        break;
      case 'password2':
        trig = verify.equalString(e.value, document.querySelector('input[name="password"]').value) === 0? true:false;
      break;
  default:
    console.log('name.error in input tag')
    }
    
    trig  ? (document.querySelector(`input[name='${e.name}']`).className = 'form-control is-valid')
    : (document.querySelector(`input[name='${e.name}']`).className =
        'form-control is-invalid');

  }

};
