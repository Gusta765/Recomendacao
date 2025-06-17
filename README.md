🛍️ Sistema de Recomendação de Produtos com Similaridade Cosseno
Este projeto é uma aplicação web interativa para recomendação de produtos baseada em similaridade cosseno, utilizando técnicas de filtragem colaborativa. Desenvolvido com Python, Streamlit e scikit-learn, o sistema simula um cenário realista de compras e permite ao usuário explorar recomendações personalizadas de forma visual e intuitiva.

🔗 Acesse a aplicação:
https://recomendacao-d23k2ucfmjz3anxevvwnak.streamlit.app/

🚀 Funcionalidades
Interface moderna e responsiva com Streamlit e CSS customizado

Geração de dados fictícios simulando compras reais

Cálculo de similaridade cosseno entre produtos (matriz item-item)

Recomendação de produtos similares com base em um item selecionado

Visualização interativa com Plotly:

Gráficos de vendas

Produtos mais populares

Evolução de compras por mês

Heatmap da matriz de similaridade

🧠 Tecnologias Utilizadas
Ferramenta	Finalidade
Python	Linguagem principal
Streamlit	Interface Web
scikit-learn	Cálculo da similaridade cosseno
Plotly	Visualizações interativas
pandas / numpy	Manipulação e geração de dados

🔍 Como Funciona
Geração de dados fictícios: o sistema cria automaticamente uma base com clientes, produtos, categorias e transações.

Matriz item-item: é construída com base na quantidade de compras por cliente.

Cálculo de similaridade: utiliza a função cosine_similarity da scikit-learn para encontrar produtos semelhantes.

Recomendações: ao selecionar um produto, o sistema retorna os mais similares com métricas e gráficos.

📸 Capturas de Tela
Recomendação Personalizada	Análise de Vendas	Produtos Populares

💻 Executando Localmente
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/sistema-recomendacao.git
cd sistema-recomendacao
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a aplicação:

bash
Copiar
Editar
streamlit run app.py
🌐 Deploy
Este projeto está hospedado gratuitamente no Streamlit Cloud. Para hospedar o seu:

Crie um repositório no GitHub com seu código.

Acesse https://streamlit.io/cloud e conecte ao seu GitHub.

Escolha o repositório e a branch principal.

Configure o arquivo inicial (app.py) e publique.

📁 Estrutura do Projeto
bash
Copiar
Editar
├── app.py              # Código principal da aplicação Streamlit
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
📬 Contato
Desenvolvido por Gustavo Barbosa
📧 gustavobarbosa.dev [at] gmail.com
🔗 LinkedIn | GitHub

