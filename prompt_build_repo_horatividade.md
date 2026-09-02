# PROMPT — BUILD DO REPOSITÓRIO HORATIVIDADE

> **Como usar:** crie uma pasta vazia, coloque dentro dela `contexto/Horatividade_Contexto_Seed.md`, `contexto/VTSD_Extrato_Montagem_de_Curso.md` e `contexto/Horatividade_Estrutura_do_Curso.md`. Abra o Claude Code nessa pasta e cole tudo o que está abaixo da linha.

---

Você vai montar o repositório de produção de um curso digital chamado **Horatividade**. Comece lendo os três arquivos em `contexto/` — eles são a fonte de verdade e você não deve contradizê-los. Este prompt define o que construir; eles definem o que o produto é.

## 1. O que estamos construindo

Um repositório que contém tudo o que precisa existir em arquivo para o curso ser gravado, empacotado e vendido: os materiais de apoio entregues ao aluno, o produto do order bump, o repositório-modelo que o professor baixa e preenche, os insumos de gravação e os scripts que geram e empacotam tudo.

O que **não** entra aqui: vídeo, copy de página de vendas, tráfego pago, conteúdo de Instagram.

## 2. Regras invioláveis

Aplique estas regras em cada arquivo que escrever. Elas valem mais que qualquer instrução de formato abaixo.

1. **Voz.** Professor falando com professor. Direto, didático, professoral sem formalidade. Proibido: "coachês", clichê motivacional, apelo emocional forçado, "transforme", "revolucione", "descomplique", emoji, exclamação. Tratamento por "você". Frases curtas. Se um parágrafo pode ser cortado sem perda, corte.
2. **Nenhuma instituição real.** Todo exemplo usa uma escola fictícia única, definida na Fase 1 e usada de ponta a ponta. Nenhum nome de colégio real, nenhum template institucional real, nenhuma nomenclatura interna de escola específica. Todo arquivo de exemplo carrega no topo a marca de que é fictício.
3. **LGPD.** Nenhum dado de aluno em lugar nenhum, nem inventado com cara de real. Perfil de turma se descreve por características agregadas.
4. **Escopo fechado.** O produto principal cobre **planejamento anual e plano de aula**. Não escreva material sobre prova, banco de questões, correção, parecer descritivo ou AEE. Isso é produto 2 e contamina o posicionamento.
5. **Não invente código de habilidade.** Esta é literalmente uma regra do curso — não a viole nos próprios materiais. Se um exemplo pedir código de BNCC ou de currículo estadual e você não puder conferir contra o documento oficial, escreva `[HABILIDADE — conferir no documento oficial]`. Em nenhuma hipótese produza um código plausível.
6. **Promessa calibrada.** O produto resolve burocracia. Não transforma prática pedagógica, não melhora aula, não aumenta aprendizagem. Nenhum material pode sugerir o contrário.
7. **Plano gratuito.** Tudo precisa funcionar no Claude gratuito. Quando um material depender de recurso que não existe lá, ofereça o caminho alternativo no mesmo arquivo.

## 3. Estrutura alvo

```
.
├── README.md
├── DECISOES.md
├── CHANGELOG.md
├── MANIFESTO.csv
├── Makefile
├── .gitignore
├── contexto/                          # interno, nunca empacotado
│   ├── (os três .md de origem)
│   ├── VOZ.md
│   └── termos_proibidos.txt           # gitignored
├── produto/
│   ├── principal/
│   │   ├── 00_checklist_prerequisitos.md
│   │   ├── 01_tabela_equivalencia_ferramentas.md
│   │   ├── 02_roteiro_entrevista_reversa.md
│   │   ├── 03_bloco_diretriz_comentado.md
│   │   ├── 04_prompt_template_reverso.md
│   │   ├── 07_checklist_auditoria.md
│   │   ├── repositorio_modelo/        # o que o professor baixa e preenche
│   │   ├── formatos/                  # fontes dos .docx/.xlsx
│   │   └── exemplos/
│   └── bump/
│       ├── LEIA-ME.md
│       ├── diretrizes/                # 8 referenciais
│       ├── ajustes_por_area/          # 4 áreas
│       ├── variacoes_template/        # 4 variações
│       └── exemplos_disciplinas/      # 2 disciplinas completas
├── demo/
│   └── escola_ficticia/               # insumo de gravação
├── producao/
│   ├── roteiros/                      # aula0 a aula8
│   ├── checklist_gravacao.md
│   └── blindagem_tela.md
├── scripts/
│   ├── gerar_formatos.py
│   ├── verificar_vazamento.py
│   └── empacotar.py
└── dist/                              # gitignored
```

## 4. Especificação dos arquivos

### 4.1 `contexto/VOZ.md`
Destile a seção 15 do Seed em um guia operacional de uma página: o que fazer, o que nunca fazer, cinco pares de "assim não / assim sim" tirados do próprio material. É o arquivo que você consulta antes de escrever qualquer outro.

