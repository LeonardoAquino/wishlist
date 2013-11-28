App.Controllers.Registro = function(){
    this.$nombre = $("#nombre");
    this.$apellido = $("#apellido");
    this.$rut = $("#rut");
    this.$email = $("#email");
    this.$region = $("#region");
    this.$comuna = $("#comuna");

    this.addEventos();
};

App.Controllers.Registro.mixin({
    addEventos: function(){
        $("#region").on("change", this.redibujarComunas);
        $("#f_registro").on("submit", this.validarEnvio());
    },

    redibujarComunas: function(){
        var regionId = $(this).val();

        if(!regionId){
            return;
        }

        $.get("/registro/obtener_comunas/",{ region : regionId }, function(data){
            var plantilla = templateLoader.render("/templates/registro/comunas/",{
                comunas : JSON.parse(data)
            });

            $("#comuna").empty().html(plantilla);
        });
    },

    validarEnvio: function(){
        var _this = this;

        return function(evt){
            evt.preventDefault();
            $(".error_message").removeClass("error_message").text("");

            var valido, $span;

            valido = _this.validacionCampo(_this.$nombre, "nombre");
            valido = valido && _this.validacionCampo(_this.$apellido, "apellido");
            valido = valido && _this.validacionCampo(_this.$rut, "rut");
            valido = valido && _this.validacionCampo(_this.$email, "email");
            valido = valido && _this.validacionCampo(_this.$region, "region");
            valido = valido && _this.validacionCampo(_this.$comuna, "comuna");

            if(!/^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$/.test(_this.$email.val())){
                valido = false;
                _this.$email.parent().find("span").addClass("error_message").text("El email es inválido");
            }

            if(!$.Rut.validar(_this.$rut.val())){
                valido = false;
                _this.$rut.parent().find("span").addClass("error_message").text("El rut es inválido");
            }

            if(valido){
                this.submit();
            }
        };
    },

    validacionCampo: function(campo, tipo){
        var valido = true, $span;

        if(campo.val().trim() === ""){
            valido = false;
            $span = campo.parent().find("span");
            $span.addClass("error_message").text("Debe agregar " + tipo);
        }else if(campo.val().trim().length > 140){
            valido = false;
            $span = campo.parent().find("span");
            $span.addClass("error_message").text("El " + tipo + " debe poseer menos de 140 caracteres");
        }

        return valido;
    }
});
