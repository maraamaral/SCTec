# 🚢 Análise Exploratória - Dataset Titanic

Este projeto realiza uma análise exploratória do dataset **Titanic.csv**, com o objetivo de compreender as características populacionais dos passageiros e investigar os fatores associados à sobrevivência.

---

## 📌 Objetivos da análise
- Limpeza e organização dos dados (remoção, reordenação e renomeação de colunas).
- Tratamento de valores nulos de forma consistente.
- Verificação da premissa de que o valor do ticket reflete a classe social.
- Descrição das características populacionais dos passageiros por classe (idade e sexo).
- Descrição das características dos sobreviventes por classe (idade e sexo).
- Relação das chances de sobrevivência com classe, idade e sexo.
- Visualização comparativa com **star plot** (população geral vs sobreviventes).

---
## Análise
### Observações acerca das características populacionais dos passageiros:
Classe 1: Total de 216 pessoas.
          É a classe com a maior mediana de idade (37),
          formada por maioria de passageiros do sexo masculino (56,5%), adultos (75,5%).
          Possui a menor taxa de crianças pequenas (1,4%)
          e a maior taxa de idosos (6,5).
          É a classe com maior poder aquisitivo - maior valor médio pago pela tarifa (84,1547).

Classe 2: Total de 184 pessoas.
          Formada por maioria do sexo masculino (58,7%)
          também maioria adultos (66,8%),
          com uma taxa significativamente mais alta de crianças pequenas (8,2%)
          e jovens adultos (19,0%).
          É a classe menos populosa do navio (20,7% dos passageiros).

Classe 3: Total 491 pessoas
          É a classe mais populosa do navio (55,1%)
          e também a mais jovem (mediana 24),
          composta em sua maioria por jovens adultos (48,5%)
          e uma taxa significativamente maior de crianças maiores (9,4%).

### Observações acerca das características populacionais dos sobreviventes por classe:
A mediana da idade dos passageiros e sobreviventes não se alterou significativamente em nenhuma das classes, o que pode significar que a idade não foi fator determinante para a sobrevivência.
Já se comparado ao gênero, percebe-se que a taxa de sobrevivência foi muito maior entre mulheres que entre homens, o que pode indicar fatores sociais e costumes da época ("mulheres primeiro").
Percebe-se que a classe com a menor taxa de sobreviventes foi a 2 (25,4%) e que a classe 1 foi a que apresentou a maior proporção de sobreviventes - 39,8% dos passageiros da classe 1 sobreviveram.
A classe 3, manteve leve diferença para baixo em comparação à classe 1 o que foi uma surpresa nesta análise - esperava-se que esta diferença fosse maior.

## Conclusão
A análise demonstrou que, entre os fatores sociais avaliados — classe social, idade e gênero — o gênero foi o mais determinante para a sobrevivência.
Observou-se uma diferença significativa na taxa de sobrevivência entre passageiros da 1ª e 2ª classes, refletindo distintos níveis de poder aquisitivo. No entanto, essa diferença não se repetiu entre as classes 1ª e 3ª, apesar de também apresentarem desigualdade socioeconômica.
Esse resultado sugere que circunstâncias específicas impactaram negativamente a taxa de sobrevivência da 2ª classe, reduzindo-a de forma relevante. Contudo, os dados disponíveis não permitiram identificar com precisão quais fatores explicam essa discrepância.

## 📊 Resultados- Gráfico comparativo em formato star plot mostrando diferenças entre população geral e sobreviventes.

