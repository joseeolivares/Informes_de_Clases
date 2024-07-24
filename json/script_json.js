let a =   [
    {
      "nombre": "Francisco Ramirez",
      "edad": 29,
      "puesto": "Contable",
      "Emails": [
        "francisco@gmail.com",
        "francisco@hotmail.es",
        "francisco@thebridgeschool.es"
      ]
    },
    {
        "nombre": "Isabel Pérez",
        "edad": 31,
        "puesto": "Profesora",
        "Emails": [
          "isabel@gmail.com",
          "isabel@hotmail.es",
          "isabel@thebridgeschool.es"
        ]
      }
  ]
/*
console.log(a[0].edad);
a[0].edad = "Asereje"
a[0].edad2 = 14
console.log(a[0].edad);
console.log(a);*/

//2. Partiendo del siguiente JSON

let j = {
  "localidade 1": {
  "Continente": "África",
  "País": "Angola",
  "Capital": "Luanda"
  },
  "localidade 2": {
  "Continente": "América do Norte",
  "País": "Estados Unidos",
  "Capital": "Washington DC"
  },
  "localidade 3": {
  "Continente": "América Central",
  "País": "México",
  "Capital": "Cidade do México"
  },
  "localidade 4": {
  "Continente": "América do Sul",
  "País": "Brasil",
  "Capital": "Brasília"
  },
  "localidade 5": {
  "Continente": "Europa",
  "País": "Espanha",
  "Capital": "Madri"
  },
  "localidade 6": {
  "Continente": "Europa",
  "País": "Alemanha",
  "Capital": "Berlim"
  },
  "localidade 7": {
  "Continente": "Oceania",
  "País": "Austrália",
  "Capital": "Camberra"
  },
  "localidade 8": {
  "Continente": "Ásia",
  "País": "Japão",
  "Capital": "Tóquio"
  }
}


//Código para obtener el país de la localidade 8

//console.log(j["localidade 8"].País); 

//Código que permite añadir una localidad a tu elección
 /* j["localidade 9"] = {
  
  "localidade 9": {
    "Continente": "America del Sur",
    "País": "Venezuela",
    "Capital": "Caracas"
  }
} 

console.log(j)*/

//Modifica la localidade 4, añadiendo el número de habitantes

console.log(j["localidade 4"].habitantes);
j.habitantes = 15.000;
console.log(j.habitantes);

console.log(j["localidade 4"]); 

//Cambia la estructura del JSON de forma que sea más directo acceder a las capitales de las localidades, dado que va a ser el dato que más vamos a consultar

