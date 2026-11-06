# Vision — site institucional

Site estático construído com **HTML, CSS e JavaScript nativos**. Não usa Next.js, bundler nem bibliotecas obrigatórias. O conteúdo principal fica no HTML servido, para funcionar sem depender de JavaScript para renderizar as páginas.

## Abrir e executar no VS Code

Recomendado: VS Code e a extensão Live Server. Opcionalmente, Python 3 para o servidor local e o gerador de cards. Não é preciso instalar pacotes com npm ou pip.

Abra a pasta `vision-site-liveserver` no VS Code. O arquivo `index.html` fica diretamente na raiz. Clique com o botão direito nele e selecione **Open with Live Server** (ou **Abrir com Live Server**). O site abrirá em um endereço local, geralmente `http://127.0.0.1:5500/`.

As páginas internas também estão em pastas na raiz, cada uma com seu próprio `index.html`; navegue até elas pelos links do menu. Se preferir o servidor Python opcional, execute `python3 scripts/serve.py` na raiz e abra `http://localhost:3000/`.

## Estrutura

- `index.html`: homepage.
- `agenciamento-digital/index.html`, `criacao-de-sites/index.html`, `seo-local/index.html`, `inteligencia-digital/index.html`, `projetos/index.html` e `diagnostico/index.html`: páginas internas, cada uma com conteúdo e metadados próprios.
- `assets/css/`: `tokens.css` centraliza cores, fontes, espaços e raios; `base.css` contém regras globais; `components.css` contém componentes; `layouts.css` define as composições; `responsive.css` contém breakpoints; `visual-refresh.css` aplica o acabamento visual refinado em todas as páginas.
- `assets/js/`: `site.js` controla o menu mobile e o ano; `diagnostic-form.js` valida os campos, monta a mensagem e abre o WhatsApp para revisão e envio pelo visitante.
- `assets/images/`: símbolo original da Vision e imagens de portfólio obtidas nos sites correspondentes e otimizadas para a página.
- `manus-routes.json`: rotas conhecidas pelo preview gerenciado.
- `content/projects.json`: fonte única dos dados dos três cards de projeto.
- `scripts/build_projects.py`: gera os cards estáticos da homepage e da página de projetos a partir do catálogo JSON. O HTML final continua presente no carregamento inicial e pode ser rastreado.
- `scripts/generate_sitemap.py`: adiciona canonical, `og:url`, `og:image`, sitemap e referência no robots quando o domínio HTTPS real for conhecido.
- `scripts/serve.py`: servidor local mínimo, sem dependências.
- `scripts/check_site.py`: confere as rotas, limites SEO, metadados, JSON-LD/catalogação de projetos, links/fragmentos, navegação da 404 e ação de contato no WhatsApp.
- `plan.md` e `TODO.md`: plano aprovado e critérios de escopo.

## Editar conteúdo

Os textos de cada página podem ser alterados no respectivo `index.html`. As cores, tipografia, espaçamentos e bordas ficam concentrados em `assets/css/tokens.css`; ajustes de estilo compartilhados ficam nos demais arquivos CSS.

Para adicionar, remover ou editar um projeto, modifique `content/projects.json` e execute:

```bash
python3 scripts/build_projects.py
```

O comando atualiza os blocos marcados nas duas páginas de portfólio sem depender de pacote externo. As descrições devem continuar fiéis aos respectivos sites; não acrescentar métricas, depoimentos ou resultados sem confirmação.

Para substituir a marca, coloque a versão oficial aprovada em `assets/images/` e atualize a referência da imagem no cabeçalho/rodapé. O símbolo entregue deve permanecer intacto; use-o com o lettering neutro temporário até haver versão horizontal oficial.

Para adicionar uma página, crie uma pasta na raiz do projeto com um `index.html`, seus metadados e conteúdo; atualize links de navegação/rodapé e `manus-routes.json`. Se houver novo título e descrição, escreva-os especificamente para a página.

## SEO e publicação

As páginas têm HTML semântico, title, description, Open Graph/Twitter e JSON-LD de organização/serviço baseado apenas em informações fornecidas ou confirmadas. Canonical, `og:url`, `og:image` absoluto e sitemap dependem do domínio público real; não são usados endereços de preview ou URLs inventadas. No WebDev publicado, o gateway gera `/sitemap.xml` e `/robots.txt` a partir das rotas e da origem canônica. Na validação atual, o servidor do Preview respondeu 404 para esses dois caminhos; eles não são substituídos por arquivos estáticos incompletos.

Quando o domínio HTTPS real estiver definido, rode na raiz do projeto:

```bash
python3 scripts/generate_sitemap.py https://seudominio.com.br
```

O comando valida a origem, insere URLs absolutas no HTML e gera `sitemap.xml` e `robots.txt` com as rotas declaradas. Use-o somente para uma hospedagem estática independente depois de confirmar o domínio HTTPS. No WebDev, deixe o gateway gerar esses documentos; não mantenha arquivos manuais que possam sobrescrever a política do preview ou do domínio canônico. Revise e publique as alterações. Não use um endereço de preview como domínio canônico.

Para publicação em hospedagem estática, sirva a raiz do projeto como raiz do site. O código-fonte também está preparado para saída estática no ambiente de preview gerenciado. Não é necessária conta/credencial externa para executar esta versão.

Antes de publicar uma alteração, rode `python3 scripts/build_projects.py` se tiver alterado o catálogo e então execute `python3 scripts/check_site.py`. O verificador não substitui testes visuais nem a confirmação de um domínio real.

## Formulário e integrações

O formulário valida os campos, monta uma mensagem com as respostas e abre o WhatsApp para que o visitante revise e envie. O site não armazena as respostas. O número provisório solicitado está definido como `000000000` em `assets/js/diagnostic-form.js`; para receber conversas de verdade, substitua-o pelo número real no formato internacional, somente dígitos (incluindo o código do país, sem `+`). A página também contém um atalho direto para o mesmo destino. Enquanto o número permanecer zerado, o link abrirá o WhatsApp, mas não poderá endereçar uma conta real.

Não há variáveis de ambiente nesta versão; por isso não existe `.env.example` por enquanto. Quando uma integração exigir variáveis, criar `.env.example` sem valores secretos e documentar as chaves.

## Informações ainda necessárias para uma publicação final

Domínio oficial; logotipo horizontal/completo (se existir); número oficial do WhatsApp para substituir o destino provisório; redes sociais oficiais; eventual integração de CRM; texto e dados para uma política de privacidade; IDs reais de GA4 e Search Console, caso sejam usados; e confirmação de quais imagens de projetos podem permanecer em uso público.
