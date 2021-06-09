from automataFinito import AF

afvar = AF(
    estados = ['q0', 'q1'],
    alfabeto_entrada = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    estado_inicial = 'q0',
    estados_finales = ['q1'],
    transiciones = {
        'q0': {'_': ['q1'], 'a': ['q1'], 'b': ['q1'], 'c': ['q1'], 'd': ['q1'], 'e': ['q1'], 'f': ['q1'], 'g': ['q1'], 'h': ['q1'], 'i': ['q1'], 'j': ['q1'], 'k': ['q1'], 'l': ['q1'], 'm': ['q1'], 'n': ['q1'], 'o': ['q1'], 'p': ['q1'], 'q': ['q1'], 'r': ['q1'], 's': ['q1'], 't': ['q1'], 'u': ['q1'], 'v': ['q1'], 'w': ['q1'], 'x': ['q1'], 'y': ['q1'], 'z': ['q1']},
        'q1': {'_': ['q1'], 'a': ['q1'], 'b': ['q1'], 'c': ['q1'], 'd': ['q1'], 'e': ['q1'], 'f': ['q1'], 'g': ['q1'], 'h': ['q1'], 'i': ['q1'], 'j': ['q1'], 'k': ['q1'], 'l': ['q1'], 'm': ['q1'], 'n': ['q1'], 'o': ['q1'], 'p': ['q1'], 'q': ['q1'], 'r': ['q1'], 's': ['q1'], 't': ['q1'], 'u': ['q1'], 'v': ['q1'], 'w': ['q1'], 'x': ['q1'], 'y': ['q1'], 'z': ['q1'], '0': ['q1'], '1': ['q1'], '2': ['q1'], '3': ['q1'], '4': ['q1'], '5': ['q1'], '6': ['q1'], '7': ['q1'], '8': ['q1'], '9': ['q1']},
    }
)

afproceso = AF(
    estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'],
    alfabeto_entrada = ['p', 'r', 'o', 'c', 'e', 's'],
    estado_inicial = 'q0',
    estados_finales = ['q7'],
    transiciones = {
        'q0': {'p': ['q1']},
        'q1': {'r': ['q2']},
        'q2': {'o': ['q3']},
        'q3': {'c': ['q4']},
        'q4': {'e': ['q5']},
        'q5': {'s': ['q6']},
        'q6': {'o': ['q7']},
    }
)

afescribir = AF(
    estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'],
    alfabeto_entrada = ['e', 's', 'c', 'r', 'i', 'b'],
    estado_inicial = 'q0',
    estados_finales = ['q8'],
    transiciones = {
        'q0': {'e': ['q1']},
        'q1': {'s': ['q2']},
        'q2': {'c': ['q3']},
        'q3': {'r': ['q4']},
        'q4': {'i': ['q5']},
        'q5': {'b': ['q6']},
        'q6': {'i': ['q7']},
        'q7': {'r': ['q8']},
    }
)

afleer = AF(
    estados = ['q0', 'q1', 'q2', 'q3', 'q4'],
    alfabeto_entrada = ['l', 'e', 'r'],
    estado_inicial = 'q0',
    estados_finales = ['q4'],
    transiciones = {
        'q0': {'l': ['q1']},
        'q1': {'e': ['q2']},
        'q2': {'e': ['q3']},
        'q3': {'r': ['q4']},
    }
)

afsi = AF(
    estados = ['q0', 'q1', 'q2'],
    alfabeto_entrada = ['s', 'i'],
    estado_inicial = 'q0',
    estados_finales = ['q2'],
    transiciones = {
        'q0': {'s': ['q1']},
        'q1': {'i': ['q2']},
    }
)

affin = AF(
    estados = ['q0', 'q1', 'q2', 'q3'],
    alfabeto_entrada = ['f', 'i', 'n'],
    estado_inicial = 'q0',
    estados_finales = ['q3'],
    transiciones = {
        'q0': {'f': ['q1']},
        'q1': {'i': ['q2']},
        'q2': {'n': ['q3']},
    }
)

# print ('estados:', afsi.estados)
# print ('alfabeto entrada:', afsi.alfabeto_entrada)
# print ('estado inicial:', afsi.estado_inicial)
# print ('estados finales:', afsi.estados_finales)
# print ('transiciones:', afsi.transiciones)
print ('palabra aceptada:', afleer.palabra_aceptada('leer'))