### 4.2 `demo/escola_ficticia/`
O conjunto coerente usado em todos os exemplos do repositório. Sem ele os materiais se contradizem entre si.

Defina uma escola fictícia com nome claramente inventado e genérico, rede particular, ensino fundamental II e médio, calendário bimestral. Produza:

- `ESCOLA.md` — identidade fictícia, aviso de que é fictícia, referencial pedagógico adotado (**Taxonomia de Bloom revisada**, porque é o que se demonstra na tela)
- `01_CALENDARIO.md` — ano letivo completo, quatro bimestres, feriados, semanas de prova, conselho, recessos, eventos fixos. Datas plausíveis e aritmeticamente consistentes
- `02_EMENTA.md` — ementa de Física, 1º ano do ensino médio, por unidade
- `03_TURMAS.md` — três turmas, perfil agregado, carga horária semanal, recursos disponíveis
- `04_TEMPLATE.md` — descrição do template exigido pela coordenação fictícia (colunas, valores aceitos, nomenclatura)

**Consistência é obrigatória:** o número de aulas que sai do calendário × grade precisa fechar com a distribuição da ementa e com os exemplos gerados depois. Confira a conta antes de seguir.

### 4.3 `produto/principal/`

Cada material é autocontido, imprimível, com cabeçalho `Horatividade — método A.U.L.A.` e rodapé com versão e data. Um material, um arquivo, sem dependência de leitura na ordem.

| Arquivo | Conteúdo |
|---|---|
| `00_checklist_prerequisitos.md` | Lista literal e curta do que o professor precisa ter em mãos antes de começar, com o que fazer quando não tem (apostila só em papel, calendário só em imagem, escola sem ementa escrita) |
| `01_tabela_equivalencia_ferramentas.md` | Tabela do conceito de repositório em cada ferramenta (projeto, base de conhecimento, arquivo anexado, instrução personalizada), com nota de que os nomes de botão mudam e a função não |
| `02_roteiro_entrevista_reversa.md` | O prompt que faz a IA entrevistar o professor para montar o perfil de turmas, mais as perguntas de reserva quando ela pergunta pouco, mais o que fazer com a resposta (vira arquivo `03_TURMAS`) |
| `03_bloco_diretriz_comentado.md` | O material mais vendável do curso. Bloco de instruções de projeto completo, na estrutura de seis partes da Aula 3, **com comentários linha a linha** explicando por que cada trecho existe e o que trocar. Versão Bloom como base |
| `04_prompt_template_reverso.md` | O prompt de subir template vazio e pedir a descrição de volta, mais o passo de correção, mais a instrução de salvar a descrição corrigida como arquivo permanente |
| `07_checklist_auditoria.md` | As quatro passadas em ordem — aritmética, códigos e nomenclatura, alinhamento pedagógico, viabilidade material — como checklist marcável, dez minutos no total. Fecha com o critério binário do colega que daria a aula amanhã |

**`repositorio_modelo/`** — a pasta que o professor baixa. Arquivos nomeados no padrão do curso, **vazios com instrução de preenchimento dentro**, não preenchidos:

`LEIA-ME.md`, `00_DIRETRIZ.md`, `01_CALENDARIO.md`, `02_EMENTA.md`, `03_TURMAS.md`, `04_TEMPLATE.md`, `05_ATA_DO_PROJETO.md`.

Cada um abre com uma linha do que é, uma linha de para que a IA usa, e depois a estrutura a preencher com marcadores `[...]`. O `LEIA-ME.md` explica a arquitetura de um projeto por disciplina e por que não um por turma. O `05_ATA_DO_PROJETO.md` é o arquivo da Aula 8 onde o professor registra as correções que precisou fazer, para virarem instrução no ciclo seguinte.

**`formatos/`** — fontes em markdown/YAML que os scripts convertem: esquema de colunas do planejamento em tabela, esquema da planilha por aula, e a versão markdown colável no Word para quem não tem geração de arquivo.

**`exemplos/`** — planejamento anual completo de Física 1º ano da escola fictícia + 12 planos de aula do 1º bimestre derivados dele. Cada plano cita a linha do planejamento de que derivou. Mais um exemplo reduzido em humanas (mapa do ano + 2 planos) para o professor de história não achar que o curso não é para ele.

### 4.4 `produto/bump/` — "Kit Diretriz Pedagógica + Formatos", R$47

- `diretrizes/` — oito blocos prontos, um arquivo cada, mesma estrutura de seis partes, plugáveis sem mexer no resto: Bloom revisada, BNCC por habilidades, currículo estadual, metodologias ativas, ensino técnico e IFs, escola confessional, pedagogia própria (construtivista/sociointeracionista), foco ENEM/vestibular
- `ajustes_por_area/` — quatro arquivos curtos: exatas, ciências da natureza, linguagens, humanas. Só o que muda em relação ao bloco base
- `variacoes_template/` — tabela por unidade, tabela por aula, planilha por aula, formulário de sistema
- `exemplos_disciplinas/` — dois pacotes completos além de Física: História (8º ano) e Língua Portuguesa (1º ano EM), cada um com planejamento anual + 6 planos de aula, na mesma escola fictícia

