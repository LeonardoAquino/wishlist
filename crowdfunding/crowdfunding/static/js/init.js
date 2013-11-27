var App = {};
App.Controllers = {};
App.Models = {};

//inicio de nuestro cargador dinamico de plantillas
var templateLoader = new TemplateLoader(Handlebars);

Handlebars.render = function(string, data){
    return Handlebars.compile(string)(data);
};
