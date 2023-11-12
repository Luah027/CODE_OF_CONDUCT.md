culturas_por_tipo_solo = {
    "Argissolo": ["Eucalipto", "Pinheiro"],
    "Latossolo": ["Carvalho", "Palmiteiro"],
    "Podzolico": ["Cedro", "Acer"],
    "Areia Quartzosa": ["Freixo", "Seringueira"],
}

culturas_por_regiao = {
    "Norte": ["Eucalipto", "Picea"],
    "Nordeste": ["Acer", "Palmiteiro"],
    "Sudeste": ["Carvalho", "Cedro"],
}

culturas_por_clima = {
    "Tropical Úmido": ["Eucalipto", "Carvalho"],
    "Semiárido": ["Palmiteiro", "Acer"],
    "Subtropical": ["Cedro", "Picea"],
}

tipos_solo = {
    "Argissolo": {"Fator Solo": 1.2},
    "Latossolo": {"Fator Solo": 1.5},
    "Podzolico": {"Fator Solo": 1.1},
    "Areia Quartzosa": {"Fator Solo": 1.3},
}

regioes = {
    "Norte": {"Fator Regiao": 1.3},
    "Nordeste": {"Fator Regiao": 1.2},
    "Sudeste": {"Fator Regiao": 1.1},
}

climas = {
    "Tropical Úmido": {"Fator Clima": 1.4},
    "Semiárido": {"Fator Clima": 1.3},
    "Subtropical": {"Fator Clima": 1.2},
}

culturas_arvores = {
    "Eucalipto": {"Diametro Medio (m)": 0.3, "Fator Solo": 1.2, "Fator Regiao": 1.3, "Fator Clima": 1.4},
    "Carvalho": {"Diametro Medio (m)": 0.4, "Fator Solo": 1.5, "Fator Regiao": 1.1, "Fator Clima": 1.2},
    "Pinheiro": {"Diametro Medio (m)": 0.35, "Fator Solo": 1.4, "Fator Regiao": 1.3, "Fator Clima": 1.4},
    "Palmiteiro": {"Diametro Medio (m)": 0.3, "Fator Solo": 1.5, "Fator Regiao": 1.2, "Fator Clima": 1.3},
    "Cedro": {"Diametro Medio (m)": 0.45, "Fator Solo": 1.3, "Fator Regiao": 1.1, "Fator Clima": 1.4},
    "Acer": {"Diametro Medio (m)": 0.4, "Fator Solo": 1.6, "Fator Regiao": 1.2, "Fator Clima": 1.3},
    "Picea": {"Diametro Medio (m)": 0.4, "Fator Solo": 1.2, "Fator Regiao": 1.4, "Fator Clima": 1.2},
    "Freixo": {"Diametro Medio (m)": 0.35, "Fator Solo": 1.4, "Fator Regiao": 1.3, "Fator Clima": 1.2},
    "Seringueira": {"Diametro Medio (m)": 0.3, "Fator Solo": 1.3, "Fator Regiao": 1.4, "Fator Clima": 1.3},
    "Picea": {"Diametro Medio (m)": 0.4, "Fator Solo": 1.5, "Fator Regiao": 1.1, "Fator Clima": 1.2},
}

valor_credito_carbono = 81.30
fator_area = 10000

tipo_solo = input("Selecione o tipo de solo (Argissolo, Latossolo, Podzolico, Areia Quartzosa): ")
regiao = input("Selecione a região (Norte, Nordeste, Sudeste): ")
clima = input("Selecione o tipo de clima (Tropical Úmido, Semiárido, Subtropical): ")
tamanho_area = float(input("Informe o tamanho da área (em metros quadrados): "))
def recomendar_cultura(tipo_solo, regiao, clima):
    culturas_validas = []

    if tipo_solo in culturas_por_tipo_solo:
        culturas_validas.extend(culturas_por_tipo_solo[tipo_solo])
    if regiao in culturas_por_regiao:
        culturas_validas.extend(culturas_por_regiao[regiao])
    if clima in culturas_por_clima:
        culturas_validas.extend(culturas_por_clima[clima])

    melhor_cultura = None
    melhor_pontuacao = 0

    for cultura in set(culturas_validas):
        fator_solo = tipos_solo.get(tipo_solo, {"Fator Solo": 1.0})["Fator Solo"]
        fator_regiao = regioes.get(regiao, {"Fator Regiao": 1.0})["Fator Regiao"]
        fator_clima = climas.get(clima, {"Fator Clima": 1.0})["Fator Clima"]

        # Cálculo da pontuação com base nos fatores escolhidos.
        pontuacao = fator_solo * fator_regiao * fator_clima

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_cultura = cultura

    return melhor_cultura

melhor_cultura = recomendar_cultura(tipo_solo, regiao, clima)
print(f"Com base nos fatores escolhidos, a melhor cultura é: {melhor_cultura}")

if tamanho_area > fator_area:
    tamanho_area = fator_area


pontuacoes = {}
valores_reais = {}

for cultura, dados in culturas_arvores.items():
    diametro_medio = dados["Diametro Medio (m)"]
    fator_solo = tipos_solo.get(tipo_solo, {"Fator Solo": 1.0})["Fator Solo"]
    fator_regiao = regioes.get(regiao, {"Fator Regiao": 1.0})["Fator Regiao"]
    fator_clima = climas.get(clima, {"Fator Clima": 1.0})["Fator Clima"]

    pontuacao = (diametro_medio ** 2) * fator_solo * fator_regiao * fator_clima * (tamanho_area / 1000)  # Assumindo tamanho em metros quadrados
    pontuacoes[cultura] = pontuacao

    valor_em_reais = pontuacao * valor_credito_carbono
    valores_reais[cultura] = valor_em_reais

ranking = sorted(pontuacoes, key=pontuacoes.get, reverse=True)

print("Ranking de culturas de árvores (da melhor para a pior):")
for i, cultura in enumerate(ranking, start=1):
    print(f"{i}. {cultura} - Pontuação: {pontuacoes[cultura]:.2f} - Valor em Reais: R${valores_reais[cultura]:.2f}")