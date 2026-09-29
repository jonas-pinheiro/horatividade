# CHANGELOG

Versão semântica. A versão atual é lida por `scripts/empacotar.py`.

## [0.2.0] — 2026-09-29

Repositório-modelo, exemplos e materiais de apoio realinhados à Apostila do aluno (`apostila-do-aluno.html`), fonte de verdade mais recente do método, escrita depois da turma piloto.

- `repositorio_modelo/LEIA-ME.md`: corrige a ordem de preenchimento (00→02→03 Alimentar, 04 Uniformizar, 01 Ligar) e acrescenta o `06_REFERENCIAL`
- `repositorio_modelo/02_EMENTA.md`: volta a ser um arquivo único (estava pré-dividido em 1em/2em); convenção de múltiplas séries documentada como nota
- `repositorio_modelo/01_CALENDARIO.md`: acrescenta a saída de datas por turma e totais que o passo Ligar da apostila pede
- `repositorio_modelo/04_TEMPLATE.md`: nota para o caso de dois documentos exigidos pela escola
- `repositorio_modelo/06_REFERENCIAL.md`: novo arquivo-modelo opcional, para quem precisa de código de habilidade oficial
- `exemplos/repositorio_preenchido/`: pasta nova com os seis arquivos preenchidos do Colégio Exemplo, referenciada pela apostila em sete pontos e que nunca tinha sido criada
- `01_tabela_equivalencia_ferramentas.md`, `02_roteiro_entrevista_reversa.md`, `04_prompt_template_reverso.md`: alinhados ao texto e aos prompts de copiar-colar da apostila
- `03_bloco_diretriz_comentado.md`: nota cruzada com o Passo A1 da apostila (métodos complementares para o mesmo `00_DIRETRIZ`)
- `CONTEXTO/Horatividade_Estrutura_do_Curso.md`: Aula 2/3 corrigidas com a ordem de preenchimento real e o `06_REFERENCIAL`
- Decisões desta rodada registradas em `DECISOES.md`

## [0.1.0] — 2026-08-27

Primeira versão completa do repositório de produção.

- Fundação: VOZ, decisões, escola fictícia (Colégio Exemplo, ano letivo 2027) com aritmética conferida
- Produto principal: seis materiais de apoio, repositório-modelo, fontes de formatos
- Exemplos: planejamento anual de Física (1º EM, 71 aulas) + 12 planos de aula do 1º bimestre + exemplo reduzido de História (8º ano)
- Order bump: 8 diretrizes, 4 ajustes por área, 4 variações de template, 2 disciplinas completas
- Produção: briefings das aulas 0 a 8, checklist de gravação, blindagem de tela, roteiro da turma piloto
- Scripts: gerar_formatos, verificar_vazamento, empacotar; Makefile
