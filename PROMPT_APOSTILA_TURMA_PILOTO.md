# Prompt pronto — Apostila de apoio da turma piloto (Claude Design)

> **Revisão:** 23/09/2026. Ajusta `PROMPT_APOSTILA_TURMA_PILOTO.md` (revisão de 08/09/2026).
>
> **O que mudou nesta versão:** a Seção 2 ganhou uma caixa explicando onde cada arquivo do repositório-modelo entra de fato na ferramenta (instruções do projeto × arquivos da base de conhecimento) e apresentou o sexto arquivo, `05_ATA_DO_PROJETO`, que antes não aparecia em lugar nenhum da apostila; a Seção 6 (Auditar) ganhou a linha que fecha o ciclo, ligando o checklist ao registro no `05_ATA_DO_PROJETO`; a Seção 1 ganhou uma caixa sobre limite de uso em ferramenta paga, com o pedido pronto para adiantar a conversão do material bruto em `.md` (e o calendário também em `.csv`) antes da sessão. Motivo: os seis arquivos do repositório-modelo estavam prontos mas a apostila só descrevia o conceito, sem amarrar ao uso mecânico — parecia que os modelos tinham sido feitos à toa; e faltava prever o caso de quem usa ferramenta com limite de uso mais apertado que o Claude gratuito.
>
> **Revisão anterior (08/09/2026):** "turma zero" passou a "turma piloto" em todo o material; a apostila passou a seguir a ordem A.U.L.A., com uma seção por bloco da sessão; entraram o mapa do método, o checklist de auditoria, a decisão de arquitetura de projetos, a entrevista reversa e o bloco de privacidade; o jargão técnico foi substituído por linguagem de professor; a extensão foi de 3–4 para 5–6 páginas A4.
>
> **Como usar:** cole tudo abaixo da linha no Claude Design. Anexe junto os arquivos `logo_horizontal.png`, `logo_sozinho.png`, `IDENTIDADE_VISUAL.md` e, se quiser que o texto saia com a redação exata em vez de resumida, os três materiais-fonte: `produto/principal/00_checklist_prerequisitos.md`, `produto/principal/01_tabela_equivalencia_ferramentas.md` e `produto/principal/03_bloco_diretriz_comentado.md`.
>
> O resultado é um HTML de poucas páginas, pensado para exportar em PDF e imprimir — é a "cola" que cada participante acompanha na própria tela ou no papel, e leva depois da sessão. **Não é o repositório-modelo** (esse já existe pronto em `produto/principal/repositorio_modelo/` e se entrega em pasta, sem precisar de design).

---

Monte uma apostila em HTML/CSS, em português do Brasil, para a marca **Horatividade** — material de apoio impresso/PDF para os participantes da sessão ao vivo "turma piloto", onde acompanham a montagem do próprio repositório de planejamento com IA. Formato A4, pensado para impressão (`@media print`, quebra de página limpa entre seções), mas também legível na tela. Extensão: o quanto o conteúdo abaixo pedir — não corte conteúdo para caber num número de páginas. É cola de consulta durante a sessão, não material de leitura — cada seção corresponde a um bloco da aula e precisa ser localizável de relance.

## Marca e direção visual

Seguir `IDENTIDADE_VISUAL.md`: fundo branco, preto `#060606` para texto e símbolo, dourado `#CE9631` só como acento (números de seção, títulos, linhas finas, checkboxes). Tipografia sans-serif geométrica (Inter ou DM Sans), hierarquia enxuta. Cantos retos ou raio pequeno, bordas finas em tabelas e caixas. Logo horizontal pequeno no cabeçalho de cada página; rodapé com "Horatividade — método A.U.L.A. · turma piloto" e numeração de página.

Cada seção de conteúdo leva, ao lado do título, a letra correspondente do método em dourado, grande, como marcador. Isso permite ao participante achar a página só olhando a lateral.

## Tom de voz (obrigatório)

Professor falando com professor. Direto, sem floreio. Proibido: emoji, exclamação, "transforme/revolucione/descomplique", clichê motivacional.

Proibido também jargão técnico: não usar "renderizar", "checkpoint", "hierarquia das fontes", "em lote", "métrica", "cota". Usar as formulações em linguagem de professor indicadas abaixo.

Não parafrasear pontos técnicos — nomes de arquivo, ordem de passos e frases para copiar saem com a redação exata.

## Estrutura e conteúdo

**Capa / topo da primeira página**

