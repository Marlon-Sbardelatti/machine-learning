# Trabalho 1: Regressão

## Fase 1: Análise de Correlação e Regressão Linear

#### 3. Qual dos datasets não é apropriado para regressão linear? Justifique sua resposta.

Apesar de todos os datasets demonstrarem um alto coeficiente de correlação positivo (maior que 0.8), a análise visual dos gráficos gerados permitiu a identificação de algumas inconsistências em relação ao modelo de regressão linear. A equipe aponta como não apropriados:

- **Dataset 2**: Os pontos do dataset original evidenciam um formato curvilíneo característico da regressão polinomial negativa.

- **Dataset 3**:

#### 4. Ao analisar o gráfico de dispersão e o resultado da regressão linear para o dataset 4, observa-se um problema. O que deveria ser feito antes de ajustar o modelo de regressão? Justifique sua resposta.

O problema é a presença do outlier A(13, 12.74) nos dados de entrada. Ele, justamente por ter valor tão diferente da grande maioria dos dados, tem poder de distorcer valores - como a inclinação da reta.

Antes de ajustar o modelo de regressão, deve-se verificar se é possível (e necessário) realizar algum tratamento nos dados. Esse ponto que é um outlier, por exemplo, pode ser resultado de medição incorreta ou dados fora do escopo.

Para verificar se a remoção do outlier é uma decisão correta (e não somente inserção de viés no dataset), deve ser analisada sua adequação ao conjunto de dados/contexto e o impacto de sua remoção no desempenho do modelo através de métricas como o R² e o EQM.
