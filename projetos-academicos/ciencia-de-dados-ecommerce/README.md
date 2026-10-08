# 🛒 E-commerce Data Analysis — Amazon & Olist

Projeto de Ciência de Dados desenvolvido como trabalho acadêmico, com análise exploratória, construção de KPIs, visualizações e aplicação de algoritmos de Machine Learning sobre dois datasets de e-commerce: **Amazon Sales** (mercado indiano) e **Olist** (e-commerce brasileiro).

---

## 📦 Datasets

### Amazon Sales Dataset
Dataset com produtos vendidos na Amazon India, contendo informações de preço, desconto, avaliação dos usuários e categorias.
Fonte: [Kaggle — Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)

### Olist Brazilian E-commerce
Dataset público do e-commerce brasileiro Olist, composto por 8 tabelas relacionais cobrindo pedidos, clientes, produtos, vendedores, pagamentos, avaliações e geolocalização.
Fonte: [Kaggle — Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 🗂️ Estrutura do Repositório

```
Ecommerce-Data-Analysis/│
├── scripts/
│   ├── data_analysis.ipynb   # Notebook principal com todo o projeto (Amazon + Olist)
│   └── data_analysis.py      # Script Python standalone com ETL, KPIs e dashboards do Olist
│
├── .gitignore
└── README.md
```

> **Nota:** os arquivos `.csv` dos datasets não estão incluídos no repositório por conta do tamanho. Faça o download diretamente pelos links do Kaggle acima. No notebook, os caminhos estão configurados para o Google Drive — ajuste conforme seu ambiente.

---

## 🎯 O que o projeto faz

### 1. ETL — Amazon Sales
- Remoção de colunas irrelevantes (`img_link`, `product_link`)
- Limpeza e conversão de tipos: `rating_count`, `discounted_price`, `actual_price`, `discount_percentage`, `rating`
- Remoção de caracteres especiais (`₹`, `%`, `|`, `,`)
- Conversão de moeda: rúpias → reais (×0,057)
- Remoção de nulos e duplicatas por `product_id`
- Explode de categorias múltiplas (separadas por `|`)
- Feature Engineering: `faixa_preco`, `faixa_desconto` com `pd.cut`

### 2. ETL — Olist
- Limpeza de nulos e duplicatas em todas as 8 tabelas
- Remoção de colunas com alto índice de nulos (`review_comment_title`, `review_comment_message`, `order_approved_at`, etc.)
- Conversão de timestamps para `datetime`
- Tradução de categorias via `product_category_name_translation`
- Deduplicação da tabela de geolocalização
- Merge relacional de 8 tabelas em uma base consolidada
- Feature Engineering: `discount_value`, `discount_pct` calculados a partir do cruzamento entre subtotal e valor pago
- Filtro de pedidos com `order_status == 'delivered'` como base para os KPIs

---

## 📊 KPIs Construídos

### KPIs de Preço (Olist)
| # | Indicador |
|---|-----------|
| 1 | Preço médio dos produtos |
| 2 | Preço médio por categoria |
| 3 | Preço máximo |
| 4 | Preço mínimo e desvio padrão |
| 5 | Percentual médio de desconto |
| 6 | Valor médio de desconto |
| 7 | Produtos com maior desconto |
| 8 | Produtos com menor desconto |

### KPIs de Avaliação (Olist)
| # | Indicador |
|---|-----------|
| 9 | Rating médio dos produtos |
| 10 | Rating médio por categoria (mín. 50 reviews) |
| 11 | Produtos com maior rating (mín. 10 reviews) |
| 12 | Produtos com menor rating (mín. 10 reviews) |
| 13 | Produtos com maior número de reviews |
| 14 | Distribuição de ratings |
| 15 | Correlação rating vs preço |
| 16 | Correlação rating vs desconto |

### KPIs de Produtos (Olist)
| # | Indicador |
|---|-----------|
| 17 | Número total de produtos |
| 18 | Número de categorias |
| 19 | Produtos por categoria |
| 20 | Categoria com maior número de produtos |
| 21 | Produto mais caro |
| 22 | Produto mais barato |
| 23 | Produto mais avaliado (nº de reviews) |
| 24 | Produto com melhor avaliação |
| 25 | Reviews por categoria |

### KPIs — Amazon Sales
- 10 produtos mais caros e mais baratos
- 10 produtos com maior e menor rating
- 10 produtos com maior nº de avaliações
- Produtos com maior e menor desconto
- Distribuição de avaliações por preço e por faixa de desconto
- Preço médio por categoria
- Rating médio por categoria

---

## 📈 Visualizações

### Amazon
- Scatter: avaliação × preço
- Scatter: avaliação × desconto
- Histograma: distribuição de avaliações
- Histograma: distribuição de preços

### Olist (dashboard com 8 subplots)
- Preço médio por categoria (Top 15)
- Distribuição de preços com média, mínimo e máximo
- Distribuição do percentual de desconto
- Distribuição de ratings (com média)
- Rating médio por categoria
- Correlação rating vs preço (scatter com linha de tendência)
- Produtos por categoria (Top 15)
- Reviews por categoria (Top 15)

---

## 🤖 Machine Learning

### Amazon
| Algoritmo | Objetivo |
|---|---|
| Regressão Linear | Prever rating a partir de preço e desconto |
| Regressão Logística | Classificar se produto tem rating ≥ 4 (`bom_produto`) |
| K-Means | Segmentar produtos por preço, desconto, rating e nº de reviews |
| DBSCAN | Detectar outliers em preço e desconto |

### Olist
| Algoritmo | Objetivo |
|---|---|
| Regressão Linear | Prever `review_score` a partir de preço, frete e desconto |
| Árvore de Decisão | Classificar review alto/baixo (`review_score ≥ 4`) |
| K-Means | Segmentar vendedores por receita, pedidos, rating e preço médio |

---

## 📐 Métricas de Avaliação

- **Regressão Linear:** R² e RMSE
- **Regressão Logística:** Acurácia, Precisão, Recall, F1-Score, Matriz de Confusão
- **Árvore de Decisão:** Acurácia, Matriz de Confusão, visualização da árvore
- **K-Means:** Método do cotovelo (inércia por K), perfil de cada cluster

---

## 🧠 Conceitos de Ciência de Dados Aplicados

| # | Conceito |
|---|---|
| 1 | Coleta de Dados |
| 2 | Limpeza e Pré-processamento (Limpeza, Integração, Transformação) |
| 3 | Estatísticas Descritivas (média, mediana, moda, desvio padrão) |
| 4 | Definição e Construção de KPIs |
| 5 | Visualização de Dados e Dashboards |
| 6 | Transformação de Dados e Feature Engineering |
| 7 | Modelagem Preditiva (Regressão Linear, Regressão Logística, Árvore de Decisão) |
| 8 | Machine Learning — Clusterização (K-Means, DBSCAN) |
| 9 | Métricas de Avaliação de Modelos (Precisão, Recall, F1-Score, Matriz de Confusão) |

---

## 🛠️ Ferramentas e Bibliotecas

| Ferramenta | Uso |
|---|---|
| `Python 3.x` | Linguagem principal |
| `pandas` | Manipulação e análise de dados |
| `numpy` | Operações numéricas |
| `matplotlib` | Visualizações e dashboards |
| `seaborn` | Gráficos estatísticos |
| `scikit-learn` | Machine Learning (modelos, métricas, pré-processamento) |
| `Google Colab` | Ambiente de execução do notebook |

---

## ▶️ Como Executar

### Notebook (Google Colab)
1. Faça upload dos datasets para o Google Drive
2. Abra `scripts/data_analysis.ipynb` no Google Colab
3. Ajuste os caminhos de leitura dos CSVs para o seu Drive
4. Execute as células em ordem

### Script Python (local)
1. Clone o repositório e instale as dependências:
```bash
git clone https://github.com/EduardoCunhaConti/Ecommerce-Data-Analysis.git
cd Ecommerce-Data-Analysis
pip install pandas numpy matplotlib seaborn scikit-learn
```
2. Coloque os arquivos `.csv` do Olist em uma pasta `data/` na raiz do projeto
3. Execute o script:
```bash
python scripts/data_analysis.py
```

---

## 👤 Autor

Desenvolvido por Eduardo da Cunha Conti como projeto da disciplina de Ciência de Dados.
