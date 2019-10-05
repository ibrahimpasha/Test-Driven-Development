from enum import Enum
from collections import Counter


class CellState(Enum):
  DEAD = 0
  ALIVE = 1


def next_cell_state(current_state, number_of_life_neighbors):
  return CellState.ALIVE if number_of_life_neighbors == 3 \
    or current_state == CellState.ALIVE and number_of_life_neighbors == 2 \
    else CellState.DEAD


def generate_signal(position):
    x, y = position
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]


def generate_signals(positions=[]):
  if not positions:
    return []
  else:
    returning_signal = []
    for position in positions:
      returning_signal.extend(generate_signal(position))
    return returning_signal


def count_signals(signals=[]):
  signal_map_counts = Counter()
  if not signals:
    return {}
  else:
    signal_map_counts.update([signals] if type(signals) == tuple else signals)
  return signal_map_counts
  
  
def next_generation(living_positions=[]):
  if not living_positions or type(living_positions)==tuple:
    return []
  else:
    signal_map_counts = count_signals(generate_signals(living_positions))
    positions_with_three_neighbors = [signal for signal, count in signal_map_counts.items() if count == 3]
    positions_with_two_neighbors = [signal for signal, count in signal_map_counts.items() if count == 2]

    list(filter(lambda key_value: key_value[1] >= 3, signal_map_counts.items()))
    return list(set(living_positions) & set(positions_with_two_neighbors)) + positions_with_three_neighbors
    #Feedback: let's refactor this, we can do something like this:
    # signals_count = count_signals(generate_signals(living_positions))
    #
    # we can then use the filter function to iterate over the positions in the 
    #signals and get only those positions that will live to the next 
    #generation. After giving a try to use filter if you can't find how, 
    #please ask for help.
  
