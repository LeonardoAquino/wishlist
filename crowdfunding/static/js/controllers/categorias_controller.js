App.Controllers.Categoria = function(urlConsulta){
    this.categorias = $("#sel_categoria");
    this.urlConsulta = urlConsulta.replace("/99/", "/");
    console.log(this.urlConsulta);
    this.init();
};

App.Controllers.Categoria.prototype = {
    constructor: App.Controllers.Categoria,
    init: function(){
        console.log("pasando por aqui");
        this.categorias.on("change", this.cambiarCategorias());
    },

    cambiarCategorias: function(evt){
        var _this = this;

        return function(evt){
            var nuevaUrl = _this.urlConsulta + $(this).val() + "/";

            $.get(nuevaUrl, function(data){
                console.log(data);
                var html = templateLoader.render("/templates/ajax/proyecto_list", data);
                $("#proyectos").empty().html(html);
            });
        };
    }
}
