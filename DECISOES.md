# DECISOES — pendências e escolhas do build

## O que entendi do produto (e conflitos entre o prompt de build e o contexto)

O produto é um curso curto (9 aulas, ~107 min) que ensina professor de anos finais/EM a montar **um repositório de contexto por disciplina** no Claude gratuito e derivar dele o planejamento anual e os planos de aula em lote, no formato exato da coordenação — método A.U.L.A., com auditoria final do professor. Conflitos identificados:

1. O extrato VTSD sugere 6 aulas (~73 min); a Estrutura do Curso fecha em 9 (~107 min). **Segui a Estrutura** — é o documento mais recente e o prompt de build pede roteiros de aula0 a aula8.
2. O VTSD recomenda improvisação orientada; o build pede roteiros. Sem conflito real: os roteiros são **briefings de beats**, não scripts de leitura.
3. O Seed marca "logo/paleta" como fora de escopo, mas as logos já existem e o usuário pediu a LP — usei a marca nos extras de marketing, sem tocar no empacotado.
4. Assinatura do Seed ("o planejamento do seu ano inteiro em uma tarde") × slogan da logo ("Burocracia resolvida. A aula é sua."). Na LP usei o quadro como headline e o slogan junto à marca.

## Pendências que só o Jonas fecha (da seção 6 da Estrutura)

| Decisão | Recomendação registrada |
|---|---|
| Nível de suporte prometido | Sem suporte individual: FAQ + atualizações do material. Prometido antes de vender, sustentável em volume |
| Pré-venda progressiva × curso completo no ar | Completo no ar: a turma piloto antecipa a validação que a pré-venda daria, e o prazo de 30/09 favorece entrega única |
| Plataforma de entrega | Hotmart Club (infra já existente do produto anterior) |
| Gravação da turma piloto vira aula? | Sim para a Aula 5 (já refletido no briefing); demais regravadas limpas |
| Ferramenta da demonstração | Claude (o curso já assume o plano gratuito dele); tabela de equivalência cobre as demais |

## Escolhas feitas durante o build (com a alternativa descartada)

1. **Executei as seis fases sem parar para aprovação.** O pedido desta sessão ("produza tudo o que não depende de gravação") substituiu a regra de parada do prompt de build. Alternativa (parar por fase) descartada por instrução direta.
2. **Escola fictícia: "Colégio Exemplo".** Alternativa — nome inventado com cara de real ("Colégio Meridiano") — descartada: nome genérico e assumidamente fictício elimina risco de colidir com escola existente.
3. **Ano letivo da demo: 2027.** É o ano que o aluno vai planejar na janela dez–fev. Feriados nacionais de 2027 reais e conferidos por script (dias da semana corretos). Alternativa (2026) descartada: nasceria vencida.
4. **Estrutura do calendário:** avaliações sempre na última semana do bimestre, conselho no sábado seguinte, recuperação final em dezembro; 203 dias letivos (>200). Alternativa (provas no meio do bimestre) descartada por complicar a aritmética sem ganho didático.
5. **Física com 2 aulas semanais e três turmas em grades diferentes** (ter/qui, seg/qua, qua/sex → 71/72/71 aulas). Permite demonstrar "múltiplas turmas" com números que realmente diferem.
6. **Template do Colégio Exemplo em Bloom, sem coluna de código BNCC.** Evita 71 placeholders `[HABILIDADE — …]` no exemplo e é coerente ("nenhuma coluna pede código → documentos não citam código"). A mecânica de códigos vive nas diretrizes BNCC/estadual/ENEM do bump, com placeholder e arquivo `06_*` oficial.
7. **12 planos de aula em documento único** (não 12 arquivos). Espelha a variação "documento único" da Aula 6 e reduz atrito de download. Alternativa descartada: um arquivo por plano.
8. **Exemplo reduzido de humanas = subconjunto do pacote História do bump** (mesmo planejamento, 2 dos 6 planos). Garante coerência entre pacotes; o bump segue com planejamento completo + 6 planos + LP inteiro, então o teaser não o canibaliza.
9. **Diretrizes do bump entregam o bloco da Parte 3 + restrições extras**, não as seis partes repetidas oito vezes. É o modelo "plugável" ensinado na Aula 3. Alternativa (oito blocos completos) descartada: duplicação e risco de divergência entre cópias.
10. **Referenciais que dependem de documento oficial (BNCC, estadual, técnico, ENEM) exigem um arquivo `06_*` copiado do oficial pelo professor.** Única forma de cumprir "nunca inventar código" na prática.
11. **Pasta `CONTEXTO/` mantida em maiúsculas** (veio assim); scripts procuram `contexto/` e `CONTEXTO/`. Alternativa (renomear) descartada para não quebrar nada do usuário.
12. **Acrescentei `producao/roteiro_turma_piloto.md`** (fora da spec): o usuário vai apresentar aos colegas e os briefings cobriam só a gravação, não a sessão ao vivo — inclui convite, agenda de 2h30 e coleta de depoimento.
13. **Acrescentei `PROMPT_LP_CAPTACAO.md` na raiz** (pedido desta sessão). LP não entra nos zips.
14. **Palavra "prova" evitada nos materiais do principal**; "avaliação bimestral" é o valor de instrumento. O critério de escopo veta material *sobre* provas, não a existência de datas de avaliação. "Semana de provas" aparece apenas em `demo/` (interno).
15. **Termos proibidos incluem "transforme/revolucione/descomplique"**, além de concorrentes, VTSD e referências pessoais — o build falha se a voz escorregar (pegou um caso real durante este build, corrigido).
16. **Nome dos zips com versão completa** `vX.Y.Z` (spec dizia `vX.Y`). Mais preciso; o padrão do CHANGELOG é semântico.
17. **Turma de referência dos exemplos: 1ºA (ter/qui).** O mapa do ano mostra as três turmas; detalhar as 71 linhas de cada turma triplicaria o exemplo sem ensinar nada novo.
18. **git não inicializado** — a pasta não era repo e o usuário não pediu; `.gitignore` pronto para quando quiser (`git init`).

