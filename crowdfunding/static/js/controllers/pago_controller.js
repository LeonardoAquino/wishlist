App.Controllers.Pago = function(){
    this.form = $("#f_pago");
    this.init();
};

App.Controllers.Pago.prototype = {
    constructor: App.Controllers.Pago,
    init: function(){
        //this.form.on("submit", this.validarForm());
        console.log('some');
    },

    validarForm: function(){
        var _this = this;

        return function(evt){
            evt.preventDefault();
        };
    }
};
