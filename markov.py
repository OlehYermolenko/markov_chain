"""
This is the module docstring for the markov module

>>> m = Markov('ab')
>>> m.predict('a')
'b'
"""

# define class
class Markov:
    # constructor method
    def __init__(self, txt):
        # attribute: transition table
        self.table = None

    def predict(self, data_in):
        return 'b'