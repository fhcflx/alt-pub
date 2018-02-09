Title: Guia completo de como contribuir com Publicações Acadêmicas
Date: 2017-12-27 16:03:45 -0300
Category: Guia da página
Lang: pt
Tags: guia

[![GitHub release](https://img.shields.io/github/release/fhcflx/alt-pub.svg)](https://github.com/fhcflx/alt-pub/releases?colorB=dd4814)
[![Project DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.845747.svg)](https://doi.org/10.5281/zenodo.845747)
[![Article DOI](https://img.shields.io/badge/ARTICLE--DOI-10.6084/m9..5435968-dd4814.svg)](http://dx.doi.org/10.6084/m9.figshare.5435968)
[![pdf](https://img.shields.io/badge/pdf-download-dd4814.svg)]()

Este guia ensina como contribuir de maneira ética e livre com a página Publicações Acadêmicas, e participar ativamente do movimento da [Ciência Aberta][ca] [1]. Dúvidas podem ser endereçadas ao e-mail do autor ([fhcflx@outlook.com][mail]), ou ao seu Twitter [@fhcflx][twit]. O projeto é livre para ser copiado, modificado e ampliado. Comentários e contribuições são muito bem-vindos! A ciência deve ser feita por todos e deve ser livre para todos!

## Por quê contribuir com Publicações Acadêmicas?

Existem cada vez mais vias de publicação de todo tipo de material acadêmico e não acadêmico. Pré-publicações, pós-publicações, auto-arquivamento, publicações de pôsteres, diapositivos e outros materiais apresentados em reuniões, congressos, encontros, etc. Resultados brutos de pesquisa, desenho experimental, projetos para agências de fomento ou comissões de ética, monografias, opiniões, comentários, revisões por pares. A diversidade de materiais que pode ser publicada de alguma forma em formato eletrônico somente será limitada pela imaginação humana. No futuro, essa promete ser a fonte de uma grande revolução na pesquisa científica e dará origem a novos campos de estudo, como a [metapesquisa científica][meta] [2], a pesquisa acerca da pesquisa (ou dos dados publicados de alguma forma).

Sendo assim, para quê mais um canal de publicação eletrônica? Ainda mais, sem características que os outros canais se esforçam em possuir, como revisão por pares, indexação, atribuição automática de número de [DOI][doi], entre outros. A verdade, é que este projeto constitui apenas mais um entre muitos. Nisto, não vejo realmente fraqueza, pois o volume futuro de dados produzidos pela humanidade será tão grande que sempre haverá espaço para praticamente todas as iniciativas. No entanto, identifiquei algumas lacunas nos projetos mais populares hoje em dia, nas quais eu gostaria de inovar, tornando Publicações Acadêmicas realmente a única do seu tipo:

1. **Este é um projeto feito para ser conduzido pela comunidade e descentralizado.** Apesar de ter um repositório único (no momento), e de ter apenas um iniciador (por hora), este projeto pode
_ser escalado_ e aceitar um número ilimitado de contribuições e participantes.
2. **Este é um projeto completamente hackeável.** Basta ter uma conta no servidor remoto [Git][git] que usamos agora ([GitHub][github], mas pode não ser aquele usado no futuro, nem o único) e contribuir. É possível mudar praticamente tudo. Quanto mais a comunidade que contribui aumentar, mais o projeto vai se transformar e adquirir uma feição própria. O poder de gerenciamento local do [Git][git] permitirá que a comunidade use facilmente qualquer servidor remoto que quiser, mesmo vários deles no futuro.
3. **Este é um projeto seguro.** Usando [assinaturas por chaves GPG][gpg], os autores poderão estar tranquilos de proteger sua autoridade e precedência sobre seus trabalhos. O projeto é baseado na idéia de livre acesso, porém com atribuição da autoria. Dessa forma, é completamente à prova de plágio (_plagiarismo pode ocorrer, mas com [assinatura de chaves GPG][gpg] será possível provar de imediato a falsidade_).
4. **Este é um projeto completamente citável e rastreável.** Usando plataformas existentes e consagradas de arquivamento eletrônico ([figshare][figshare] e [Zenodo][zenodo]), um número [DOI][doi] pode ser atribuído ao projeto como um todo e a cada publicação em especial. Por exemplo, este texto está registrado no [figshare][figshare] com o [DOI][doi] 10.6084/m9.figshare.5735136 e o projeto completo (versão atual de Publicações Acadêmicas) está registrado no [Zenodo][zenodo] com o [DOI][doi] 10.5281/zenodo.594582. Existem formas de automatizar este processo, mas para manter uma checagem de qualidade mínima, o ideal é manter o processo através de um curador.
5. **Este é um projeto com qualidade checada pela comunidade.** Ao invés de um editor(es) como canais usuais de publicação, este projeto terá um curador(es), que zelará pela qualidade mínima e organização do material contribuído. Ao longo do tempo, a comunidade passará a criticar e revisar ativamente as postagens, através de comentários, questões (_[issues][issue]_) e contribuições (_[pull requests][pull]_).
6. **Este é um projeto legal!** Eu acredito firmemente na participação da comunidade em projetos de comunicação e integração do conhecimento científico. Criar este projeto e fazer parte dele, mesmo que não obtenha uma grande ressonância, já constitui um grande privilégio! É uma das coisas mais legais que já fiz!

## Formatos de contribuição:

Este projeto não é um jornal científico, não tem registro em ISSN, nem é indexado em nenhuma base de dados acadêmica. Existem formas simples de indexar os trabalhos no Google Acadêmico, as quais descrevemos em outro local. Assim, não é correto falar no material postado aqui como tendo sido "publicado", nem colocar esta informação em currículos. Apesar de pessoalmente defender uma visão menos restritiva de _publicação_ (daí o título do projeto), esta distinção é necessária para evitar abusos. É preciso deixar claro que uma "publicação" (se quiser chamar assim) neste projeto não se trata de uma _publicação revisada por pares em revista indexada_. Mais apropriadamente, deve-se chamar a contribuição de material não previamente publicado de _pré-publicação_ e de material já previamente publicado de _pós-publicação_. Estas são as duas modalidades básicas de _publicação_ suportadas por este projeto.

Dito isto, esta é uma lista não exaustiva e não completa de formatos que podem ser submetidos:

1. **Pré-publicação:** ou _[preprint][preprint]_, material acadêmico redigido com o objetivo de publicação em um periódico tradicional ou outro canal de publicação, depositado **antes** da submissão e revisão por pares. Mais recentemente, uma quantidade de _[preprints][preprint]_ nunca chega a ser publicada em canais revisados por pares, mantendo seu estado de _pré-publicação_ e sendo mesmo citados como _[preprints][preprint]_. Uma pré-condição para depositar _[preprints][preprint]_ é verificar se o veículo onde se deseja a publicação final permite esta prática.
Os mesmos formatos que podem ser publicados num canal convencional podem ser depositados como pré-publicações:
  - **artigos**
  - **revisões**
  - **comentários** (cartas) e outras formas de _front matter_
  - **comunicações breves**, etc
2. **Pós-publicação:** ou _[postprint][post]_, prática menos comum até o surgimento de canais como o Researchgate, [figshare][figshare], [Zenodo][zenodo] e outros. Trata-se do depósito de material **após** a submissão, revisão por pares e publicação em canais tradicionais. Um pré-requisito para essa modalidade é a posse dos direitos autoriais sobre a obra pelos autores. Alguns jornais tradicionais permitem o depósito em repositórios institucionais.
Assim como quanto às pré-publicações, os mesmos formatos podem ser depositados como pós-publicações.
3. **Auto-arquivamento:** ou _[self-archiving][self]_, uma distinção arbitrária em relação às modalidades anteriormente descritas. Pode-se dizer que tanto as pré como as pós-publicações depositadas pelo autor são formas de _auto-arquivamento_. Dessa forma, torna-se menos relevante distinguir esta modalidade. Poder-se-ia dizer, mais especificamente, que textos criados _exclusivamente para serem auto-arquivados_ ou cujo autor não visa mais a publicação (por exemplo, material submetido mas não aceito em algum canal de publicação) poderiam entrar nesta definição. No entanto, uma definição menos estrita de _preprint_ também engloba estas hipóteses. O depósito institucional de pós-publicações também pode ser classificado assim.
4. **Material de pesquisa:** desenhos experimentais, projetos de pesquisa, resultados brutos, plano de análise estatística, análises estatísticas preliminares, notas de cadernos de pesquisa, e quaisquer outros materiais, textos, figuras, coleções de dados que possam ser depositados de forma **livre e acessível**, sob uma licença compatível com [Ciência Aberta][ca] (na maioria dos casos, [Creative Commons Atribuição 4.0][ccby]). Qualquer material postado necessitará automaticamente disponível publicamente. Ciente disto, é uma ótima maneira de mostrar para a comunidade o progresso de uma linha de pesquisa.
5. **Apresentação em conferência:** pôsteres, diapositivos, resumos simples, resumos estendidos, trabalhos completos publicados em anais de conferências. Mais uma vez, apenas material sobre o qual os autores detiverem os direitos autorais poderá ser postado.
6. **Literatura cinzenta:** ou _[grey literature][grey]_, de acordo com a definição de Praga, "representa múltiplos tipos de documentos produzidos em todos os níveis de governo, academia, empresas e indústria em formatos impressos e eletrônicos, protegidos por direitos de propriedade intelectual, de qualidade suficiente para serem coletados e preservados por bibliotecas ou repositórios institucionais, mas não controlados por editoras comerciais, ou seja, em que a publicação não é a atividade principal do corpo de produção" [3]. Na maioria das vezes, publicações internas e formatos alternativos em instituições públicas ou empresariais. Na definição menos restrita de Farace & Schöpfel [3], inclui livros brancos (_[white papers][white]_), postagens em blogs, manuais técnicos e muitas outras formas não tradicionais de material acadêmico. Também se aplica a exigência de controle de direitos autorais pelos autores.

## Instruções para autores:

Apenas material acadêmico será aceito. Nenhum material com fins publicitários ou comerciais poderá ser incluído. Se os autores pretendem usar parte ou todo o material a ser postado em algum empreendimento comercial no futuro, recomenda-se que a contribuição não seja feita. Para todos os formatos, os autores devem mandar seu nome completo e filiação. Além disso, pede-se que escrevam três ou quatro linhas (em torno de 200 a 400 caracteres) para mostrar na página principal como sumário da postagem.

### Limites para o material postado:

- **Pré-publicações:** não há limites de número de caracteres ou exigências para a postagem. Todos os textos serão transformados através do programa [Pandoc][pandoc] em formato [Markdown][markdown] e, posteriormente, compilados em arquivos em formato `pdf`. O aspecto final é padronizado e um exemplo da tipografia utilizada pode ser visto aqui. Textos em formato de rascunho, formato de revisão ou formato final de submissão para outro meio de publicação podem ser aceitos. Material audiovisual (figuras, gráficos, vídeos, som) podem ser incluídos em qualquer formato (arquivos individuais), mas não há garantia de que possam ser sempre incluídos no resultado final, dependendo de limitações da infraestrutura utilizada (veja próxima subseção). Os autores devem checar, inicialmente, se os meios aos quais desejam submeter seus trabalhos posteriormente são compatíveis com pré-publicação (veja próxima seção). Nesse momento, somente é possível receber submissões em português e inglês e nos formatos suportados pelo programa [Pandoc][pandoc] (veja próxima subseção).
- **Pós-publicações:** o mesmo que se aplica às pré-publicações aplica-se aqui. A diferença é que os autores devem manter os direitos autorais completos sobre suas obras. Se você assinou um têrmo de cessão de direitos autorais ao publicar em outro meio, isso não é mais possível. Alguns periódicos e meios de publicação permitem a auto-arquivamento pelo autor de _rascunhos_ (próxima seção).
- **Auto-arquivamento:** o mesmo em relação a limitações de texto e recursos audiovisuais. Os autores devem informar que, pelo menos no momento, não tencionam publicar o material. No entanto, não se exige nenhuma obrigação quanto a isso (os autores são livres para mudar de idéia no futuro e publicar seu material, caso em que a _auto-arquivamento_ funciona como _pré-publicacão_).
- **Material de pesquisa:** além de texto e material audiovisual, pode incluir planilhas e bancos de dados. Os formatos suportados são explicados na próxima subseção. Os autores devem anexar um "resumo" ou texto explicativo, arbitrariamente conciso, desde que suficiente para explicar do que se trata o conjunto de dados compartilhado. *Nenhuma informação relativa a seres humanos será aceita se puder ser identificada de maneira direta ou indireta* (veja a subseção sobre _desidentificação_).
- **Apresentação em conferência:** a melhor forma de disponibilizar materiais como pôsteres e diapositivos é depositá-los num serviço especializado como o [Slideshare][slide] e incluí-los na página da postagem. Caso os autores não desejem esta solução, pode-se incluir uma ligação para baixar o arquivo da apresentação. Os autores devem anexar um "resumo" ou texto explicativo, arbitrariamente conciso, desde que suficiente para explicar do que se trata a apresentação. Também devem indicar em que evento (nome completo, local e data) a apresentação ocorreu. A contribuição de resumos, resumos extendidos e trabalhos completos publicados em anais procede da mesma forma que a pós-publicação de material revisado por pares.
- **Literatura cinzenta:** de forma geral, os mesmos limites de formato, conteúdo e restrições éticas se aplicam a este tipo de material.

### Formatos aceitos:

- **Texto:** texto simples (`.txt`), microsoft office (`.doc,.docx,.rtf`), open office (`.odt,.fodt`), [Markdown][markdown] (vários "sabores"), html, LaTeX, reStructuredText.
- **Imagens:** qualquer formato, mas apenas os formatos `jpg, png` e `gif` poderão ser visualizados na página. Os outros poderão ser convertidos ou anexados como ligações para baixar os arquivos. É possível que imagens muito grandes ou alguns formatos não possam ser suportados pela infraestrutura do [GitHub Pages][githubp], onde a página é hospedada.
- **Gráficos:** serão aceitos códigos em R e LaTeX para serem convertidos em imagens com rmarkdown.  
- **Vídeo:** a forma preferida de postar vídeos é fazer o _upload_ do material para o [Youtube][youtube] ou serviços similares e, então, incluir na página.
- **Audio:** qualquer formato, mas os arquivos ficarão apenas disponíveis para serem baixados. Limites de tamanho podem se aplicar.
- **Planilhas:** qualquer formato, mas apenas o formato `csv` poderá ser visualizado na página. Os outros poderão ser convertidos ou anexados como ligações para baixar os arquivos.
- **Bancos de dados:** qualquer formato, mas os arquivos ficarão apenas disponíveis para serem baixados. Limites de tamanho podem se aplicar.

## Declaração sobre ética:

### Conformidade com pré-publicação:

Os autores que contribuírem com pré-publicação devem checar se o veículo a que se destina a submissão final está em conformidade com esta prática. Na página do projeto [SHERPA/RoMEO][sherpa] pode-se buscar com facilidade pelo nome ou ISSN de jornais. Veículos listados como "verdes" permitem pré e pós-publicação. Por rotina, quaisquer trabalhos publicados em veículos de Acesso Aberto com uma licença [Creative Commons][cc] pode ser auto-arquivado. Se houverem dúvidas, o autor deste projeto pode ajudar.

### Ética para trabalhos usando animais experimentais:

Para a contribuição de auto-arquivamentos ou materiais de pesquisa usando animais experimentais, a **carta de aceitação** do projeto por uma **[Comissão de Ética em Uso de Animais][ceua]** devidamente registrada deve ser enviada junto com a contribuição. Pós-publicações, uma vez que já passaram pelo crivo de revisão editorial e por pares, estão isentas.

### Ética para trabalhos com seres humanos:

Para a contribuição de auto-arquivamentos ou materiais de pesquisa com seres humanos, a **carta de aceitação** do projeto por um **[Comitê de Ética em Pesquisa][cep]** devidamente registrado, além do **termo de consentimento informado** assinado por cada participante (ou representante legal) devem ser enviados junto com a contribuição. Pós-publicações, uma vez que já passaram pelo crivo de revisão editorial e por pares, estão isentas.

Da mesma forma, não serão aceitos materiais que não tenham sido devidamente _desidentificados_. Este processo visa evitar a identificação direta ou indireta dos sujeitos experimentais em um estudo clínico. Normalmente, basta retirar dos resultados, bancos de dados ou texto os seguintes itens:
- Nome, incluindo iniciais ou apelidos.
- Procedência, mesmo a cidade. Se necessário identificar pacientes oriundos de mais de um centro de tratamento, codificar a informação (p.e. "centro A").
- Data de diagnóstico, data da última informação coletada, data de nascimento, outras datas.
- Outras informações que, combinadas, possam identificar os participantes da pesquisa.
Igualmente, na contribuição de material audiovisual de estudos com seres humanos, não serão aceitos aqueles que permitem a identificação. Por exemplo: fotos da face inteira não podem ser aceitas, apenas de partes da face, descaracterizando a identidade.

## Atribuição de [DOI][doi]:

Para que a postagem tenha um [DOI][doi] atribuído, será necessário depositar os arquivos no [figshare][figshare], ou outro serviço compatível. Os próprios autores podem fazer isso, ou devem registrar no material enviado uma *autorização* para que o autor deste projeto possa fazer isso em seu nome.

## Envio da contribuição:

### Usando Git e GitHub:

- Se você já tem uma conta no GitHub e já tem noção de como usar Git, faça um _fork_ e clone o projeto, acrescente seus arquivos em formato [Markdown][markdown] na pasta `content/posts` (em português e/ou inglês), suas figuras em `content/images`, seus pdf em `content/docs` e crie um _[pull request][pull]_.
- Se você não sabe de nada disso ainda mas gostaria muito de aprender, o [GitHub][gittut] e a [Atlassian][atlassian] têm ótimos tutoriais!
- Aproveite e hackeie o projeto! Faça modificações, introduza novas características e funcionalidades, faça parte do projeto!

### Usando o bom e velho e-mail:
- Não tem interesse no Git? Sem problema, mande um e-mail com seus arquivos, nos formatos aceitos, anexados.
- Ou, mais simples ainda, está contribuindo com um texto simples? Apenas escreva seu texto completo no corpo do e-mail e mande! Siga as instruções para os autores e contribua!

### Comentando as outras contribuições:
- Através do GitHub: abra um _[issue][issue]_, ou
- Na página do projeto, deixe seus comentários.

## Referências:

1. Ciência aberta, questões abertas / Sarita Albagli, Maria Lucia Maciel e Alexandre Hannud Abdo organizadores. – Brasília: IBICT; Rio de Janeiro: UNIRIO, 2015. 312 p.
2. Ioannidis, John P. A.; Fanelli, Daniele; Dunne, Debbie Drake; Goodman, Steven N. (2015). Meta-research: Evaluation and Improvement of Research Methods and Practices. PLOS Biology. 13 (10): e1002264.
3. Grey literature in library and information studies / edited by Dominic J. Farace and Joachim Schöpfel, 2010, Walter de Gruyter GmbH & Co. KG, Berlin/New York, ISBN 978-3-598-11793-0.

[atlassian]: https://www.atlassian.com/git/tutorials
[gittut]: https://try.github.io/levels/1/challenges/1
[cep]: http://bvsms.saude.gov.br/bvs/saudelegis/cns/2013/res0466_12_12_2012.html
[ceua]: http://www.planalto.gov.br/ccivil_03/_Ato2007-2010/2008/Lei/L11794.htm
[white]: https://en.wikipedia.org/wiki/White_paper
[grey]: https://en.wikipedia.org/wiki/Grey_literature
[cc]: https://creativecommons.org/licenses/?lang=pt_BR
[ccby]: https://creativecommons.org/licenses/by/4.0/
[ca]: https://www.fosteropenscience.eu/content/what-open-science-introduction
[self]: https://en.wikipedia.org/wiki/Self-archiving
[post]: http://www.sherpa.ac.uk/romeoinfo.html
[preprint]: https://en.wikipedia.org/wiki/Preprint
[pull]: https://help.github.com/articles/creating-a-pull-request-from-a-fork/
[issue]: https://guides.github.com/features/issues/
[githubp]: https://pages.github.com
[github]: https://github.com
[git]: https://git-scm.com
[doi]: https://doi.org
[meta]: https://en.wikipedia.org/wiki/Meta-research
[zenodo]: https://zenodo.org
[figshare]: https://figshare.com
[pandoc]: https://pandoc.org
[sherpa]: http://www.sherpa.ac.uk/romeo/index.php?la=pt&fIDnum=|&mode=simple
[mail]: mailto:valkyr.ie@outlook.com
[twit]: https://twitter.com/fhcflx
[markdown]: https://daringfireball.net/projects/markdown/syntax
[slide]: https://www.slideshare.net
[youtube]: https://www.youtube.com
[gpg]: https://www.gnupg.org/gph/en/manual/c14.html
