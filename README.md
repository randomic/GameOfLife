# Game of Life #

## Libraries ##

This branch of the project uses arrays from the `numpy` library to store the
state of the game. It also uses the `matplotlib` library to make an animated
demonstration of a Gosper Glider Gun.

Install the dependencies with: `pip install -r requirements.txt`

View the animated demonstration:

`python main.py`

## Task ##

My task was to implement the rules of Conway's Game of Life as explained in the
document statement.

## My approach ##

The document which accompanied this task contained 6 scenarios describing the
rules of Conway's game of life. The first and fifth of these scenarios were
implemented as a unit test case in the project skeleton. This inspired me to
add test cases for the other 4 scenarios and apply a test-driven approach to
solving the problem.

## World borders ##

The expected behaviour for cells at the edges or corners of a Game of Life
world was not specified in the document so I added a boolean option to the
World class which would allow the user to switch between two different types of
border behaviour. Namely whether a cell would be considered to have no
neighbours outside of the world or whether the borders would wrap around to
create a closed world.

## Counting neighbours ##

The game state is embedded in the centre of an array which is 2 cells larger in
each dimension.

* In the case of non-wrapping borders this, in essence, puts a border of 'dead'
    cells around the edge of the world.
* In the case of wrapping borders the right edge becomes equal to the left edge
    of the game state, the top to the bottom, etc.

The neighbours of a cell can then be counted by summing the 3x3 sub-array
centred on that cell and finally subtracting the value of the cell in question.

## Further development ##

* It is possible to vectorise the computation of neighbours and the updating of
    the game state with numpy arrays. This will eliminate nested loops in the
    code. Doing so should significantly improve the performance.
* The rules of Conway's Game of Life are just 1 out of many possible rules for
    this kind of cellular automaton. It might be interesting to allow rules to
    be specified.
