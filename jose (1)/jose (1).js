let caja = [0, 0, 0, 1, 4, 8, 2, 5, 4, 0, 0, 1, 2, 3, 1];
let importes = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01];
let precio = 265.73;
let pago = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
let devolucion = [];

/*function total(dinero){
    return 500*dinero[0]+200*dinero[1]+100*dinero[2]+50*dinero[3]+
    20*dinero[4]+10*dinero[5]+5*dinero[6]+2*dinero[7]+
    1*dinero[8]+0.5*dinero[9]+0.2*dinero[10]+0.1*dinero[11]+
    0.05*dinero[12]+0.02*dinero[13]+0.01*dinero[14];
}*/

function total(dinero) {
    let resultado = 0;
    for (let i = 0; i < dinero.length; i++) {
        resultado += importes[i] * dinero[i];
    }
    return resultado;
}
function abrir_caja(caja) {
    caja.push(parseFloat(total(caja).toFixed(2)));
    return caja;
}
function calcular_pago(pago) {
    pago.push(parseFloat(total(pago).toFixed(2)));
    return pago;
}
caja = abrir_caja(caja);
pago = calcular_pago(pago);
if (precio == pago[pago.length - 1]) {//Importe exacto
    alert("Importe exacto");
    for (let i = 0; i < caja.length; i++) {
        caja[i] += pago[i];
    }
    alert(caja);
} else {//Importe no exacto
    if (parseFloat((pago[pago.length - 1] - precio).toFixed(2)) > parseFloat(caja[caja.length - 1].toFixed(2))) { //No hay cambio
        alert("No tenemos cambio, ve a cambiar y vuelve a por tu producto");
    } else {
        if (parseFloat((pago[pago.length - 1] - precio).toFixed(2)) == parseFloat(caja[caja.length - 1].toFixed(2))) {//Me deja sin cambio
            for (let i = 0; i < caja.length; i++) {
                devolucion.push(caja[i]);
                caja[i] = 0;
            }
            alert("Me has dejado sin cambio");
            alert("Caja: " + caja);
            alert("Devolucion" + devolucion);
        }else{ //Devuelvo algo (cambio)

        }
    }
}
