class HashTableEnderecamentoAberto:
    def __init__(self, tamanho=10):
        self.tamanho_tabela = tamanho
        self.tabela = [None] * tamanho
        self.DELETADO = "<DELETED>"
        self.colisoes_total = 0
        self.elementos_inseridos = 0

    def funcao_hash(self, chave):
        return chave % self.tamanho_tabela

    def _calcular_fator_carga(self):
        total_elementos = sum(1 for item in self.tabela if item not in (None, self.DELETADO))
        self.fator_carga = round(total_elementos / self.tamanho_tabela, 3) if self.tamanho_tabela > 0 else 0.0
        return self.fator_carga

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        colisao_detectada = False

        while self.tabela[indice] not in (None, self.DELETADO):
            colisao_detectada = True
            indice = (indice + 1) % self.tamanho_tabela

        if colisao_detectada:
            self.colisoes_total += 1
        
        self.tabela[indice] = chave
        self.elementos_inseridos += 1
        self._calcular_fator_carga()

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        inicio = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                return True
            indice = (indice + 1) % self.tamanho_tabela
            if indice == inicio:
                break

        return False

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        inicio = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                self.tabela[indice] = self.DELETADO
                self._calcular_fator_carga()
                return True
            indice = (indice + 1) % self.tamanho_tabela
            if indice == inicio:
                break

        return False

    def imprimir(self):
        for i, valor in enumerate(self.tabela):
            print(f"{i}: {valor}")