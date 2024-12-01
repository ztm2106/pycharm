1. Approximately how long did this assignment take you to complete?
cumulatively it has been about 6 hours.

2. Which features did you implement?
[5 points] Randomly choose a starting location for the ball
[5 points] Randomly choose a starting velocity for the ball
[7 points] Support mouse events for moving the paddle
[7 points] Keep track of the user’s score
[10 points] Add a barrier to the middle of the game board for the ball to bounce against


3. Briefly, but thoroughly, describe the features you implemented. You may also provide

[5 points] Randomly choose a starting location for the ball
I change the constant number to a random.range  function for both x between 150 and 600 and y between 0 and 600 of ball

[5 points] Randomly choose a starting velocity for the ball
I change the constant number to a random.range function horizontally between 2, 4 secs  and vertically the same way.

[7 points] Support mouse events for moving the paddle
I print the x, y coordinates of y movement. Changed event type to pygame.MOUSEMOTION. sync x and y position of mouse event and changed only y coordinate for paddle.

[7 points] Keep track of the user’s score
set a initial number to the running total in main prog. In the while function we have statement is the ball hit paddle to add one to the running total. score is then blit to the win as a i set the font and size earlier in the main prog
with the position of the text. I blit the score under the barrier to make show it shows on top of it.

[10 points] Add a barrier to the middle of the game board for the ball to bounce against
I add the dimensions of the barrier in the main prog. I used pygame draw rect to show barrier in the while function to always see it in the win. In the move function, I added when the barrier collides with the ball so the ball can change directions.
In the move function I add the width and y cord calculations and the height and x cord calculations and also the ball center calculation into the move function because is is not steady like the barrier.


4. Is there a part of the program you had to try to write several times to get correct?
Explain what went wrong with your initial attempts.

I have tried the feature of adding a barrier to the middle of the game board for the ball to bounce against several times to get correct. Majority of the time of the project completion was this part.
In initial attempts, the ball will interact with the side however not always bounce off the correct side and show random motions. I had to use a picture to understand the conditions of the beginning if statement and embedded if and else statements in the move function.
I need to add the ball center x, y and wy and hx calculations in to the move function because it needs to be changed each time because ball is always moving.