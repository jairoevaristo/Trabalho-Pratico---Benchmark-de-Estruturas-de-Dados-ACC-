import sys

from gerador_de_dados import GeradorDeDados
from benchmark import Benchmark
from arvore_avl import ArvoreAVL  

# --- Parâmetros Globais do Benchmark ---
N_ELEMENTOS = 100000        
M_BUSCAS = 100000           
K_REMOCOES = N_ELEMENTOS // 10  
NUM_EXECUCOES = 3          
CHAVE_MIN = 1
CHAVE_MAX = 10**9

if __name__ == "__main__":
    sys.setrecursionlimit(5000) 
    
    print("===============================================")
    print(">>> PREPARANDO O AMBIENTE DE BENCHMARK <<<")
    
    # 1. GERAÇÃO DOS DADOS ÚNICOS
    gerador = GeradorDeDados(N_ELEMENTOS, M_BUSCAS, K_REMOCOES, CHAVE_MIN, CHAVE_MAX)
    datasets_insercao, chaves_busca_unica, chaves_remocao_unica = gerador.gerar_todos_datasets()
    
    print("===============================================")
    
    # 2. CONFIGURAÇÃO E EXECUÇÃO 

    estruturas_para_testar = [
        {"nome": "AVL", "classe": ArvoreAVL},
        # {"nome": "BST", "classe": ArvoreBST},
        # {"nome": "HASH_ENC", "classe": TabelaHashEncadeamento},
    ]

    for config in estruturas_para_testar:
        print(f"\n[EXECUÇÃO] Iniciando testes para {config['nome']}...")
        
        app_benchmark = Benchmark(
            nome_tipo=config['nome'],
            classe_estrutura=config['classe'],
            n=N_ELEMENTOS,
            m=M_BUSCAS,
            k=K_REMOCOES,
            execucoes=NUM_EXECUCOES,
            min_chave=CHAVE_MIN,
            max_chave=CHAVE_MAX
        )
        
        try:
            app_benchmark.executar_processo_completo(datasets_insercao, chaves_busca_unica, chaves_remocao_unica)
            print("\n===============================================")
            print("Benchmark Concluído.")
        except Exception as e:
            print(f"Erro ao rodar {config['nome']}: {e}", file=sys.stderr)
            
    