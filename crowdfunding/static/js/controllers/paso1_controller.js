App.Controllers.Paso1 = function(cantidadImpuesto){
    this.btnOtroProducto = $("#btn_otro_producto");
    this.htmlTipoMoneda = $("#tipo_moneda_0").html();
    this.listaProductos = $("#lista_productos");
    this.cantidadProductos = 1;
    this.cantidadImpuesto = cantidadImpuesto;

    this.addEvents();
};

App.Controllers.Paso1.mixin({
    addEvents: function(){
        this.btnOtroProducto.on("click", this.cargarPlantilla.bind(this));
        $("#lista_productos").on("keyup","input[id^=valor_]", this.calcularMonto(this.cantidadImpuesto));
        $("#lista_productos").on("click","a[data-accion=eliminar_producto]", this.eliminarProducto());
        $("#btn_continuar").on("click", this.guardarPaso1);
    },

    cargarPlantilla: function(){
        var plantilla = templateLoader.render("/templates/nuevo_proyecto/nuevo_producto",{
            numero : this.cantidadProductos++,
            monedas : this.htmlTipoMoneda
        });

        this.listaProductos.append(plantilla);
    },

    calcularMonto: function(cantidadImpuesto){
        return function(){
            var total = 0;

            $("input[id^=valor_]").each(function(){
                var valor = parseInt($(this).val(), 10);

                if(!type.isNaN(valor)){
                    total += valor;
                }
            });

            $("#total").val(total);
            $("#con_impuesto").val(total + (total * (cantidadImpuesto/100)));
        };
    },

    eliminarProducto: function(){
        var _this = this;

        return function(){
            if(!confirm("¿ Esta seguro(a) de eliminar este producto ?")){
                return;
            }

            $(this).closest(".producto").remove();
            _this.recalcularProductos();
        };
    },

    recalcularProductos: function(){
        $(".producto").each(function(index, producto){
            $(producto).find("*[id]").each(function(i, elem){
                var id = $(this).attr("id");
                id = id.replace(/\d+$/, index);
                $(this).attr("id", id);
            });
        });

        this.calcularMonto(this.cantidadImpuesto);
    },

    guardarPaso1: function(){
        var $titulo = $("#titulo"),
            $descripcion = $("#descripcion"),
            $video = $("#video"),
            $categoria = $("#categoria"),
            $duracion = $("#duracion"),
            errores = [],
            $productos = $(".producto"),
            valido = true;

        if($titulo.val().trim() === ""){
            valido = false;
            errores.push("Debes agregar título al proyecto");
        }

        if($descripcion.val().trim() === ""){
            valido = false;
            errores.push("Debes agregar una descripción al proyecto");
        }

        if($categoria.val() === ""){
            valido = false;
            errores.push("Debes seleccionar un tipo de categoria");
        }

        if($duracion.val() === ""){
            valido = false;
            errores.push("Debes seleccionar la duración del proyecto");
        }

        if(!$productos.length){
            valido = false;
            errores.push("Se debe ingresar al menos 1 producto");
        }

        $(".producto").each(function(i){
            var debeCompletarse = false;

            $(this).find("*[id]").each(function(){
                if($(this).val().trim() === ""){
                    debeCompletarse = true;
                }
            });

            if(debeCompletarse){
                valido = false;
                errores.push("El producto {0} debe completarse".format(i + 1));
            }
        });

        if(!valido){
            alert(errores.join("\n"));
            return;
        }

        $("#f_paso_1").trigger("submit");
    }
});
