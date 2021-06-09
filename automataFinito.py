class AF:
    def __init__(self):
        self.estados = []           # Lista de estados del automata
        self.alfabeto_entrada = []  # Lista de todos los simbolos del alfabeto
        self.estado_inicial = ''    # Estado inicial
        self.estados_finales = []   # Estados finales
        self.transiciones = {}      # Diccionario de las transiciones del automata. El key es el estado y el value es un diccionario con todos los simbolos y a que estado van

    def __init__(self, estados, alfabeto_entrada, estado_inicial, estados_finales, transiciones):
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.transiciones = transiciones

    def palabra_aceptada(self, palabra):
        estados = [self.estado_inicial]
        palabra_valida = True

        # Valida si empieza por el estado inicial
        try:
            self.transiciones[estados[0]][palabra[0]]
        except:
            return False

        # Valida toda la palabra
        for letra in palabra:
            cantidad_estados_erroneos = 0
            for estado in estados:
                try:
                    estados_siguientes = self.transiciones[estado][letra]
                    palabra_valida = True
                    # print (estados, estado, letra)
                except:
                    palabra_valida = False
                    cantidad_estados_erroneos += 1

                if cantidad_estados_erroneos == len(estados):
                    return False
            estados = estados_siguientes

        # Valida si el estado final de la palabra es igual al estado final del automata
        if palabra_valida:
            palabra_valida = estados == self.estados_finales
            # print (estados, self.estados_finales)

        return palabra_valida