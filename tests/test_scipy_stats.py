from testbook import testbook
import numpy as np

def test_values():
    with testbook('scipy_statcs_3d_plots.ipynb', execute=True) as tb:
        # Use np.array() to handle both numpy arrays and nested lists uniformly
        sigma_value = tb.value('float(np.array(sigma)[0,0])')
        assert np.isclose(sigma_value, 4.0, atol=1e-6), f"sigma[0,0]={sigma_value} of task 1 is not equal to 4"

        Z_value = tb.value('float(np.max(Z))')
        assert np.isclose(Z_value, 0.0003063, atol=1e-5), f"max(Z)={Z_value} of task 2 is not equal to 0.00031"
