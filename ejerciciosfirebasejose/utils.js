   // Import the functions you need from the SDKs you need
   import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
   import { getFirestore, collection, getDocs, doc, setDoc, deleteDoc, updateDoc} from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js';
   // TODO: Add SDKs for Firebase products that you want to use
   // https://firebase.google.com/docs/web/setup#available-libraries

   // Your web app's Firebase configuration
   const firebaseConfig = {
       apiKey: "AIzaSyBthA5sDDMzwqwbycYYKe6ef2ApdHrWO_c",
       authDomain: "comida-f1afa.firebaseapp.com",
       projectId: "comida-f1afa",
       storageBucket: "comida-f1afa.appspot.com",
       messagingSenderId: "355927608668",
       appId: "1:355927608668:web:bba53ea34a45c934028599",
       measurementId: "G-GDC89L4MYM"
   };

   // Initialize Firebase
   export const app = initializeApp(firebaseConfig);
   export const db = getFirestore(app);
   export const querySnapshot = await getDocs(collection(db, "Desayunos"));
   //export const collectionTask = collection(db, 'tasks');

   function createCard(id, desayunos) {
       //<div class="card text-white bg-info mb-6  offset-md-4" style="max-width: 20rem;">
       const principalDiv = document.createElement('div');
       principalDiv.setAttribute("class", "card bg-light mb-3");
       principalDiv.style = "max-width: 20rem;";
       principalDiv.setAttribute("nombre",id);
       //<div class="card-header">Formulario Tareas</div>
       const headerDiv = document.createElement('div');
       const contentDiv = document.createTextNode("Id: " + id);
       headerDiv.setAttribute("class", "card-header");
       
       headerDiv.appendChild(contentDiv);
       principalDiv.appendChild(headerDiv);
       // <div class="card-body">
       const bodyDiv = document.createElement('div');
       const pTitle = document.createElement("p");
       const pTitleText = document.createTextNode("Nombre: " + desayunos.nombre);
       const hr = document.createElement('hr');
       const pDesc = document.createElement("p");
       const pDescText = document.createTextNode("Descripcion: " + desayunos.descripcion);
       
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
       input.setAttribute("id",id);
       bodyDiv.appendChild(input);

       var input2 = document.createElement("input");
       input2.type = "button";
       input2.value = "Actualizar Desayuno";
       input2.setAttribute("name", "update");
       input2.setAttribute("class",id);
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
   function generateRandomIdDesayunos(num) {
       const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
       let result = '';
       const charactersLength = characters.length;
       for (let i = 0; i < num; i++) {
           result += characters.charAt(Math.floor(Math.random() * charactersLength));
       }

       return result;
   }
   export async function insertDesayuno(desayuno) {
    let id = generateRandomIdDesayunos(20)
       await setDoc(doc(db, "Desayunos", id), desayuno);
       alert("Insertado el desayuno: "+ id);
   }

   export async function deleteDesayuno(id){
       await deleteDoc(doc(db, "Desayunos", id));   
       alert("Borrada la tarea: "+id);
   }
   
   export async function updateDesayuno(id, datos) {
        await updateDoc(doc(db, "Desayunos", id), datos);
        alert("Actulizada la tarea: " + id);
   }
