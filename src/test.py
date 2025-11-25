import sys
import os

from constants import sp_total, five_by_five_matrix, categories
from matrix import Matrix

if __name__ == "__main__":
    res = Matrix.gaussian_elimination(five_by_five_matrix, sp_total)
    print(f"\nTotal Hours Required: {Matrix.total_hours(res):.2f} hours")
    print("\nMatrix Representation (A):")
    Matrix.print_matrix(five_by_five_matrix)
    production = Matrix.calculate_production(five_by_five_matrix, res)
    print("\nStory Points (B):")
    for i, p in enumerate(production):
        print(f"Category {categories[i]}: {p:} story points")
    breakdown = Matrix.get_detailed_breakdown(five_by_five_matrix, res)
    print(breakdown[0])