## Reestrutura de setembro/2026 — apostila do aluno como fonte de verdade

A Apostila do aluno (Claude Design, `apostila-do-aluno.html`) nasceu depois da turma piloto e unificou o A.U.L.A. com o preenchimento de cada arquivo do repositório-modelo, em formato tutorial — mais testada e mais detalhada que os materiais de apoio anteriores. Esta rodada trouxe o repositório-modelo, os exemplos e os materiais de apoio para bater com ela. Escolhas feitas, com a alternativa descartada:

19. **`02_EMENTA` volta a ser um arquivo único no repositório-modelo.** Tinha sido dividido em `02_EMENTA_1em.md`/`02_EMENTA_2em.md` sem necessidade — a apostila trata a divisão por série (`02_EMENTA_1EM.md`, `02_EMENTA_2EM.md`...) como o caso de quem dá mais de uma série, não o padrão de todo comprador. A convenção de nome fica documentada como nota, não como arquivo pré-dividido. **Decisão do Jonas**, não minha escolha unilateral.
20. **`03_bloco_diretriz_comentado.md` continua existindo separado do Passo A1 da apostila**, como o caminho manual/comentado para quem quer entender e editar o `00_DIRETRIZ` à mão, em vez de deixar a IA preencher a partir das orientações da escola. Os dois métodos chegam no mesmo arquivo final; um não substitui o outro. Alternativa descartada: reescrever o material para forçar o método da apostila. **Decisão do Jonas.**
21. **Os prompts de copiar-colar dos materiais de apoio foram alinhados palavra por palavra com os da apostila** (`02_roteiro_entrevista_reversa`, `04_prompt_template_reverso`), em vez de manter frases equivalentes mas com redação própria. Motivo: quem usa os dois materiais não pode ver dois textos diferentes pedindo a mesma coisa. **Decisão do Jonas.**
22. **`06_REFERENCIAL.md` criado como arquivo-modelo opcional.** Já estava previsto na decisão 10 acima (referenciais que dependem de documento oficial exigem um `06_*`), mas nunca tinha sido criado como arquivo do repositório-modelo — só existia como conceito. A apostila (Passo A1, caixa "O recorte da BNCC") o torna explícito, e agora ele existe.
23. **`exemplos/repositorio_preenchido/` criado com os seis arquivos preenchidos do Colégio Exemplo.** A apostila referencia essa pasta em sete pontos diferentes ("compare com o exemplo") e ela nunca tinha sido montada — maior lacuna estrutural encontrada nesta reestrutura. As datas de `01_CALENDARIO.md` foram derivadas por aritmética (script) da "Memória de conferência" já existente em `demo/escola_ficticia/01_CALENDARIO.md`, não inventadas. As três linhas de `05_ATA_DO_PROJETO.md` vêm de problemas já documentados no checklist de auditoria e na própria apostila, não de um erro novo.
24. **`CONTEXTO/Horatividade_Estrutura_do_Curso.md` (Aula 2/3) foi atualizado** para corrigir a ordem de preenchimento e citar `05_ATA_DO_PROJETO`/`06_REFERENCIAL`, mesmo com a turma piloto já realizada — fica como referência para quando as aulas 0/1/7/8 forem regravadas. Alternativa descartada (deixar como está por ser documento histórico): rejeitada pelo Jonas.
25. **Não mexi em `produto/bump/diretrizes/*.md`** (BNCC por habilidades, currículo estadual, ensino técnico, ENEM) para apontarem ao `06_REFERENCIAL.md` — o Jonas preferiu deixar de fora desta rodada. Fica pendente.
26. **`BRIEF_BUILD.md` não existe no repositório** — o Jonas confirmou que a referência era ao `prompt_build_repo_horatividade.md` (o prompt original do build v0.1.0). Como esse arquivo é uma instrução estática, não um log, o que mudou nesta rodada foi registrado aqui e no `CHANGELOG.md` (nova versão 0.2.0), que já cumprem esse papel no repositório.
27. **`arquivos-planejamento/` e `colegio_jacaranda_azul/` ficaram fora desta reestrutura.** São o material real de preparo da turma piloto (escola fictícia "Colégio Jacarandá Azul", separada do "Colégio Exemplo" usado nos materiais do produto), não o produto reutilizável — não foram tocados.
