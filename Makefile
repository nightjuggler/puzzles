
all: nqueens-naive nqueens-wirth queens3d-naive

nqueens-naive: nqueens-naive.c
	gcc -o nqueens-naive -O2 nqueens-naive.c

nqueens-wirth: nqueens-wirth.c
	gcc -o nqueens-wirth -O2 nqueens-wirth.c

queens3d-naive: queens3d-naive.c
	gcc -o queens3d-naive -O2 queens3d-naive.c
