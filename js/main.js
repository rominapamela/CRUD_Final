if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            mascotas: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/mascotas'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.mascotas = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(mascota) {
                const url = 'http://localhost:5000/mascotas/' + mascota;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
