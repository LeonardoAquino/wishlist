App.Controllers.Paso1 = function(cantidadImpuesto){
    this.htmlTipoMoneda = $("#tipo_moneda_0").html();
    this.listaProductos = $("#lista_productos");
    this.cantidadProductos = 1;
    this.cantidadImpuesto = cantidadImpuesto;

    this.addEvents();
};

App.Controllers.Paso1.mixin({
    addEvents: function(){
        alert("HOLA");
        $("#lista_productos").on("keyup","input[id^=valor_]", this.calcularMonto(this.cantidadImpuesto));

        $("#btn_continuar").on("click", this.guardarPaso1);
    },

    guardarPaso1: function(){
        var $titulo = $("#titulo"),
            $descripcion = $("#descripcion"),
            $thumbnail = $("#thumbnail"),
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

        if($thumbnail.val().trim() === ""){
            valido = false;
            errores.push("Debes agregar una imagen de avatar representando al evento");
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


});
