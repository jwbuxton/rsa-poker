# rsa-poker
Have you used some form of 2-factor authentication?  Does it involve the generation of a six-digit integer? Are you sometimes bored with nothing more interesting than this?  Have you tried to develop some sort of game to play with others in the same boat?

If you've answered "yes" to all four of the above, RSA Poker is for you!  

The project is currently a work in progress, but I've used Python to calculate the odds via brute force for some simple hands.  

| Hand | Frequency | Probability | Odds | Math
|---|---|---|---|---|
| Six of a kind | 10 | 0.001% | 100,000:1 | $${10 \choose 1}$$ |
| Five of a kind | 540 | 0.054% | 1,852:1 | $${10 \choose 1}{6 \choose 1}{9 \choose 1} 1!$$ |
| Double threes of a kind | 900 | 0.09% | 1,111:1 | $${10 \choose 2}{6 \choose 3}$$ |
| Four-two full house | 1,350 | 0.135% | 741:1 | $${10 \choose 1}{6 \choose 4}{9 \choose 1}$$ |
| Four of a kind | 10,800 | 1.08% | 92.6:1 | $${10 \choose 1}{6 \choose 4}{9 \choose 2} 2!$$ |
| Three pairs | 10,800 | 1.08% | 92.6:1 | $${10 \choose 3}{6 \choose 2}{4 \choose 2}$$ |
| Three-two full house | 43,200 | 4.32% | 23.1:1 | $${10 \choose 1}{6 \choose 3}{9 \choose 1}{3 \choose 2}{8 \choose 1} 1!$$ |
| Three of a kind | 100,800 | 10.08% | 9.92:1 | $${10 \choose 1}{6 \choose 3}{9 \choose 3} 3!$$ |
| Two pairs | 226,800 | 22.68% | 4.41:1 | $${10 \choose 2}{6 \choose 2}{4 \choose 2}{8 \choose 2} 2!$$ |
| One pair | 453,600 | 45.36% | 2.20:1 | $${10 \choose 1}{6 \choose 2}{9 \choose 4} 4!$$ |
| High card | 151,200 | 15.12% | 6.61:1 | $${10 \choose 6} 6!$$ |
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg4NzY5MDUwLC0xNTc3MzA1ODQ1LC0yNT
M5MjEwNDUsLTE2MzE3NTIyODUsLTE4NzEyMDA0NDYsMTIwNjgy
ODI2NV19
-->