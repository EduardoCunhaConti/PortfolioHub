# Challenge-Alura-TelecomX
## 📊 Análise de Evasão de Clientes (Churn) - Telecom

### 📌 Sobre o Projeto

Este projeto tem como objetivo analisar os fatores associados à evasão de clientes (Churn) em uma empresa de telecomunicações.

A evasão de clientes impacta diretamente a receita e a sustentabilidade do negócio. Através de técnicas de Análise Exploratória de Dados (EDA), buscamos identificar padrões que expliquem o comportamento de cancelamento e gerar insights estratégicos para retenção.

---

### 🎯 Objetivos

- Realizar limpeza e tratamento dos dados
- Explorar padrões associados ao churn
- Identificar variáveis mais relevantes
- Gerar insights estratégicos
- Preparar o dataset para futura modelagem preditiva

---

### 📥 Fonte dos Dados

Os dados foram importados via API no formato `.json` e convertidos para `pandas DataFrame`.

---

### 🧹 Limpeza e Tratamento de Dados

Durante o pré-processamento foram realizadas as seguintes etapas:

- Conversão de tipos de dados
- Tratamento de valores ausentes
- Substituição de strings vazias por `NaN`
- Conversão de variáveis binárias (Yes/No → 1/0)
- Verificação de duplicidades
- Padronização de categorias

Valores ausentes identificados:

- 224 registros em `Churn`
- 11 registros em `Charges.Total`

Após o tratamento, o dataset ficou consistente e pronto para análise.

---

## 🛠️ Tecnologias

- Python 3, pandas e NumPy (tratamento e análise)
- Matplotlib (visualizações)
- requests (importação dos dados via API)
- Jupyter Notebook / Google Colab

---

## 📁 Estrutura do projeto

```
Challenge-Alura-TelecomX/
├── Alura_TelecomX.ipynb   # importação, limpeza, EDA e relatório final
└── README.md
```

---

## ▶️ Como executar

1. Abra `Alura_TelecomX.ipynb` no Google Colab ou no Jupyter.
2. Execute as células em ordem. Os dados são importados via API pelo próprio notebook.

---

## 🔗 Próxima etapa

A modelagem preditiva desta análise está em [Challenge-Alura-TelecomX-Parte-2](https://github.com/EduardoCunhaConti/Challenge-Alura-TelecomX-Parte-2).

---

## 📊 Análise Exploratória de Dados (EDA)

### 📌 Distribuição da Variável Alvo

- ~73% dos clientes permaneceram
- ~27% cancelaram

Indica leve desbalanceamento da variável alvo.

---

### 📌 Principais Variáveis Categóricas Analisadas

- Gênero
- Tipo de contrato
- Método de pagamento
- Serviços adicionais

#### 🔎 Insights

- Clientes com contrato mensal possuem maior taxa de evasão.
- Contratos de 1 e 2 anos apresentam menor churn.
- Métodos de pagamento automáticos reduzem a probabilidade de cancelamento.
- Gênero não demonstrou influência significativa.

---

### 📌 Variáveis Numéricas

Analisadas:

- `tenure` (tempo de contrato)
- `Charges.Monthly`
- `Charges.Total`

#### 🔎 Insights

- Clientes que cancelam possuem menor tempo médio de permanência.
- A evasão ocorre principalmente nos primeiros meses.
- Clientes com menor valor acumulado gasto tendem a cancelar mais.

---

## 📈 Principais Insights Estratégicos

1. Contratos mensais apresentam maior risco de evasão.
2. O período inicial do contrato é crítico para retenção.
3. Pagamentos automáticos aumentam fidelização.
4. O tempo de permanência é forte indicador de churn.

---

## 🚀 Recomendações

- Incentivar contratos de longo prazo.
- Criar programa de retenção nos primeiros meses.
- Oferecer benefícios para pagamento automático.
- Desenvolver modelo preditivo de churn.

---

## 👨‍💻 Autor

Eduardo da Cunha Conti — Challenge de Data Science do programa ONE (Oracle Next Education × Alura).
