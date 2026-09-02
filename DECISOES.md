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
| Pré-venda progressiva × curso completo no ar | Completo no ar: a turma zero antecipa a validação que a pré-venda daria, e o prazo de 30/09 favorece entrega única |
| Plataforma de entrega | Hotmart Club (infra já existente do produto anterior) |
| Gravação da turma zero vira aula? | Sim para a Aula 5 (já refletido no briefing); demais regravadas limpas |
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
12. **Acrescentei `producao/roteiro_turma_zero.md`** (fora da spec): o usuário vai apresentar aos colegas e os briefings cobriam só a gravação, não a sessão ao vivo — inclui convite, agenda de 2h30 e coleta de depoimento.
13. **Acrescentei `PROMPT_LP_CAPTACAO.md` na raiz** (pedido desta sessão). LP não entra nos zips.
14. **Palavra "prova" evitada nos materiais do principal**; "avaliação bimestral" é o valor de instrumento. O critério de escopo veta material *sobre* provas, não a existência de datas de avaliação. "Semana de provas" aparece apenas em `demo/` (interno).
15. **Termos proibidos incluem "transforme/revolucione/descomplique"**, além de concorrentes, VTSD e referências pessoais — o build falha se a voz escorregar (pegou um caso real durante este build, corrigido).
16. **Nome dos zips com versão completa** `vX.Y.Z` (spec dizia `vX.Y`). Mais preciso; o padrão do CHANGELOG é semântico.
17. **Turma de referência dos exemplos: 1ºA (ter/qui).** O mapa do ano mostra as três turmas; detalhar as 71 linhas de cada turma triplicaria o exemplo sem ensinar nada novo.
18. **git não inicializado** — a pasta não era repo e o usuário não pediu; `.gitignore` pronto para quando quiser (`git init`).
