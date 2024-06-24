class Grafo:
    def __init__(self, num_medicos, num_dias_ferias):
        self.num_medicos = num_medicos
        self.num_dias_ferias = num_dias_ferias
        self.lista_adjacencia = [[] for _ in range(num_medicos)]

    def adicionar_aresta(self, medico, dia_ferias):
        self.lista_adjacencia[medico].append(dia_ferias)

    def dfs(self, medico, visitado, emparelhamento):
        for dia_ferias in self.lista_adjacencia[medico]:
            if not visitado[dia_ferias]:
                visitado[dia_ferias] = True
                if emparelhamento[dia_ferias] == -1 or self.dfs(emparelhamento[dia_ferias], visitado, emparelhamento):
                    emparelhamento[dia_ferias] = medico
                    return True
        return False

    def emparelhamento_maximo(self):
        emparelhamento = [-1] * self.num_dias_ferias
        for medico in range(self.num_medicos):
            visitado = [False] * self.num_dias_ferias
            self.dfs(medico, visitado, emparelhamento)
        return emparelhamento

def obter_entrada():
    num_medicos = int(input("Digite o número de médicos: "))
    num_dias_ferias = int(input("Digite o número de dias de férias: "))

    medicos_disponiveis = []
    for i in range(num_medicos):
        disponiveis = list(map(int, input(f"Digite os dias disponíveis para o médico {i}: ").split()))
        medicos_disponiveis.append(disponiveis)

    dias_ferias = list(range(num_dias_ferias))
    return num_medicos, num_dias_ferias, medicos_disponiveis, dias_ferias

def resolver(num_medicos, num_dias_ferias, medicos_disponiveis, dias_ferias):
    grafo = Grafo(num_medicos, num_dias_ferias)
    for medico, disponiveis in enumerate(medicos_disponiveis):
        for dia_ferias in disponiveis:
            grafo.adicionar_aresta(medico, dia_ferias)

    emparelhamento = grafo.emparelhamento_maximo()
    if all(medico != -1 for medico in emparelhamento):
        return emparelhamento
    else:
        return None

# Obtenha os dados de entrada do usuário
num_medicos, num_dias_ferias, medicos_disponiveis, dias_ferias = obter_entrada()

# Resolva o problema
resultado = resolver(num_medicos, num_dias_ferias, medicos_disponiveis, dias_ferias)
if resultado:
    print("Atribuição de médicos aos dias de férias:")
    for dia_ferias, medico in enumerate(resultado):
        print(f"Dia {dia_ferias}: Médico {medico}")
else:
    print("Não é possível fazer a atribuição de médicos.")
GIT