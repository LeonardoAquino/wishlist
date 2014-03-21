App.Controllers.Paso1 = function(cantidadImpuesto){
    this.htmlTipoMoneda = $("#tipo_moneda_0").html();
    this.listaProductos = $("#lista_productos");
    this.cantidadProductos = 1;
    this.cantidadImpuesto = cantidadImpuesto;

    this.addEvents();
};

App.Controllers.Paso1.mixin({
    addEvents: function(){
        $("#lista_productos").on("keyup","input[id^=valor_]", this.calcularMonto(this.cantidadImpuesto));
        $("#btn_continuar").on("click", this.guardarPaso1);

        $("#fecha").datepicker({
            onRender: function(date) {
                var now = new Date();
                return date.valueOf() < now.valueOf() ? 'disabled' : '';
            }
        });

        $("#descripcion").on("keyup",function(evt){
            if( $(this).val().length > 140 ){
                $(this).val( $(this).val().substring(0,140) );
            }
        });
    },

    guardarPaso1: function(){
        var $titulo = $("#titulo"),
            $descripcion = $("#descripcion"),
            $thumbnail = $("#thumbnail"),
            $fecha = $("#fecha"),
            errores = [],
            valido = true,
            hoy = new Date(),
            fechaNueva = new Date(),
            tmp = null,
            $duracion = $("#duracion");

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

        if($fecha.val() === ""){
            valido = false;
            errores.push("Debes seleccionar la fecha del proyecto");
        }

        if(!valido){
            alert(errores.join("\n"));
            return;w
        }

        tmp = $fecha.val().split("-");
        fechaNueva.setDate(tmp[0]);
        fechaNueva.setMonth(tmp[1] - 1);
        fechaNueva.setFullYear(tmp[2]);

        tmp = fechaNueva - hoy;
        tmp /= 1000;//sacandole los milisegundos
        tmp /= 86400;//pasandolo a dias

        $("#duracion").val(tmp);
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
