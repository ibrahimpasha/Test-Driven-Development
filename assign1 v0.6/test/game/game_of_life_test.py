import unittest

from src.game.game_of_life import *


class GameOfLifeTests(unittest.TestCase):

  def setUp(self):
    self.living_coordinates = []

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

  def test_live_cell_dies_with_live_neighbors_0(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 0))

  def test_live_cell_dies_with_live_neighbors_1(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 1))

  def test_live_cell_dies_with_live_neighbors_5(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 5))

  def test_live_cell_dies_with_live_neighbors_8(self):
    self.assertEqual(CellState.DEAD, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 8))

  def test_live_cell_lives_with_live_neighbors_2(self):
    self.assertEqual(CellState.ALIVE, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 2))

  def test_live_cell_lives_with_live_neighbors_3(self):
    self.assertEqual(CellState.ALIVE, next_cell_state(
      current_state = CellState.ALIVE, number_of_life_neighbors = 3))

  def test_generate_signals_for_one_position(self):         
    expected_signals = \
      [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    
    self.assertTrue(expected_signals, generate_signal((3, 3)))

  def test_generate_signals_for_another_position(self):
    expected_signals = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
    self.assertTrue(expected_signals, generate_signal((2, 4)))

  def test_generate_signal_for_position_00(self):
    expected_signals = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1)         , (0, 1),
                        (1, -1), (1, 0), (1, 1)]
    self.assertTrue(expected_signals, generate_signal((0, 0)))
  
  def test_generate_signal_at_no_position_returns_empty_list(self):
    self.assertEqual([], generate_signals())
  
  def test_generate_signals_for_1_positions_returns_8_positions(self):
    self.assertTrue(8, len(generate_signals([(2, 4)])))

  def test_generate_signals_for_2_positions_returns_16_positions(self):
    self.assertEqual(16, len(generate_signals([(3, 3), (2, 4)])))
  
  def test_generate_signals_for_3_positions_returns_24_positions(self):
    self.assertEqual(24, len(generate_signals([(3, 3), (2, 4), (2, 2)])))

  def test_count_signals_at_no_position_returns_empty_map(self):
    self.assertEqual({}, count_signals())

  def test_count_signals_at_one_position(self):
    expected_map = {(2, 2): 1}
    self.assertEqual(expected_map, count_signals([(2, 2)]))
  
  def test_count_signals_at_two_position(self):
    expected_map = {(2, 2): 2}
    self.assertEqual(expected_map, count_signals([(2, 2), (2, 2)]))
  
  def test_count_signals_at_three_position(self):
    expected_map = {(2, 2): 2, (3, 2): 1}
    self.assertEqual(expected_map, count_signals([(3, 2), (2, 2), (2, 2)]))

  def test_next_generation_at_no_position(self):
    self.assertEqual([], next_generation())

  def test_next_generation_at_one_position(self):
    self.assertEqual([], next_generation([(2, 2)]))

  def test_next_generation_at_multiple_positions_1(self):
    expected_signal = []
    self.assertEqual(expected_signal, next_generation([(2, 3), (2, 4)]))
  
  def test_next_generation_at_multiple_positions_2(self):
    expected_signal = [(2, 1)]
    self.assertEqual(expected_signal, next_generation([(1, 1), (1, 2), (3, 0)]))

  def test_next_generation_at_multiple_positions_3(self):
    expected_signal = [(1, 2), (1, 1), (2, 2), (2, 1)]
    self.assertEqual(expected_signal.sort(), next_generation([(1, 1), (1, 2), (2, 2)]).sort())

  def test_given_block_next_generation_returns_same_block(self):
    expected_signal = [(1, 2), (1, 1), (2, 1), (2, 2)]
    self.assertEqual(expected_signal.sort(), next_generation([(1, 1), (1, 2), (2, 1), (2, 2)]).sort())

  def test_given_beehive_next_generation_returns_same_behive(self):
    expected_signal = [(1, 1), (1, 2), (2, 0), (3, 1), (3, 2), (2, 3)]
    self.assertEqual(expected_signal.sort(), next_generation([(1, 1), (1, 2), (2, 0), (3, 1), (3, 2), (2, 3)]).sort())
  
  def test_horizontal_blinker_next_generation_returns_vertical_blinker(self):
    expected_signal = [(2, 1), (2, 2), (2, 3)]
    self.assertEqual(expected_signal.sort(), next_generation([(1, 2), (2, 2), (3, 2)]).sort())
  
  def test_vertical_blinker_next_generation_returns_horizontal_blinker(self):
    expected_signal = [(1, 2), (2, 2), (3, 2)]
    self.assertEqual(expected_signal.sort(), next_generation([(2, 1), (2, 2), (2, 3)]).sort())

  def test_glider_with_one_top_cell_moves_to_right(self):
    expected_signal = [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
    self.assertEqual(expected_signal.sort(), next_generation([(3, 1), (3, 2), (3, 3), (2, 3), (1, 2)]).sort())

  def test_get_bounds_returns_empty_list_given_empty_list(self):
    self.assertEqual([], get_bounds([]))

  def test_get_bounds_given_one_point_returns_same_point_twice(self):
    self.assertEqual([(3, 4), (3, 4)], get_bounds([(3, 4)]))

  def test_get_bounds_given_two_points_returns_top_left_then_bottom_right(self):
    self.assertEqual([(2, 0), (5, 4)], get_bounds([(5, 4), (2, 0)]))

  def test_get_bounds_given_two_points_that_are_bottom_left_and_top_right_creates_top_left_and_bottom_right(self):
    self.assertEqual([(3, -2), (5, 4)], get_bounds([(3, 4), (5, -2)]))

  def test_get_bounds_given_three_points_returns_top_left_then_bottom_right(self):
    self.assertEqual([(-2, -2), (3, 5)], get_bounds([(2, 0), (-2, -2), (3, 5)]))

  def test_get_bounds_given_four_points_returns_top_left_then_bottom_right(self):
    self.assertEqual([(-5, -1), (7, 9)], get_bounds([(-1, 8), (-5, 8), (5, 9), (7, -1)]))


if __name__ == '__main__':
  unittest.main()
