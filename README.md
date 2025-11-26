## 📝 Tarefas do Trabalho Prático 01: Benchmark de Estruturas de Dados

Este *README* lista todas as funcionalidades e requisitos de entrega para o "Trabalho Prático 01 - Benchmark de Estruturas de Dados" da disciplina de Algoritmos e Complexidade Computacional, da Universidade Federal do Ceará - Campus Crateús.

O trabalho consiste em implementar três estruturas de dados, um programa de *benchmark* e um relatório técnico.

---

### 1. Implementação das Estruturas de Dados

As três estruturas devem ser implementadas com **código-fonte próprio**, **sem uso de bibliotecas prontas**.

#### 1.1 Tabela Hash (Hash Table)
Implementar uma Tabela Hash que suporte as seguintes operações:
* [ ] **Inserir** uma dada chave.
* [ ] **Buscar** uma dada chave.
* [ ] **Remover** uma dada chave.
* [ ] Implementar uma **Função de *Hash*** (a escolha deve ser justificada no relatório).
* [ ] Implementar **Tratamento de Colisões** por **Encadeamento Externo**.
* [ ] Implementar **Tratamento de Colisões** por **Endereçamento Aberto** (Linear, Quadrático ou *Double Hashing*).

#### 1.2 Árvore AVL (AVL Tree)
Implementar uma Árvore AVL que suporte as seguintes operações:
* [ ] **Inserção** de elementos].
* [ ] **Remoção** de elementos.
* [ ] Empregar **rotações simples e duplas**.
* [ ] Fazer a manutenção correta dos **fatores de balanceamento**.

#### 1.3 Árvore Binária de Busca (Binary Search Tree - BST)
Implementar uma Árvore Binária de Busca **simples**, **sem balanceamento**.

---

### 2. Programa de Benchmark

Implementar um programa responsável por executar e medir experimentos de desempenho.

#### 2.1 Geração e Conjuntos de Dados
* [ ] Gerar **chaves inteiras** no intervalo entre 1 e $10^{9}$.
* [ ] Definir a **quantidade de elementos ($N$)**, sugerida entre 50.000 e 200.000.
* [ ] Utilizar os **mesmos conjuntos de chaves** para todas as três estruturas.
* [ ] Gerar e testar com os seguintes três conjuntos de dados:
    * [ ] **Aleatório uniforme**.
    * [ ] **Ordenado crescente**.
    * [ ] **Quase ordenado** (90% em ordem crescente e 10% embaralhados aleatoriamente).

#### 2.2 Fases de Execução
Para cada estrutura e cada conjunto de dados, executar as seguintes fases:
* [ ] **Inserção de $N$ chaves**.
* [ ] **Busca de $M$ chaves**, onde $M$ é o número total de buscas, com metade das chaves **presentes** e metade **não presentes**.
* [ ] **Remoção de $K$ chaves**, onde $K=10\%$ de $N$.

#### 2.3 Métricas a Serem Registradas
O *benchmark* deve registrar, para cada operação e estrutura, as seguintes métricas:

##### Tabela Hash (Encadeamento Externo e Endereçamento Aberto)
* [ ] **Número total de colisões**.
* [ ] **Tamanho da tabela** e **fator de carga**.
* [ ] **Tempo médio** de cada operação.

##### Árvore AVL
* [ ] **Número de rotações** ao longo das inserções.
* [ ] **Altura da árvore** após cada fase experimental.
* [ ] **Tempo médio** das operações.

##### Árvore Binária de Busca (BST)
* [ ] **Altura da árvore** após cada fase experimental.
* [ ] **Tempo médio** das operações.

---

### 3. Relatório Técnico

O relatório deve ser entregue em **PDF** e deve conter os seguintes elementos:

#### 3.1 Seções Obrigatórias
* [ ] **Capa**.
* [ ] **Sumário**.
* [ ] **Introdução**:
    * [ ] Objetivo do trabalho.
    * [ ] Explicação das estruturas estudadas.
    * [ ] Breve resumo da metodologia experimental.
* [ ] **Método Experimental**:
    * [ ] Descrever a linguagem e ambiente de execução utilizados.
    * [ ] Descrever o tamanho dos *datasets*.
    * [ ] Descrever como foram medidos tempos e métricas internas.
    * [ ] Descrever como os dados foram gerados.
* [ ] **Resultados**:
    * [ ] Apresentar **tabelas e gráficos**.
    * [ ] Apresentar **tempo médio das operações**, por estrutura e *dataset*.
    * [ ] Apresentar **quantidade de colisões**.
    * [ ] Apresentar **quantidade de rotações**.
    * [ ] Apresentar **altura das árvores**.
* [ ] **Discussão**:
    * [ ] Explicar por que a BST degrada fortemente em dados ordenados.
    * [ ] Explicar por que a AVL mantém altura $O(\log N)$.
    * [ ] Analisar o impacto do **fator de carga** na eficiência da tabela *hash*.
    * [ ] Discutir as diferenças entre **complexidade teórica** e **resultados empíricos**.
* [ ] **Conclusões**:
    * [ ] Indicar qual estrutura teve **melhor desempenho** e por quê.
    * [ ] Evidenciar em quais cenários cada estrutura é mais adequada.
    * [ ] Principais lições aprendidas.

#### 3.2 Normas e Formatação
* [ ] Redigir conforme a **norma culta** da língua portuguesa, com correção gramatical e clareza.
* [ ] Incluir **título, identificação dos autores e seções bem definidas**.
* [ ] Incluir **paginação**.
* [ ] **Figuras e tabelas** devidamente numeradas e legendadas.
* [ ] Incluir **referências** quando necessárias.
* [ ] Padronizar **fonte, margens e espaçamento**.

---

### 4. Entrega Final

A entrega deve ser realizada **somente pela tarefa do SIGAA** e deve conter **um arquivo zip** com:

* [ ] **Código-fonte completo** das três estruturas de dados.
* [ ] Programa de **benchmark**.
* [ ] **Relatório em PDF**.
* [ ] **Instruções de compilação/execução**.
