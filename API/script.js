const mostrarnombre = function (nombre) {
    p = document.createElement('p');
    texto = document.createTextNode(nombre);
    p.appendChild(texto);
    document.body.appendChild(p);
}

const todos = () => {
    console.log("Entro")
    fetch('http://127.0.0.1:5000/all')
        .then(res => res.json())
        .then(json => {
            const claves = Object.keys(json);
            mostrarnombre('Todas personas que hay en la BD: ');
            claves.forEach(element => {
                mostrarnombre(json[element].nombre);
            });
        });
}

const empleadosId = () => {
    id = document.getElementsByName('id')[0].value;
    fetch('http://127.0.0.1:5000/all?id=' + id)
        .then(res => res.json())
        .then(json => alert(json[id].nombre));
}

const empleados_insert = () => {

    fetch("http://127.0.0.1:5000/insert", {
        method: "POST",
        body: JSON.stringify(
            {
                nombre: document.getElementsByName('nombre')[0].value,
                apellidos: document.getElementsByName('apellidos')[0].value,
                trabaja_desde: document.getElementsByName('trabaja_desde')[0].value
            }),
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then(res => res.json())
        .then(json => alert(json.resultinsert));

}

const empleadosIddelete = () => {
    id = document.getElementsByName('id')[1].value;
    fetch('http://127.0.0.1:5000/delete/'+id, {
        method: "DELETE"})
        .then(res => res.json())
        .then(json => alert(json.resultdelete));
}

const empleadosIdupdate = () => {
    id = document.getElementsByName('id')[2].value;
    nombre = document.getElementsByName('nombre').value;
    fetch('http://127.0.0.1:5000/update/'+id, nombre, {
        method: "PUT"})
        .then(res => res.json())
        .then(json => alert(json.resultupdate));
}