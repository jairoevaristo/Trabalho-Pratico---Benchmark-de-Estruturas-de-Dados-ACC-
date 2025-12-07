from encadeamento import HashTableEncadeamento
from encadeamento_aberto import HashTableEnderecamentoAberto

def main():
    print("=== Encadeamento Externo ===")
    ht1 = HashTableEncadeamento(10)
    ht1.inserir(10)
    ht1.inserir(17)
    ht1.inserir(24)
    ht1.imprimir()

    print("Buscar 17:", ht1.buscar(17))
    ht1.remover(17)
    ht1.imprimir()


    print("\n=== Endereçamento Aberto ===")
    ht2 = HashTableEnderecamentoAberto(10)
    ht2.inserir(10)
    ht2.inserir(17)
    ht2.inserir(24)
    ht2.imprimir()

    print("Buscar 24:", ht2.buscar(24))
    ht2.remover(24)
    ht2.imprimir()

if __name__ == "__main__":
    main()
