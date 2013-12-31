App.Controllers.Paso2 = function(){
    this.$titularCuenta = $("#titular_cuenta");
    this.$numCuenta = $("#num_cuenta");
    this.$rut = $("#rut");
    this.$banco = $("#banco");
    this.$tipoCuenta = $("#tipo_cuenta");
    this.$btnContinuar = $("#btn_continuar");
    this.$form = $("#f_paso_2");

    this.addEvents();
}

App.Controllers.Paso2.mixin({
    addEvents: function(){
        console.log("iniciando eventos");
        this.$btnContinuar.on("click", this.validarEnvio.bind(this));
    },

    validarEnvio: function(){
        var valido = true;

        if(valido){
            this.$form.trigger("submit");
        }
    }
});
