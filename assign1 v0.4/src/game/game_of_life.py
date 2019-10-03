from enum import Enum

class CellState(Enum):
  DEAD = 0
  ALIVE = 1


def next_cell_state(current_state, number_of_life_neighbors):
  
  return CellState.ALIVE if number_of_life_neighbors == 3 \
    or current_state == CellState.ALIVE and number_of_life_neighbors == 2 \
    else CellState.DEAD


def generate_signals(positions=[]):
  if not positions:
    return []
  elif type(positions)==tuple:
    x, y = positions
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
  else:
    returning_signal = []
    for position in positions:
      x, y = position
      returning_signal.extend([(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                                                (x, y - 1), (x, y + 1),
                                                (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)])
    return returning_signal


def count_signals(signals=[]):
  count_signals_tracker = {}
  if not signals:
    return {}
  elif type(signals) == tuple:
    return {signals: 1}
  else:
    for signal in signals:
        count_signals_tracker[signal] = count_signals_tracker.get(signal, 0) + 1
    return count_signals_tracker
  
  
def next_generation(living_positions=[]):
  if not living_positions or type(living_positions)==tuple:
    return []
  else:
    signals = generate_signals(living_positions)
    signal_map_counts = count_signals(signals)
    positions_with_three_neighbors = [signal for signal, count in signal_map_counts.items() if count == 3]
    positions_with_two_neighbors = [signal for signal, count in signal_map_counts.items() if count == 2]
    return list(set(living_positions) & set(positions_with_two_neighbors)) + positions_with_three_neighbors

print(next_generation([(1, 1), (1, 2), (2, 2)]))