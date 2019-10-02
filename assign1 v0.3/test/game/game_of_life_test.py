import unittest

from src.game.game_of_life import *

class GameOfLifeTests(unittest.TestCase):
  def test_test_Canary(self):
    self.assertTrue(True)

  def test_dead_cell_remains_dead_for_live_neighbors_0(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 0))

  def test_dead_cell_remains_dead_for_live_neighbors_1(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 1))

  def test_dead_cell_remains_dead_for_live_neighbors_2(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 2))

  def test_dead_cell_remains_dead_for_live_neighbors_5(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 5))

  def test_dead_cell_remains_dead_for_live_neighbors_8(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 8))

  def test_dead_cell_comes_to_live_with_3_live_neighbors(self):
    self.assertEqual(CellState.ALIVE, next_cell_state(
      current_state = CellState.DEAD, number_of_life_neighbors = 3))

  def test_live_cell_dies_with_live_neibhbors_0(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 0))

  def test_live_cell_dies_with_live_neibhbors_1(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 1))

  def test_live_cell_dies_with_live_neibhbors_5(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 5))

  def test_live_cell_dies_with_live_neibhbors_8(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 8))

  def test_live_cell_lives_with_live_neibhbors_2(self):
    self.assertEqual(CellState.ALIVE, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 2))

  def test_live_cell_lives_with_live_neibhbors_3(self):
    self.assertEqual(CellState.ALIVE, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 3))
  
  def test_generate_signal_at_a_position(self):
    self.assertEqual(2, signal_generator((2, 2)))

  def test_generate_signal_at_a_position_0_0(self):
    self.assertEqual(1, signal_generator((0, 0)))

  def test_neighor_count_at_a_position(self):
    neighbours_tracker[(3,3)] = 3
    self.assertEqual(3, get_neighbor_count((3,3)))

  def test_get_cell_state_at_a_position(self):
    self.assertEqual(CellState.ALIVE, get_cell_state((2,3)))

if __name__ == '__main__':
  unittest.main()