Logo horizontal. Título "Apostila da turma piloto". Subtítulo "Leve isto para a sessão — em tela ou impresso." Uma linha de instrução: "Cada seção corresponde a um bloco da sessão ao vivo. Acompanhe pela letra na lateral."

**Seção 0 — O caminho da tarde**

Meia página. As quatro letras do método, uma por linha: letra em destaque dourado, nome da etapa, uma frase de descrição, e o entregável à direita em peso menor precedido de seta.

```
A  Alimentar    Você monta a pasta que a IA lê      → os arquivos do seu ano
U  Uniformizar  Você ensina o formato que a sua     → o template virou regra
                escola exige
L  Ligar        Uma coisa puxa a outra              → o planejamento e os
                                                      planos de aula
A  Auditar      Você confere e assina               → o documento que você
                                                      entrega
```

Linha de fecho: "É isso, e é sempre nessa ordem."

**Seção 1 — Antes de começar**

Lista de checkbox (☐) com o texto exato de `produto/principal/00_checklist_prerequisitos.md`, seção "O essencial": calendário escolar do ano, grade de aulas, sumário/ementa do material, template da coordenação, referencial curricular, conta na ferramenta de IA. Acrescentar dois itens ao final da lista: "☐ Estou no computador, não no celular" e "☐ A ferramenta de IA está aberta agora".

Caixa menor, título "Se algo não existe do jeito ideal": apostila só em papel → fotografar o sumário; calendário só em imagem → subir e transcrever; escola sem ementa escrita → reconstruir a partir do sumário e aprovar.

Caixa de destaque com borda dourada, título "A primeira decisão da tarde":

> Um projeto por disciplina. Nunca um por turma.
> **Certo:** Física · História · Química — as turmas vivem dentro do projeto, identificadas numa coluna do template.
> **Errado:** 1ºA · 1ºB · 2ºA · 2ºB — cinco projetos gastos, e você fica sem projeto no meio do ano.

Caixa de destaque com borda dourada, título "Se sua ferramenta tem limite de uso":

> Ferramenta paga (ChatGPT, Gemini, Copilot) costuma ter limite de uso por sessão ou por dia. Pode não dar tempo de montar os cinco arquivos do zero numa tarde só — e não tem problema, dá pra continuar depois.
>
> Adiante o trabalho pesado antes da sessão: mande pra IA o material bruto que você já tem, do jeito que estiver (foto, PDF, texto solto), com este pedido, copiando e ajustando o nome do arquivo:
>
> "Organize isto em um arquivo `.md`, com o título `01_CALENDARIO`, mantendo todas as datas: [colar o material]." — troque `01_CALENDARIO` por `02_EMENTA`, `03_TURMAS` ou `04_TEMPLATE` conforme o material.
>
> Para o calendário, peça também: "gere uma segunda versão em `.csv`, uma linha por data." Facilita conferir e corrigir depois.
>
> Assim, se a sessão parar no meio — limite de uso, internet, o que for — você retoma com os arquivos já prontos pra revisar e subir, em vez de montar tudo de novo.

**Seção 2 — A · Alimentar: os arquivos**

Abrir com a definição do termo, em uma linha antes da tabela: "Repositório é a pasta que a IA lê antes de responder qualquer coisa."

Tabela de duas colunas (Camada / O que é) com Normativa, Operacional, Material, Realidade e Formal, com a descrição curta de cada uma (fonte: `CONTEXTO/Horatividade_Estrutura_do_Curso.md`, seção Aula 2).

Abaixo da tabela, os cinco nomes de arquivo em sequência com seta entre eles:

`00_DIRETRIZ` → `01_CALENDARIO` → `02_EMENTA` → `03_TURMAS` → `04_TEMPLATE`

Caixa de destaque com borda dourada, título "Onde cada arquivo entra na sua ferramenta" — este é o ponto em que o repositório-modelo deixa de ser teoria e vira ação, então vale o destaque:

- `00_DIRETRIZ` vai no campo **instruções do projeto** — não é arquivo anexado, é a regra permanente que vale para toda conversa.
- `01_CALENDARIO`, `02_EMENTA`, `03_TURMAS` e `04_TEMPLATE` sobem como **arquivos**, na base de conhecimento do projeto.
- Existe um sexto arquivo na pasta, `05_ATA_DO_PROJETO`. Você não preenche hoje: é onde registra, ao longo do ano, o que a IA errou e como você corrigiu — cada linha dali vira instrução nova na diretriz no ciclo seguinte.

