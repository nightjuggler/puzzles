package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

const N = 8

type Rows [N]int

type State struct {
	rows       Rows
	columns    [N]bool
	diagonals1 [2*N - 1]bool
	diagonals2 [2*N - 1]bool
	channel    chan<- Rows
}

const ColEmpty = "_"
const ColQueen = "Q"
const ColSep = "|"

var columns []string

func init() {
	columns = make([]string, N)
	for i := range columns {
		columns[i] = ColEmpty
	}
}

func printBoard(rows *Rows) {
	for _, queenCol := range rows {
		columns[queenCol] = ColQueen
		fmt.Println(strings.Join(columns, ColSep))
		columns[queenCol] = ColEmpty
	}
	fmt.Println()
}

func printBoardFromKey(key string) {
	var rows Rows
	for i, colStr := range strings.Split(key, ",") {
		col, err := strconv.Atoi(colStr)
		if err != nil {
			fmt.Printf("Failed to print board from key %q: %v\n", key, err)
			return
		}
		rows[i] = col
	}
	printBoard(&rows)
}

func doRow(row int, state *State) {
	d1 := row
	d2 := row + N - 1

	for col, colHasQueen := range &state.columns {
		if !(colHasQueen || state.diagonals1[d1] || state.diagonals2[d2]) {
			state.rows[row] = col
			state.columns[col] = true
			state.diagonals1[d1] = true
			state.diagonals2[d2] = true

			if (row + 1) == N {
				state.channel <- state.rows
			} else {
				doRow(row+1, state)
			}

			state.columns[col] = false
			state.diagonals1[d1] = false
			state.diagonals2[d2] = false
		}
		d1++
		d2--
	}
}

func doRow0(col int, channel chan<- Rows) {
	var state State

	state.rows[0] = col
	state.columns[col] = true
	state.diagonals1[col] = true
	state.diagonals2[N-1-col] = true
	state.channel = channel

	doRow(1, &state)
	state.rows[1] = -1
	channel <- state.rows
}

func (rows *Rows) Rotate() *Rows {
	for row, col := range *rows {
		rows[col] = N - 1 - row
	}
	return rows
}

func (rows *Rows) Mirror() *Rows {
	for row, col := range rows {
		rows[row] = N - 1 - col
	}
	return rows
}

func (rows *Rows) Key() string {
	var colStr [N]string
	for row, col := range rows {
		colStr[row] = strconv.Itoa(col)
	}
	return strings.Join(colStr[:], ",")
}

func (rows *Rows) FirstKey() string {
	keys := []string{
		rows.Key(),
		rows.Mirror().Key(),
		rows.Mirror().Rotate().Key(),
		rows.Mirror().Key(),
		rows.Mirror().Rotate().Key(),
		rows.Mirror().Key(),
		rows.Mirror().Rotate().Key(),
		rows.Mirror().Key(),
	}
	sort.Strings(keys)
	return keys[0]
}

func main() {
	solutions := make(map[string]int)

	numChildren := N
	rowsChannel := make(chan Rows, numChildren)

	for col := range columns {
		go doRow0(col, rowsChannel)
	}

	timeout := time.After(2 * time.Second)
loop:
	for {
		select {
		case rows := <-rowsChannel:
			if rows[1] >= 0 {
				solutions[rows.FirstKey()] += 1
			} else if numChildren--; numChildren == 0 {
				break loop
			}
		case <-timeout:
			fmt.Println("Timed out!")
			return
		}
	}

	numSolutions := 0
	numFundamental := len(solutions)

	keys := make([]string, numFundamental)
	i := 0
	for key, num := range solutions {
		numSolutions += num
		keys[i] = key
		i++
	}

	sort.Strings(keys)

	for i, key := range keys {
		fmt.Printf("==== Fundamental Solution %d (%s) (%d variations) ====\n\n", i+1, key, solutions[key])
		printBoardFromKey(key)
	}
	fmt.Printf("There are %d fundamental solutions (%d total)\n", numFundamental, numSolutions)
}
