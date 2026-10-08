# 🤖 TelecomX — Previsão de Churn com Machine Learning

Segunda etapa do Challenge de Data Science do programa **ONE (Oracle Next Education × Alura)**. A [Parte 1](https://github.com/EduardoCunhaConti/Challenge-Alura-TelecomX) analisou por que os clientes cancelam; aqui o objetivo é **prever** quais clientes têm risco de cancelar, para que a empresa aja antes da perda.

---

## 🎯 Objetivo

- Treinar modelos de classificação para prever o churn
- Avaliar os modelos com acurácia, precisão, recall, F1-score e matriz de confusão
- Identificar as variáveis que mais pesam na decisão de cancelamento

---

## 📦 Dados

- **7.043 clientes** após o tratamento (arquivo `dados_tratados.csv`)
- 5.174 permaneceram (**73,46%**) e 1.869 cancelaram (**26,54%**): base desbalanceada

---

## 🧹 Preparação dos dados

- Remoção do identificador `customerID`
- Separação das colunas em numéricas e categóricas
- `OneHotEncoder` aplicado às categóricas (`gender`, `InternetService`, `Contract`, `PaymentMethod`)
- Divisão **80% treino / 20% teste**, estratificada pelo churn (`random_state=42`): 5.634 clientes para treino e 1.409 para teste
- Valores ausentes preenchidos com a **mediana do conjunto de treino**
- `StandardScaler` para a Regressão Logística

> **Nota:** nesta versão o treinamento usa as 15 variáveis numéricas/binárias (`tenure`, `Charges.Monthly`, `Charges.Total`, serviços contratados etc.). As categóricas codificadas ainda não entram no treino (veja *Próximos passos*).

---

## 🤖 Modelos

| Modelo | Configuração |
|---|---|
| Regressão Logística | `max_iter=1000`, dados padronizados |
| Random Forest | `random_state=42` |

---

## 📊 Resultados (conjunto de teste — 1.409 clientes)

| Modelo | Acurácia | Precisão (churn) | Recall (churn) | F1 (churn) |
|---|---:|---:|---:|---:|
| Regressão Logística | 0,795 | 0,650 | 0,492 | 0,560 |
| Random Forest | 0,789 | 0,638 | 0,471 | 0,542 |

Matrizes de confusão (linhas = real, colunas = previsto):

- **Regressão Logística:** `[[936, 99], [190, 184]]`
- **Random Forest:** `[[935, 100], [198, 176]]`

**Leitura dos resultados:** os dois modelos acertam cerca de 79% das previsões, mas capturam menos da metade dos cancelamentos (recall entre 47% e 49%). Ou seja, são conservadores ao apontar churn.

---

## 🔎 Variáveis mais relevantes

- **Random Forest (importância):** `Charges.Monthly` (0,252), `Charges.Total` (0,250) e `tenure` (0,214).
- **Regressão Logística (coeficientes):** `tenure` é o fator que mais reduz a chance de cancelamento (−1,61) e `Charges.Monthly` o que mais a aumenta (+1,15).

Em resumo: clientes novos e com mensalidade alta têm maior risco de cancelar.

---

## 🚀 Próximos passos

- Incluir no treino as variáveis categóricas codificadas, especialmente `Contract`, principal fator da Parte 1
- Tratar o desbalanceamento (pesos de classe ou reamostragem) e ajustar o limiar de decisão para aumentar o recall
- Testar outros algoritmos (KNN, SVM) e usar validação cruzada com ajuste de hiperparâmetros

---

## 🛠️ Tecnologias

Python 3 · pandas · scikit-learn · Matplotlib · Seaborn · Google Colab / Jupyter

---

## 📁 Estrutura do projeto

```
Challenge-Alura-TelecomX-Parte-2/
├── Challenge Alura_TelecomX_Parte_2.ipynb   # preparação, modelagem e avaliação
├── dados_tratados.csv                       # dados tratados usados na modelagem
└── README.md
```

---

## ▶️ Como executar

```bash
git clone https://github.com/EduardoCunhaConti/Challenge-Alura-TelecomX-Parte-2.git
cd Challenge-Alura-TelecomX-Parte-2
pip install pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook
```

1. Abra `Challenge Alura_TelecomX_Parte_2.ipynb`.
2. O notebook lê `/content/dados_tratados.csv` (caminho do Google Colab). No Colab, envie o CSV para a pasta `/content`; localmente, ajuste a variável `url` na segunda célula.
3. Execute as células em ordem.

---

## 👨‍💻 Autor

Eduardo da Cunha Conti — Ciência da Computação.
