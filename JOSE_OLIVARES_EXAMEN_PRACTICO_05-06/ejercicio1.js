let hora = parseInt(prompt('Ingresa la hora, utilizando el formato 24 hrs')); {


    if (hora >=7 && hora <= 14) {
        alert('Estamos en la mañana');
    } else
        if (hora >=15 && hora <=20) {
            alert('Estamos en la tarde');
        } else
            if (hora >=21 && hora <=23) {
                alert('Estamos en la noche');
        } else
        if (hora >=0 && hora <=6) {
             alert('Estamos en la noche');
    }
}
