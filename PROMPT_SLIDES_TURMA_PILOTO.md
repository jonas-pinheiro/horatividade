# Prompt pronto — Slides de apoio da turma piloto (Claude Design)

> Cole tudo abaixo da linha no Claude Design. Anexe junto os arquivos `logo_horizontal.png`, `logo_sozinho.png`, `logo_texto_slogan.png` e `IDENTIDADE_VISUAL.md`. O resultado é um deck HTML único, para tela cheia no notebook durante a sessão ao vivo — não é o material de venda, é o apoio visual enquanto você fala e demonstra na ferramenta de IA. Depois de gerado, abra no navegador e teste a navegação por teclado antes do dia da sessão.

---

Monte um deck de slides em HTML/CSS, em português do Brasil, para a marca **Horatividade** — apoio visual de uma sessão AO VIVO chamada "turma piloto", onde o professor Jonas ensina o método A.U.L.A. a um pequeno grupo de colegas professores, compartilhando a tela do notebook. A maior parte da aula é demonstração ao vivo dentro da ferramenta de IA, não slide — os slides aparecem só nos momentos de conceito, antes ou depois da demonstração. Por isso: pouco texto por slide, letra grande (a tela será compartilhada em videochamada, às vezes em resolução reduzida), no máximo 4-5 linhas de conteúdo por slide além do título.

## Marca e direção visual

Seguir `IDENTIDADE_VISUAL.md` à risca: fundo predominante branco, preto `#060606` para tipografia e símbolo, dourado `#CE9631` só como acento (títulos de destaque, numeração, linhas divisórias, o "A" de HORATIVIDADE). Tipografia sans-serif geométrica (Inter ou DM Sans). Sem emoji, sem exclamação, sem gradiente, sem sombra pesada. Formato 16:9. Logo horizontal pequeno no canto de cada slide de conteúdo; logo com slogan no slide de abertura e no de fechamento.

## Tom de voz (obrigatório)

Professor falando com professor — ver `CONTEXTO/VOZ.md` se anexado. Frases curtas, diretas. Proibido: "transforme", "revolucione", "descomplique", clichê motivacional, emoji, ponto de exclamação.

## Requisitos técnicos

- Um único arquivo HTML autocontido (CSS embutido, sem dependência de internet — Jonas vai apresentar ao vivo e não pode depender de CDN de fonte; usar `font-family` com fallback de sistema caso a fonte não carregue).
- Navegação por seta do teclado (→/←) e por clique; contador de slide discreto no canto (ex. "6/20").
- Também precisa funcionar bem impresso/exportado em PDF como cópia de segurança (`@media print`, um slide por página).
- Sem animação que dependa de clique duplo ou timing — Jonas está com atenção dividida entre falar, compartilhar tela e trocar de slide.

## Estrutura do deck — 22 slides, na ordem

Os blocos abaixo seguem exatamente os blocos de `producao/roteiro_turma_piloto.md`. Onde houver tabela ou lista, reproduzir como elemento visual (tabela real ou cards), não como parágrafo corrido.

**1. Abertura**
- Slide 1 — Capa: logo com slogan, "Turma piloto", subtítulo "Método A.U.L.A. — sessão ao vivo".
- Slide 2 — "O contrato": "No fim desta tarde: o SEU planejamento encaminhado, na SUA disciplina, no formato da SUA escola." Abaixo, uma linha: "Abra agora a ferramenta de IA que você vai usar."
- Slide 3 — Panorama do método, antes de entrar no Bloco 1: quatro linhas grandes, uma por letra — "**A**limentar — os arquivos que a IA precisa" · "**U**niformizar — o formato que a escola aceita" · "**L**igar — o calendário virando plano" · "**A**uditar — a assinatura continua sua". Abaixo, uma linha menor: "Hoje a gente faz os três primeiros ao vivo. O quarto — auditar — fecha a sessão." (conteúdo-base: `CONTEXTO/Horatividade_Estrutura_do_Curso.md`, seção Aula 1 e tabela da seção 3).

