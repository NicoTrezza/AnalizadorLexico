class AL:
    pass

def lee_codigo(ruta):
    f = open(ruta, "r")
    codigo = []
    for line in f.readlines():
        separado = line.split()
        # si no es una linea en blanco o un comentario, lo agrega
        if separado and separado[0] != '//':
            codigo.append([i.lower() for i in separado])

    return codigo

for line in lee_codigo("./codigosPSeInt/suma.txt"):
    print (line)