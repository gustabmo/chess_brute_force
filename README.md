# Project chess brute force
## Description
### Program input:
- nothing -> starts from a standard starting position chess board
- a fen -> describes the position to start
- a list of moves in algebraic form -> starts from a standard starting position chess board, plays these as fixed moves

### How it works:
Starting from the position given as input, it creates a tree of all possible movements, then tracksback to decide if the initial position was a win, a draw or a loss
Grab a LONG book to wait for the program to run ;-)

### Next steps: 
Not sure if there will be any

## Initial ideas:

Fazer uma arvore com todas as jogadas possiveis.

A raiz da árvore é nivel 0, os niveis impares da arvore sao jogadas das brancas, os pares sao jogadas das pretas

Cada nó pode ter uma marca vitória (de quem fez a jogada), empate, derrota ou vazio.

Na construção da árvore todas as folhas (últimos nós) vão estar marcados como vitória ou empate. O resto vai estar vazio.

Percorre todos os nós de arvore que sao vitoria.
Pra cada um:
- Sobe um nó 
- se vazio:
- - marca derrota 
- - se todos os irmãos estiverem derrota, sobe um, marca vitória e não esquece de por ele na lista de vitórias que estão sendo percorridas

Marca todos os vazios como empate

No nó 0 estará o resultado das pretas no começo do jogo


Construcao da arvore:

O nó de nivel 0 nao tem jogada nenhuma, mas ele representa a posicao inicial do tabuleiro.

A partir daí voce passa por cada nó fazendo assim: se ele for de um nivel par voce pensa em jogadas com as pecas brancas (pois elas vao estar no proximo nivel, que vai ser impar), se for impar voce pensa em jogadas com as pecas pretas.

Pra comecar voce pensa na posicao de tabuleiro que ele representa, que é comecar com a posicao inicial e ir jogando os nós da arvore que chegaram nesse nó. Pode ser que seja um empate por repeticao, ou por pecas insuficientes (exemplo: so tem os dois reis, ou outras combinacoes), nesse caso voce marca o nó como empate e passa pro proximo. Daí voce faz um loop em todas as pecas da cor que vai jogar e pra cada uma voce faz um loop em todas as jogadas validas dessa peça. Cada jogada valida de cada peça cria um nó filho.

Se não tiver nenhuma jogada valida: se o rei da cor que iria jogar estiver atacado voce marca vitoria. Se nao estiver atacado voce marca empate (stalemate).

E continua até acabarem os nós.
