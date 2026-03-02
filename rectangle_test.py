import io
import unittest.mock
import exercise_rectangle


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle(self, mock_stdout):
        exercise_rectangle.rectangle()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "50")  # area
        self.assertEqual(results[1], "30")  # perimetro


if __name__ == '__main__':
    unittest.main()
