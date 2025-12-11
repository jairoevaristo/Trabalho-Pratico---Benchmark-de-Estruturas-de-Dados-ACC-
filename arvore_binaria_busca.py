import random
import time
from Estruturas.no import Node

class ArvoreBST:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Node(chave)
            self.tamanho += 1
            return

        atual = self.raiz
        while True:
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
            if chave == atual.key:
                return True
            atual = atual.left if chave < atual.key else atual.right
        return False

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return None

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
                return no.left

            sucessor = self._minimo(no.right)
            no.key = sucessor.key
            no.right = self._remover(no.right, sucessor.key)

        return no

    def _minimo(self, no):
        while no.left:
            no = no.left
        return no

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return -1
        return 1 + max(self._altura(no.left), self._altura(no.right))