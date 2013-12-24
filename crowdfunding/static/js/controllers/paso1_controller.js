App.Controllers.Paso1 = function(){
    this.btnOtroProducto = $("#btn_otro_producto");
    this.htmlTipoMoneda = $("#tipo_moneda_0").html();
    this.listaProductos = $("#lista_productos");
    this.addEvents();
    this.cantidadProductos = 1;
};

App.Controllers.Paso1.mixin({
    addEvents: function(){
        this.btnOtroProducto.on("click", this.cargarPlantilla.bind(this));
    },

    cargarPlantilla: function(){
        var plantilla = templateLoader.render("/templates/nuevo_proyecto/nuevo_producto",{
            numero : this.cantidadProductos++,
            monedas : this.htmlTipoMoneda
        });

        console.log(plantilla);
        this.listaProductos.append(plantilla);
    }
});
