# TODO — Vision

Critérios do briefing original, organizados nas etapas autorizadas: Fase 1 + 1B, Fases 2 + 3, e Fases 4 + 5. Status não significa publicação.

## Fase 0 — Diagnóstico inicial

- [x] Executar `scripts/check_site.py` antes das alterações e guardar o resultado.
- [x] Rodar Lighthouse mobile em todas as páginas de origem para acessibilidade, SEO e boas práticas, guardando as notas de base.
- [x] Varrer `http`, scripts, fontes, analytics, iframes e formulários; registrar destinos externos e coleta de dados.
- [x] Registrar problemas de contraste, imagens sem `alt`, headings, foco e CSS duplicado/morto.
- [x] Entregar diagnóstico priorizado antes de alterar a aplicação.

## Fase 1 — Fundação global

- [x] Incorporar `visual-refresh.css` aos módulos CSS apropriados, manter tokens como fonte única para cores, espaçamentos e tipografia, remover o remendo visual e estilos sem uso.
- [x] Hospedar WOFF2 localmente quando havia Google Fonts, com `font-display: swap`.
- [x] Padronizar header e footer em todas as páginas. Footer com razão social, CNPJ, endereço e e-mail de contato, todos como `[PREENCHER: ...]`, e links para Privacidade, Termos e Cookies.
- [x] Foco visível nos elementos interativos; skip link funcional; menu mobile operável por teclado, fecha com Escape e mantém `aria-expanded` correto; `lang="pt-BR"`; um único `h1` por página.
- [x] `title` e `description` únicos, Open Graph e Twitter coerentes (`summary_large_image` quando houver imagem) e canonical.
- [x] Incorporar a instrução adicional do usuário: header transparente, sem painel/faixa opaca, com marca/navegação e botões, sticky e acompanhando a rolagem; comportamento responsivo e sem ocultar conteúdo/foco.

## Fase 1B — Sistema visual e protótipos

- [x] Estudar as referências `ref 1–8` e `savee-01–05`, e criar `content/visual-brief.md` com três adjetivos, análise de cada referência legível (o que usar/evitar), paleta e contraste, tipografia, imagens e padrões de layout. Usar princípios, não cópia.
- [x] Atualizar `tokens.css` para cores, tipografia, espaçamentos, raios, sombras e durações; preservar nome/símbolo Vision e derivar um único acento do símbolo.
- [x] Criar protótipos separados dentro de `prototipos/`, sem substituir a home: ambos têm header, hero, CTA “Solicitar diagnóstico” e faixa de prova de projetos reais; A escuro com acento; B claro/texturizado com acento.
- [x] Garantir que a tipografia seja versátil para web e composição editorial/social semelhante a post de Instagram: manchete expressiva, apoio conciso, alinhamento e margem legíveis em telas estreitas.
- [x] Usar imagens de referência fornecidas com origem registrada; manter fotos de referência nos protótipos e fora das rotas indexáveis e do build público; imagens fornecidas não implicam direito automático de publicação.
- [x] Evitar gradientes em ondas/blobs, neon/glow, glassmorphism, 3D genérico, imagens geradas por IA sem curadoria, texto fino/cinza em fundo escuro, mais de um acento, ícones em círculos, layouts repetitivos e cópia literal. Sem autoplay; respeitar `prefers-reduced-motion`.
- [x] Escolher a direção clara/editorial para seguir sem interromper por aprovação intermediária, conforme a autorização posterior do usuário. É a premissa adotada para execução e pode ser alterada pelo usuário.

## Fases 2 + 3 — Páginas legais e formulário

