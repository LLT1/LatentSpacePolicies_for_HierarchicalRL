"""Define base class for an agent.
"""
from abc import ABCMeta, abstractclassmethod

class Agent(metaclass=ABCMeta):
    @abstractclassmethod
    def select_action(self, state, eval=False, random=False):
        pass

    @abstractclassmethod
    def post_process_action(self, state, action):
        pass

    @abstractclassmethod
    def update_parameters(self, batch_data, total_updates):
        pass

    @abstractclassmethod
    def state_dict(self):
        pass

    @abstractclassmethod
    def load_state_dict(self, state_dict):
        pass
