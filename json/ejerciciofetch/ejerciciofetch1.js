function usuario(){
    //alert("ingrese un usuario");
    let user = document.getElementsByTagName("input")[0].value;

fetch('https://api.github.com/users/'+user)
    .then(res=>res.json())
    .then(infoUserGitHub=>alert(infoUserGitHub.id));
}


/*fetch('https://api.github.com/users/daviniathebridge')
.then(res => res.json())

*/


/*fetch(0000'https://api.github.com/users/daviniathebridge')
    .then((resultado) => resultado.json())
    .then((data) => console.log(data))
*/


//console.log(fetch('https://api.github.com/users/daviniathebridge'))
