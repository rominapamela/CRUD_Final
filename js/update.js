var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtTipo").value = parts[1][1]
document.getElementById("txtNombre").value = parts[2][1]
document.getElementById("txtFoto").value = parts[3][1]
document.getElementById("txtEdad").value = parts[4][1]
document.getElementById("txtDescripcion").value = parts[5][1]
document.getElementById("txtFechaPerdida").value = parts[6][1]
 
function modificar() {
    let id = document.getElementById("txtId").value
    let t = document.getElementById("txtTipo").value
    let n = document.getElementById("txtNombre").value
    let fo = document.getElementById("txtFoto").value
    let e = parseInt(document.getElementById("txtEdad").value)
    let d = document.getElementById("txtDescripcion").value
    let f = document.getElementById("txtFechaPerdida").value

    let mascota = {
        tipo: t,
        nombre: n,
        foto: fo,
        edad: e,
        descripcion: d,
        fechaPerdida: f
    }
    let url = "http://localhost:5000/mascotas/"+id
    var options = {
        body: JSON.stringify(mascota),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
