"""Test module for gameoflife.world in Conway's Game of Life exercise.

This module contains test cases for an implementation of Conway's Game of Life.

Example:
    Run with nosetests::

        $ nosetests -v

"""
import unittest

import numpy as np

from gameoflife.world import World


class TestWorld(unittest.TestCase):
    """Test unit for gameoflife.world World class"""
    def test_no_interaction(self):
        """Empty state should remain empty after evolving."""
        empty_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        test_world = World(empty_state)
        self.assertTrue(np.array_equal(empty_state, test_world.evolve()))

    def test_underpopulation(self):
        """Cells should 'die' to underpopulation after evolving."""
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
        self.assertTrue(np.array_equal(expected_state, test_world.evolve()))

    def test_overcrowding(self):
        """Centre cell should 'die' to overcrowding after evolving."""
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
        self.assertTrue(np.array_equal(expected_state, test_world.evolve()))

    def test_survival(self):
        """State should remain the same after evolving."""
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
        self.assertTrue(np.array_equal(expected_state, test_world.evolve()))

    def test_creation(self):
        """Centre cell should 'live' after evolving."""
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
        self.assertTrue(np.array_equal(expected_state, test_world.evolve()))

    def test_blinker(self):
        """Initial state should oscillate in two evolutions."""
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
        self.assertTrue(np.array_equal(evolved_state, test_world.evolve()))
        self.assertTrue(np.array_equal(init_state, test_world.evolve()))

    def test_wrap(self):
        """State should remain the same after evolving."""
        init_state = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        expected_state = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        test_world = World(init_state, True)
        self.assertTrue(np.array_equal(expected_state, test_world.evolve()))

    def test_simulate(self):
        """Oscillator should return initial state after evolving 15 times."""
        init_state = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        test_world = World(init_state)
        self.assertTrue(np.array_equal(init_state, test_world.simulate(15)))

    def test_simulate_wrap(self):
        """Oscillator should return initial state after evolving 15 times.

        Note:
            Same oscillator as test_simulate but offset into a corner and
            World boundary wrapping switched on.

        """
        init_state = [
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        test_world = World(init_state, True)
        self.assertTrue(np.array_equal(init_state, test_world.simulate(15)))

    def test_embed_state(self):
        """State should be surrounded by dead cells.

        """
        init_state = np.array([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])
        embed_state = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        test_world = World(init_state)
        self.assertTrue(np.array_equal(embed_state,
                                       test_world.embed_state(init_state)))

    def test_embed_state_wrap(self):
        """State should be surrounded by dead cells.

        """
        init_state = np.array([
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ])
        embed_state = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        test_world = World(init_state, True)
        self.assertTrue(np.array_equal(embed_state,
                                       test_world.embed_state(init_state)))