**2. Bloco 1 — Alimentar I: os arquivos (~35 min)**
- Slide 4 — Divisória de seção: "Bloco 1 · Alimentar I — os arquivos".
- Slide 5 — Tabela "As cinco camadas do repositório": Normativa, Operacional, Material, Realidade, Formal — coluna com o nome da camada e coluna com um exemplo curto de cada (usar o conteúdo de `CONTEXTO/Horatividade_Estrutura_do_Curso.md`, seção Aula 2).
- Slide 6 — Duas frases-chave lado a lado ou empilhadas: "O sumário vale mais que o livro." / "Nomeie e versione: `00_DIRETRIZ` → `04_TEMPLATE`."
- Slide 7 — "Privacidade — o que não sobe": lista curta (nome, nota, laudo, contato de aluno; documento que não circula fora da escola). Fundo preto, texto branco, título dourado — é o único slide da sessão nesse estilo, para marcar peso do assunto.

**3. Bloco 2 — Alimentar II: a diretriz pedagógica (~25 min)**
- Slide 8 — Divisória de seção: "Bloco 2 · Alimentar II — a diretriz pedagógica".
- Slide 9 — Comparação em duas colunas: "Arquivo diz o que existe" × "Instrução diz como pensar".
- Slide 10 — Lista numerada, as seis partes do bloco de diretriz: Papel e escopo · Fontes de verdade e hierarquia · Referencial pedagógico declarado · Nomenclatura obrigatória · Restrições invioláveis · Comportamento na falta de informação (nomes exatos de `produto/principal/03_bloco_diretriz_comentado.md`).
- Slide 11 — Slide de citação, texto grande centralizado: "As colunas do template são a gramática pedagógica da instituição."

**Pausa**
- Slide 12 — "Pausa — 10 min", minimalista, só texto centralizado.

**4. Bloco 3 — Uniformizar (~25 min)**
- Slide 13 — Divisória de seção: "Bloco 3 · Uniformizar — o formato como regra".
- Slide 14 — Diagrama simples (três caixas conectadas por seta a partir de uma caixa central "Conteúdo"): Conteúdo → Word/PDF (coordenação) · Planilha (sistema) · Markdown (colar direto). Legenda: "Gera-se uma vez. Renderiza-se quantas vezes precisar."
- Slide 15 — Três passos do template reverso, em sequência numerada: "1. Sobe o template vazio → 2. Corrige a leitura da IA → 3. Salva como `04_TEMPLATE.md`, regra permanente".

**5. Bloco 4 — Ligar I: o mapa do ano (~35 min)**
- Slide 16 — Divisória de seção: "Bloco 4 · Ligar I — o mapa do ano e o planejamento".
- Slide 17 — Três etapas em sequência com um checkpoint marcado entre elas: "Etapa 1 — Mapa do ano" → *(checkpoint: aprovar antes de seguir)* → "Etapa 2 — Distribuição" → *(checkpoint: aprovar antes de seguir)* → "Etapa 3 — Planejamento no formato".
- Slide 18 — Slide de citação: "Quase sempre é um número menor do que você supunha."

**6. Bloco 5 — Ligar II: planos em lote (~15 min)**
- Slide 19 — Divisória de seção: "Bloco 5 · Ligar II — planos de aula em lote".
- Slide 20 — Texto grande centralizado: "Cada linha da tabela é um plano de aula esperando para nascer." Abaixo, menor: "Todo plano cita a linha de origem — é o que impede a aula bonita que não tem nada a ver com o que foi entregue à coordenação."

**7. Fechamento**
- Slide 21 — "Auditar — o A final", fechando o método antes da métrica: pergunta em destaque "Um colega da sua disciplina conseguiria dar essa aula amanhã só com esse papel na mão?" Abaixo, menor: "A IA não decidiu nada pedagógico. Ela redigitou, distribuiu e formatou. A escolha continua sua — e a assinatura também." (conteúdo-base: `CONTEXTO/Horatividade_Estrutura_do_Curso.md`, seção Aula 7 — este passo não é praticado ao vivo na sessão, só apresentado como fechamento conceitual do método).
- Slide 22 — A métrica do curso, texto grande: "Ao fim: o planejamento estava pronto e no formato da escola — sim ou não?" Abaixo, menor: "Se sim, me conta em 30 segundos — é o seu depoimento." Fecha com logo horizontal pequeno e slogan.

## Detalhe de execução

Nos slides de "divisória de seção" (4, 8, 13, 16, 19), usar numeração grande em dourado ("Bloco 1", "Bloco 2"...) como elemento gráfico dominante — é o que dá ao professor, olhando de relance durante a fala, a noção imediata de onde está na sessão.

Os slides 3 e 21 (panorama do A.U.L.A. e o A final de Auditar) usam o mesmo tratamento visual dos slides de citação — texto grande, sem tabela, sem card — para marcar que são momentos de conceito do método, não conteúdo de bloco.
