import sys
import os

from constants import sp_total
from constants import five_by_five_matrix
from matrix import Matrix

if __name__ == "__main__":
    Matrix.gaussian_elimination(five_by_five_matrix, sp_total)
