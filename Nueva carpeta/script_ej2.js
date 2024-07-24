//Pedir a un usuario su nombre completo e indicar 
//si la cantidad de letras 'a' que tiene en su nombre es par o impar.
//Ejercicio 2
let nombre = prompt('Inserta tu nombre completo');//DAvinia de la Rosa 
let cont = 0;
for (let i = 0; i < nombre.length; i++) {
    if(nombre[i]=='a' || nombre[i]=='A'){//i == 0 => ¿'D' == 'a'? NO, i == 1 => ¿'a' == 'a'? SI
        cont++;
    }
}
console.log(cont);
if (cont % 2 == 0) {
    alert('El número de letras "a" es par');
} else {
    alert('El número de letras "a" es impar');
}

/*const contarA = function (nombre) {
    let cont = 0;
    for (let i = 0; i < nombre.length; i++) {
        if (nombre[i] == 'a' || nombre[i] == 'A') {
            cont++;
        }
    }
    return cont;
}
let nombre = prompt('Inserta tu nombre completo');//DAvinia de la Rosa 
console.log(contarA(nombre))
contarA(nombre) % 2 == 0 ? alert('El número de letras "a" es par') : alert('El número de letras "a" es impar');
*/
