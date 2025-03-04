import pytest
import numpy as np
from model import predict  # Import your ML model's prediction function

def test_prediction_output():
    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])  # Example input
    output = predict(sample_input)  # Call the function
    assert isinstance(output, np.ndarray), "Output should be a NumPy array"

def test_prediction_length():
    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])
    output = predict(sample_input)
    assert len(output) == len(sample_input), "Output length should match input length"
