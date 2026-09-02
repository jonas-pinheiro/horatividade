# Horatividade — repositório de produção

Tudo o que precisa existir em arquivo para o curso **Horatividade (método A.U.L.A.)** ser gravado, empacotado e vendido. Fora daqui: vídeo, copy de página de vendas, tráfego, Instagram.

## Mapa

| Pasta | O que é | Empacotado? |
|---|---|---|
| `CONTEXTO/` | fonte de verdade (Seed, Estrutura, VTSD), guia de voz, termos proibidos | nunca |
| `demo/escola_ficticia/` | Colégio Exemplo: o cenário único de todos os exemplos e da gravação | nunca |
| `produto/principal/` | materiais do curso (R$97): apoios, repositório-modelo, formatos, exemplos | sim |
| `produto/bump/` | Kit Diretriz Pedagógica + Formatos (R$47) | sim |
| `producao/` | briefings das aulas 0–8, checklist de gravação, blindagem de tela, roteiro da turma zero | nunca |
| `scripts/` | geração de formatos, verificação de vazamento, empacotamento | nunca |
| `dist/` | zips gerados (artefato, gitignored) | — |

## Como rodar

Requisitos: Python 3 com `python-docx` e `openpyxl`.

```
python scripts/gerar_formatos.py       # regenera modelo_planejamento.docx e modelo_planilha.xlsx
python scripts/verificar_vazamento.py  # varre produto/ por termos proibidos e padroes de risco
python scripts/empacotar.py            # verifica e gera dist/horatividade-{principal,bump}-vX.Y.Z.zip
```

Com make: `make formatos`, `make verifica`, `make pacote`, `make limpa`. A versão dos pacotes vem do primeiro cabeçalho `[X.Y.Z]` do `CHANGELOG.md`.

## Regras que valem em todo arquivo

1. Voz de professor para professor — ver `CONTEXTO/VOZ.md` antes de escrever qualquer coisa.
2. Nenhuma instituição real: todo exemplo é o **Colégio Exemplo** (fictício, ano letivo 2027).
3. LGPD: nenhum dado de aluno, nem inventado com cara de real.
4. Escopo fechado: planejamento anual e plano de aula. Nada de avaliações/pareceres (produto 2).
5. Nenhum código de habilidade não conferido — o placeholder é `[HABILIDADE — conferir no documento oficial]`.
6. Tudo funciona no Claude gratuito; onde depende de recurso pago, o caminho alternativo está no mesmo arquivo.

## Onde estão as decisões

`DECISOES.md` — pendências que só o Jonas pode fechar (suporte, pré-venda, plataforma) e todas as escolhas feitas durante o build, com as alternativas descartadas. `MANIFESTO.csv` mapeia cada entregável para aula/pacote (vira a estrutura de módulos na plataforma de venda).

## Extras fora do empacotamento

- `PROMPT_LP_CAPTACAO.md` — prompt pronto para montar a landing page de captação no Claude Design (marca preto/dourado)
- `logo_*.png` — arquivos de marca (preto `#060606`, dourado `#CE9631`, slogan "Burocracia resolvida. A aula é sua.")
- `producao/roteiro_turma_zero.md` — a sessão ao vivo com os colegas, passo a passo
