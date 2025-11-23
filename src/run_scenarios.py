
import numpy as np
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from constants import five_by_five_matrix, sp_total
from optimize_schedule import optimize_schedule

# --- SCENARIO 1: The Default (Impossible) ---
# This uses the values currently in constants.py
optimize_schedule(five_by_five_matrix, sp_total, "Default (High Complex, Low Testing)")
print("\n" + "="*40 + "\n")

# --- SCENARIO 2: Balanced Workload ---
# We increase the targets for Maintenance and Testing to match the team's output
# when they are working on Complex tasks.
balanced_targets = np.array([60, 40, 40, 30]) 
# (Original was [60, 40, 30, 20])
optimize_schedule(five_by_five_matrix, balanced_targets, "Balanced Workload")
print("\n" + "="*40 + "\n")

# --- SCENARIO 3: High Complex Demand ---
high_complex_targets = np.array([100, 40, 30, 20])
optimize_schedule(five_by_five_matrix, high_complex_targets, "High Complex Demand")
print("\n" + "="*40 + "\n")

# --- SCENARIO 4: Maintenance & Testing Heavy ---
maintenance_heavy_targets = np.array([30, 30, 60, 50])
optimize_schedule(five_by_five_matrix, maintenance_heavy_targets, "Maintenance & Testing Heavy")
