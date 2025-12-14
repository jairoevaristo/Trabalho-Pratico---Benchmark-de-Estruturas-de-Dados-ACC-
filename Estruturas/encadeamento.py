class HashTableEncadeamento:
    def __init__(self, tamanho=10):
        self.tamanho_tabela = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.colisoes_total = 0
        self.elementos_inseridos = 0

    def funcao_hash(self, chave):
        return chave % self.tamanho_tabela

    def _calcular_fator_carga(self):
        total_elementos = sum(len(lista) for lista in self.tabela)
        self.fator_carga = round(total_elementos / self.tamanho_tabela, 3) if self.tamanho_tabela > 0 else 0.0
        return self.fator_carga

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        if chave not in self.tabela[indice]:
            if len(self.tabela[indice]) > 0:
                self.colisoes_total += 1
            self.tabela[indice].append(chave)
            self.elementos_inseridos += 1
        self._calcular_fator_carga()

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        return chave in self.tabela[indice]

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        if chave in self.tabela[indice]:
            self.tabela[indice].remove(chave)
            self._calcular_fator_carga()
            return True
        return False

    def imprimir(self):
        for i, lista in enumerate(self.tabela):
            print(f"{i}: {lista}")