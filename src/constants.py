import numpy as np

five_by_five_matrix = np.array([
    # Senior,     Mid,        Junior,     QA
    [6.0,         3.0,        1.0,        1.0],   # Complex Story Points
    [2.0,         2.0,        1.0,        1.0],   # Infra Story Points
    [2.0,         1.0,        1.0,        3.0],   # Maintenance Story Points
    [0.0,         1.0,        0.0,        3.0],   # Testing Story Points
])

sp_total = np.array([
    100,
    60,
    70,
    40,
])

categories = ["Complex Story Points", "Infra Story Points", "Maintenance Story Points", "Testing Story Points"]