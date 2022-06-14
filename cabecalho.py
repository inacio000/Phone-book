def line(length=42):
    return '-' * length


def cabecalho(txt):
    print(line())
    print(txt.center(42))
    print(line())