from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View

import os, json

def get_js_template(req):
    my_path = os.path.dirname(__file__) + req.path
    my_path = my_path.replace("\\","/").rstrip("/") + ".html"

    js_template = open(my_path,"rb").read()

    return HttpResponse(js_template)


class LoginView(View):
    def post(self, req):
        username = req.POST.get("username")
        password = req.POST.get("password")

        data = {
            "status" : "ok",
            "message" : "",
            "url" : "sadsa"
        }

        try:
            usuario = User.objects.get(username = username, password = password)
        except User.DoesNotExist as e:
            data["status"] = "fail"

        return HttpResponse(json.dumps(data))

login = LoginView.as_view()