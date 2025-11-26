## 📝 Tarefas do Trabalho Prático 01: Benchmark de Estruturas de Dados

[cite_start]Este *README* lista todas as funcionalidades e requisitos de entrega para o "Trabalho Prático 01 - Benchmark de Estruturas de Dados" da disciplina de Algoritmos e Complexidade Computacional, da Universidade Federal do Ceará - Campus Crateús[cite: 2, 3, 4].

[cite_start]O trabalho consiste em implementar três estruturas de dados, um programa de *benchmark* e um relatório técnico[cite: 16, 20].

---

### 1. Implementação das Estruturas de Dados

[cite_start]As três estruturas devem ser implementadas com **código-fonte próprio**, **sem uso de bibliotecas prontas**[cite: 18, 19].

#### 1.1 Tabela Hash (Hash Table)
Implementar uma Tabela Hash que suporte as seguintes operações:
* [cite_start][ ] **Inserir** uma dada chave[cite: 28].
* [cite_start][ ] **Buscar** uma dada chave[cite: 28].
* [cite_start][ ] **Remover** uma dada chave[cite: 28].
* [cite_start][ ] Implementar uma **Função de *Hash*** (a escolha deve ser justificada no relatório)[cite: 25, 26].
* [cite_start][ ] Implementar **Tratamento de Colisões** por **Encadeamento Externo**[cite: 27].
* [cite_start][ ] Implementar **Tratamento de Colisões** por **Endereçamento Aberto** (Linear, Quadrático ou *Double Hashing*)[cite: 27].

#### 1.2 Árvore AVL (AVL Tree)
Implementar uma Árvore AVL que suporte as seguintes operações:
* [cite_start][ ] **Inserção** de elementos[cite: 34].
* [cite_start][ ] **Remoção** de elementos[cite: 34].
* [cite_start][ ] Empregar **rotações simples e duplas**[cite: 34].
* [cite_start][ ] Fazer a manutenção correta dos **fatores de balanceamento**[cite: 34].

#### 1.3 Árvore Binária de Busca (Binary Search Tree - BST)
[cite_start]Implementar uma Árvore Binária de Busca **simples**, **sem balanceamento**[cite: 38, 39].

---

### 2. Programa de Benchmark

[cite_start]Implementar um programa responsável por executar e medir experimentos de desempenho[cite: 20, 55].

#### 2.1 Geração e Conjuntos de Dados
* [cite_start][ ] Gerar **chaves inteiras** no intervalo entre 1 e $10^{9}$[cite: 49].
* [cite_start][ ] Definir a **quantidade de elementos ($N$)**, sugerida entre 50.000 e 200.000[cite: 49, 50].
* [cite_start][ ] Utilizar os **mesmos conjuntos de chaves** para todas as três estruturas[cite: 43].
* [ ] Gerar e testar com os seguintes três conjuntos de dados:
    * [cite_start][ ] **Aleatório uniforme**[cite: 46].
    * [cite_start][ ] **Ordenado crescente**[cite: 47].
    * [cite_start][ ] **Quase ordenado** (90% em ordem crescente e 10% embaralhados aleatoriamente)[cite: 48].

#### 2.2 Fases de Execução
Para cada estrutura e cada conjunto de dados, executar as seguintes fases:
* [cite_start][ ] **Inserção de $N$ chaves**[cite: 52].
* [cite_start][ ] **Busca de $M$ chaves**, onde $M$ é o número total de buscas, com metade das chaves **presentes** e metade **não presentes**[cite: 53].
* [cite_start][ ] **Remoção de $K$ chaves**, onde $K=10\%$ de $N$[cite: 54].

#### 2.3 Métricas a Serem Registradas
[cite_start]O *benchmark* deve registrar, para cada operação e estrutura, as seguintes métricas[cite: 55, 56]:

##### [cite_start]Tabela Hash (Encadeamento Externo e Endereçamento Aberto) [cite: 29]
* [cite_start][ ] **Número total de colisões**[cite: 30].
* [cite_start][ ] **Tamanho da tabela** e **fator de carga**[cite: 31].
* [cite_start][ ] **Tempo médio** de cada operação[cite: 32, 55].

