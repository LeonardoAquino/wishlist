def is_valid_text(texto, largo=140):
    if texto is None or texto.strip() == "":
        return False

    if len(texto) > largo:
        return False

    return True
