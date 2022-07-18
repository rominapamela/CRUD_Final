function guardar() {
 
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
    let url = "http://localhost:5000/mascotas"
    var options = {
        body: JSON.stringify(mascota),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado") 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}
