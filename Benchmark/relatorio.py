import json
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import sys
from matplotlib.backends.backend_pdf import PdfPages

def carregar_dados_do_json(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.", file=sys.stderr)
        return None

    try:
        with open(nome_arquivo, 'r') as f:
            dados_json = json.load(f)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {nome_arquivo} não é um JSON válido.", file=sys.stderr)
        return None
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo {nome_arquivo}.", file=sys.stderr)
        return None
    
    lista_de_registros = []
    for estrutura, datasets in dados_json.items():
        for dataset in datasets:
            registro = {
                'Estrutura': estrutura,
                'Dataset': dataset['dataset'],
                'Tempo_Insercao_ms': dataset.get('tempo_insercao_ms_med', 0),
                'Tempo_Busca_ms': dataset.get('tempo_busca_ms_med', 0),
                'Tempo_Remocao_ms': dataset.get('tempo_remocao_ms_med', 0),
                'Altura_Ins': dataset.get('altura_apos_insercao', 0),
                'Altura_Rem': dataset.get('altura_apos_remocao', 0),
                'Rotacoes_Total': dataset.get('rotacoes_total', 0),
                'Colisoes_Total': dataset.get('colisoes_total', 0),
                'Fator_Carga': dataset.get('fator_carga', 0.0),
            }
            lista_de_registros.append(registro)
            
    return pd.DataFrame(lista_de_registros)

def gerar_grafico_barras(df, metrica, titulo, eixo_y):
    plt.figure(figsize=(12, 6))
    
    datasets = df['Dataset'].unique()
    largura = 0.8 / len(df['Estrutura'].unique())
    posicoes = np.arange(len(datasets)) 
    
    i = 0
    
    for estrutura, dados_estrutura in df.groupby('Estrutura'):
        valores = dados_estrutura.set_index('Dataset')[metrica]
        plt.bar(posicoes + i * largura, valores, largura, label=estrutura)
        i += 1

    plt.xlabel('Tipo de Dataset')
    plt.ylabel(eixo_y)
    plt.title(titulo)
    plt.xticks(posicoes + largura * (i - 1) / 2, datasets)
    plt.legend()
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()

def gerar_pdf_relatorio(nome_arquivo_json):
    df = carregar_dados_do_json(nome_arquivo_json)
    if df is None or df.empty:
        print("Não há dados válidos para gerar o relatório.")
        return

    nome_pdf = "relatorio_benchmark.pdf"
    
    with PdfPages(nome_pdf) as pdf:
        print("\n===============================================")
        print(f"\nGerando PDF de relatório em {nome_pdf}...")

        # 1. Gráfico de Tempos de Inserção
        gerar_grafico_barras(df, 'Tempo_Insercao_ms', 'Tempo Médio de Inserção (ms)', 'Tempo (ms)')
        pdf.savefig()
        plt.close()

        # 2. Gráfico de Tempos de Busca
        gerar_grafico_barras(df, 'Tempo_Busca_ms', 'Tempo Médio de Busca (ms)', 'Tempo (ms)')
        pdf.savefig()
        plt.close()
        
        # 3. Gráfico de Altura Final (Apenas para estruturas de árvore)
        if df['Altura_Ins'].sum() > 0: # Verifica se alguma estrutura registrou altura
             gerar_grafico_barras(df, 'Altura_Ins', 'Altura Máxima Média (Após Inserção)', 'Altura')
             pdf.savefig()
             plt.close()

        # 4. Gráfico de Rotações/Colisões (Métricas específicas)
        if df['Rotacoes_Total'].sum() > 0:
             gerar_grafico_barras(df, 'Rotacoes_Total', 'Média de Rotações por Execução (AVL)', 'Total de Rotações')
             pdf.savefig()
             plt.close()
             
        if df['Colisoes_Total'].sum() > 0:
             gerar_grafico_barras(df, 'Colisoes_Total', 'Média de Colisões por Execução (Hash)', 'Total de Colisões')
             pdf.savefig()
             plt.close()
     
        print("PDF gerado com sucesso!")
        print("\n===============================================")