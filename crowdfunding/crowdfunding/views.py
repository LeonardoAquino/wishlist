from django.http import HttpResponse
import os

def get_js_template(req):
    my_path = os.path.dirname(__file__) + req.path
    my_path = my_path.replace("\\","/")

    js_template = open(my_path,"rb").read()

    return HttpResponse(js_template)
