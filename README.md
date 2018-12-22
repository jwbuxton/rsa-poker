# rsa-poker
Have you used some form of 2-factor authentication?  Does it involve the generation of a six-digit integer? Are you sometimes bored with nothing more interesting than this?  Have you tried to develop some sort of game to play with others in the same boat?

If you've answered "yes" to all four of the above, RSA Poker is for you!  

The project is currently a work in progress, but I've used Python to calculate the odds via brute force for some simple odds.  

| Hand | Frequency | Probability | Odds | Math
|---|---|---|---|---|
| Six of a kind | 10 | 0.001% | 100,000:1 | $${10 \choose 1}$$ |
| Five of a kind | 540 | 0.054% | 1,852:1 | $${10 \choose 1}{6 \choose 1}{9 \choose 1}$$ |
| Double threes of a kind | 900 | 0.09% | 1,111:1 |  |
| Four-two full house | 1,350 | 0.135% | 741:1 |  |
| Four of a kind | 10,800 | 1.08% | 93:1 |  |
| Three pairs | 10,800 | 1.08% | 93:1 |  |
| Three-two full house | 43,200 | 4.32% | 23:1 |  |
| Five of a kind | 540 | 0.054% | 1,852:1 |  |
| Five of a kind | 540 | 0.054% | 1,852:1 |  |
| Five of a kind | 540 | 0.054% | 1,852:1 |  |
| Five of a kind | 540 | 0.054% | 1,852:1 |  |
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE4ODA5NTY2NSwtMTU3NzMwNTg0NSwtMj
UzOTIxMDQ1LC0xNjMxNzUyMjg1LC0xODcxMjAwNDQ2LDEyMDY4
MjgyNjVdfQ==
-->