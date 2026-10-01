from collections import deque
import random


class ReplayMemory():
    def __init__(self,max_len,seed = None):
        self.memory = deque([],maxlen = max_len)

    def append(self,new_exp):
        self.memory.append(new_exp)

    def sample(self,smaple_size):
        return random.sample(self.memory,smaple_size)

    def __len__(self):
        return len(self.memory)