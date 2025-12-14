class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0
        
        self.comparacoes_insercao = 0
        self.comparacoes_busca = 0
        self.comparacoes_remocao = 0

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Node(chave)
            self.tamanho += 1
            return

        atual = self.raiz
        while True:
            self.comparacoes_insercao += 1
            
            if chave < atual.key:
                if atual.left is None:
                    atual.left = Node(chave)
                    self.tamanho += 1
                    return
                atual = atual.left
            elif chave > atual.key:
                if atual.right is None:
                    atual.right = Node(chave)
                    self.tamanho += 1
                    return
                atual = atual.right
            else:
                return

    def buscar(self, chave):
        atual = self.raiz
        while atual:
            self.comparacoes_busca += 1
            
            if chave == atual.key:
                return True
            atual = atual.left if chave < atual.key else atual.right
        return False

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return None

        self.comparacoes_remocao += 1
        
        if chave < no.key:
            no.left = self._remover(no.left, chave)
        elif chave > no.key:
            no.right = self._remover(no.right, chave)
        else:
            if no.left is None:
                self.tamanho -= 1
                return no.right
            if no.right is None:
                self.tamanho -= 1
                return no.right

            self.tamanho -= 1
            sucessor = self._minimo(no.right)
            no.key = sucessor.key
            no.right = self._remover(no.right, sucessor.key)
            self.tamanho += 1 
            self.comparacoes_remocao -= 1

        return no

    def _minimo(self, no):
        while no.left:
            no = no.left
        return no

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0
        return 1 + max(self._altura(no.left), self._altura(no.right))