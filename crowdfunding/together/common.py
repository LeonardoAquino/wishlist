from django.http import HttpResponse

def is_valid_text(texto, largo=140):
    if texto is None or texto.strip() == "":
        return False

    if len(texto) > largo:
        return False

    return True

class Http500(Exception):
    pass
