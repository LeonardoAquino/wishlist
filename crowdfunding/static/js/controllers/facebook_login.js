window.fbAsyncInit = function() {
    FB.init({
        appId : '1420749211490800',
        status : false, // check login status
        cookie : true, // enable cookies to allow the server to access the session
        xfbml : true  // parse XFBML
    });

    FB.Event.subscribe('auth.authResponseChange', function(response) {
        if (response.status === 'connected') {
            console.log("paso 1");
            testAPI();
        } else if (response.status === 'not_authorized') {
            console.log("paso 2");
        }else{
            console.log("paso 3");
        }
    });
};

(function(d){
    var js,
        id = 'facebook-jssdk',
        ref = d.getElementsByTagName('script')[0];

    if (d.getElementById(id)) {
        return;
    }

    js = d.createElement('script');
    js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js";
    ref.parentNode.insertBefore(js, ref);
})(document);

$("#btn_login_facebook").on("click",function(){
    FB.login(function(response){
        console.log("pshh pshh pshhhh");
        console.log(response);
    });
});