##### [cite_start]Árvore AVL [cite: 35]
* [cite_start][ ] **Número de rotações** ao longo das inserções[cite: 36, 56].
* [cite_start][ ] **Altura da árvore** após cada fase experimental[cite: 36, 56].
* [cite_start][ ] **Tempo médio** das operações[cite: 37, 55].

##### [cite_start]Árvore Binária de Busca (BST) [cite: 39]
* [cite_start][ ] **Altura da árvore** após cada fase experimental[cite: 40, 56].
* [cite_start][ ] **Tempo médio** das operações[cite: 41, 55].

---

### 3. Relatório Técnico

[cite_start]O relatório deve ser entregue em **PDF** [cite: 21] [cite_start]e deve conter os seguintes elementos[cite: 58]:

#### 3.1 Seções Obrigatórias
* [cite_start][ ] **Capa**[cite: 60].
* [cite_start][ ] **Sumário**[cite: 61].
* [ ] **Introdução**:
    * [cite_start][ ] Objetivo do trabalho[cite: 62].
    * [cite_start][ ] Explicação das estruturas estudadas[cite: 62].
    * [cite_start][ ] Breve resumo da metodologia experimental[cite: 62].
* [ ] **Método Experimental**:
    * [cite_start][ ] Descrever a linguagem e ambiente de execução utilizados[cite: 63].
    * [cite_start][ ] Descrever o tamanho dos *datasets*[cite: 63].
    * [cite_start][ ] Descrever como foram medidos tempos e métricas internas[cite: 63].
    * [cite_start][ ] Descrever como os dados foram gerados[cite: 63].
* [ ] **Resultados**:
    * [cite_start][ ] Apresentar **tabelas e gráficos**[cite: 64].
    * [cite_start][ ] Apresentar **tempo médio das operações**, por estrutura e *dataset*[cite: 64].
    * [cite_start][ ] Apresentar **quantidade de colisões**[cite: 64].
    * [cite_start][ ] Apresentar **quantidade de rotações**[cite: 64].
    * [cite_start][ ] Apresentar **altura das árvores**[cite: 65].
* [ ] **Discussão**:
    * [cite_start][ ] Explicar por que a BST degrada fortemente em dados ordenados[cite: 66].
    * [cite_start][ ] Explicar por que a AVL mantém altura $O(\log N)$[cite: 67].
    * [cite_start][ ] Analisar o impacto do **fator de carga** na eficiência da tabela *hash*[cite: 67].
    * [cite_start][ ] Discutir as diferenças entre **complexidade teórica** e **resultados empíricos**[cite: 68].
* [ ] **Conclusões**:
    * [cite_start][ ] Indicar qual estrutura teve **melhor desempenho** e por quê[cite: 69].
    * [cite_start][ ] Evidenciar em quais cenários cada estrutura é mais adequada[cite: 69].
    * [cite_start][ ] Principais lições aprendidas[cite: 69].

#### 3.2 Normas e Formatação
* [cite_start][ ] Redigir conforme a **norma culta** da língua portuguesa, com correção gramatical e clareza[cite: 70].
* [cite_start][ ] Incluir **título, identificação dos autores e seções bem definidas**[cite: 72].
* [cite_start][ ] Incluir **paginação**[cite: 72].
* [cite_start][ ] **Figuras e tabelas** devidamente numeradas e legendadas[cite: 73].
* [cite_start][ ] Incluir **referências** quando necessárias[cite: 73].
* [cite_start][ ] Padronizar **fonte, margens e espaçamento**[cite: 74].

---

### 4. Entrega Final

[cite_start]A entrega deve ser realizada **somente pela tarefa do SIGAA** [cite: 9] [cite_start]e deve conter **um arquivo zip** com[cite: 21]:

* [cite_start][ ] **Código-fonte completo** das três estruturas de dados[cite: 18].
* [cite_start][ ] Programa de **benchmark**[cite: 20].
* [cite_start][ ] **Relatório em PDF**[cite: 20, 21].
* [cite_start][ ] **Instruções de compilação/execução**[cite: 21].

---
Gostaria que eu detalhasse algum dos pontos acima, como as métricas específicas para a Tabela Hash ou o conteúdo do Relatório Técnico?
