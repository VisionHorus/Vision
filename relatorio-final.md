# Relatório de entrega — Vision

**Estado:** redesign cinematográfico implementado e validado como site estático. O commit do redesign foi aceito em `origin/main` como `46bc977`; o site **não foi publicado** e `publishing.auto_publish` segue desligado. O resultado do push não incluiu cartão/recibo de Version history, então não afirmo que o registro formal do checkpoint foi confirmado nesta sessão.

## Direção aplicada

A Vision é apresentada como parceira de presença digital: ajuda a empresa a explicar e vender o próprio produto, aparecer nos lugares em que o público procura — Instagram, Google e respostas de IA — e sustentar confiança com um site profissional. A copy não promete primeiro lugar, recomendação garantida por IA nem resultado comercial. Automação permanece complementar.

O sistema visual usa canvas carvão `#090A10`, superfícies grafite, marfim e cenas ocasionais em papel/ameixa; o acento laranja queimado é `#F47A40`. Os títulos usam **Fraunces** variável local, com **DM Sans** para texto e interface. O header mantém transparência e posição sticky; os CTAs são quadrados. Boards translúcidos aparecem só onde ajudam a explicar os canais. A paleta e o ritmo das páginas evitam a aparência clara e genérica da direção anterior.

A home abre com o robô âmbar fornecido, um painel de sinais digitais e uma faixa de projetos reais. A silhueta feminina aparece uma vez na seção editorial da home. A coruja fornecida abre Inteligência Digital. Projetos ganhou um trabalho em destaque e quatro peças com composição alternada, em vez de um catálogo de cartões todos iguais. Serviços, projetos, páginas legais, diagnóstico e 404 usam variações próprias do mesmo sistema.

As cenas de fundo mudam suavemente com a rolagem; reveals são discretos; duas microfrases typewriter começam em momentos distintos, incluindo uma acionada ao entrar na seção editorial. O hero das páginas internas aparece imediatamente, sem aguardar animação, para reduzir o LCP. O preload local da Fraunces itálica reduziu a mudança de layout da página de privacidade. Header/menu, hover/foco, navegação por teclado, conteúdo sem JavaScript e `prefers-reduced-motion` foram revisados.

## Rotas e conteúdo

Mantidas as URLs existentes. A distribuição inclui dez rotas públicas: `/`, `/diagnostico/`, `/projetos/`, `/agenciamento-digital/`, `/criacao-de-sites/`, `/seo-local/`, `/inteligencia-digital/`, `/privacidade/`, `/termos/` e `/cookies/`. A página `/404.html` e os protótipos A/B não aparecem no manifesto público. O build gera `dist/`, `manus-routes.json`, sitemap e robots; canonicals e sitemap usam `https://www.visionintelligence.com.br` — confirmar domínio, contatos e conteúdo finais antes de publicar.

Foram criadas páginas claras de privacidade, termos e cookies com placeholders e comentário HTML para revisão jurídica. Não foi criada política de reembolso porque não há venda direta no site.

## Formulário e LGPD

O diagnóstico solicita apenas nome e negócio como campos obrigatórios; site/Instagram e objetivo são opcionais. Não solicita telefone, não envia dados a um servidor da Vision e não os persiste. O visitante só transfere o resumo se optar por abrir o WhatsApp. Há labels, `autocomplete`, mensagens de estado com `aria-live`, honeypot sem CAPTCHA de terceiro e link para a política de privacidade junto à finalidade.

O botão de envio permanece desativado até configurar e testar o número oficial. Analytics, pixels e scripts de tracking não foram adicionados; por isso, não há banner de cookies. A coleta/retenção de logs do provedor/CDN ainda precisa ser confirmada e está ressalvada na política.

## Verificações

