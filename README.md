<h1 align="center">🔗 Sistema de Recomendação com Similaridade Cosseno</h1>

---

## 📌 Descrição do Projeto

Este projeto implementa um sistema de recomendação baseado no comportamento de compra dos clientes, utilizando **similaridade do cosseno** entre produtos. O objetivo é sugerir itens que costumam ser comprados juntos, com base em padrões históricos de compra.

A aplicação foi desenvolvida em **Python** com **Streamlit**, e utiliza conceitos de **álgebra linear** para calcular a similaridade entre vetores de produtos.

---

## 🧠 Fundamento Matemático

O coração do projeto está na **similaridade cosseno**, uma métrica vetorial que mede o ângulo entre dois vetores em um espaço n-dimensional.

### 🔸 Vetorização dos Produtos

Cada produto é representado como um vetor, onde:

- Cada dimensão representa um cliente.
- Os valores indicam a quantidade de vezes que o cliente comprou o produto.

**Exemplo:**

Produto A → `[3, 0, 2, 1]`  
Produto B → `[0, 1, 0, 1]`

---

### 🔸 Similaridade do Cosseno

A **similaridade cosseno** entre dois vetores A e B é definida como:

\[
\text{similaridade}(A, B) = \cos(\theta) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \cdot \|\vec{B}\|}
\]

Onde:

- \( \vec{A} \cdot \vec{B} \): produto escalar entre A e B.
- \( \|\vec{A}\| \): norma (magnitude) de A.
- \( \|\vec{B}\| \): norma (magnitude) de B.

O resultado varia entre:

- `1` → vetores idênticos (máxima similaridade)
- `0` → vetores ortogonais (sem similaridade)
- `-1` → vetores opostos (não aplicável neste contexto, pois não há pesos negativos)

---

## ⚙️ Como Funciona?

1. **Carregamento de dados** de compra.
2. Construção de uma **matriz esparsa Produto x Cliente**.
3. Cálculo da **similaridade cosseno** entre todos os produtos.
4. Exibição dos **produtos mais similares** ao item selecionado.

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn (`cosine_similarity`)
- Streamlit
- Jupyter Notebook (para análise e testes)

---

## 🚀 Executando o Projeto

Clone o repositório e execute localmente:

```bash
git clone https://github.com/seu-usuario/recomendacao-cosseno.git
cd recomendacao-cosseno
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Estrutura do Projeto

```
├── app.py                  # Interface com Streamlit
├── dados/                  # Dados fictícios ou reais
├── utils.py                # Funções auxiliares
├── notebooks/              # Análises e prototipação
├── requirements.txt        # Dependências do projeto
└── README.md               # Este documento
```

---

## 📊 Exemplo de Uso

Suponha que o usuário selecione o produto **"Arroz Branco 1kg"**.  
O sistema verifica quais produtos têm padrões de compra semelhantes — por exemplo:

- **Feijão Carioca 1kg** (similaridade: 0.89)
- **Óleo de Soja 900ml** (similaridade: 0.76)

Esses produtos são então **recomendados ao cliente** com base nos comportamentos de outros consumidores.

---

## 🔧 Possíveis Extensões

- Recomendação por **cliente individual**.
- Inclusão de **filtros por categoria ou preço**.
- **Clusterização de clientes** com K-means.
- Avaliação com **métricas de precisão/recall**.

---

## 👨‍💻 Autor

**Gustavo Barbosa**  
📘 Engenharia da Computação | 📊 Analista de Dados | 🎯 Foco em Ciência de Dados

<p align="center">
  <a href="https://www.linkedin.com/in/gustavo-barbosa-868976236/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:gustavobarbosa7744@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://github.com/seu-usuario">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>
