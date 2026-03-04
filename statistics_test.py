import io
import unittest.mock
import exercise_statistics


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_statistics(self, mock_stdout):
        exercise_statistics.statistics()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "14.5")  # promedio
        self.assertEqual(results[1], "23")  # maximo
        self.assertEqual(results[2], "8")  # minimo
        self.assertEqual(results[3], "15")  # rango (max - min)


if __name__ == '__main__':
    unittest.main()
