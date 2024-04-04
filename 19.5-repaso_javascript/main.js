function MuestraMiNombre (nombre, altura){
    var misDatos = `
        <h1>Soy la caja de datos</h1>
        <h2>Mi nombre es: ${nombre}</h2>
        <h3>Mido: ${altura}</h3>
    `;

    return misDatos;
}

function imprimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Luis",190);
}

alert('hola mundo');

var nombre = "Luis";
var altura = 180;

var concatenacion = nombre + " " + altura

document.write(concatenacion);


if(altura >= 190){
    datos.innerHTML += `<h1>Eres una persona alta</h1>`;
}else{
    datos.innerHTML += `<h1>Eres una persona bajita</h1>`;
}

for(var i = 2000; i <=2020; i++){
    // Bloque de instrucciones
    datos.innerHTML += "<h2>Estamos en el año: " + i;
}

imprimir();

var nombres = ['Luis','Antonio','Joaquin'];
alert(nombres[0]);

for(i=0;i<nombres.length;i++){
    document.write('<br/>' + nombres[i] + '<br/>');
}

// Callback forma 1
nombres.forEach(function(nombre){
    document.write(nombre + '<br/>');
});

// Callback forma 2
nombres.forEach((nombre) => {
    document.write(nombre + '<br/>');
});