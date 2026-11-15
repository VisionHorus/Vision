# Plano de revisão visual — Vision

## Decisão atual

A orientação mais recente do usuário substitui a direção clara/editorial usada na versão anterior. O site deve ter presença artística, tecnológica e dinâmica, com predomínio de fundos escuros em tons pensados, algumas áreas claras para contraste, laranja como acento, títulos de personalidade serifada/arredondada, botões quadrados e quadros de interface com vidro usado seletivamente. O robô humanoide de moletom âmbar que veio no novo `Sites.rar` será a peça do hero da home. Imagens fornecidas poderão ser usadas conforme agreguem à narrativa; não há obrigação de incluir todas.

O usuário aprovou a execução sem novas interrupções para aprovação visual. O estilo de Kantsuo foi enviado como referência de personalidade e ritmo, não como template: criar expressão e interação próprias para a Vision, sem reproduzir sua identidade, copy, ilustração ou composição. O usuário rejeitou o aspecto excessivamente branco, a manchete em sans condensada/geométrica simples e a apresentação estática com aparência de PDF.

## Abordagem técnica

Manter a base estática existente em HTML semântico, CSS modular e JavaScript nativo; não adicionar framework, biblioteca de animação, serviço externo nem analytics. O conteúdo principal, SEO e navegação permanecem no HTML inicial. Adicionar um controlador leve com `IntersectionObserver` para alternar o tom do canvas conforme as seções, revelar elementos ao entrarem na tela e escrever uma ou duas microfrases após rolagem; conteúdo deve permanecer disponível sem JavaScript e legível por leitores de tela. `prefers-reduced-motion` transforma animações em estados imediatos/estáticos.

Usar o robô fornecido como ativo principal da primeira dobra, comprimido para WebP com dimensão compatível com a exibição. Se a imagem tiver fundo escuro opaco, integrá-la à base escura com composição e mistura CSS testadas, sem remover detalhes por recorte destrutivo. Servir as versões otimizadas locais de `assets/images/` no Preview e no build estático; manter os arquivos-fonte fora da árvore do site. A silhueta fornecida aparece uma vez na seção editorial da home e a coruja abre a página de inteligência digital, sem repetir ativos como decoração genérica. Manter licença/crédito e pendências de direito em `content/image-credits.md`.

## Direção de arte

- **Movimento:** editorial digital cinematográfico, experimental e acolhedor, com referências de estúdio criativo e interface de produto — conteúdo ativo e navegável, não uma sequência de slides ou uma folha impressa.
- **Princípios:** (1) oferecer protagonismo à marca e ao produto do cliente; (2) combinar uma composição memorável com hierarquia de leitura impecável; (3) reservar animação para indicar aparecimento, conexão e mudança de contexto; (4) fazer cada seção ter um ritmo próprio sem perder unidade.
- **Paleta:** base carvão `#090A10`, superfícies `#13161E` e grafite `#1B1E28`; texto marfim `#F4EFE8`; laranja queimado `#F47A40`; as cenas alternam ameixa, azul-fumaça, papel e brasa, sem introduzir outro acento. Contraste WCAG AA continua obrigatório.
- **Layout:** hero assimétrico e de altura cinematográfica, com headline grande sobre/ao lado do robô e um board translúcido sobreposto; painel de sinal digital como interface, não como card genérico. Depois, alternar canvas escuro contínuo, uma ou duas passagens claras e quadros de projeto amplos. As transições de cor do canvas acontecem suavemente ao cruzar limites entre grupos de conteúdo; evitar regra horizontal em todas as seções.
- **Elementos de assinatura:** o robô em escala editorial; boards de vidro localizados com bordas finas e tipografia de interface; composições texto/imagem que se cruzam sem perder leitura. Pode haver um único halo/gradiente radial discreto no hero e em até uma transição quando tiver função de luz; não usar ondas/blobs genéricos.
- **Interação:** header transparente e sticky mantido; CTA principal quadrado, com movimento curto de seta/borda no hover e estados de foco; cartões/links com resposta tátil visual. O menu de celular mantém estados e foco corretos. Revelações são acionadas uma vez; microtypewriter aparece só em frases pequenas e jamais substitui ou anuncia fragmentos do conteúdo principal a tecnologias assistivas.
- **Animação:** entrada de elementos em `opacity`/`transform` de baixa distância, mudança lenta de canvas, um indicador textual curto escrito por letras quando chega à seção e movimento opcional leve em um traço/constelação. Sem autoplay de vídeo, sem parallax obrigatório, sem movimento infinito para leitores que prefiram reduzir movimento, sem bloqueio de clique ou leitura.
- **Tipografia:** `Fraunces` variável/local nos títulos — serifada expressiva, com formas mais redondas e escala fluida, pesos 600–800; `DM Sans` local para corpo, interface e botões; pequenos índices podem usar monospace local/de sistema. Evitar manter Barlow Condensed como fonte principal de manchetes. O texto do hero deve ser pesado, curto e legível sobre o recorte da imagem.
- **Essência e voz:** presença digital para empresas locais e PMEs que precisam mostrar seus produtos/serviços, construir confiança e ampliar a chance de serem encontradas do Instagram ao Google e a respostas de IA. A voz é energética, clara e responsável. Exemplos de direção: “Sua empresa não pode ser um segredo.” e “Do Instagram à busca, tudo precisa apontar para o seu negócio.” Manter disclaimer de que SEO/IA não permitem prometer posição ou resultado.
- **Wordmark:** preservar símbolo e nome Vision existentes; não desenhar ícone substituto. Usar wordmark tipográfico consistente com a nova fonte de interface.

