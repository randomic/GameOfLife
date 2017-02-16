"""world module for Conway's Game of Life exercise.

This module contains the `World` class which describes a 2 dimensional array
of cells in either a living or dead state. The cells follow the rules of
Conway's Game of Life. The `World` can be initialised with wrap_boundries=True
to create a 'closed' world in which the bottom wraps to the top and the right
wraps to the left.

Example:
    Initialise a 3x3 world which contains a period 2 blinker and evolve it
    n_steps times::

        >>> n_steps = 3
        >>> initial_state = init_state = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        >>> world = World(initial_state)
        >>> world.simulate(n_steps)
        >>> print(world)
        [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

"""
import numpy as np


class World(object):
    """2 Dimensional world for Conway's Game of Life.

    Stores the state of the `World` in a `list` which will be updated whenever
    the `evolve` method is called.

    Attributes:
        logger: Logger named after this module.
        size (`tuple`): Contains the size of the `World` as (rows, columns).
        state (`list` of `list`): Contains the current state of the `World`.
        wrap (`bool`): Whether or not the edges of the `World` 'wrap around'.

    """
    def __init__(self, initial_state, wrap_boundaries=False):
        """Initialise the world from `initial_state`.

        Take the initial_state argument and validate it,  while also setting
        the `size` attribute.

        Args:
            initial_state (`list` of `list`): Describing the initial state of
                the `World`.
            wrap_boundaries (`bool`): If `True` bottom of the `World` will wrap
                to the top and the right edge will wrap to the left. If `False`
                the `World` will act as though it has a border of permanently
                'dead' cells.

        """
        self.wrap = wrap_boundaries
        self.state = np.array(initial_state, dtype='int8')

    def simulate(self, n_steps):
        """Evolve the world n_steps times and return the final state.

        Returns:
            The current state after evolving n_steps times.

        """
        for dummy_i in range(n_steps):
            self.evolve()

        return self.state

    def evolve(self):
        """Evaluate the new state from the current one and then update.

        Returns:
            The current state after being evolved and updated.

        """
        new_state = self.step_cells()
        self.state = new_state
        return self.state

    def step_cells(self):
        """Apply the rules of Game of Life to each cell in the `World`.

        Note:
            Only returns the new state, does not update `state`.

        Returns:
            The next state of the simulation after applying the rules.

        """
        em_state = self.embed_state(self.state)
        new_state = em_state.copy()

        for row in range(1, em_state.shape[0] - 1):
            for column in range(1, em_state.shape[1] - 1):
                n_count = np.sum(em_state[row - 1:row + 2,
                                          column - 1:column + 2])
                n_count -= em_state[row][column]  # Do not count original cell
                if n_count < 2:
                    new_state[row][column] = 0
                elif n_count > 3:
                    new_state[row][column] = 0
                elif n_count == 3:
                    new_state[row][column] = 1

        return new_state[1:-1, 1:-1]

    def embed_state(self, state):
        """Return state embeded in a bigger array.

        Note:
            For a non-wrapping world the state will have a border of dead cells
            and for a wrapping world the edges of the state will be wrapped
            around.

        """
        em_state = np.zeros((state.shape[0] + 2,
                             state.shape[1] + 2), dtype='int8')
        em_state[1:-1, 1:-1] = state           # Set middle of big array

        if self.wrap:
            em_state[0, 1:-1] = state[-1]       # Top edge
            em_state[-1, 1:-1] = state[0]     # Bottom edge
            em_state[1:-1, 0] = state[:, -1]    # Left edge
            em_state[1:-1, -1] = state[:, 0]  # Right edge
            em_state[0, 0] = state[-1, -1]     # Top-left corner
            em_state[0, -1] = state[-1, 0]     # Top-right corner
            em_state[-1, 0] = state[0, -1]     # Bottom-left corner
            em_state[-1, -1] = state[0, 0]     # Bottom-right corner

        return em_state