O `LEIA-ME.md` do bump explica em quatro linhas como trocar o bloco de diretriz dentro de um projeto já montado.

### 4.5 `producao/`

- `roteiros/aula0.md` a `aula8.md` — **briefings, não scripts.** Para cada aula: objetivo em uma frase, o entregável que o aluno tem no fim, os beats de tela em ordem, o que precisa estar aberto antes de gravar, a métrica da aula, a duração alvo do documento de estrutura, e os pontos onde não pode haver corte
- `checklist_gravacao.md` — o que conferir antes de apertar gravar (abas fechadas, notificações, nome de conta visível, arquivos abertos, zoom da tela)
- `blindagem_tela.md` — lista do que não pode aparecer em nenhum frame: nome de colégio, template real, material didático identificável, nome de colega, nome de aluno, e-mail institucional, grupo de WhatsApp

### 4.6 `scripts/`

Python 3, só biblioteca padrão + `python-docx` e `openpyxl`. Cada script roda sozinho, imprime o que fez, retorna código de saída não-zero em falha.

- **`gerar_formatos.py`** — lê `produto/principal/formatos/` e gera o `.docx` de planejamento com tabela formatada e o `.xlsx` com esquema de colunas, cabeçalho travado e validação de valores aceitos onde fizer sentido. Regenerável: a fonte é o markdown, o binário é artefato
- **`verificar_vazamento.py`** — varre tudo que vai ser empacotado procurando os termos de `contexto/termos_proibidos.txt` (uma linha por termo, case-insensitive, sem acento). Também sinaliza padrões de risco: e-mail, CPF, telefone, CEP, e códigos de habilidade que pareçam inventados. Falha o build se achar qualquer coisa
- **`empacotar.py`** — roda a verificação, depois gera `dist/horatividade-principal-vX.Y.zip` e `dist/horatividade-bump-vX.Y.zip` com a versão lida do `CHANGELOG.md`. Nunca inclui `contexto/`, `demo/`, `producao/` nem `scripts/`

O `Makefile` expõe: `make formatos`, `make verifica`, `make pacote`, `make limpa`.

### 4.7 Raiz

- `README.md` — o que é o repositório, como rodar, o que é entregável e o que é interno, onde estão as decisões abertas
- `DECISOES.md` — as decisões pendentes da seção 6 da Estrutura do Curso, mais **toda escolha que você fizer por conta própria durante o build**, registrada com a alternativa que foi descartada. Este arquivo é obrigatório e importa mais que os outros: é onde eu vejo o que você decidiu no meu lugar
- `MANIFESTO.csv` — colunas `arquivo,aula,pacote,formato_entrega,status`. É o que vira a estrutura de módulos na Hotmart
- `CHANGELOG.md` — versão semântica, começa em 0.1.0
- `.gitignore` — `dist/`, `contexto/termos_proibidos.txt`, `*.docx`, `*.xlsx`, temporários

## 5. Ordem de execução

Trabalhe em fases e **pare ao fim de cada uma para eu aprovar** antes de seguir. Não emende as fases.

1. **Esqueleto e fundação** — estrutura de pastas, `VOZ.md`, `DECISOES.md`, `README.md`, `.gitignore`, `CHANGELOG.md`, e a escola fictícia completa em `demo/` com a aritmética conferida. *Pare.*
2. **Repositório-modelo e materiais do principal** — os seis materiais + `repositorio_modelo/` + `formatos/`. *Pare.*
3. **Exemplos** — planejamento anual de Física, 12 planos de aula, exemplo reduzido em humanas. *Pare.*
4. **Bump completo.** *Pare.*
5. **Produção** — roteiros das nove aulas, checklists. *Pare.*
6. **Scripts, manifesto e build** — gerar formatos, verificar, empacotar, rodar `make pacote` e mostrar o resultado.

## 6. Critério de pronto

- [ ] `make pacote` roda limpo e produz os dois zips
- [ ] Nenhum nome de instituição real em nenhum arquivo
- [ ] Nenhum código de habilidade não conferido
- [ ] A aritmética do calendário fecha com a distribuição dos exemplos
- [ ] Cada plano de aula do exemplo cita a linha do planejamento de onde saiu
- [ ] Nenhum material do principal fala de prova, correção ou parecer descritivo
- [ ] `MANIFESTO.csv` bate com o que existe em disco
- [ ] `DECISOES.md` lista tudo que você decidiu sem me perguntar
- [ ] Nenhum arquivo contém "transforme", "revolucione", "descomplique" ou equivalente

---

*Antes de começar: leia os três arquivos de contexto e me diga em cinco linhas o que você entendeu que o produto é e onde acha que este prompt conflita com eles. Só depois comece a Fase 1.*