- [x] Criar `/privacidade/`, `/termos/` e `/cookies/` em português claro, com `[PREENCHER: ...]` onde faltam dados e comentário HTML “Revisar com advogado antes de publicar”.
- [x] Privacidade/LGPD: explicar controlador, dados coletados, finalidade, base legal, compartilhamento/ferramenta que recebe o formulário, retenção, direitos do titular do art. 18 e canal de contato para exercer direitos.
- [x] Termos: explicar regras de uso, propriedade intelectual, limitação de responsabilidade e foro; não inventar dados empresariais.
- [x] Cookies: corresponder à varredura real. Analytics de plataforma e selo/scripts estão desativados; não foi encontrado tracking do site; declarar isso e não criar banner. Manter ressalva sobre logs técnicos e serviços externos.
- [x] Criar política de reembolso somente se houver venda direta pelo site; como não há venda direta, não criar e registrar essa decisão.
- [x] Refatorar `assets/js/diagnostic-form.js` e `/diagnostico/index.html` para coletar somente o necessário, remover campos supérfluos, informar finalidade junto ao botão e linkar a política de privacidade.
- [x] Checkbox de aceite não é usado. Se um checkbox vier a ser necessário, ele nunca deve iniciar pré-marcado.
- [x] Usar labels reais, erros claros, feedback acessível em `aria-live`, `autocomplete` adequado e proteção honeypot sem CAPTCHA de terceiros.
- [x] Explicar destino, retenção e exclusão: dados não são armazenados pelo site; a mensagem só é preparada localmente e é enviada voluntariamente pela ferramenta WhatsApp. Não ativar até receber/testar o número oficial, sem inventar destinatário.

## Fase 4 — Reformulação das páginas

- [x] Reformular na ordem prescrita: `/diagnostico/` → `/projetos/` → home → `/agenciamento-digital/` → `/criacao-de-sites/` → `/seo-local/` → `/inteligencia-digital/` → `404.html`.
- [x] Para cada página, definir objetivo e ação principal; reescrever copy concreta e humana para uma agência de Salvador falando com donos de negócios.
- [x] Apagar texto sobre a própria página/redação; remover frases vazias/genéricas, frases simétricas de efeito, listas de três itens por hábito, repetição do mesmo esqueleto de seções, mistura de idiomas, travessões excessivos, adjetivos vagos e promessas sem prova.
- [x] Explicar que a Vision ajuda empresas a venderem seus produtos/serviços e organiza presença para descoberta em Instagram, Google e inteligências artificiais; comunicar que um site profissional transmite confiança; deixar automações em segundo plano.
- [x] Não garantir primeiro lugar no Google, recomendação por IA ou resultados comerciais; usar placeholders para prazos, preços, métricas e dados não fornecidos.
- [x] Corrigir HTML semântico/headings, `alt`, contraste (4,5:1 para texto normal; 3:1 para texto grande), foco visível e teclado. Declarar `width`/`height`, usar `loading="lazy"` abaixo da dobra e WebP quando apropriado.
- [x] Aplicar o sistema visual sem repetir o esqueleto de uma página a outra; preservar URLs existentes (nenhum redirecionamento foi necessário).
- [x] Manter catálogo com os cinco projetos exigidos: Tamo Junto Botequim, Lopes Tattoo, Eurogenesis, Astromentor e Kantsuo (`https://kfezin.github.io/sitekantsuo/`, imagem `kantsuo.webp`). Atualizar `content/projects.json` e gerar blocos `PROJECTS`/JSON-LD pelo script, sem editar esses blocos gerados à mão.
- [x] Remover `eurogenesis-citizenship.jpg` vazio (0 bytes) e usar cartão tipográfico para Eurogenesis; registrar origem/direitos das imagens em `content/image-credits.md`. Capturas de clientes e imagens de referência exigem confirmação de autorização por escrito antes de publicação.

## Fases 4 + 5 — Verificação final agrupada

- [x] Executar `scripts/build_projects.py`, `scripts/generate_sitemap.py` e `scripts/check_site.py`, sincronizando sitemap, catálogo, rotas e páginas.
- [x] Validar HTML com Nu Validator; rodar axe-core; testar teclado/menu em pelo menos duas páginas; inspecionar roles, nomes e headings na árvore de acessibilidade do Chromium nas páginas Home e Diagnóstico.
- [x] Comparar notas Lighthouse mobile de acessibilidade, SEO e boas práticas com a linha de base; guardar 42 capturas da primeira dobra: antes/depois desktop e celular nas oito rotas antigas, mais novas páginas legais e protótipos.
- [x] Fechar comparativo Lighthouse mobile de desempenho, registrar LCP/CLS de Home, Diagnóstico e Projetos no relatório final; LCP ficou abaixo de 2,5 s e CLS abaixo de 0,1 nas três rotas.
- [ ] Testar manualmente com um leitor de tela dedicado em pelo menos duas páginas. A árvore de acessibilidade do Chromium e o teste de teclado foram verificados, mas não substituem o uso auditivo de leitor de tela.
- [x] Criar seis commits locais claros por página ou tarefa no branch `refactor/base`.
- [x] Integrar a branch a `origin/main` e registrar o checkpoint gerenciado; `publishing.auto_publish` permaneceu desligado e nenhuma publicação foi solicitada.
- [x] Entregar `relatorio-final.md` com mudanças por página, os 19 placeholders únicos, pendências que dependem do usuário/advogado, comparação Lighthouse e itens fora do escopo.

