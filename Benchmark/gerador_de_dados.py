import random

class GeradorDeDados:

    def __init__(self, n, m, k, min_chave, max_chave):
        self.N = n
        self.M = m
        self.K = k
        self.MIN_CHAVE = min_chave
        self.MAX_CHAVE = max_chave
        random.seed(42)  # Garante a reprodutibilidade dos dados aleatórios

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

    def gerar_todos_datasets(self):
        print(">>> Gerando Datasets ÚNICOS para Inserção (Aleatório, Ordenado, Quase Ordenado) <<<")
        
        datasets = {
            "aleatorio": self._gerar_chaves_aleatorias(self.N, self.MIN_CHAVE, self.MAX_CHAVE),
            "ordenado": self._gerar_chaves_ordenadas(self.N, self.MIN_CHAVE),
            "quase_ordenado": self._gerar_chaves_quase_ordenadas(self.N, self.MIN_CHAVE)
        }
        
        # GERAÇÃO DAS CHAVES DE BUSCA E REMOÇÃO 
        base_chaves_inseridas = datasets["ordenado"]

        # Busca (Metade Presente, Metade Ausente)
        chaves_busca_presentes = base_chaves_inseridas[:self.M // 2]
        
        # Chaves ausentes fora do intervalo de chaves usadas para inserção (MAX_CHAVE + 1)
        chaves_busca_ausentes = self._gerar_chaves_aleatorias(self.M // 2, self.MAX_CHAVE + 1, self.MAX_CHAVE + self.M + 1)
        
        chaves_busca_final = chaves_busca_presentes + chaves_busca_ausentes
        random.shuffle(chaves_busca_final)
        
        # Remoção (K = 10% de N)
        chaves_remocao_final = base_chaves_inseridas[:self.K]
        random.shuffle(chaves_remocao_final) 
        
        print("Datasets de Inserção, Busca e Remoção gerados com sucesso.")

        return datasets, chaves_busca_final, chaves_remocao_final