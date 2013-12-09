App.Controllers.Login = function(){
    this.usuario = $("#usuario_login");
    this.password = $("#password_login");

    this.addEvents();
};

App.Controllers.Login.mixin({
    addEvents: function(){
        $("#f_login").on("submit", this.verificar.bind(this));
    },

    verificar: function(evt){
        evt.preventDefault();

        $(".error_message").removeClass("error_message").text("");

        if(this.usuario.val().trim() === ""){
            this.usuario.parent().find("span").addClass("error_message").text("Ingrese usuario");
            return;
        }

        if(this.password.val().trim() === ""){
            this.password.parent().find("span").addClass("error_message").text("Ingrese contraseña");
            return;
        }

        var data = {
            username : this.usuario.val(),
            password : this.password.val()
        };

        $.post("/login/",data, function(data){
            data = JSON.parse(data);
            console.log(data);
            if(data.status === "ok"){
                window.location.href = data.url
            }else if(data.status === "fail"){
                alert(data.message);
            }
        });
    }
});
