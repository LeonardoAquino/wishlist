App.Controllers.Login = function(){

};

App.Controllers.Login.mixin({
    verificar: function(){
        var data = {
            username : "juannito",
            password : "perez"
        };

        $.post("/login/",data,function(data){
            console.log(data);
        });
    }
});