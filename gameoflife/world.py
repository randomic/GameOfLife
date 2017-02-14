import copy


class World(object):
    def __init__(self, initial_state, wrap_boundaries=False):
        self.size = (0, 0)
        self.state = self.validate_state(initial_state)
        self.wrap = wrap_boundaries

    def validate_state(self, state):
        '''
        Ensure the state is not missing information (i.e. irregular shape)
        and determine the dimensions of the World.
        Return a regularly shaped state.
        '''
        self.size = (len(state), len(state[0]))
        return state

    def count_neighbours(self, row, column):
        '''
        Return the number of living neighbours the cell at
        (row, column) has.
        '''
        region = self.get_region(row, column)
        n_count = 0
        for r_row in region:
            for cell in r_row:
                n_count += cell

        n_count -= self.state[row][column]  # Do not count original cell
        return n_count

    def get_region(self, row, column):
        '''
        Return a 3x3 list of lists containing the cell at row, column
        and its 8 adjacent cells.
        '''
        region = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        for row_offset in range(-1, 2):
            for column_offset in range(-1, 2):
                n_row = row + row_offset
                n_column = column + column_offset
                if self.wrap:
                    if n_row == self.size[0]:
                        n_row = 0
                    elif n_column == self.size[1]:
                        n_column = 0
                else:
                    if (n_row in (-1, self.size[0]) or
                            n_column in (-1, self.size[1])):
                        region[row_offset + 1][column_offset + 1] = 0
                        continue
                region[row_offset + 1][column_offset + 1] = int(
                    self.state[n_row][n_column]
                )
        return region

    def evolve(self):
        new_state = self.step_cells()
        self.state = new_state
        return self.state

    def step_cells(self):
        new_state = copy.deepcopy(self.state)

        for row in range(self.size[0]):
            for column in range(self.size[1]):
                n_count = self.count_neighbours(row, column)
                if n_count < 2:
                    new_state[row][column] = 0
                elif n_count > 3:
                    new_state[row][column] = 0
                elif n_count == 3:
                    new_state[row][column] = 1

        return new_state
