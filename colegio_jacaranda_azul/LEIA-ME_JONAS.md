# Colégio Jacarandá Azul — kit da demo ao vivo

> **Só para você. Este arquivo não sobe para o Claude.** Escola, apostila ("Sistema Ápice de Ensino"), portal e horários são fictícios. Cada arquivo tem um rodapé discreto "Documento fictício · demonstração Horatividade".
> O calendário usa exatamente as datas do Colégio Exemplo (2027, bimestral), então todos os gabaritos do repo continuam valendo.

## O que tem em cada pasta

| Pasta | Arquivo | Como a escola "entregaria" |
|---|---|---|
| 01_comum | `Calendario_Escolar_2027.pdf` | PDF de 2 páginas: grade colorida dos 12 meses + lista de datas |
| 01_comum | `Comunicado_02-2027_Orientacoes_Planejamento.pdf` | Comunicado da coordenação: Bloom, listas fechadas, recursos, prazo |
| 01_comum | `Modelo_Planejamento_Anual_FII_2027.docx` | Word do Fundamental II: planejamento anual de conteúdos (tabela por bimestre) |
| 01_comum | `Modelo_Plano_de_Aula_FII_2027.docx` | Word do Fundamental II: plano de aula de uma página (desenvolvimento, avaliação, adaptações) |
| 01_comum | `Planilha_Planejamento_EM_2027.xlsx` | Planilha do Ensino Médio: abas Planejamento Anual (com soma automática por bimestre) e Planos de Aula (uma linha por aula), com listas suspensas |
| 02_fisica | `Print_Horario_Professor_Fisica.png` | Print do portal da escola |
| 02_fisica | `Print_Sumario_Apostila_Fisica_1EM.png` | Print da plataforma da apostila |
| 03_historia | `Print_Horario_Professor_Historia.png` | Print do portal da escola |
| 03_historia | `Print_Sumario_Apostila_Historia_8ano.png` | Print da plataforma da apostila |

**A regra dos modelos está no comunicado:** Fundamental II entrega em Word, Ensino Médio entrega na planilha. Então Física (1º EM) sai em .xlsx e História (8º ano) sai em .docx, com os mesmos arquivos comuns nos dois projetos. Quem escolhe o formato é o documento da escola, não você.

O que **não** tem arquivo, de propósito: perfil das turmas. Isso nenhuma escola entrega; sai da entrevista reversa (cola abaixo).

## Prompts

Os prompts atualizados (com os nomes 00_DIRETRIZ a 04_TEMPLATE, iguais aos da apostila e dos slides) estão no roteiro da sessão, com botão de copiar. Use o roteiro como referência principal.

## Cola da entrevista reversa (o que responder quando o Claude perguntar)

**Física — 1ª série EM**
- 1ºA, 28 alunos: heterogênea; um terço veio de fora da rede e tem defasagem em frações e potências de dez. Vai bem em atividade prática, dispersa em exposição longa.
- 1ºB, 25 alunos: ritmo uniforme, autônoma em exercício, responde bem a estudo dirigido. Resolve certo e registra mal.
- 1ºC, 22 alunos: menor e mais dispersa; dificuldade com leitura de gráficos. Rende em atividades curtas com fechamento a cada bloco.

**História — 8º ano**
- 8ºA, 30 alunos: participa muito em discussão oral, mas lê pouco texto longo. Confunde cronologia (antes/depois, séculos). Gosta de trabalhar com imagem e fonte curta.

## Gabarito (conferido dia a dia por script)

**Aulas efetivas por bimestre** (descontados feriados, recessos e semanas de avaliação):

| Turma | Dias | 1º | 2º | 3º | 4º | Ano |
|---|---|---|---|---|---|---|
| 1ºA | ter/qui | 17 | 21 | 17 | 16 | **71** |
| 1ºB | seg/qua | 16 | 21 | 18 | 17 | **72** |
| 1ºC | qua/sex | 16 | 20 | 18 | 17 | **71** |
| 8ºA | seg/qua | 16 | 21 | 18 | 17 | **72** |

Pergunta-teste do Alimentar: "quantas aulas de Física a 1ºA tem no 2º bimestre?" → **21**.

**Datas do 1º bimestre**
- 1ºA: 02/02, 04/02, 11/02, 16/02, 18/02, 23/02, 25/02, 02/03, 04/03, 09/03, 11/03, 16/03, 18/03, 23/03, 25/03, 30/03, 01/04 (17)
- 8ºA: 01/02, 03/02, 15/02, 17/02, 22/02, 24/02, 01/03, 03/03, 08/03, 10/03, 15/03, 17/03, 22/03, 24/03, 29/03, 31/03 (16)

**Conflito com a apostila** (é o que força o corte ao vivo)
- Física: apostila sugere **80 aulas** (11 capítulos, com Estática no cap. 7) para **71** disponíveis, antes de reservar revisão, exercícios e folga. Por caderno: 20 · 27 · 15 · 18 contra 17 · 21 · 17 · 16.
- História: apostila sugere **77 aulas** (14 capítulos) para **72**. Por caderno: 16 · 23 · 23 · 15 contra 16 · 21 · 18 · 17.

## Armadilhas plantadas (bons momentos de Auditar)

1. **Carnaval:** 08/02 (seg) e 10/02 (qua) são recesso, 09/02 (ter) é feriado. A 1ºA perde a terça; a 8ºA perde segunda **e** quarta. Qualquer aula nessas datas é erro.
2. **Semana de avaliações:** o calendário marca em cor e a observação 1 diz "não há aula regular". Se o Claude contar essas semanas, o número passa do gabarito.
3. **Cadernos × bimestres:** a apostila tem 4 cadernos que parecem bimestres, mas não cabem neles. Se o Claude simplesmente seguir os cadernos, estoura a conta.
4. **Laboratório:** no máximo uma aula por turma a cada três semanas. Física com "demonstração experimental" toda semana é erro.
5. **Modelo errado:** Física é Ensino Médio → planilha. Se sair Word para Física (ou planilha para História), o Claude não aplicou a regra do comunicado.
6. **Sábados:** Festa Junina (19/06), Feira de Ciências (18/09) e conselhos são sábado; não geram nem tiram aula.
7. **Coerência plano → planejamento:** todo plano de aula precisa preencher "Ref. planejamento". Soma dos planos de um bimestre = aulas efetivas do gabarito.
8. **Planilha que se audita sozinha:** na aba Planejamento Anual, preencha as aulas efetivas do gabarito na coluna amarela do resumo; a diferença aparece na hora. Diferença negativa = planejou mais aulas do que existem.

## Sequência

Está no roteiro da sessão (HTML), bloco a bloco, com horários, slides, arquivos e prompts.
