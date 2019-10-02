import unittest
import sys

sys.path.insert(0, 'src/game')

from src.game.game_of_life import GameOfLife, Neighbors, Cell


class GameOfLifeTests(unittest.TestCase):
  
  def test_Canary(self):
    self.assertTrue(True)
  
  def setUp(self):
    self.gol_obj = GameOfLife()
  
  def test_checking_empty_game_matrix(self):
    self.assertEqual(0, self.gol_obj.game_matrix.sum())
  
  def test_activate_a_cell(self):
    self.assertEqual(True, self.gol_obj.activate_cell(1, 1))
  
  def test_deactivate_a_cell(self):
    self.assertEqual(True, self.gol_obj.deactivate_cell(1, 1))
  
  def test_count_neighbors(self):
      self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
      self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
      self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
      self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
      self.gol_obj.game_matrix[3, 2] = Cell.ALIVE
      self.assertEqual(Neighbors.FOUR, self.gol_obj.count_neighbors(2, 2))
    
  def test_count_neighbors_at_a_corner_or_edge_cell(self):
    try:
      self.gol_obj.count_neighbors(0, 0)
    except ValueError:
      self.assertTrue(True)
  
  def test_dead_cell_with_zero_neighbors_stays_dead(self):
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_one_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_two_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_three_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.assertEqual(Cell.ALIVE, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_four_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_five_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_six_neighbor_dead(self):
  
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_seven_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 2] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))
    
  def test_a_dead_cell_with_eight_neighbor_dead(self):
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 3] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.dead_constraints(2, 2))

  def test_a_dead_constraint_for_an_active_cell_throw_exception(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    try:
      self.gol_obj.dead_constraints(2, 2)
    except ValueError:
      self.assertTrue(True)

  def test_an_alive_cell_with_zero_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))
    
  def test_an_alive_cell_with_one_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))
    
  def test_an_alive_cell_with_two_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE

    self.assertEqual(Cell.ALIVE, self.gol_obj.alive_constraints(2, 2))

  def test_an_alive_cell_with_three_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.assertEqual(Cell.ALIVE, self.gol_obj.alive_constraints(2, 2))

  def test_an_active_cell_with_four_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))
    

  def test_an_alive_cell_with_five_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))

  def test_an_alive_cell_with_six_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))

  def test_an_alive_cell_with_seven_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 2] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))

  def test_an_alive_cell_with_eight_neighbors_is_dead(self):
    self.gol_obj.game_matrix[2, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[1, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[2, 3] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 1] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 2] = Cell.ALIVE
    self.gol_obj.game_matrix[3, 3] = Cell.ALIVE
    self.assertEqual(Cell.DEAD, self.gol_obj.alive_constraints(2, 2))
    
  def test_alive_constraint_on_dead_cell_throws_exception(self):
    self.gol_obj.game_matrix[2, 2] = Cell.DEAD
    try:
      self.gol_obj.alive_constraints(2, 2)
    except ValueError:
      self.assertTrue(True)
if __name__ == '__main__':
  unittest.main()
