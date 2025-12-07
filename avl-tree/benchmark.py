import json
import os
import sys
from metricas import MetricasBenchmark

class Benchmark:
    
    def __init__(self, nome_tipo, classe_estrutura, n, m, k, execucoes, min_chave, max_chave):
        self.nome_tipo = nome_tipo
        self.classe_estrutura = classe_estrutura
        self.N = n
        self.M = m
        self.K = k
        self.EXECUCOES = execucoes
        self.MIN_CHAVE = min_chave
        self.MAX_CHAVE = max_chave
        self.NOME_ARQUIVO = "resultados_benchmark.json"

    def executar_teste_unico(self, nome_dataset, chaves_insercao, chaves_busca, chaves_remocao):        
    
        print(f"\n--- Iniciando Benchmark [{self.nome_tipo}] - Dataset: {nome_dataset} (N={self.N}) ---")
        
        benchmark = MetricasBenchmark(execucoes=self.EXECUCOES, N=len(chaves_insercao))
        
        for execucao in range(self.EXECUCOES):            
            estrutura = self.classe_estrutura()
            
            # --- FASE DE INSERÇÃO ---
            if hasattr(estrutura, 'colisoes_total'): estrutura.colisoes_total = 0
            
            inicio_ins = benchmark.iniciar_cronometro()
            for chave in chaves_insercao:
                estrutura.inserir(chave)
            fim_ins = benchmark.parar_cronometro(inicio_ins)
            
            metricas_pos_ins = self._extrair_metricas(estrutura, fase="insercao")
            
            # --- FASE DE BUSCA ---
            if hasattr(estrutura, 'comparacoes_busca'): estrutura.comparacoes_busca = 0
            
            inicio_busca = benchmark.iniciar_cronometro()
            for chave in chaves_busca:
                estrutura.contem(chave)
            fim_busca = benchmark.parar_cronometro(inicio_busca)

            # --- FASE DE REMOÇÃO ---
            if hasattr(estrutura, 'comparacoes_remocao'): estrutura.comparacoes_remocao = 0
            
            inicio_rem = benchmark.iniciar_cronometro()
            for chave in chaves_remocao:
                estrutura.remover(chave)
            fim_rem = benchmark.parar_cronometro(inicio_rem)
            
            metricas_pos_rem = self._extrair_metricas(estrutura, fase="remocao")
            
            resultado_rodada = {
                "estrutura": self.nome_tipo,
                **metricas_pos_ins, 
                **metricas_pos_rem,
                "comparacoes_busca": getattr(estrutura, 'comparacoes_busca', 0),
                "comparacoes_remocao": getattr(estrutura, 'comparacoes_remocao', 0),
                "colisoes_total": getattr(estrutura, 'colisoes_total', 0),
                "rotacoes_total": getattr(estrutura, 'rotacoes_simples', 0) + getattr(estrutura, 'rotacoes_duplas', 0),
                "rotacoes_simples": getattr(estrutura, 'rotacoes_simples', 0),
                "rotacoes_duplas": getattr(estrutura, 'rotacoes_duplas', 0),
                "tamanho_tabela": getattr(estrutura, 'tamanho_tabela', 0),
                "fator_carga": getattr(estrutura, 'fator_carga', 0.0),
            }
            
            benchmark.adicionar_resultado_execucao(resultado_rodada, fim_ins, fim_busca, fim_rem)

        medias_finais = benchmark.calcular_medias(nome_dataset)
        medias_finais["estrutura"] = self.nome_tipo
        return medias_finais

    def _extrair_metricas(self, estrutura, fase: str) -> dict:
        metricas = {}
        
        altura = getattr(estrutura, 'altura', None)
        if altura is not None:
             metricas[f"altura_apos_{fase}"] = altura()
        
        metricas["comparacoes_insercao"] = getattr(estrutura, 'comparacoes_insercao', 0)
        
        return metricas

    def _salvar_no_arquivo(self, novos_resultados):
        dados_existentes = {}

        if os.path.exists(self.NOME_ARQUIVO):
            try:
                with open(self.NOME_ARQUIVO, "r") as f:
                    conteudo = f.read()
                    if conteudo:
                        dados_existentes = json.loads(conteudo)
            except (json.JSONDecodeError, IOError):
                dados_existentes = {}

        dados_existentes[self.nome_tipo] = novos_resultados

        try:
            with open(self.NOME_ARQUIVO, "w") as f:
                json.dump(dados_existentes, f, indent=2)
            print(f"\nSucesso: Resultados de '{self.nome_tipo}' salvos em {self.NOME_ARQUIVO}.")
        except IOError as e:
            print(f"Erro ao salvar arquivo: {e}", file=sys.stderr)

    def executar_processo_completo(self, datasets_insercao: dict, chaves_busca_unica: list, chaves_remocao_unica: list):
       
        lista_resultados_tipo = []
        
        for nome_ds, chaves_insercao in datasets_insercao.items():
            
            resultado = self.executar_teste_unico(
                nome_ds, 
                chaves_insercao, 
                chaves_busca_unica, 
                chaves_remocao_unica
            )
            lista_resultados_tipo.append(resultado)

        self._salvar_no_arquivo(lista_resultados_tipo)