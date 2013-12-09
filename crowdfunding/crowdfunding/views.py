# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

import os, json

def get_js_template(req):
    my_path = os.path.dirname(__file__) + req.path
    my_path = my_path.replace("\\","/").rstrip("/") + ".html"

    js_template = open(my_path,"rb").read()

    return HttpResponse(js_template)


class LoginView(View):
    def post(self, req):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")

        data = { "status" : "ok", "message" : "" }
        user = authenticate(username=username, password=password)

        if user is not None:
            log_in(self.request, user)
            data["url"] = reverse("dashboard")
        else:
            data["status"] = "fail"
            data["message"] = "El usuario y/o contraseña son inválidos"

        return HttpResponse(json.dumps(data))


class LogoutView(View):
    def get(self, req):
        log_out(req)
        return redirect(reverse("index"))

login = LoginView.as_view()
logout = LogoutView.as_view()
