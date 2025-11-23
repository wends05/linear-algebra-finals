import numpy as np
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from constants import five_by_five_matrix, sp_total
from matrix import Matrix

def optimize_schedule(matrix=five_by_five_matrix, targets=sp_total, scenario_name="Default Configuration"):
    print(f"=== SCENARIO: {scenario_name} ===")
    print(f"Targets (Story Points): {targets}")
    
    try:
        # Try importing scipy first
        from scipy.optimize import nnls
        hours, residual = nnls(matrix, targets)
    except ImportError:
        # print("Scipy not found. Using custom NumPy NNLS implementation...")
        
        def numpy_nnls(A, b, max_iter=10000, tol=1e-9):
            # Simple Projected Gradient Descent
            m, n = A.shape
            x = np.zeros(n)
            
            # Precompute
            AtA = A.T @ A
            Atb = A.T @ b
            
            # Estimate step size (1 / Lipschitz constant)
            alpha = 1.0 / np.linalg.norm(A, ord=2)**2
            
            for _ in range(max_iter):
                grad = AtA @ x - Atb
                x_new = np.maximum(0, x - alpha * grad)
                
                if np.linalg.norm(x_new - x) < tol:
                    x = x_new
                    break
                x = x_new
                
            # Calculate residual ||Ax - b||_2
            r = np.linalg.norm(A @ x - b)
            return x, r

        hours, residual = numpy_nnls(matrix, targets)
        
    print("--- OPTIMAL FEASIBLE PLAN (Non-negative) ---")
    roles = ["Senior", "Mid-Level", "Junior", "QA", "Intern"]

    # Print matrix
    print("Matrix (Roles vs Categories):")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print(f"{matrix[i, j]:8.2f}", end=" ")
        print()

    # Adjust roles list based on matrix size
    if len(hours) == 4:
        roles = ["Senior", "Mid-Level", "Junior", "QA"]
        
    for i, h in enumerate(hours):
        print(f"{roles[i]:<12}: {h:.2f} hours")
        
    # Calculate actual production
    production = np.dot(matrix, hours)
    print("--- PREDICTED OUTPUT vs TARGET ---")
    categories = ["Complex", "Infra", "Maintenance", "Testing", "Docs"]
    # Adjust categories based on matrix size (4x4 has 4 rows)
    if len(production) == 4:
        categories = ["Complex", "Infra", "Maintenance", "Testing"]
        
    for i, p in enumerate(production):
        diff = p - targets[i]  # Note: This diff is just for display, comparing to the passed targets would be better but sp_total is global.
        status = "(MET)" if abs(diff) < 0.1 else f"({diff:+.2f})"
        print(f"{categories[i]:<12}: {p:.2f} / {targets[i]} {status}")
        
    print(f"Residual (Error): {residual:.4f}")

    breakdown, total_person, total_category = Matrix.get_detailed_breakdown(matrix, hours)
    
    print("\n--- DETAILED BREAKDOWN (SP per Person per Category) ---")
    header = f"{'Category':<15}"
    for role in roles:
        header += f"{role:>12}"
    header += f"{'Total':>10}"
    print(header)
    print("-" * len(header))

    for i, cat in enumerate(categories):
        row_str = f"{cat:<15}"
        for j, _ in enumerate(roles):
            row_str += f"{breakdown[i, j]:12.2f}"
        row_str += f"{total_category[i]:10.2f}"
        print(row_str)
        
    print("-" * len(header))
    
    total_row = f"{'TOTAL SP':<15}"
    for sp in total_person:
        total_row += f"{sp:12.2f}"
    total_row += f"{np.sum(total_person):10.2f}"
    print(total_row)

if __name__ == "__main__":
    optimize_schedule()
