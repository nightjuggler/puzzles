#include <stdio.h>

#ifndef N
#define N 8
#endif

static unsigned char board[N][N];
static unsigned int numSolutions;

void printBoard()
{
	int row, col;

	printf("==== Solution #%d ====\n\n", ++numSolutions);

	for (row = 0; row < N; ++row)
	{
		for (col = 0; col < N; ++col)
			printf(" %u", board[row][col]);
		printf("\n");
	}
	printf("\n");
}

int safe(int row, int col)
{
	int i, j;

	for (i = row - 1; i >= 0; --i)
		if (board[i][col]) return 0;

	for (i = row - 1, j = col - 1; i >= 0 && j >= 0; --i, --j)
		if (board[i][j]) return 0;

	for (i = row - 1, j = col + 1; i >= 0 && j < N; --i, ++j)
		if (board[i][j]) return 0;

	return 1;
}

void doRow(int row)
{
	int col;

	for (col = 0; col < N; ++col)
		if (safe(row, col))
		{
			board[row][col] = 1;
			if (row + 1 == N)
				printBoard();
			else
				doRow(row + 1);
			board[row][col] = 0;
		}
}

int main(int argc, char **argv)
{
	doRow(0);

	printf("There are %d solutions.\n", numSolutions);

	return 0;
}
