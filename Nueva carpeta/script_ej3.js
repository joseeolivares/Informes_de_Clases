function mayorEdad() {
    let edad = parseInt(document.getElementsByName('edad')[0].value);
    edad > 18 ? alert('Eres mayor de edad') : alert('No eres mayor de edad');
}
/*function mayorEdad() {
    let edad = parseInt(document.getElementsByName('edad')[0].value);
    //console.log(edad);
    //<label for="">Eres mayor de edad</label>
    let formulario = document.getElementsByTagName('form')[0]; //Capturo el formulario 1
    let resultado;
    edad > 18 ? resultado = 'Eres mayor de edad' : resultado = 'No eres mayor de edad';
    let labelResultado = document.getElementById('resultado');
    if (labelResultado) { //Si existe lo actualizo
        labelResultado.innerText="";
        labelResultado.innerText=resultado;
    } else { //Si no existe lo creo
        //Creo un label y le pongo resultado dentro como texto
        let label = document.createElement('label');
        label.id = "resultado";
        let texto = document.createTextNode(resultado);
        label.appendChild(texto); //Pongo el texto en el label
        formulario.appendChild(label); //Pongo el label en el formulario 1
    }
}*/

function numeroAes() {
    let nombre = document.getElementsByName('nombre')[0].value;
    let cont = 0;
    for (let i = 0; i < nombre.length; i++) {
        if (nombre[i] == 'a' || nombre[i] == 'A') {//i == 0 => ¿'D' == 'a'? NO, i == 1 => ¿'a' == 'a'? SI
            cont++;
        }
    }
    if (cont % 2 == 0) {
        alert('El número de letras "a" es par');
    } else {
        alert('El número de letras "a" es impar');
    }
}


