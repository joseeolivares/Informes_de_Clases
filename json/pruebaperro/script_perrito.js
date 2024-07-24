// Informacion del API.

//const url = 'https://dog.ceo/api/breeds/image/random';



/*function perritos() {

    fetch('https://dog.ceo/api/breeds/image/random')
        .then(res => res.json())
        .then(perro => document.getElementsByTagName("img")[0].src = perro.message);


}

*/
function addDog(url, width, height){
    let img = document.createElement('img');
    img.width=width;
    img.height=height;
    img.src=url;
    document.body.appendChild(img);
}


function perritos() {

    fetch('https://dog.ceo/api/breeds/image/random')
        .then(res => res.json())
        .then(perro => {addDog(perro.message, 100, 100);});
        

}