# Vision — brief visual atualizado

## Revisão solicitada pelo usuário

O site não deve parecer uma apresentação estática ou “PDF”: deve ter presença artística, energia tecnológica e conteúdo que se transforma com a rolagem. Predominam fundos escuros em tonalidades cuidadosas, com algumas seções claras. O laranja das imagens é o acento principal; gradientes só entram quando funcionam como luz ou profundidade, não como decoração repetida. Botões quadrados. Títulos grandes e pesados com uma serifada expressiva/arredondada, em vez da sans condensada geométrica que estava no primeiro redesenho. Boards podem ter vidro quando esse material ajudar a contar a história.

O robô de moletom âmbar enviado no RAR é a imagem da abertura. Imagens sobrepostas ao texto são bem-vindas quando a composição mantém contraste, leitura e ordem de foco. As demais imagens do pacote são opções, não uma lista obrigatória. Referência de energia: https://kfezin.github.io/sitekantsuo/ — extrair personalidade e cadência narrativa, sem reproduzir a identidade, a arte, as frases ou o layout daquela página.

## Essência da Vision

A Vision torna negócios compreensíveis e encontrados nos lugares em que as pessoas procuram: Instagram, Google, site e respostas de inteligências artificiais. O centro é o produto ou serviço real do cliente; o site sustenta confiança e reúne a história. A voz é enérgica, clara, humana e responsável. Frases de direção: **“Sua empresa não pode ser um segredo.”** e **“Do Instagram à busca, tudo precisa apontar para o seu negócio.”** São referências de tom, não promessas de ranking. Copy não deve garantir primeiro lugar, recomendação por IA ou resultado comercial.

## Fontes e imagem de referência

As oito referências do site e as capturas Savee continuam repertório de princípios, não layout para copiar. Da referência 1 pode vir o contraste de um hero noturno e um diagrama com intenção — não seu produto, marca, verde-limão nem estrutura. Da referência 2, escala fotográfica e espaço em volta da headline — não paisagem, paleta verde ou narrativa de viagem. Da referência 3, clareza ao agrupar serviços — sem reproduzir marca agrícola, cartões ou conteúdo. Da referência 4, relação direta de hero, CTA e trabalhos reais — sem selo, números ou alegações do screenshot. Da referência 5, a alternância dramática entre claro e escuro — sem copiar mosaico, marca, fotos ou moldura vermelha. Da referência 6, títulos grandes e chamada concisa — sem repetir fundo vermelho luminoso, blur ou identidade. Da referência 7, imagem em escala ao lado de texto e trabalhos — sem reproduzir rosto, enquadramento ou telas. Da referência 8, boas imagens de projeto e separação legível — somente com trabalhos da Vision e sem imitar o arranjo.

Savee-01 e Savee-02 mostram páginas variadas de esporte, moda e serviço digital. Podem inspirar mudança de ritmo; não copiar pessoas, marcas, mosaicos ou verde fluorescente. Savee-03 reúne quadra, pôster editorial, viagem e filosofia; a variedade pode guiar a cadência, não a paleta/cópia/ornamento. Savee-04 e Savee-05 só mostram “NO IMAGE AVAILABLE”; não são fonte de estilo.

## Paleta e materiais

- **Canvas escuro:** carvão quase preto `#090A10`, com superfícies grafite e subtom azul-violeta; o preto não precisa ser chapado em todas as seções.
- **Luz:** marfim quente para títulos e leitura, cinza claro de contraste controlado e papel/creme nas áreas claras.
- **Acento:** laranja âmbar derivado do robô e do símbolo. Usar com intenção em CTA, borda, traço, número ou palavra-chave; evitar espalhar laranja por todo o corpo de texto.
- **Gradientes:** no máximo dois focos localizados, como um halo radial atrás do robô e uma passagem de luz entre cenas. Sem ondas, blobs, neon difuso ou gradientes genéricos em cada seção.
- **Boards de vidro:** translúcidos, com blur discreto, fio de borda e sombra curta. Reservar para o painel que explica canais/sinais e um conteúdo que realmente pareça interface; não converter todo bloco em glass. Sem `backdrop-filter`, o painel recebe fallback opaco e legível.
- **Contraste:** manter WCAG AA — ao menos 4,5:1 em texto normal e 3:1 em texto grande/elementos visuais. O laranja é ótimo sobre fundo escuro e com texto escuro em botão; não usar laranja como texto fino em fundo claro.

## Tipografia e composição

`Fraunces` variável local é a fonte de título: expressiva, serifada e com formas redondas; `DM Sans` permanece no corpo, navegação e interface. Peso 600–800 e `clamp()` dão presença sem apertar o texto. Microdados podem usar mono. Títulos podem atravessar a margem do recorte ou ficar parcialmente sobre a imagem, mas nenhuma letra importante deve perder contraste. A composição deve funcionar como página web e como recorte editorial/social: manchete curta, apoio conciso, CTA claro e margem segura. Não colocar copy essencial dentro de imagens.

## Composição e ritmo

1. **Abertura:** o robô domina a primeira dobra. Título serifado grande em interseção com a arte, CTA quadrado e um board flutuante que conecta Instagram, site, busca e respostas de IA. Um halo laranja muito localizado ajuda a separar a figura do fundo.
2. **Descoberta:** trocar escala e ritmo. A silhueta feminina sobre laranja aparece uma vez na composição editorial da home; garantir que a imagem não pareça decorativa sem função.
3. **Soluções:** mostrar serviços como peças com identidades visuais e informações próprias, não uma matriz de quatro cartões iguais. A automação continua em segundo plano.
4. **Trabalhos reais:** preservar projetos verdadeiros e suas descrições; capturas não são prova de métricas. O card sem imagem de Eurogenesis continua tipográfico.
5. **Próximo passo:** CTA de contato convincente, sem preço/prazo/resultado inventado; WhatsApp permanece bloqueado até configurar o número real.

Evitar divisórias horizontais em toda seção. O fundo global transita lentamente entre carvão, violeta-grafite e papel conforme o visitante cruza blocos de conteúdo, para ligar cenas sem parecer uma pilha de páginas. Elementos podem entrar com deslocamento curto, opacity ou um typewriter em microfrase; movimento é leve e acionado ao chegar na área. Não usar autoplay nem parallax que tome o controle do scroll.

## Acessibilidade e degradação

Manter header transparente/sticky, hierarquia semântica, foco, menu móvel com Escape, contraste, texto alternativo, `prefers-reduced-motion` e dimensões de imagem. Revelações não começam escondidas a menos que o JavaScript esteja ativo; sem JS, todo conteúdo continua visível. O typewriter é decorativo para leitores de tela: a frase completa está disponível de imediato no nome acessível/versão visualmente oculta e nunca é anunciada letra a letra. As composições que cruzam imagens preservam ordem de leitura e não cobrem CTA.

## Uso dos arquivos enviados

O hero da home usa `Humanoid_robot_wearing_amber_hoodie_a474dafd_2K-Photoroom.png`, enviado pelo usuário no RAR e otimizado para WebP. A silhueta `Woman_in_silhouette_with_light_dde76c0a_2K-Photoroom.png` entra uma vez na seção editorial da home; a coruja `Black_owl_perched_on_branch_e3a9968c_2K.png` abre a página de inteligência digital, como apoio visual à ideia de observar antes de automatizar. Não usar a mulher de headset VR nem a raposa sem uma razão editorial. As licenças/créditos dos assets enviados permanecem a confirmar antes da publicação.

Fontes externas e fatos consultados constam em `content/visual-sources.md`. Nenhuma imagem de stock dos resultados de busca foi incorporada.
