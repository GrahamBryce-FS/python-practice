import unittest
from unittest.mock import patch
from grader import Grader  

# run "python3 -m unittest test_grader2.py" to initiate
class TestGrader(unittest.TestCase):
    # CONDITION COVERAGE
    def test_upper(self):
        self.assertTrue(Grader.upper('bryce'), "BRYCE")
    # BRANCH COVERAGE
    def test_divide(self):
        grader = Grader()
        self.assertEqual(grader.divide(10, 5), "Exact division")
        self.assertEqual(grader.divide(10, 3), "Non-exact division")
        self.assertEqual(grader.divide(10, 0), "Cannot divide by zero")

    #STATEMENT COVERAGE this works
    # this is your test below
    def test_gradeInfo(self):
        gr = Grader()
        self.assertEqual(gr.gradeInfo(),"You did not entered a grade number between 0 ant 100.")

    # everything below will run automatically
    # FUNCTION COVERAGE
    @patch("builtins.input", side_effect=["Bryce", "Assignment1", "95"])
    def test_gradeInfo_A(self, mock_input):
        grader = Grader()
        result = grader.gradeInfo()
        self.assertIsNone(result)  

    @patch("builtins.input", side_effect=["Bryce", "Assignment2", "85"])
    def test_gradeInfo_B(self, mock_input):
        grader = Grader()
        result = grader.gradeInfo()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["Bryce", "Assignment3", "75"])
    def test_gradeInfo_C(self, mock_input):
        grader = Grader()
        result = grader.gradeInfo()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["Bryce", "Assignment4", "65"])
    def test_gradeInfo_D(self, mock_input):
        grader = Grader()
        result = grader.gradeInfo()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["Bryce", "Assignment5", "55"])
    def test_gradeInfo_F(self, mock_input):
        grader = Grader()
        result = grader.gradeInfo()
        self.assertEqual(result, 55)

if __name__ == "__main__":
    unittest.main()