import time

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
            "estrutura": "AVL", # Todo : Adicionar suporte para outras estruturas
            "dataset": nome_dataset,
            "N": self.N,
            "execucoes": self.execucoes,
            "tempo_insercao_ms_med": round((self.tempo_total_insercao / self.execucoes) * 1000, 3),
            "tempo_busca_ms_med": round((self.tempo_total_busca / self.execucoes) * 1000, 3),
            "tempo_remocao_ms_med": round((self.tempo_total_remocao / self.execucoes) * 1000, 3),
        }

        soma_metricas = {
            "rotacoes_total": 0,
            "rotacoes_simples": 0,
            "rotacoes_duplas": 0,
            "altura_apos_insercao": 0,
            "altura_apos_remocao": 0,
            "comparacoes_insercao": 0,
            "comparacoes_busca": 0,
            "comparacoes_remocao": 0,
        }

        for resultado in self.resultados:
            for chave in soma_metricas.keys():
                if chave in resultado:
                    soma_metricas[chave] += resultado[chave]

        # Calcula médias
        medias["rotacoes_total"] = soma_metricas["rotacoes_total"] // self.execucoes
        medias["rotacoes_simples"] = soma_metricas["rotacoes_simples"] // self.execucoes
        medias["rotacoes_duplas"] = soma_metricas["rotacoes_duplas"] // self.execucoes
        medias["altura_apos_insercao"] = soma_metricas["altura_apos_insercao"] // self.execucoes
        medias["altura_apos_remocao"] = soma_metricas["altura_apos_remocao"] // self.execucoes
        medias["comparacoes_insercao"] = soma_metricas["comparacoes_insercao"] // self.execucoes
        medias["comparacoes_busca"] = soma_metricas["comparacoes_busca"] // self.execucoes
        medias["comparacoes_remocao"] = soma_metricas["comparacoes_remocao"] // self.execucoes

        return medias