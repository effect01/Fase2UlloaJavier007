const verify = {};

verify.cap = varName =>{
    if(varName){
        let noValid = false;
        const stringCapVer = /^[A-Z]+$/;
        for (let i = 0; i <varName.length; i++) {
            if( stringCapVer.test(varName.charAt(i)) ){
                noValid=true;
            }
        }
        return noValid;
}	}

verify.lengthAndCharacter = (object, lMin, lMax)=>{
    const stringVer = /^[A-Za-z0-9]+$/;
    if(stringVer.test(object) && object.length > lMin && object.length <lMax ){
        return true; 
    }else{
        return false;
    }
}
verify.emailCharacter = (object)=>{
    const stringEmailVer = /^(?:[^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*|"[^\n"]+")@(?:[^<>()[\].,;:\s@"]+\.)+[^<>()[\]\.,;:\s@"]{2,63}$/i;
    if(stringEmailVer.test(object)){
        return true;
    }else{
        return false;
    }
}
verify.equalString = (object, object2)=>{
    return object.localeCompare(object2)
}

