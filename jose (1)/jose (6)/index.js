
//Me traigo mi db firestore
import { getDesayunos, insertDesayuno, deleteDesayuno, updateDesayuno } from "./utils.js";
//console.log(db);
//Extraigo todos los documentos de tasks y creo tarjetas con ellos
getDesayunos();


//Obtenemos el form y capturamos el submit
const form = document.getElementById("desayuno-form");
form.addEventListener("submit", e => {
    e.preventDefault();
    const desayuno = {
        nombre: form["desayuno-nombre"].value,
        descripcion: form["desayuno-descripcion"].value
    }
    insertDesayuno(desayuno);
})


const buttonsCardD = document.getElementsByName("delete");
buttonsCardD.forEach(element => {
    element.addEventListener("click", () => {
        var divDelete = element.parentNode.parentNode;
        document.body.removeChild(divDelete);
        //console.log("Estoy borrando la tarea: "+element.id);
        deleteDesayuno(element.id);
    })
});

const buttonsCardU = document.getElementsByName("update");
buttonsCardU.forEach(element => {
    element.addEventListener("click", () => {
        //console.log(element.getAttribute("class"));
        let descripcion = prompt('Inserta la nueva descripción:');
        updateDesayuno(element.getAttribute("class"), {descripcion});
    })
});
