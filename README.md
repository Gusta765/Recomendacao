cat << 'EOF' > README.md
# 🔗 Sistema de Recomendação com Similaridade Cosseno  
### Recomendando produtos com base em vetores de comportamento de compra

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*G5eDcA1vMpGg2s0gN4tX4g.gif" width="600" alt="Recommender GIF"/>
</p>

---

## 📌 Descrição do Projeto

Este projeto implementa um sistema de recomendação de produtos com base em **similaridade cosseno** entre vetores de comportamento de compra. Utilizando técnicas de **álgebra linear** e **ciência de dados**, é possível identificar produtos que apresentam padrões de compra semelhantes entre os clientes.

---

## 🧠 Fundamentação Matemática

### 1. Representação Vetorial de Produtos  
Cada produto é modelado como um vetor no espaço n-dimensional, onde cada dimensão representa um cliente:

\[
Produto_i = [qtd_{cliente1},\ qtd_{cliente2},\ ..., qtd_{clienteN}]
\]

---

### 2. Matriz de Utilidade  

Matriz onde as linhas representam produtos e as colunas, clientes. Os valores indicam a quantidade comprada:

\`\`\`
           Cliente1  Cliente2  ...  ClienteN
Produto1     2         0      ...     1
Produto2     0         3      ...     0
Produto3     1         1      ...     4
\`\`\`

---

### 3. Similaridade Cosseno  

Mede o ângulo entre dois vetores (independente da magnitude):

\[
\cos(\theta) = \frac{A \cdot B}{\|A\| \times \|B\|}
\]

- \( A \cdot B \): Produto escalar  
- \( \|A\| \): Norma Euclidiana do vetor A  
- \( \|B\| \): Norma Euclidiana do vetor B

---

## ⚙️ Como Funciona

1. Carrega a base de dados com históricos de vendas.
2. Constrói a matriz de utilidade produto-cliente.
3. Aplica a função \`cosine_similarity\` da biblioteca \`scikit-learn\`.
4. Retorna os produtos mais similares ao escolhido.

---

## 🚀 Deploy Local

### Pré-requisitos

- Python 3.10+
- Jupyter Notebook
- Bibliotecas: \`pandas\`, \`scikit-learn\`, \`numpy\`

### Instalação

\`\`\`bash
git clone https://github.com/Gusta765/Recomenda-es-de-Produtos-por-Afinidade.git
cd Recomenda-es-de-Produtos-por-Afinidade
pip install -r requirements.txt
\`\`\`

### Executando o projeto

1. Abra o notebook \`Sistema_Recomendação.ipynb\` com o Jupyter
2. Execute as células do notebook
3. Insira o ID de um produto quando solicitado
4. Veja a lista de recomendações personalizadas

---

## 💡 Exemplo de Recomendação

\`\`\`bash
Digite o ID do produto comprado: 10
\`\`\`

**Saída:**
\`\`\`
Produtos recomendados para quem comprou o produto 10:
Produto  Similaridade
  11         72%
  13         64%
  50         62%
\`\`\`

---

## 📈 Interpretação dos Resultados

- Produtos com maior percentual têm comportamento de compra mais parecido.
- As recomendações podem indicar **substitutos**, **complementares** ou **tendências** de compra.
- A similaridade vetorial traz uma abordagem mais robusta do que simples contagens ou regras de associação.

---

## 📂 Tecnologias Utilizadas

- **Python** – Linguagem principal  
- **Pandas** – Análise e manipulação de dados  
- **Scikit-learn** – Similaridade cosseno  
- **Jupyter Notebook** – Ambiente interativo

---

## 🧪 Teste você mesmo

👉  [Download do arquivo de vendas](https://github.com/Gusta765/Recomenda-es-de-Produtos-por-Afinidade/raw/main/data/Vendas_simi.xlsx)  
👉  [Acesse o notebook do projeto](https://github.com/Gusta765/Recomenda-es-de-Produtos-por-Afinidade/blob/main/Sistema_Recomenda%C3%A7%C3%A3o.ipynb)

---

## 📫 Contato

<p align="center">
  <a href="https://www.linkedin.com/in/gustavo-barbosa-868976236/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:gustavobarbosa7744@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://github.com/Gusta765">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>
EOF
