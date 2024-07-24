
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getFirestore, collection, getDocs, doc, setDoc, deleteDoc, updateDoc } from 'https://www.gstatic.com/firebasejs/10.7.2/firebase-firestore.js';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDGyYvDaE27ElsPDymYtgLk85d9V4XPWdk",
    authDomain: "ejercicio-1a15b.firebaseapp.com",
    projectId: "ejercicio-1a15b",
    storageBucket: "ejercicio-1a15b.appspot.com",
    messagingSenderId: "601089492502",
    appId: "1:601089492502:web:61c68c94e554ff2edb9737"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const querySnapshot = await getDocs(collection(db, "Desayunos"));

function createCard(id, desayuno) {
    //<div class="card text-white bg-info mb-6  offset-md-4" style="max-width: 20rem;">
    const principalDiv = document.createElement('div');
    principalDiv.setAttribute("class", "card bg-light mb-3");
    principalDiv.style = "max-width: 20rem;";
    principalDiv.setAttribute("name", id);
    //<div class="card-header">Formulario Tareas</div>
    const headerDiv = document.createElement('div');
    const contentDiv = document.createTextNode("Id: " + id);
    headerDiv.setAttribute("class", "card-header");

    headerDiv.appendChild(contentDiv);
    principalDiv.appendChild(headerDiv);
    // <div class="card-body">
    const bodyDiv = document.createElement('div');
    const pTitle = document.createElement("p");
    const pTitleText = document.createTextNode("Nombre: " + desayuno.nombre);
    const hr = document.createElement('hr');
    const pDesc = document.createElement("p");
    const pDescText = document.createTextNode("Description: " + desayuno.descripcion);

    pTitle.appendChild(pTitleText);
    bodyDiv.appendChild(pTitle);
    bodyDiv.appendChild(hr);
    pDesc.appendChild(pDescText);
    bodyDiv.appendChild(pDesc);
    bodyDiv.appendChild(hr);


    var input = document.createElement("input");
    input.type = "button";
    input.value = "Borrar Desayuno";
    input.setAttribute("name", "delete");
    input.setAttribute("id", id);
    bodyDiv.appendChild(input);

    var input2 = document.createElement("input");
    input2.type = "button";
    input2.value = "Actualizar Desayuno";
    input2.setAttribute("name", "update");
    input2.setAttribute("class", id);
    bodyDiv.appendChild(input2);

    principalDiv.appendChild(bodyDiv);

    document.body.appendChild(principalDiv);
    const br = document.createElement("br");
    document.body.appendChild(br);

}

export function getDesayunos() {
    querySnapshot.forEach((doc) => {
        createCard(doc.id, doc.data());
    });
}
function generateRandomIdDesayuno(num) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#@';
    let result = '';
    const charactersLength = characters.length;
    for (let i = 0; i < num; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}
export async function insertDesayuno(desayuno) {
    let id = generateRandomIdDesayuno(20)
    await setDoc(doc(db, "Desayunos", id), desayuno);
    alert("Insertada el desayuno: " + id);
}

export async function deleteDesayuno(id) {
    await deleteDoc(doc(db, "Desayunos", id));
    alert("Borrada la tarea: " + id);
}
/*
import { doc, updateDoc } from "firebase/firestore";



// Set the "capital" field of the city 'DC'
await updateDoc( doc(db, "cities", "DC"), {
  capital: true
});
*/ 
export async function updateDesayuno(id, datos) {
    await updateDoc(doc(db, "Desayunos", id), datos);
    alert("Actualizado el desayuno: " + id);
}