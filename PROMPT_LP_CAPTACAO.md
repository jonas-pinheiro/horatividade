# Prompt pronto — Landing page de captação (Claude Design)

> Cole tudo abaixo da linha no Claude Design. Anexe junto os arquivos `logo_horizontal.png`, `logo_sozinho.png` e `logo_texto_slogan.png`. Depois de gerar, troque o placeholder do formulário pela integração real (provedor de e-mail) e publique na Netlify.

---

Monte uma landing page de captação de leads, em português do Brasil, para a marca **Horatividade** — um método que ensina professores a resolver a burocracia de planejamento usando IA. A página tem um único objetivo: capturar e-mail em troca de um material gratuito. Sem menu, sem links externos, sem seção de preço. Uma página, um CTA.

## Marca e direção visual

- Cores: preto `#060606`, dourado `#CE9631`, branco `#FFFFFF`. Fundo predominante branco, tipografia preta, dourado só como acento (destaques, botão, detalhes) — nunca como fundo de blocos longos de texto.
- Tipografia: sans-serif neutra e geométrica (Inter, DM Sans ou similar). Títulos em peso bold, texto em regular. Sem serifada, sem fonte decorativa.
- Logo: usar a versão horizontal no topo e a versão com slogan no rodapé (arquivos anexados). Na palavra HORATIVIDADE, o "A" (4ª letra) é dourado — se reproduzir o nome em texto, manter esse detalhe.
- Estética: sóbria e profissional, mais "material de professor bem-feito" do que "página de lançamento". Espaço em branco generoso, cantos pouco arredondados, sem gradientes chamativos, sem emoji, sem ponto de exclamação em lugar nenhum da página.
- Mobile-first: a maioria do tráfego vem do Instagram (link em DM).

## Tom de voz (obrigatório)

Professor falando com professor. Direto, didático, sem formalidade e sem "coachês". Proibido: clichê motivacional, apelo emocional forçado, as palavras "transforme", "revolucione", "descomplique", emojis e exclamações. Frases curtas.

## Estrutura e copy (usar este texto como base, ajustando só o necessário para o layout)

**1. Topo:** logo horizontal, pequena.

**2. Hero:**
- Headline: "O planejamento do seu ano inteiro em uma tarde."
- Subheadline: "Baixe gratuitamente o repositório-modelo do método A.U.L.A.: os cinco arquivos que fazem a IA gerar planejamento e planos de aula no formato que a sua coordenação exige — em vez de mais um plano genérico."
- Formulário: campo de e-mail + botão dourado com texto "Quero o repositório-modelo". Abaixo, em letra pequena: "Sem spam. Você recebe o material e os avisos do curso. Sai da lista quando quiser."

**3. Seção "O que você recebe" (3 itens em cards simples, borda fina):**
- "Os 5 arquivos do repositório — Calendário, ementa, turmas, template e diretriz: nomeados, estruturados e com instrução de preenchimento dentro de cada um."
- "O roteiro da entrevista reversa — O prompt que faz a IA te entrevistar para montar o perfil das suas turmas, sem página em branco."
- "O checklist de pré-requisitos — O que separar antes de começar, com solução para apostila em papel, calendário em foto e escola sem ementa escrita."

**4. Seção "Por que isso funciona" (texto curto, sem card):**
"A IA não devolve plano genérico por ser ruim. Devolve genérico porque a única coisa específica que ela recebeu foi o nome do conteúdo. Ela não sabe quantas aulas você tem no bimestre, qual apostila usa, nem o que a coordenação exige na tabela. O repositório resolve isso uma única vez — e o ano inteiro passa a derivar dele. Funciona no plano gratuito das ferramentas de IA."

**5. Seção de credencial (foto opcional, fundo preto, texto branco, detalhe dourado):**
"Quem montou isso dá aula até hoje. Sou professor de Física há mais de 14 anos, doutor na área, em sala de aula agora. Uso esse método no meu próprio planejamento e compartilho as ferramentas com colegas há anos — este material é o que eles vêm pedir. — Prof. Jonas"

**6. CTA final:** repetir o formulário com a frase "Preencha uma vez. Pare de redigitar burocracia." e o mesmo botão.

**7. Rodapé:** logo com slogan ("Burocracia resolvida. A aula é sua."), aviso de privacidade em uma linha ("Seu e-mail é usado só para envio do material e das novidades da Horatividade, conforme a LGPD.") e © Horatividade 2026.

## Requisitos técnicos

- HTML/CSS estático, leve, sem framework pesado — vai para a Netlify.
- Formulário com placeholder de action claro (`FORM_ACTION_AQUI`) para eu conectar o provedor de e-mail depois; validação simples de e-mail no front.
- Página de obrigado simples no mesmo estilo: "Material a caminho do seu e-mail. Enquanto isso, confira a caixa de spam e marque o remetente como confiável."
