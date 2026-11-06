# Plano de implementação — Vision

## Abordagem

Construir o site com HTML semântico, CSS e JavaScript nativos, sem Next.js nem framework obrigatório. Assim, os arquivos poderão ser abertos e editados diretamente no VS Code. Cada página terá seu próprio `index.html` estático na raiz ou em pasta de rota, com conteúdo visível no HTML inicial para SEO. CSS e JavaScript compartilhados ficarão em `assets/`. A estrutura será servida diretamente pela raiz do projeto, sem subpasta `public/`, para abrir com Live Server. Um servidor local simples, sem dependências externas, será documentado para testar as rotas amigáveis; também será possível servir a pasta do projeto com uma extensão como Live Server. O projeto será exportável como site estático. Sem domínio, não inventar URLs canônicas ou analytics; o contato usa o destino provisório de WhatsApp 000000000 solicitado, que deverá ser substituído pelo número oficial antes do atendimento real.

## Estrutura proposta

- `index.html`: homepage.
- `agenciamento-digital/index.html`, `criacao-de-sites/index.html`, `seo-local/index.html`, `inteligencia-digital/index.html`, `projetos/index.html` e `diagnostico/index.html`: páginas estáticas nas rotas solicitadas.
- `assets/css/`: tokens, estilos base, componentes/layouts e ajustes responsivos.
- `assets/js/`: interações pequenas, como menu mobile, ano do rodapé e formulário que prepara uma conversa de WhatsApp para revisão e envio.
- `assets/images/`: símbolo oficial original e imagens/capas de projetos.
- `manus-routes.json`: declaração das rotas do site.
- `README.md`: instalação/abertura local, estrutura, edição, SEO e publicação.
- `.env.example`: somente se a configuração da entrega final precisar de variáveis; sem segredos reais.

## Direção visual aprovada pelo briefing

**Movimento:** minimalismo tecnológico com sofisticação corporativa, sem estética de painel futurista.

**Princípios:** clareza primeiro; contraste e hierarquia disciplinados; tecnologia percebida pela precisão; interação útil e discreta.

**Cor:** base em carvão/azul profundo (#0B0F16 e #142238), texto claro (#F3F2EF), apoio cinza (#A5ACB8), laranja original da marca como destaque intencional e roxo dessaturado (#6956A5) apenas em detalhes raros. Preservar integralmente o símbolo anexado.

**Layout:** composição editorial assimétrica, grandes blocos tipográficos, grids abertos, espaço negativo e faixas de conteúdo que alternam alinhamento; evitar uma sucessão de grades genéricas centralizadas.

**Elementos de assinatura:** linhas e nós digitais muito sutis; pequenos marcadores geométricos e molduras finas; detalhes em laranja ligados a ações e navegação.

**Interação e movimento:** transições curtas e funcionais, feedback claro, estados de foco visíveis e respeito a `prefers-reduced-motion`; nenhum efeito constante ou chamativo.

**Tipografia:** sans-serif contemporânea e legível, com hierarquia expressiva e textos de leitura confortável; títulos firmes sem exagero, corpo claro e metadados compactos.

**Essência da marca:** estrutura presença digital e tecnologia para negócios que precisam ser encontrados, comunicar valor e organizar oportunidades; personalidade estratégica, confiável e contemporânea.

**Voz:** direta, acessível, segura e comercial sem exagero. Exemplos: “Sua empresa merece ser encontrada.” e “Estratégia antes da tecnologia.”

**Marca:** preservar o símbolo oficial laranja como imagem fornecida; usar “VISION” em tipografia neutra provisória, sem criar um novo logotipo definitivo nem alterar o símbolo.

## Conteúdo, SEO e experiência

A home seguirá as oito seções do briefing. As seis páginas internas terão conteúdo específico e conexões entre os serviços. O portfólio utilizará links externos e descrições verificadas nos sites de Tamo Junto Botequim, Lopes Tattoo e Eurogenesis; não atribuir resultados, métricas ou depoimentos à Vision. Usar assets reais dos próprios sites se forem acessíveis e adequados; caso contrário, utilizar capas gráficas sóbrias identificadas como representações visuais, nunca fotografia genérica apresentada como trabalho real.

Implementar navegação acessível, responsividade mobile-first, HTML semântico, sitemap, robots, Open Graph/Twitter e dados estruturados apenas com fatos confirmados. Definir título e descrição exclusivos por rota. Como não há domínio informado, não emitir canonical ou `og:url` absolutos inventados; deixar a configuração documentada para quando o domínio real for fornecido. O formulário de diagnóstico abre uma conversa de WhatsApp pré-preenchida com as respostas para o visitante revisar e enviar; o site não armazena os dados. O número provisório é 000000000 e deve ser substituído pelo destino real para receber mensagens.

## Execução e entrega

Manter o código claro, editável e separado por responsabilidade, sem minificação e sem dependências desnecessárias. Incluir `README.md` com como abrir/servir localmente, estrutura, edição de conteúdo, imagens/logo, CSS/tokens, rotas, SEO e publicação. Preparar `.env.example` se aplicável. Entregar todas as páginas e assets, instruções e checklist, além de um ZIP editável do código-fonte. A publicação pública e o domínio não serão presumidos; a versão de preview e o pacote de código serão preparados, e as pendências de domínio, número oficial do WhatsApp e analytics serão registradas.