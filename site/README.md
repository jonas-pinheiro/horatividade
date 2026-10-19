# horatividade.com.br

Site estático do Horatividade. Não tem build: o que está nesta pasta é o que vai para o ar.

## Páginas

- `index.html`: landing page de vendas, em https://horatividade.com.br/
- `politica-de-privacidade.html`: em https://horatividade.com.br/politica-de-privacidade
- `404.html`: página de erro

## Imagens

- `assets/img/og-image.jpg` (1200×630): prévia ao compartilhar o link (WhatsApp, Instagram, Facebook)
- `assets/img/jonas.jpg`: foto da seção "Quem ensina"
- `assets/img/apple-touch-icon.png`: ícone ao salvar na tela inicial do celular

## Publicar

**Netlify (recomendado, é o que a Política de Privacidade cita):** conecte este repositório no Netlify, sem comando de build e com a pasta de publicação `.`. O `netlify.toml` já cuida dos redirecionamentos e cabeçalhos. Em *Domain management*, adicione horatividade.com.br.

**GitHub Pages:** em *Settings → Pages*, publique a branch `main`, pasta raiz. O arquivo `CNAME` já aponta para horatividade.com.br. Se usar GitHub Pages em vez do Netlify, atualize a seção 4 da Política de Privacidade.

## Onde mexer

- Link do checkout (4 botões): procure por `pay.hotmart.com/S107441178R` no `index.html`.
- Pixel da Meta (ID 2573799186430774) e verificação de domínio: no início do `<head>` das duas páginas.
- Vídeo e depoimentos: chaves `data-vsl` e `data-depoimentos` na tag `<html>` do `index.html`.
- Depois de trocar a imagem de compartilhamento, force a atualização em https://developers.facebook.com/tools/debug/
