package main

import "fmt"

const N = 8

var (
	rows         [N]int
	columns      [N]bool
	diagonals1   [2*N - 1]bool
	diagonals2   [2*N - 1]bool
	numSolutions int
)

func printBoard() {
	numSolutions++
	fmt.Printf("==== Solution #%d ====\n\n", numSolutions)

	for _, queenCol := range rows {
		for col := range columns {
			if col == queenCol {
				fmt.Print(" 1")
			} else {
				fmt.Print(" 0")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func doRow(row int) {
	d1 := row
	d2 := row + N - 1

	for col, colHasQueen := range columns {
		if !(colHasQueen || diagonals1[d1] || diagonals2[d2]) {
			rows[row] = col
			columns[col] = true
			diagonals1[d1] = true
			diagonals2[d2] = true

			if (row + 1) == N {
				printBoard()
			} else {
				doRow(row + 1)
			}

			columns[col] = false
			diagonals1[d1] = false
			diagonals2[d2] = false
		}
		d1++
		d2--
	}
}

func main() {
	doRow(0)

	fmt.Printf("There are %d solutions.\n", numSolutions)
}
