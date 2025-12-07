class HashTableEncadeamento:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave):
        indice = self.funcao_hash(chave)
        if chave not in self.tabela[indice]:
            self.tabela[indice].append(chave)

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        return chave in self.tabela[indice]

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        if chave in self.tabela[indice]:
            self.tabela[indice].remove(chave)
            return True
        return False

    def imprimir(self):
        for i, lista in enumerate(self.tabela):
            print(f"{i}: {lista}")
