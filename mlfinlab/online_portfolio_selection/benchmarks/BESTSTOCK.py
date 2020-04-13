# pylint: disable=missing-module-docstring
from mlfinlab.online_portfolio_selection.OLPS import OLPS
import pandas as pd
import numpy as np


class BESTSTOCK(OLPS):
    """
    returns best stock in hindsight
    """

    # Buy the asset that increased the most for the given period
    def first_weight(self, _weights):
        """
        :param _weights
        """
        # index of stock that increased the most
        best_idx = np.argmax(self.final_relative_return[-1])
        new_weight = np.zeros(self.number_of_assets)
        new_weight[best_idx] = 1
        return new_weight