### Pendências antes de uma eventual publicação

- Preencher razão social, CNPJ, endereço, e-mail de contato e canal oficial para solicitações LGPD.
- Confirmar com advogado textos legais, foro, responsabilidade, titularidade/licenças e exclusões juridicamente válidas.
- Confirmar com provedor de hospedagem/CDN quais logs técnicos são coletados e seu prazo de retenção.
- Configurar e testar número oficial do WhatsApp para habilitar envio do formulário.
- Confirmar direitos e créditos das imagens dos projetos/clientes e das imagens de referência usadas nos protótipos.
- O site não foi publicado; essa entrega não inclui publicação/indexação.

## Revisão visual v2 — nova orientação do usuário

A preferência anterior por uma direção B clara foi explicitamente substituída: esta revisão passa a orientar o site público. A implementação e as validações v2 foram concluídas, com a limitação do reenvio Nu por HTTP 429 registrada no relatório. O push de `origin/main` foi aceito, mas não retornou recibo/card de Version history; por isso, a confirmação formal do checkpoint permanece pendente. A publicação automática está desligada.

- [x] Reorientar todas as páginas para uma identidade predominantemente escura, artística e tecnológica, com tons cuidadosos e seções claras ocasionais para contraste. Evitar uma apresentação estática com cara de PDF.
- [x] Trocar a fonte principal de manchetes por uma serifada expressiva/arredondada (Fraunces variável local), manter DM Sans no corpo e criar uma hierarquia de títulos mais pesada, fluida e bonita em layouts web e composições semelhantes a posts de Instagram.
- [x] Usar o robô em moletom âmbar enviado no RAR como arte principal da primeira dobra, integrando texto e imagem de modo intencional; usar outras imagens do usuário somente quando servirem à seção, sem obrigação de colocar todas.
- [x] Criar boards/painéis com acabamento de vidro apenas onde fizer sentido, mantendo texto/foco legíveis e fallback sem `backdrop-filter`.
- [x] Manter botões quadrados e acrescentar hovers responsivos com movimento curto e estados de teclado/foco visíveis.
- [x] Dar composição visual e ritmo próprios a cada seção: imagem sobreposta a parte do texto quando legível, algumas seções claras, superfícies escuras variadas e ritmo editorial/tecnológico sem repetir grids de cards.
- [x] Fazer o fundo transitar suavemente de tonalidade quando a rolagem alcança outra cena/seção; não dividir sistematicamente cada seção com uma linha ou uma troca abrupta de cor.
- [x] Introduzir animações discretas acionadas ao entrar na viewport; incluir uma ou duas microfrases em efeito typewriter após a seção aparecer, sem ocultar conteúdo quando JS faltar nem inundar leitores de tela.
- [x] Usar no máximo poucos gradientes localizados quando houver função clara de luz/realce; evitar ondas/blobs genéricos, glow excessivo e movimentos sem propósito.
- [x] Implementar todas as interações com HTML/CSS/JavaScript nativos, honrar `prefers-reduced-motion` e manter navegação, hover e foco funcionando por teclado e em mobile.
- [x] Aplicar a direção às páginas existentes sem alterar rotas, copy aprovada, política de dados ou promessa comercial; manter SEO, contraste WCAG AA e projeto real como prova.
- [x] Atualizar brief visual, créditos, capturas desktop/mobile, checker, axe, HTML Validator e métricas Lighthouse depois do redesign; registrar commits claros por tarefa.
- [x] Enviar o commit de entrega a `origin/main` sem publicar; o push foi aceito e `publishing.auto_publish` permaneceu desligado.
- [ ] Confirmar que o commit aceito em `main` consta na Version history como checkpoint gerenciado. A sessão não recebeu cartão/recibo após o push; não repetir o push apenas para tentar obter o mesmo comprovante.