## Escopo de execução

1. Atualizar este plano, `TODO.md` e `content/visual-brief.md` para esta revisão visual.
2. Localizar, otimizar e incluir o robô do novo RAR; reorientar tokens, tipografia e componentes globais; acrescentar mudança de cena, reveal, microtypewriter e hover usando código nativo.
3. Recriar a home com hero de grande personalidade, imagem do robô, quadro de sinal digital e composição de texto/imagem. Dar visuais próprios à faixa de prova, serviços, método, portfólio e CTA, aproveitando o conteúdo verdadeiro e preservando a ação “Solicitar diagnóstico”.
4. Reaplicar o sistema às páginas existentes sem alterar URL, política legal, fluxo de dados do diagnóstico ou metadados corretos; personalizar o visual dos serviços, projetos, páginas legais, diagnóstico e 404 para que não pareçam páginas repetidas.
5. Revisar contraste/teclado/ARIA, `prefers-reduced-motion`, overflow mobile, o funcionamento das transições e das animações com JavaScript desativado, e os estados hover/focus.
6. Regenerar a saída estática, refazer checker/Nu/axe/Lighthouse e capturas específicas da versão escura. Atualizar relatório e crédito de imagens. Não publicar.

## Organização

- `assets/css/tokens.css`, `fonts.css`, `base.css`, `components.css`, `layouts.css`, `motion.css` e `responsive.css`: design tokens, famílias locais, canvas escuro, tipografia, vidro, componentes, ritmos por página, movimento e breakpoints.
- `assets/js/site.js`: menu, ano, observação de cenas, reveal progressivo e microtypewriter acessível.
- `assets/js/diagnostic-form.js`: fluxo de diagnóstico existente; continua separado da interação visual.
- HTML de rotas existentes: novo hero/composições, cenas e atributos de movimento, mantendo conteúdo semântico e estado de dados.
- `content/`: créditos, brief atualizado, capturas e relatório da revisão.
- `scripts/`: geradores atuais e build estático; não há mudança de framework.

## Limites e pendências herdados

O site continua sem publicação. Antes dela ainda é necessário preencher razão social, CNPJ, endereço, e-mail e canal LGPD; confirmar hospedagem/logs; revisar políticas com advogado; ativar número oficial de WhatsApp; confirmar por escrito os direitos/créditos das imagens de clientes e referências. Analytics permanece desligado. Nenhum prazo, preço, ranking, métrica, prova social ou resultado de venda será inventado. A validação auditiva com leitor de tela dedicado segue pendente por indisponibilidade no ambiente.
