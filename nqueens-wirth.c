#include <stdio.h>

#ifndef N
#define N 8
#endif

typedef unsigned char bool;

static unsigned char rows[N];
static bool columns[N];
static bool diagonals1[2*N-1];
static bool diagonals2[2*N-1];
static unsigned int numSolutions;

void printBoard()
{
	int row, col, queenCol;

	printf("==== Solution #%d ====\n\n", ++numSolutions);

	for (row = 0; row < N; ++row)
	{
		queenCol = rows[row];
		for (col = 0; col < N; ++col)
			printf(" %u", col == queenCol);
		printf("\n");
	}
	printf("\n");
}

void doRow(int row)
{
	int col;
	int d1 = row;
	int d2 = row + N - 1;

	for (col = 0; col < N; ++col, ++d1, --d2)
		if (!columns[col] && !diagonals1[d1] && !diagonals2[d2])
		{
			rows[row] = col;
			columns[col] = 1;
			diagonals1[d1] = 1;
			diagonals2[d2] = 1;

			if (row + 1 == N)
				printBoard();
			else
				doRow(row + 1);

			columns[col] = 0;
			diagonals1[d1] = 0;
			diagonals2[d2] = 0;
		}
}

int main(int argc, char **argv)
{
	doRow(0);

	printf("There are %d solutions.\n", numSolutions);

	return 0;
}
