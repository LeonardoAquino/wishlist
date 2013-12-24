import re
from django.http import HttpResponse

def is_text_valid(texto, largo=140):
    if texto is None or texto.strip() == "":
        return False

    if len(texto) > largo:
        return False

    return True

class Http500(Exception):
    pass

def is_email_valid(email):
    return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',email.lower())

def is_rut_valid(rut):
    rut = rut.split('-')
    rut[1] = str(rut[1]).upper()

    value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut[0]).zfill(8), '32765432')]) % 11
    dv = { 10 : 'K', 11 : '0'}.get(value, str(value))

    return str(dv) == str(rut[1])