import io
import unittest.mock
import exercise_temperature


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_temperature(self, mock_stdout):
        exercise_temperature.temperature()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "77.0")  # celsius a fahrenheit
        self.assertEqual(results[1], "25.0")  # valor original de celsius


if __name__ == '__main__':
    unittest.main()
