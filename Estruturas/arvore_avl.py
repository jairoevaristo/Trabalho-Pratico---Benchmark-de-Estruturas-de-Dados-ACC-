
    # --- Classes Fundamentais da Árvore AVL ---

class No:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1 
        self.esquerda = None
        self.direita = None

class ArvoreAVL:    
    def __init__(self):
        self.raiz = None
        self._tamanho = 0
        self.rotacoes_simples = 0
        self.rotacoes_duplas = 0
        
        self.comparacoes_insercao = 0
        self.comparacoes_busca = 0
        self.comparacoes_remocao = 0

    # --- Métodos Auxiliares de Altura e Fator de Balanceamento ---

    def _obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _atualizar_altura(self, no):
        if no:
            no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))

    def _obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    # --- Métodos de Rotação ---

    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self._atualizar_altura(y)
        self._atualizar_altura(x)
        
        self.rotacoes_simples += 1
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self._atualizar_altura(x)
        self._atualizar_altura(y)
        
        self.rotacoes_simples += 1
        return y
    
    def _rotacao_esquerda_direita(self, z):
        z.esquerda = self._rotacao_esquerda(z.esquerda)
        self.rotacoes_simples -= 1 
        z = self._rotacao_direita(z)
        self.rotacoes_simples -= 1 
        self.rotacoes_duplas += 1
        return z

    def _rotacao_direita_esquerda(self, z):
        z.direita = self._rotacao_direita(z.direita)
        self.rotacoes_simples -= 1
        z = self._rotacao_esquerda(z)
        self.rotacoes_simples -= 1
        self.rotacoes_duplas += 1
        return z

    # --- Rebalanceamento ---

    def _balancear(self, no):
        if not no:
            return no

        self._atualizar_altura(no)
        balanceamento = self._obter_fator_balanceamento(no)

    # Caso 1: Desbalanceamento à Esquerda
        if balanceamento > 1:
            if self._obter_fator_balanceamento(no.esquerda) >= 0:
                return self._rotacao_direita(no)
            else:
                return self._rotacao_esquerda_direita(no)

    # Caso 2: Desbalanceamento à Direita
        if balanceamento < -1:
            if self._obter_fator_balanceamento(no.direita) <= 0:
                return self._rotacao_esquerda(no)
            else:
                return self._rotacao_direita_esquerda(no)

        return no

    # --- Operações Principais ---

    def _inserir_recursivo(self, raiz, chave):
        if not raiz:
            self._tamanho += 1
            return No(chave)

        self.comparacoes_insercao += 1
        
        if chave < raiz.chave:
            raiz.esquerda = self._inserir_recursivo(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self._inserir_recursivo(raiz.direita, chave)
        else:
            return raiz
        
        return self._balancear(raiz)

    def inserir(self, chave: int):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _no_valor_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
    def _remover_recursivo(self, raiz, chave):
        if not raiz:
            return raiz

        self.comparacoes_remocao += 1
        
        if chave < raiz.chave:
            raiz.esquerda = self._remover_recursivo(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self._remover_recursivo(raiz.direita, chave)
        else:
            self._tamanho -= 1
            
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self._no_valor_minimo(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self._remover_recursivo(raiz.direita, temp.chave)
            self._tamanho += 1
            
        if raiz is None:
            return raiz
        
        return self._balancear(raiz)

    def remover(self, chave: int):        
        self.raiz = self._remover_recursivo(self.raiz, chave)        

    def _buscar_recursivo(self, raiz, chave: int) -> bool:
        if not raiz:
            return False
        
        self.comparacoes_busca += 1
        
        if chave == raiz.chave:
            return True
        elif chave < raiz.chave:
            return self._buscar_recursivo(raiz.esquerda, chave)
        else:
            return self._buscar_recursivo(raiz.direita, chave)

    def buscar(self, chave: int) -> bool:
        return self._buscar_recursivo(self.raiz, chave)

    def altura(self) -> int:
        return self._obter_altura(self.raiz)

    def tamanho(self) -> int:
        return self._tamanho
    
    def _em_ordem_recursivo(self, raiz, chaves):
        if raiz:
            self._em_ordem_recursivo(raiz.esquerda, chaves)
            chaves.append(raiz.chave)
            self._em_ordem_recursivo(raiz.direita, chaves)

    def em_ordem(self):
        chaves = []
        self._em_ordem_recursivo(self.raiz, chaves)
        return chaves
    
    def obter_metricas(self, tag: str = "") -> dict:
        metricas = {
            "rotacoes_total": self.rotacoes_simples + self.rotacoes_duplas,
            "rotacoes_simples": self.rotacoes_simples,
            "rotacoes_duplas": self.rotacoes_duplas,
            "comparacoes_insercao": self.comparacoes_insercao,
            "comparacoes_busca": self.comparacoes_busca,
            "comparacoes_remocao": self.comparacoes_remocao,
            "tamanho_atual": self.tamanho()
        }
        
        if tag:
            metricas[f"altura_apos_{tag}"] = self.altura()
        else:
            metricas["altura"] = self.altura()
            
        return metricas