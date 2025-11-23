import numpy as np

five_by_five_matrix = np.array([
    # Senior,     Mid,        Junior,     QA
    [3.0,         2.0,        1.0,        1.0],   # Complex Story Points
    [2.0,         2.0,        1.0,        1.0],   # Infra Story Points
    [1.0,         1.0,        1.0,        3.0],   # Maintenance Story Points
    [1.0,         1.0,        0.0,        3.0],   # Testing Story Points
])

sp_total = np.array([
    60,
    50,
    40,
    30,
])

SPRINT_DAYS = 10
HRS_PER_DAY = 8
