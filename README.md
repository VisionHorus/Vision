# Vision — presença digital

Site institucional estático, escrito em HTML, CSS e JavaScript nativos. Não usa framework, bundler ou dependências obrigatórias. O conteúdo das páginas está no HTML servido; o JavaScript é progressivo e não é necessário para renderizar o conteúdo.

## Executar localmente

Na raiz do projeto, inicie um servidor estático:

```bash
python3 -m http.server 3000
```

Acesse `http://localhost:3000/`. As páginas internas ficam em diretórios com `index.html`; o arquivo `manus-routes.json` declara as 10 rotas públicas para o Preview WebDev. Para testar o build destinado a uma hospedagem estática, use o comando abaixo.

## Estrutura

- `index.html` e `404.html`: home e página de erro não indexável.
- `agenciamento-digital/`, `criacao-de-sites/`, `seo-local/`, `inteligencia-digital/`, `projetos/` e `diagnostico/`: páginas públicas de serviços, portfólio e conversão.
- `privacidade/`, `termos/` e `cookies/`: páginas legais em linguagem simples, com dados ainda pendentes indicados por `[PREENCHER: ...]` e comentário para revisão jurídica.
- `assets/css/`: `tokens.css` mantém a paleta e as variáveis tipográficas; `fonts.css` serve Barlow Condensed e DM Sans locais; `base.css`, `components.css`, `layouts.css` e `responsive.css` concentram os estilos ativos.
- `assets/fonts/`: arquivos WOFF2 locais e licenças SIL Open Font License 1.1.
- `assets/images/`: símbolo da Vision, imagens de projetos e textura de papel. As imagens de clientes ainda exigem confirmação escrita de direitos antes de uso público.
- `assets/js/site.js`: navegação móvel acessível e ano no rodapé. `assets/js/diagnostic-form.js`: honeypot, validação e montagem da mensagem, sem persistir os campos.
- `content/projects.json`: fonte central para os cinco cards de projetos; `content/visual-brief.md` documenta as referências; `content/image-credits.md` registra fontes e pendências.
- `prototipos/`: dois estudos independentes e `noindex`. A saída pública do build os exclui; usam referências visuais fornecidas pelo usuário, cuja licença precisa ser confirmada antes de publicação.
- `scripts/build_projects.py`: gera cards e JSON-LD de projetos a partir do catálogo. `scripts/generate_sitemap.py`: gera canonical/sitemap/robots para uma origem confirmada. `scripts/check_site.py`: valida rotas, metadados, referências, JSON-LD e o destino seguro do formulário. `scripts/build_static.py`: executa os geradores e o checker e monta a saída final em `dist/` sem dependências externas.

## Atualizar projetos

Edite `content/projects.json` e execute:

```bash
python3 scripts/build_projects.py
```

Os blocos delimitados por `PROJECTS:START/END` e `PROJECTS-JSONLD:START/END` são gerados; não os edite à mão. Confira descrição, URL, imagens e autorização de uso antes da publicação.

## Validar e gerar a versão estática

```bash
python3 scripts/check_site.py
python3 scripts/build_static.py
```

`build_static.py` chama o gerador de projetos, prepara sitemap e robots para `https://www.visionintelligence.com.br`, executa o checker e copia apenas páginas/ativos públicos para `dist/`. Exclui as páginas em `prototipos/` e as imagens de referência usadas apenas nesses estudos. A pasta `dist/` não é fonte editável; ajuste os HTML e scripts na raiz.

Para testar a saída final localmente, depois do build:

```bash
python3 -m http.server 3000 --directory dist
```

## Direção visual e privacidade

O sistema editorial usa Barlow Condensed em títulos e DM Sans no corpo, com papel/neutros e âmbar `#FFAB00` como único acento. O header é transparente e sticky, sem faixa sólida no estado fechado. A configuração WebDev está com analytics da plataforma desativado e selo/scripts da plataforma ocultos; o código do site não contém pixels, ferramentas de rastreamento ou iframes de terceiros identificados na revisão. Registros técnicos do provedor/CDN ainda precisam ser confirmados; não se afirma ausência universal de cookies.

O formulário pede apenas nome e empresa como obrigatórios; site/Instagram e objetivo são opcionais. O site não envia nem armazena as respostas. O botão de WhatsApp permanece desativado enquanto não for configurado um número oficial — não substitua a ausência por um número inventado. Quando o destinatário real for autorizado, atualize `whatsappNumber` em `assets/js/diagnostic-form.js`, teste o fluxo e revise as políticas antes de ativar o contato.

## Antes de publicar

- Substituir razão social, CNPJ, endereço, e-mail e canal oficial nos rodapés e documentos legais após confirmação.
- Definir e preencher o número de WhatsApp da Vision; testar o envio voluntário, a mensagem e o destino.
- Confirmar com advogado a base legal, retenção/exclusão, compartilhamento, foro, titularidade e responsabilidades descritos nas políticas; manter o comentário “Revisar com advogado antes de publicar”.
- Confirmar com o provedor os logs, cookies técnicos, métricas e prazos de retenção da hospedagem/CDN.
- Obter autorização escrita e créditos para nomes, marcas, imagens e capturas dos projetos; a imagem de Eurogenesis que veio no pacote estava vazia e foi substituída por um tratamento tipográfico.
- Rever conteúdo, contatos e links externos e confirmar o domínio público antes de ativar uma publicação.

A criação do checkpoint não publica o site por si só; a publicação é uma etapa separada e não foi solicitada.
