# Tic Tac Toe Bot

## I. Abstract
One of the most popular games of all time is **Tic Tac Toe**. In this post, I create a simple unbeatable AI that never loses. To do that, I use a minimax algorithm, a widely used and studied algorithm that is used in fields such as game theory, artificial intelligence, and more. The code features a working Tic Tac Toe game which can be played by two humans or against opponents (random bot and optimal bot).


## II. Introduction
### About Tic Tac Toe
Tic Tac Toe is a simple game in which two players (*X's* and *O's*) face each other by taking turns and placing their letter in a 3x3 grid. The game is over when a player manages to fill a row, column or diagonal fully with their letter. 

An important note is that the X player always starts. This means he has an advantage. Therefore, against a random player, I expect X to win more often that O. With two optimal players, this should have no effect and they should always tie.

Tic Tac Toe is a zero-sum perfection information game. A zero-sum game means that when a player gains an advantage, the other side faces an equivalent loss, resulting in a sum of zero. A perfect information game means that all players have perfect information of all events that have previously occurred (e.g. Chess, Backgammon, Monopoly), in other words no information is hidden. An example of an imperfect information game could be Poker. With these informations in mind, I will use a minimax algorithm to solve the game of Tic Tac Toe.


### About Minimax

Minimax is a decision rule algorithm that uses recursion to choose the optimal move in a given situation. Its goal is to minimize the maximum loss (minimize the worse case scenario). It assumes all players are playing optimally.

In other words, it's an algorithm that is thinking *"If I make this move, my opponent only has these moves, and in all of these moves I end up winning. Therefore, I will make this move."* It can easily be visualized as a tree of decisions with given scores.

## III. Implementation
For a Tic Tac Toe game, I give a score to the minimax algorithm by assigning a score to each outcome. A win gives a 10 points,  a loss gives -10 and a tie gives 0. A score of 10 is enough for our concept, because the algorithm can only go a depth of 8 (there  are 8 empty squares after 1 square has been marked).



I also have to give a penalty to nodes that lose faster. I can do that by substracting the current depth of our tree to the final score. If I don't add this depth component, the algorithm may make a mistake in situations where every outcome is a loss because he will consider every outcome equally and assign an equal score to all of them. 

Finally, I use a depth first search and calculate if each legal move would result in a win, loss or tie and return the best move. 

I also create a random bot that chooses moves randomly from legal moves in order to test our smart bot.
	    
## IV. Results
As stated earlier, I have created two types of player:

 - Random bot, who chooses a completely random move
 - Smart bot, who plays optimally and never loses
 
 To test the effectiveness of our smart player I will pit these players against each other. Simulating 10000 iterations, I achieved the following results :
 
 | **X player** \ **O player**  | **Random Bot** | **Smart Bot** | 
|:------------:|------------|-----------|
| **Random Bot** |X wins : 5830<br /> O wins : 2879<br /> Ties : 1291          |   X wins : 0<br /> O wins : 8035<br /> Ties : 1965     |   
| **Smart Bot**  | X wins : 9801<br /> O wins : 0<br /> Ties : 199             |   X wins : 0<br /> O wins : 0<br /> Ties : 10000         |   

These results show that our smart bot will either win or tie, but will never lose no matter the circumstances. Also note that the X player clearly has an advantage over the O player, as shown by the number of wins by the X player over the O player in the random matchup and the fact that the smart player achieves more wins when playing as X than playing as O. This is what I expected because the X player has the first turn.

This makes no difference when playing optimally, and every match results in a tie.
 
## IV. Conclusion
 
This post describes the creation of an optimal Tic Tac Toe bot. This bot will always win or draw, but never lose. Alpha-beta pruning could be implemented to our minimax strategy, in hopes of improving the computing time of our bot. In future work, it would be interesting to analyze how the bot is playing and understand its strategy on the board. It would also be interesting to implement this strategy to other games.
 
 
