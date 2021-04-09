# Snake em Processing modo Python
## Descrição

Código voltado para ensino de Computação a alguém que está aprendendo a programar pela primeira vez, a ser escrito com a adição gradual de elementos do jogo (comida, cobra, movimentação, etc.)

## Instalando

* Seguindo [estas instruções](https://py.processing.org/tutorials/gettingstarted/),
* [baixe a última versão do Processing](https://processing.org/download/) e
* depois instale a extensão do modo Python.
## Notas
* Algumas funcionalidades são legais, mas não essenciais. Isso abre espaço para escolher alguma funcionalidade que pareça mais interessante para quem está construindo o jogo. Por exemplo, tela de início e fim de jogo ou o efeito "arco-íris" da comida ou abrir o jogo em tela cheia (não implementado).
* Os segmentos da cobra movem-se "pulando" para a posição do próximo segmento.
* Incrementos de posição dependem de uns números mágicos que deixam de funcionar se você muda o tamanho da tela.
* A comida pode surgir em cima dos segmentos.
* Quando a cobra come, acho que o novo segmento estará junto com a ponta da cauda até a cobra se mover de novo, o que não é um problema (desde que verifiquemos a condição de fim de jogo ANTES de criar o novo segmento) porque um quadrado em cima de um quadrado não vai mudar nada visualmente. Isso se resolve quando a cobre se mover de novo, já que os segmentos mais próximos da cauda se movem primeiro (copiando o próximo segmento).
* As partes mais difíceis de entender provavelmente são a movimentação (quando e como) e o posicionamento com valores específicos.

 ### Créditos
Baseado [neste sketch de P5.js](https://openprocessing.org/sketch/387971) por [Jacob Joaquin](https://openprocessing.org/user/23998)

