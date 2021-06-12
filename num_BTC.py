import math

def num_BTC(b):

  block_level = 1
  current_reward = float(50)
  halving_event = 0
  total_reward = float(0)

  while block_level <= b:

    if halving_event < 210000:
      halving_event = halving_event + 1
    else:
      current_reward = float(current_reward/2)
      halving_event = 1

    total_reward = total_reward + current_reward
    block_level = block_level + 1

  return total_reward