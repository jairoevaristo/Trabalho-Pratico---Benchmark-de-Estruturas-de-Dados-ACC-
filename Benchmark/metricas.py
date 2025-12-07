import time
import math

class MetricasBenchmark:    
    def __init__(self, execucoes: int = 3, N: int = 0):
        self.execucoes = execucoes
        self.N = N
        self.resultados = []
        
        self.tempo_total_insercao = 0.0
        self.tempo_total_busca = 0.0
        self.tempo_total_remocao = 0.0
        
    def iniciar_cronometro(self):
        return time.perf_counter()

    def parar_cronometro(self, tempo_inicio):
        return time.perf_counter() - tempo_inicio

    def adicionar_resultado_execucao(self, metricas: dict, tempo_ins: float, tempo_busca: float, tempo_rem: float):        
        self.tempo_total_insercao += tempo_ins
        self.tempo_total_busca += tempo_busca
        self.tempo_total_remocao += tempo_rem
        self.resultados.append(metricas)
        
    def calcular_medias(self, nome_dataset: str) -> dict:
        if not self.resultados:
            return {}

        medias = {
            "dataset": nome_dataset,
            "N": self.N,
            "execucoes": self.execucoes,
            "tempo_insercao_ms_med": round((self.tempo_total_insercao / self.execucoes) * 1000, 3),
            "tempo_busca_ms_med": round((self.tempo_total_busca / self.execucoes) * 1000, 3),
            "tempo_remocao_ms_med": round((self.tempo_total_remocao / self.execucoes) * 1000, 3),
        }

        soma_metricas = {
            # --- Métricas AVL ---
            "rotacoes_total": 0, "rotacoes_simples": 0, "rotacoes_duplas": 0,
            # --- Métricas Hash ---
            "colisoes_total": 0, "tamanho_tabela": 0, "fator_carga": 0.0,
            # --- Métricas Comuns ---
            "altura_apos_insercao": 0, "altura_apos_remocao": 0,
            "comparacoes_insercao": 0, "comparacoes_busca": 0, "comparacoes_remocao": 0,
        }

        # 1. Soma as métricas de todas as execuções
        for resultado in self.resultados:
            for chave in soma_metricas.keys():
                if chave in resultado:
                    soma_metricas[chave] += resultado[chave] if chave != "fator_carga" else float(resultado[chave])

        # 2. Calcula a Média Final
        
        medias["altura_apos_insercao"] = math.ceil(soma_metricas["altura_apos_insercao"] / self.execucoes)
        medias["altura_apos_remocao"] = math.ceil(soma_metricas["altura_apos_remocao"] / self.execucoes)
        medias["fator_carga"] = round(soma_metricas["fator_carga"] / self.execucoes, 3)
        
        chaves_int_media = ["rotacoes_total", "rotacoes_simples", "rotacoes_duplas", "colisoes_total",
                            "comparacoes_insercao", "comparacoes_busca", "comparacoes_remocao"]
        for chave in chaves_int_media:
            if soma_metricas[chave] > 0:
                 medias[chave] = soma_metricas[chave] // self.execucoes

        if soma_metricas["tamanho_tabela"] > 0:
             medias["tamanho_tabela"] = self.resultados[-1].get("tamanho_tabela", 0)

        metricas_finais = {k: v for k, v in medias.items() if (v != 0 and v != 0.0) or k in ["dataset", "N", "execucoes"]}
        
        return metricas_finais