import unittest

from gameoflife.world import World


class TestWorld(unittest.TestCase):
    def test_no_interaction(self):
        empty_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        test_world = World(empty_state)
        self.assertEqual(empty_state, test_world.evolve())

    def test_underpopulation(self):
        init_state = [
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 0]
        ]
        expected_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        test_world = World(init_state)
        self.assertEqual(expected_state, test_world.evolve())

    def test_overcrowding(self):
        init_state = [
            [0, 1, 1],
            [0, 1, 0],
            [1, 1, 0]
        ]
        expected_state = [
            [0, 1, 1],
            [0, 0, 0],
            [1, 1, 0]
        ]
        test_world = World(init_state)
        self.assertEqual(expected_state, test_world.evolve())

    def test_survival(self):
        init_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        expected_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        test_world = World(init_state)
        self.assertEqual(expected_state, test_world.evolve())

    def test_creation(self):
        init_state = [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0]
        ]
        expected_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        test_world = World(init_state)
        self.assertEqual(expected_state, test_world.evolve())

    def test_blinker(self):
        init_state = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        evolved_state = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        test_world = World(init_state)
        self.assertEqual(evolved_state, test_world.evolve())
        self.assertEqual(init_state, test_world.evolve())