| Verificação | Resultado |
|---|---|
| Checker e build | `scripts/check_site.py` passou; build estático concluído com 10 rotas. |
| Manifesto/sitemap/robots | `GET /manus-routes.json`, sitemap e robots retornaram HTTP 200; o manifesto corresponde às 10 rotas públicas. |
| Nu Validator | Última rodada bem-sucedida: 13 documentos (10 páginas públicas, 404 e dois protótipos), **0 erros e 0 avisos**. A repetição após acrescentar links HTML padrão de preload foi bloqueada pelo serviço externo com HTTP 429; o checker local e o browser continuaram limpos. |
| axe-core e teclado | 13 rotas, **0 violações**, **0 overflow horizontal** e sem erros de página. Skip link, menu, Enter/Escape, retorno do foco, header sticky e mudança de cena verificados. |
| Movimento e degradação | Typewriter secundário aguarda a rolagem e digita progressivamente; as duas frases ficam completas sem JavaScript e com movimento reduzido. O caret some e as transições caem para duração residual. |
| Revisão auditiva | A árvore acessível, nomes e headings foram inspecionados; não há leitor de tela dedicado/saída de voz neste ambiente. A verificação auditiva manual permanece pendente. |

### Lighthouse mobile simulado

Lighthouse 13.6.0, servidor local, 10 páginas públicas mais a 404. A última rodada obteve médias de **93,7 em Performance**, **100 em Acessibilidade**, **100 em SEO** e **100 em Boas práticas** nas páginas públicas. LCP das dez páginas ficou entre **1,20 e 1,49 s**; CLS entre **0 e 0,0675**. TBT variou de **122 a 422 ms**; as notas e métricas podem variar com a carga do ambiente.

| Página | Performance | LCP | CLS | TBT |
|---|---:|---:|---:|---:|
| Home | 99 | 1,36 s | 0,000 | 122 ms |
| Diagnóstico | 93 | 1,23 s | 0,000 | 303 ms |
| Projetos | 91 | 1,49 s | 0,000 | 357 ms |
| Média das dez páginas públicas | 93,7 | 1,37 s | 0,008 | 285 ms |

A 404 obteve 97 em Performance e 100 em Acessibilidade/Boas práticas; seu 66 em SEO decorre do `noindex` intencional.

## Capturas e evidências

O projeto guarda **42 capturas** de primeira dobra: desktop/celular antes/depois das oito rotas originais, três páginas legais e os protótipos A/B. O índice está em [`content/screenshots/README.md`](content/screenshots/README.md). Os relatórios técnicos ficam em [`content/validation/`](content/validation/), incluindo HTML, axe/teclado, movimento reduzido e comportamento das animações.

## Placeholders e pendências antes de publicar

Há 19 strings de placeholder únicas em HTML/JavaScript. Preencher cada ocorrência antes de publicar:

- `[PREENCHER: CNPJ]`
- `[PREENCHER: canal de privacidade oficial]`
- `[PREENCHER: comarca e UF após revisão jurídica; observar regras legais aplicáveis]`
- `[PREENCHER: configurar e testar o número oficial da Vision antes de ativar este canal.]`
- `[PREENCHER: confirmar com advogado e provedor]`
- `[PREENCHER: confirmar com advogado]`
- `[PREENCHER: confirmar com o provedor de hospedagem]`
- `[PREENCHER: e-mail oficial]`
- `[PREENCHER: e-mail ou canal oficial da Vision]`
- `[PREENCHER: e-mail ou canal oficial]`
- `[PREENCHER: endereço completo]`
- `[PREENCHER: endereço]`
- `[PREENCHER: número oficial do WhatsApp da Vision]`
- `[PREENCHER: prazo e procedimento de retenção/exclusão]`
- `[PREENCHER: razão social da Vision]`
- `[PREENCHER: razão social]`
- `[PREENCHER: revisar com advogado; não inserir exclusão ampla de direitos obrigatórios]`
- `[PREENCHER: serviço de hospedagem e política aplicável]`
- `[PREENCHER: titularidade e relação de licença]`

As imagens fornecidas pelo usuário foram otimizadas para WebP local. Isso não comprova licença comercial: confirmar direitos/créditos dos assets fornecidos e autorização escrita para capturas de clientes antes de publicar. A imagem de Eurogenesis que estava vazia foi removida; o cartão é tipográfico. A permissão para os assets dos protótipos também deve ser confirmada antes de qualquer uso público.

**Fora do escopo:** publicação/indexação, ativação de tracking, disparos de marketing e automações externas. O botão de WhatsApp continuará inativo até receber o número real. A publicação permanece desligada.