Linha de fecho: "O repositório-modelo que você recebe já vem com essa divisão pronta. É só preencher e subir cada arquivo no lugar certo."

Caixa "Quando travar no perfil das turmas", com a frase em destaque, formatada para ser copiada literalmente:

> "Me faça as perguntas que faltam para montar o perfil das minhas turmas."

Linha abaixo: "Você responde falando, em dois minutos. A resposta vira o arquivo 03_TURMAS."

Caixa de privacidade, com borda mais forte, título "O que não sobe": nome de aluno · nota · laudo · contato de aluno ou de família · documento que não circula fora da escola. Uma linha de fecho: "Perfil de turma se descreve por característica, nunca por pessoa."

**Seção 3 — A · Alimentar: a diretriz pedagógica**

Lista numerada, nome de cada parte em negrito e uma frase curta do que resolve (fonte: `produto/principal/03_bloco_diretriz_comentado.md`), com estes rótulos:

1. **Quem eu sou e o que eu dou** — define a relação, não decisão pedagógica
2. **Qual arquivo manda quando dois se contradizem** — a ordem de prioridade
3. **Qual referencial vale** — a parte que se troca por escola
4. **As palavras que a coordenação usa** — nomenclatura exata, sinônimo volta corrigido
5. **O que nunca fazer** — nunca inventar código de habilidade
6. **O que fazer quando faltar informação** — perguntar, não preencher

Caixa de fecho da seção: "Peça o mesmo objetivo com dois referenciais diferentes. Se a saída mudar de estrutura e de vocabulário, a diretriz está mandando."

**Seção 4 — U · Uniformizar: o formato como regra**

Três passos numerados do template reverso:

1. Sobe o template vazio
2. Corrige o que a IA entendeu errado
3. Salva como `04_TEMPLATE`, regra permanente

Uma linha de fecho: "Gera uma vez. Salva no formato que cada um pede — documento para a coordenação, planilha para o sistema."

**Seção 5 — L · Ligar: o mapa do ano**

Três etapas em sequência horizontal, com as duas paradas marcadas entre elas:

```
Etapa 1 — Mapa do ano  →  confere e aprova  →  Etapa 2 — Distribuição
→  confere e aprova  →  Etapa 3 — Planejamento no formato
```

Linha abaixo: "Nada avança sem a sua aprovação. É o que evita descobrir na última página um erro que estava na primeira."

**Seção 6 — A · Auditar: as quatro passadas**

Lista de checkbox, dez minutos no total, nesta ordem:

- ☐ **Aritmética** — a soma das aulas fecha com o mapa do ano?
- ☐ **Códigos e nomenclatura** — nenhum código inventado, as palavras que a coordenação usa
- ☐ **Alinhamento pedagógico** — o verbo do objetivo bate com a atividade e com o instrumento
- ☐ **Viabilidade material** — cabe no tempo real da aula, usa recurso que existe na escola

Caixa de destaque, em corpo maior, como critério de fecho:

> "Um colega da sua disciplina daria essa aula amanhã só com esse papel na mão?"

Linha abaixo, corpo menor: "Toda correção que você fizer vale a pena registrar no `05_ATA_DO_PROJETO` — é o que evita o mesmo erro no bimestre seguinte, e é o único dos seis arquivos que você não termina hoje: ele cresce com o ano."

**Seção 7 — Tabela de equivalência entre ferramentas**

Reproduzir a tabela de `produto/principal/01_tabela_equivalencia_ferramentas.md` (linhas: Repositório, Arquivos do repositório, Bloco de diretriz, Conversa que enxerga tudo, Geração de .docx/.xlsx — colunas: Claude, ChatGPT, Gemini, Copilot). Abaixo, uma linha: "O nome do botão muda. A função não."

**Rodapé final (última página)**

Logo com slogan. Duas linhas:

"Depois da sessão, você recebe o repositório-modelo completo por e-mail."
"Em duas semanas eu volto com uma pergunta só: a coordenação aceitou?"

© Horatividade 2026.

## Requisitos técnicos

- HTML/CSS estático, um arquivo único, sem dependência de internet.
- `@media print` ajustado para A4, com `page-break-before` entre as seções.
- Tabelas com borda fina, sem cor de fundo alternada chamativa — a impressão em preto e branco precisa continuar legível, e as caixas de destaque precisam se distinguir por borda, não por preenchimento.
- Checkboxes desenhados como quadrado vazio com borda, preenchíveis à caneta.
