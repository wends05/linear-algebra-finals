import numpy as np
class Matrix:

    @staticmethod
    def gaussian_elimination(matrixA, B):
        try:
            X = np.linalg.solve(matrixA, B)

            if len(X) != 4:
                print(f"Error: Expected 4 values in solution vector X, but got {len(X)}. Cannot unpack for 4-person team.")
                return []
            senior_hours, mid_hours, junior_hours, qa_hours = X
            print("\n--- RESOURCE ALLOCATION PLAN (4-Person Team) ---")
            print(f"Senior Developer (x): {senior_hours:.2f} hours")
            print(f"Mid-Level Dev (y):    {mid_hours:.2f} hours")
            print(f"Junior Developer (z): {junior_hours:.2f} hours")
            print(f"QA Engineer (v):      {qa_hours:.2f} hours")

            return X
        except np.linalg.LinAlgError as e:
            print("Error: The system of equations has no unique solution.")
            return []

    @staticmethod
    def total_hours(res):
        return np.sum(res)
    
    @staticmethod
    def print_matrix(matrix):
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                print(f"{matrix[i, j]:8.2f}", end=" ")
            print()
