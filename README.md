## Puzzles

### dragon.py

This Python script solves the following puzzle:

A human settlement is attacked on a daily basis by a dragon. Every
night, the dragon returns to one of 5 adjacent caves on a mountain.
He never spends consecutive nights in the same cave. Instead he always
returns to a cave next to the one he spent the previous night. The
caves are arranged such that the first and last caves are each next to
only one other cave, while the other caves are each next to two other
caves. In other words, cave 1 is only next to cave 2, while cave 2 is
next to both cave 1 and cave 3, etc. The humans can capture the dragon
at night if they go to the cave where he's sleeping. However, they can
only go to one cave each night. How many nights do they need at a
minimum to guarantee capturing the dragon? And in which order should
they visit the caves?

The script brute-force searches for solutions. The number of caves (by
default 5) can be specified on the command line.

### flipcoins.py

This Python script calculates the expected number of coin flips needed
(on average) to get a certain sequence of heads and tails. The
sequence (by default HH, i.e. consecutive heads) can be specified on
the command line. In verbose mode, the script will print the equations
used to calculate the expected value.

The script can also repeatedly simulate a series of coin flips. Each
series ends when the specified sequence of heads and tails first
occurs. The number of flips are counted and the average over a
specified number of runs (by default 10,000) is displayed.

```
> ./flipcoins.py ht
Expected number of flips to get 'HT' = 4
> ./flipcoins.py
Expected number of flips to get 'HH' = 6
> ./flipcoins.py -v
E[HH] = 0
2E[H] = 2 + E[HT] + E[HH]
E[HT] = E[]
2E[H] = 2 + E[] + E[HH]
2E[H] = 2 + E[]
2E[] = 2 + E[T] + E[H]
E[T] = E[]
E[] = 2 + E[H]
2E[] = 4 + 2E[H]
E[] = 6
Expected number of flips to get 'HH' = 6
> ./flipcoins.py hth
Expected number of flips to get 'HTH' = 10
> ./flipcoins.py -a 100000 hth
Average number of flips to get 'HTH' = 10.00345
>
```

### twonumbers.py

This Python script solves the following puzzle:

Two integers between 2 and 100 (inclusive) are chosen.

P is given their product, and S is given their sum.

P says: "I can't figure out what the two numbers are."<br>
S replies: "Yeah, I already knew that."<br>
P replies: "Oh, really, well now I know what the two numbers are."<br>
S replies: "Oh, really, well now I do too."

What are the two numbers?

### 20180304-KnuthLetter.html

Toward the end of his 23rd annual Christmas lecture (December 7, 2017),
[Don Knuth presents a conjecture](https://www.youtube.com/watch?v=BxQw4CdxLr8&t=55m45s),
sent to him by Bill Gosper. [This](https://nightjuggler.com/proof/20180304-KnuthLetter.html)
is the HTML/MathML for the letter I
[mailed](https://www-cs-faculty.stanford.edu/~knuth/email.html) to Professor Knuth
on March 4, 2018 with a proof for the conjecture. I never received a reply.
