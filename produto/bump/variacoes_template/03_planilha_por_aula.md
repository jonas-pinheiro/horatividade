**Horatividade — método A.U.L.A. · Kit Diretriz Pedagógica**

# Variação de template — planilha por aula

**Quando usar:** a escola trabalha em planilha, ou você quer o formato-fonte mais poderoso: da planilha se filtra por bimestre, se conta aula, se reordena o ano e se gera o documento — o contrário não vale.

## Descrição para o seu `04_TEMPLATE.md`

```
Documento: planilha (.xlsx ou .csv), aba única "Planejamento",
uma linha por aula, ano inteiro.
Cabeçalho na linha 1, congelado. Colunas:
1. Nº  2. Data  3. Bimestre  4. Turma  5. Unidade  6. Conteúdo
7. Objetivo de aprendizagem  8. [Coluna do referencial]
9. Metodologia  10. Recursos  11. Instrumento avaliativo
Colunas 3, 8, 9 e 11 com lista fechada de valores (validação).
Datas em formato de data real (não texto), para ordenar e filtrar.
Uma linha por aula E por turma quando as turmas divergirem; turmas
com o mesmo plano compartilham a linha com a coluna Turma agregada.
```

## Prompt de geração

> Gere o planejamento anual como planilha por aula, conforme o 04_TEMPLATE: uma linha por aula, colunas com valores aceitos, datas cruzadas com o 01_CALENDARIO. Gere o arquivo .xlsx. [Sem geração de arquivo no seu plano: peça a tabela em CSV dentro de um bloco de código, salve como .csv e abra na planilha.]

## Por que a planilha é o formato-fonte

O documento em tabela (.docx) é a renderização para a coordenação. A planilha é o dado. Greve, ponte, semana perdida: ajusta o mapa, refaz as datas por fórmula ou por regeração, e o documento sai de novo. Mantenha a planilha como verdade e derive o resto.

## Modelo pronto

O arquivo `modelo_planilha.xlsx` do produto principal (pasta de formatos) já implementa esta variação, com cabeçalho travado e validações.

---
*Horatividade — método A.U.L.A. · v0.1.0 · agosto de 2026*
