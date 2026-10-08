# 🛍️ Challenge Alura Store — Qual loja vender?

Desafio de Data Science do programa **ONE (Oracle Next Education × Alura)**. Um proprietário possui quatro lojas e quer vender a unidade de menor potencial de retorno. Esta análise compara as lojas para embasar a decisão com dados.

---

## 🎯 Objetivo

Identificar a loja com menor desempenho geral considerando:

- Faturamento total
- Vendas por categoria
- Produtos mais e menos vendidos
- Média de avaliações dos clientes
- Frete médio

---

## 🧪 Metodologia

- Carga dos quatro arquivos CSV (`loja_1` a `loja_4`) a partir do [repositório público da Alura](https://github.com/alura-es-cursos/challenge1-data-science), com pandas.
- Cálculo do faturamento total de cada loja.
- Contagem das vendas por categoria (gráficos de barras).
- Média das avaliações e distribuição das notas (gráficos de pizza).
- Ranking dos produtos mais e menos vendidos.
- Frete médio por loja (gráfico de linha).
- Relatório final com a recomendação.

---

## 📊 Resultados

| Loja | Faturamento (R$) | Avaliação média | Frete médio (R$) |
|------|-----------------:|----------------:|-----------------:|
| 1 | 1.534.509,12 | 3,98 | 34,69 |
| 2 | 1.488.459,06 | 4,04 | 33,62 |
| 3 | 1.464.025,03 | 4,05 | 33,07 |
| 4 | 1.384.497,58 | 4,00 | 31,28 |

- Móveis e eletrônicos são as categorias mais vendidas em todas as lojas.
- Os produtos mais e menos vendidos têm volumes parecidos entre as unidades, sem vantagem competitiva clara.
- As avaliações são próximas (de 3,98 a 4,05).

---

## ✅ Conclusão

A **Loja 4** foi recomendada para venda: tem o menor faturamento (R$ 1.384.497,58) e não se destaca positivamente em categorias, avaliações ou produtos. Seu frete médio é o mais baixo (R$ 31,28), mas isso não compensa a menor receita.

---

## 🛠️ Tecnologias

- Python 3
- Pandas (e gráficos via Matplotlib)
- Google Colab / Jupyter Notebook

---

## 📁 Estrutura

```
Challenge-Alura-Store/
├── Eduardo Conti - AluraStoreBrasil.ipynb   # análise completa e relatório final
└── README.md
```

---

## ▶️ Como executar

1. Abra o notebook `Eduardo Conti - AluraStoreBrasil.ipynb` no Google Colab ou no Jupyter.
2. Execute as células em ordem. Os dados são carregados direto da internet, sem arquivos locais.

---

## 👨‍💻 Autor

Eduardo da Cunha Conti — Ciência da Computação.
