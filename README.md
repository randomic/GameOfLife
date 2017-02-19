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

## Counting neighbours ##

In order to count the number of neighbours a given cell has a 3x3 sub-section
of the game state centred on that cell is generated. For cells not on the edges
of the world this is just a small section of the game state. For cells on the
edges or in the corners the method depends on the boundary wrapping setting:

* For non-wrapping borders any 'neighbour' lying outside of the game state is
    not counted towards the number of neighbours. This is whenever a cell with
    either a -1 or out of range index is looked for.
* For wrapping borders a -1 index is used to access the last element of a list
    which causes a wrap around. An index which is past the end of the list is
    set to 0, this causes the wrapping in the other direction.

## Further development ##

* It is possible to develop a way of visualising the Game of Life using only
    standard libraries. A renderer should be relatively simple to make with
    tkinter.
* The rules of Conway's Game of Life are just 1 out of many possible rules for
    this kind of cellular automaton. It might be interesting to allow rules to
    be specified.
