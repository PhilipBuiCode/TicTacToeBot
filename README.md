# Tic Tac Toe Bot

## I. Abstract
One of the most popular games of all time is **Tic Tac Toe**. In this post, I create a simple unbeatable AI that will never lose. To do that, I use a minimax algorithm, a widely used and studied algorithm that is used in fields such as game theory, artificial intelligence, and more. This post features a working Tic Tac Toe game which can be played by two humans or against opponents (perfect bot and random bot).


## II. Introduction
### About Tic Tac Toe
Tic Tac Toe is a simple game in which two players (*X's* and *O's*) face each other by taking turns and placing their letter in a 3x3 grid. The game is over when a player manages to fill a row, column or diagonal fully with their letter. 

An important note is that the X player always starts. This means he will have an advantage. Therefore, against a random player, we expect X to win more often that O. With two optimal players, this should have no effect and they should always tie.

Tic Tac Toe is a zero-sum perfection information game. A zero-sum game means that when a player gains an advantage, the other side faces an equivalent loss, resulting in a sum of zero. A perfect information game means that all players have perfect information of all events that have previously occurred (e.g. Chess, Backgammon, Monopoly), in other words no information is hidden. An example of an imperfect information game could be Poker. With these informations in mind, we will use a minimax algorithm to solve the game of Tic Tac Toe.


### About Minimax

Minimax is a decision rule algorithm that uses recursion to choose the optimal move in a given situation. Its goal is to minimize the maximum loss (minimize the worse case scenario). It assumes all players are playing optimally.

In other words, it's an algorithm that is thinking *"If I make this move, my opponent only has these moves, and in all of these moves I end up winning. Therefore, I will make this move."* It can easily be visualized as a tree of decisions with given scores.

## III. Implementation
For a Tic Tac Toe game, we give score to the minimax algorithm by assigning a score to each outcome. A win gives a 10 points,  a loss gives -10 and a tie gives 0. 

We also have to give a penalty to nodes that lose faster. We can do that by substracting the current depth of our tree to the final score. If we don't add this depth component, the algorithm may make a mistake in situations where every outcome is a loss because he will consider every outcome equally and assign an equal score to all of them. 

Finally, we then use a depth first search and calculate if each legal move would result in a win, loss or tie and return the best move. 

We also create a random bot that chooses moves randomly from legal moves in order to test our smart bot.
	    
## IV. Results
As stated earlier, we have created two types of player:

 - Random player, who chooses a completely random move
 - Smart player, who plays optimally and never loses
 
 Simulating these players against each other, we achieved the following results :
 
