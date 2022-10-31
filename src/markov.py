"""Markov models."""


import numpy as np


class MarkovModel:
    """Representation of a Markov model."""

    init_probs: list[float]
    trans: list[list[float]]

    def __init__(self,
                 init_probs: list[float],
                 trans: list[list[float]]):
                 #self=pi, init_probs=X, trans=T
        
        result=self[init_probs[0]]
        for i in range(len(init_probs)-1):
            result=result*trans(init_probs[i], init_probs[i+1])
        return result

        """Create model from initial and transition probabilities."""
        # Sanity check...
        k = len(init_probs)
        assert k == len(trans)
        for row in trans:
            assert k == len(row)

        self.init_probs = init_probs
        self.trans = trans


def likelihood(x: list[int], mm: MarkovModel) -> float:
    """
    Compute the likelihood of mm given x.

    This is the same as the probability of x given mm,
    i.e., P(x ; mm).
    """
    ...  # FIXME: implement this
    #mm = MarkovModel(init_probs, transition_probs)
    return __init__(init_probs, x, transition_probs)

