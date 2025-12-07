import random
import json
from arvore_avl import ArvoreAVL
from metricas import MetricasBenchmark

class SistemaBenchmark:
    def __init__(self, n, m, k, execucoes, min_chave, max_chave):
        self.N = n
        self.M = m
        self.K = k
        self.EXECUCOES = execucoes
        self.MIN_CHAVE = min_chave
        self.MAX_CHAVE = max_chave

    def _gerar_chaves_aleatorias(self, qtd, min_val, max_val):
        return random.sample(range(min_val, max_val + 1), qtd)

    def _gerar_chaves_ordenadas(self, qtd, min_val):
        return list(range(min_val, min_val + qtd))

    def _gerar_chaves_quase_ordenadas(self, qtd, min_val, percentual_bagunca=0.1):
        chaves_ordenadas = list(range(min_val, min_val + qtd))
        qtd_bagunca = int(qtd * percentual_bagunca)
        indices_para_baguncar = random.sample(range(qtd), qtd_bagunca)
        valores_para_baguncar = [chaves_ordenadas[i] for i in indices_para_baguncar]
        random.shuffle(valores_para_baguncar)
        
        for i, idx in enumerate(indices_para_baguncar):
            chaves_ordenadas[idx] = valores_para_baguncar[i]
            
        return chaves_ordenadas

    def preparar_datasets(self):
        print("Preparando datasets...")
        
        # 1. Dataset Aleatório
        chaves_aleatorias = self._gerar_chaves_aleatorias(self.N, self.MIN_CHAVE, self.MAX_CHAVE)
        
        # 2. Dataset Ordenado
        chaves_ordenadas = self._gerar_chaves_ordenadas(self.N, self.MIN_CHAVE)
        
        # 3. Dataset Quase Ordenado
        chaves_quase_ordenadas = self._gerar_chaves_quase_ordenadas(self.N, self.MIN_CHAVE)
        
        datasets = {
            "aleatorio": chaves_aleatorias,
            "ordenado": chaves_ordenadas,
            "quase_ordenado": chaves_quase_ordenadas
        }
        
        # Chaves para Busca e Remoção
        chaves_busca_presentes = chaves_ordenadas[:self.M // 2]
        chaves_busca_ausentes = random.sample(range(self.MAX_CHAVE + 1, self.MAX_CHAVE + self.M // 2 + 1), self.M // 2)
        chaves_busca = chaves_busca_presentes + chaves_busca_ausentes
        random.shuffle(chaves_busca)
        
        chaves_remocao = chaves_ordenadas[:self.K]
        
        return datasets, chaves_busca, chaves_remocao

    def executar_teste_unico(self, nome_dataset, chaves_insercao, chaves_busca, chaves_remocao):
        print(f"\n--- Iniciando Benchmark para: {nome_dataset} (N={self.N}) ---")
        
        benchmark = MetricasBenchmark(execucoes=self.EXECUCOES, N=len(chaves_insercao))
        
        for execucao in range(self.EXECUCOES):
            print(f"Execução {execucao + 1}/{self.EXECUCOES}...")
            avl = ArvoreAVL()
            
            # --- FASE DE INSERÇÃO ---
            inicio_ins = benchmark.iniciar_cronometro()
            for chave in chaves_insercao:
                avl.inserir(chave)
            fim_ins = benchmark.parar_cronometro(inicio_ins)
            
            metricas_pos_ins = avl.obter_metricas(tag="insercao")
            
            # --- FASE DE BUSCA ---
            inicio_busca = benchmark.iniciar_cronometro()
            for chave in chaves_busca:
                avl.contem(chave)
            fim_busca = benchmark.parar_cronometro(inicio_busca)

            # --- FASE DE REMOÇÃO ---
            avl.comparacoes_remocao = 0 
            inicio_rem = benchmark.iniciar_cronometro()
            for chave in chaves_remocao:
                avl.remover(chave)
            fim_rem = benchmark.parar_cronometro(inicio_rem)
            
            metricas_pos_rem = avl.obter_metricas(tag="remocao")
            
            resultado_rodada = {
                **metricas_pos_ins, 
                **metricas_pos_rem,
                "comparacoes_busca": avl.comparacoes_busca,
                "comparacoes_remocao": avl.comparacoes_remocao,
            }
            
            benchmark.adicionar_resultado_execucao(resultado_rodada, fim_ins, fim_busca, fim_rem)

        return benchmark.calcular_medias(nome_dataset)

    def executar_processo_completo(self):
        datasets, chaves_busca_base, chaves_remocao_base = self.preparar_datasets()
        todos_resultados = []
        
        for nome, chaves in datasets.items():
            chaves_busca_embaralhadas = chaves_busca_base[:] 
            random.shuffle(chaves_busca_embaralhadas)
            
            chaves_remocao_subconjunto = chaves_remocao_base[:]
            random.shuffle(chaves_remocao_subconjunto)
            
            resultados = self.executar_teste_unico(nome, chaves, chaves_busca_embaralhadas, chaves_remocao_subconjunto)
            todos_resultados.append(resultados)

        nome_arquivo = "resultados_benchmark_avl.json"
        print(f"\nResultados Finais (Salvos em {nome_arquivo}):")
        json_output = json.dumps(todos_resultados, indent=2)
        print(json_output)

        with open(nome_arquivo, "w") as f:
            f.write(json_output)