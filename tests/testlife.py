from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
	def test_no_interaction(self):
		emptyState = [  [0,0,0],
				[0,0,0],
				[0,0,0]  ]
		testLife = Life()
		self.assertEqual(emptyState, testLife.evolve(emptyState))

