# Game of Life #

## Libraries ##

This branch of the project uses no external libraries and, as such, uses nested
lists as an array-like object to store the state of the game. The `use-numpy`
branch uses the arrays from the `numpy` library instead. It also uses the
`matplotlib` library to make an animated demonstration of a Gosper Glider Gun.

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
