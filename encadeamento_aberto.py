class HashTableEnderecamentoAberto:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.DELETADO = "<DELETED>"

    def funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave):
        indice = self.funcao_hash(chave)

        while self.tabela[indice] not in (None, self.DELETADO):
            indice = (indice + 1) % self.tamanho

        self.tabela[indice] = chave

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        inicio = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                return True
            indice = (indice + 1) % self.tamanho
            if indice == inicio:
                break

        return False

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        inicio = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                self.tabela[indice] = self.DELETADO
                return True
            indice = (indice + 1) % self.tamanho
            if indice == inicio:
                break

        return False

    def imprimir(self):
        for i, valor in enumerate(self.tabela):
            print(f"{i}: {valor}")
