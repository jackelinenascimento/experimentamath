import json
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def gerar_grafico_benford(caminho_json):
    with open(caminho_json, encoding='utf-8') as f:
        dados = json.load(f)

    contagem = Counter()
    total = 0

    # Contagem dos dígitos iniciais para todos os dados
    for item in dados:
        valor = item.get("populacao_atendida_agua")
        if valor and valor.isdigit():  # Verifica se a string pode ser convertida para número
            digito = str(int(valor))[0]  # Converte para int antes de pegar o primeiro dígito
            if digito in "123456789":
                contagem[digito] += 1
                total += 1

    # Frequência observada em porcentagem
    observada = [contagem.get(str(d), 0) / total * 100 for d in range(1, 10)]

    # Frequência esperada (Lei de Benford) em porcentagem
    esperada = [np.log10(1 + 1 / d) * 100 for d in range(1, 10)]

    # Criando as legendas com dados absolutos e porcentagens
    legend_observada = [
        f'Dígito {d}: {contagem.get(str(d), 0)} ({observada[d-1]:.2f}%)' for d in range(1, 10)
    ]
    legend_esperada = [
        f'Dígito {d}: {int(esperada[d-1] * total / 100)} ({esperada[d-1]:.2f}%)' for d in range(1, 10)
    ]

    # Plot
    digitos = list(map(str, range(1, 10)))
    x = np.arange(len(digitos))  # Posicionamento das barras
    width = 0.35  # Largura das barras

    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras para a distribuição observada e esperada
    barras_esperada = ax.bar(x - width/2, esperada, width, label='Esperada (Benford)', color='#6c757d', alpha=0.7)
    barras_observada = ax.bar(x + width/2, observada, width, label='Observada (População)', color='#007bff', alpha=0.7)

    # Adicionando as contagens no gráfico
    for i, digito in enumerate(range(1, 10)):
        ax.text(x[i] - width/2, esperada[i] + 0.5, f'{int(esperada[i] * total / 100)} ({esperada[i]:.2f}%)', ha='center', color='black', fontsize=10)
        ax.text(x[i] + width/2, observada[i] + 0.5, f'{contagem.get(str(digito), 0)} ({observada[i]:.2f}%)', ha='center', color='black', fontsize=10)

    # Ajustando os detalhes do gráfico
    ax.set_xlabel('Dígitos Iniciais')
    ax.set_ylabel('Frequência')
    ax.set_title('Distribuição dos Dígitos Iniciais da População Atendida por Água')
    ax.set_xticks(x)
    ax.set_xticklabels(digitos)

    # Adicionando legendas com as informações detalhadas
    ax.legend(
        title="Distribuições",
        labels=['Esperada (Benford)', 'Observada (População)'],
        bbox_to_anchor=(1.05, 1),
        loc='upper left'
    )
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Salvando a imagem na pasta 'static > img'
    caminho_imagem = os.path.join("..", "static", "img", "grafico_benford.png")
    plt.tight_layout()
    plt.savefig(caminho_imagem)
    plt.close()

    print(f"Gráfico salvo em: {caminho_imagem}")

# Caminho para seu arquivo JSON na pasta 'data/'
caminho_json = os.path.join("..", "data", "populacao.json")
gerar_grafico_benford(caminho_json)
