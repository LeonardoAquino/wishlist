var App = {};
App.Controllers = {};
App.Models = {};

//inicio de nuestro cargador dinamico de plantillas
var templateLoader = new TemplateLoader(Handlebars);

Handlebars.render = function(string, data){
    return Handlebars.compile(string)(data);
};

(function(){
var cookies = document.cookie.split(";"),
    keys = {};

cookies.forEach(function(token){
    var cookie = token.split("=");
    keys[cookie[0]] = cookie[1];
});

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", keys.csrftoken);
    }
});

})();
