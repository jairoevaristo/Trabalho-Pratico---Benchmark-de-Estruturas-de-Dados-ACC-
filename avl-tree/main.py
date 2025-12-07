import sys
from sistema_benchmark import SistemaBenchmark

N_ELEMENTOS = 500000
M_BUSCAS = 500000
K_REMOCOES = 5000
NUM_EXECUCOES = 3
CHAVE_MIN = 1
CHAVE_MAX = 10**9

if __name__ == "__main__":    
   
    app = SistemaBenchmark(
        n=N_ELEMENTOS,
        m=M_BUSCAS,
        k=K_REMOCOES,
        execucoes=NUM_EXECUCOES,
        min_chave=CHAVE_MIN,
        max_chave=CHAVE_MAX
    )
    
    try:
        app.executar_processo_completo()
    except Exception as e:
        print(f"Erro na execução do benchmark: {e}", file=sys.stderr)
        sys.exit(1)
