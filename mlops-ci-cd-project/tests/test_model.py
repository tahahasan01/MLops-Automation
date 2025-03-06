import unittest
from app.model import predict

class TestModel(unittest.TestCase):
    def test_prediction(self):
        sample_input = [1.0, 2.0, 3.0]
        result = predict(sample_input)
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
