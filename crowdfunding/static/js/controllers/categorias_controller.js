App.Controllers.Categoria = function(urlConsulta){
    this.categorias = $("#categorias");
    this.urlConsulta = urlConsulta;
};

App.Controllers.Categoria.prototype = {
    constructor: App.Controllers.Categoria,
    init: function(){
        this.categorias.on("change", this.cambiarCategorias);
    },

    cambiarCategorias: function(evt){
        var _this = this;

        return function(evt){
            /*var datos = {
                categoria : $(this).val();
            };

            $.get(_this.urlConsulta,datos, function(data){
                console.log(data);
            });*/
        };
    }
}
