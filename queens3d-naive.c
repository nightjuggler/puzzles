#include <stdio.h>

#ifndef N
#define N 8
#endif

#ifndef Z
#define Z 1
#endif

static unsigned char board[Z][N][N];
static unsigned int numSolutions;

void printBoard()
{
	int x, y, z;

	printf("==== Solution #%d ====\n\n", ++numSolutions);

	for (z = 0; z < Z; ++z) {
		for (y = 0; y < N; ++y) {
			for (x = 0; x < N; ++x)
				printf(" %u", board[z][y][x]);
			printf("\n");
		}
		printf("\n");
	}
}

int safe(int z, int y, int x)
{
	int k, j, i;

	for (j=y-1; j>=0; --j)
		if (board[z][j][x]) return 0;

	for (j=y-1, i=x-1; j>=0 && i>=0; --j, --i)
		if (board[z][j][i]) return 0;

	for (j=y-1, i=x+1; j>=0 && i<N; --j, ++i)
		if (board[z][j][i]) return 0;

	for (k=z-1; k>=0; --k)
		if (board[k][y][x]) return 0;

	for (k=z-1, j=y-1, i=x-1; k>=0 && j>=0 && i>=0; --k, --j, --i)
		if (board[k][j][i]) return 0;

	for (k=z-1, j=y-1, i=x+1; k>=0 && j>=0 && i<N; --k, --j, ++i)
		if (board[k][j][i]) return 0;

	for (k=z-1, j=y+1, i=x-1; k>=0 && j<N && i>=0; --k, ++j, --i)
		if (board[k][j][i]) return 0;

	for (k=z-1, j=y+1, i=x+1; k>=0 && j<N && i<N; --k, ++j, ++i)
		if (board[k][j][i]) return 0;

	for (k=z-1, j=y-1; k>=0 && j>=0; --k, --j)
		if (board[k][j][x]) return 0;

	for (k=z-1, j=y+1; k>=0 && j<N; --k, ++j)
		if (board[k][j][x]) return 0;

	for (k=z-1, i=x-1; k>=0 && i>=0; --k, --i)
		if (board[k][y][i]) return 0;

	for (k=z-1, i=x+1; k>=0 && i<N; --k, ++i)
		if (board[k][y][i]) return 0;

	return 1;
}

void doRow(int z, int y)
{
	int x;

	for (x = 0; x < N; ++x)
		if (safe(z, y, x)) {
			board[z][y][x] = 1;

			if (y + 1 != N)
				doRow(z, y + 1);
			else if (z + 1 != Z)
				doRow(z + 1, 0);
			else
				printBoard();

			board[z][y][x] = 0;
		}
}

int main(int argc, char **argv)
{
	doRow(0, 0);

	printf("There are %d solutions.\n", numSolutions);

	return 0;
}
