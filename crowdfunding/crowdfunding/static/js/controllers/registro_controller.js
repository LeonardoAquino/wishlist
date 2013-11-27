App.Controllers.Registro = function(){
    this.addEventos();
};

App.Controllers.Registro.mixin({
    addEventos: function(){
        $("#region").on("change", this.redibujarComunas);
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
    }
});
