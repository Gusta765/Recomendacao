import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# =========================
# Configuração da página
# =========================
st.set_page_config(
    page_title="Sistema de Recomendação de Produtos",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar o visual - CORES CORRIGIDAS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .metric-card h3 {
        color: #667eea !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 14px;
    }
    .metric-card h2 {
        color: #2c3e50 !important;
        font-weight: bold;
        margin: 0;
        font-size: 24px;
    }
    .recommendation-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #e0e6ed;
    }
    .recommendation-card h3 {
        color: #2c3e50 !important;
        margin-bottom: 0.5rem;
    }
    .recommendation-card p {
        color: #34495e !important;
        margin: 0;
    }
    .sidebar-info {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
    }
    .sidebar-info h4 {
        color: #2c3e50 !important;
        margin-bottom: 0.5rem;
    }
    .sidebar-info ul {
        color: #34495e !important;
    }
    .sidebar-info li {
        color: #34495e !important;
    }
    .sidebar-info strong {
        color: #2c3e50 !important;
    }
    .stSelectbox > div > div {
        background-color: #f8f9fa;
    }
    .stSelectbox > div > div > div {
        color: #2c3e50 !important;
        background-color: white !important;
    }
    .stSelectbox > div > div > div > div {
        color: #2c3e50 !important;
    }
    .stSelectbox select {
        color: #2c3e50 !important;
        background-color: white !important;
    }
    .stSelectbox label {
        color: #2c3e50 !important;
        font-weight: 600;
    }
    /* Dropdown options */
    .stSelectbox > div > div > div[data-baseweb="select"] > div {
        color: #2c3e50 !important;
        background-color: white !important;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    /* Garantir que textos gerais sejam visíveis */
    .stMarkdown {
        color: #2c3e50;
    }
    /* Footer styling */
    .footer-text {
        color: #666 !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Header principal
# =========================
st.markdown("""
<div class="main-header">
    <h1>🛍️ Sistema Inteligente de Recomendação de Produtos</h1>
    <p>Descubra produtos similares baseados em análise de comportamento de compra utilizando Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# =========================
# Sidebar com informações
# =========================
with st.sidebar:
    st.markdown("### 📊 Informações do Sistema")
    st.markdown("""
    <div class="sidebar-info">
        <h4>🔬 Tecnologia Utilizada</h4>
        <ul>
            <li><strong>Algoritmo:</strong> Similaridade do Cosseno</li>
            <li><strong>Método:</strong> Filtragem Colaborativa</li>
            <li><strong>Base:</strong> Matriz Item-Item</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Configurações")

# =========================
# Geração de dados fictícios mais realistas
# =========================
@st.cache_data
def gerar_dados_ficticios():
    np.random.seed(42)
    
    # Produtos com nomes mais realistas
    categorias = {
        'Eletrônicos': ['Smartphone', 'Tablet', 'Fone', 'Carregador', 'Cabo USB'],
        'Casa': ['Panela', 'Toalha', 'Travesseiro', 'Cobertor', 'Aspirador'],
        'Roupas': ['Camiseta', 'Calça', 'Tênis', 'Jaqueta', 'Meia'],
        'Livros': ['Romance', 'Ficção', 'Biografia', 'Técnico', 'Infantil']
    }
    
    produtos_dict = {}
    produto_id = 1
    for cat, items in categorias.items():
        for item in items:
            produtos_dict[f"P{str(produto_id).zfill(3)}"] = f"{item} - {cat}"
            produto_id += 1
    
    clientes = [f"Cliente_{str(i).zfill(3)}" for i in range(1, 51)]
    produtos = list(produtos_dict.keys())
    
    dados = []
    for cliente in clientes:
        # Simular preferências por categoria
        n_compras = np.random.randint(5, 15)
        produtos_comprados = np.random.choice(produtos, size=n_compras, replace=False)
        
        for produto in produtos_comprados:
            quantidade = np.random.randint(1, 8)
            preco = np.random.uniform(10, 500)
            data_compra = datetime.now() - timedelta(days=np.random.randint(1, 365))
            
            dados.append([
                cliente, 
                produto, 
                produtos_dict[produto],
                quantidade, 
                preco,
                data_compra.strftime("%Y-%m-%d")
            ])
    
    return pd.DataFrame(dados, columns=[
        "ID Cliente", "ID Produto", "Nome Produto", "Quantidade", "Preço", "Data Compra"
    ])

df = gerar_dados_ficticios()

# =========================
# Métricas do sistema
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>📦 Produtos</h3>
        <h2>{}</h2>
    </div>
    """.format(df['ID Produto'].nunique()), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>👥 Clientes</h3>
        <h2>{}</h2>
    </div>
    """.format(df['ID Cliente'].nunique()), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>🛒 Transações</h3>
        <h2>{}</h2>
    </div>
    """.format(len(df)), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>💰 Faturamento</h3>
        <h2>R$ {:.0f}K</h2>
    </div>
    """.format((df['Quantidade'] * df['Preço']).sum() / 1000), unsafe_allow_html=True)

# =========================
# Processamento dos dados
# =========================
@st.cache_data
def calcular_similaridade(dataframe):
    matriz_utilidade = dataframe.pivot_table(
        index='ID Produto',
        columns='ID Cliente',
        values='Quantidade',
        fill_value=0
    )
    
    matriz_similaridade = cosine_similarity(matriz_utilidade)
    df_similaridade = pd.DataFrame(
        matriz_similaridade,
        index=matriz_utilidade.index,
        columns=matriz_utilidade.index
    )
    
    return df_similaridade, matriz_utilidade

df_similaridade, matriz_utilidade = calcular_similaridade(df)

# =========================
# Interface principal
# =========================
st.markdown("## 🎯 Motor de Recomendação")

col1, col2 = st.columns([2, 1])

with col1:
    # Criar dicionário para exibição
    produto_display = df[['ID Produto', 'Nome Produto']].drop_duplicates().set_index('ID Produto')['Nome Produto'].to_dict()
    produto_options = [f"{k} - {v}" for k, v in produto_display.items()]
    
    produto_selecionado = st.selectbox(
        "🔍 Selecione um produto para receber recomendações:",
        produto_options,
        help="Escolha um produto da lista para ver produtos similares"
    )
    
    produto_id = produto_selecionado.split(' - ')[0]

with col2:
    n_recomendacoes = st.slider(
        "📊 Número de recomendações:",
        min_value=1,
        max_value=10,
        value=5,
        help="Quantidade de produtos similares a serem exibidos"
    )

# Botão de recomendação
if st.button("🚀 Gerar Recomendações", type="primary"):
    if produto_id not in df_similaridade.index:
        st.error("❌ Produto não encontrado na base de dados!")
    else:
        # Calcular similaridades
        similaridades = df_similaridade.loc[produto_id].drop(produto_id)
        recomendados = similaridades.sort_values(ascending=False).head(n_recomendacoes)
        
        # Preparar dados para exibição
        recomendacoes_data = []
        for prod_id, similaridade in recomendados.items():
            nome_produto = produto_display[prod_id]
            vendas_totais = df[df['ID Produto'] == prod_id]['Quantidade'].sum()
            preco_medio = df[df['ID Produto'] == prod_id]['Preço'].mean()
            
            recomendacoes_data.append({
                'Produto': nome_produto,
                'Similaridade (%)': f"{similaridade * 100:.1f}%",
                'Vendas Totais': vendas_totais,
                'Preço Médio': f"R$ {preco_medio:.2f}",
                'Score': similaridade
            })
        
        df_recomendacoes = pd.DataFrame(recomendacoes_data)
        
        # Exibir recomendações
        st.markdown(f"""
        <div class="recommendation-card">
            <h3>🎁 Produtos Recomendados para: {produto_display[produto_id]}</h3>
            <p>Baseado em padrões de compra de clientes similares</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabela de recomendações
        st.dataframe(
            df_recomendacoes[['Produto', 'Similaridade (%)', 'Vendas Totais', 'Preço Médio']],
            use_container_width=True,
            hide_index=True
        )
        
        # Gráfico de similaridade
        fig = px.bar(
            df_recomendacoes,
            x='Score',
            y='Produto',
            orientation='h',
            title='📈 Índice de Similaridade dos Produtos Recomendados',
            labels={'Score': 'Similaridade', 'Produto': 'Produtos'},
            color='Score',
            color_continuous_scale='viridis'
        )
        fig.update_layout(
            height=400,
            yaxis={'categoryorder': 'total ascending'},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Análise adicional
# =========================
st.markdown("## 📈 Análise de Dados")

tab1, tab2, tab3 = st.tabs(["🔥 Produtos Populares", "💹 Análise de Vendas", "🔗 Matriz de Similaridade"])

with tab1:
    produtos_populares = df.groupby(['ID Produto', 'Nome Produto']).agg({
        'Quantidade': 'sum',
        'ID Cliente': 'nunique'
    }).reset_index()
    produtos_populares.columns = ['ID Produto', 'Nome Produto', 'Total Vendido', 'Clientes Únicos']
    produtos_populares = produtos_populares.sort_values('Total Vendido', ascending=False).head(10)
    
    fig_pop = px.bar(
        produtos_populares,
        x='Total Vendido',
        y='Nome Produto',
        orientation='h',
        title='Top 10 Produtos Mais Vendidos',
        color='Total Vendido',
        color_continuous_scale='blues'
    )
    fig_pop.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_pop, use_container_width=True)

with tab2:
    vendas_por_mes = df.copy()
    vendas_por_mes['Data Compra'] = pd.to_datetime(vendas_por_mes['Data Compra'])
    vendas_por_mes['Mês'] = vendas_por_mes['Data Compra'].dt.to_period('M')
    vendas_mensal = vendas_por_mes.groupby('Mês')['Quantidade'].sum().reset_index()
    vendas_mensal['Mês'] = vendas_mensal['Mês'].astype(str)
    
    fig_vendas = px.line(
        vendas_mensal,
        x='Mês',
        y='Quantidade',
        title='📊 Evolução das Vendas por Mês',
        markers=True
    )
    fig_vendas.update_layout(height=400)
    st.plotly_chart(fig_vendas, use_container_width=True)

with tab3:
    st.markdown("### 🔗 Heatmap da Matriz de Similaridade")
    
    # Selecionar apenas uma amostra para melhor visualização
    sample_products = df_similaridade.index[:10]
    similarity_sample = df_similaridade.loc[sample_products, sample_products]
    
    fig_heatmap = px.imshow(
        similarity_sample.values,
        x=[produto_display.get(p, p) for p in similarity_sample.columns],
        y=[produto_display.get(p, p) for p in similarity_sample.index],
        color_continuous_scale='RdYlBu_r',
        title='Matriz de Similaridade entre Produtos (Amostra)',
        aspect='auto'
    )
    fig_heatmap.update_layout(height=600)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p class="footer-text">🚀 Sistema de Recomendação desenvolvido com Streamlit e Scikit-learn</p>
    <p class="footer-text">📧 Algoritmo: Similaridade do Cosseno | 🔄 Atualizado automaticamente</p>
</div>
""", unsafe_allow_html=True)