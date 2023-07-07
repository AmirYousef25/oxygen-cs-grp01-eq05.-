import unittest
from src.main import Main
import os


class MainTests(unittest.TestCase):
    def test_default_values(self):
        main = Main()
        self.assertEqual(main.HOST, "http://34.95.34.5")
        self.assertEqual(main.TICKETS, "1")
        self.assertEqual(main.T_MAX, "30")
        self.assertEqual(main.T_MIN, "15")
        self.assertEqual(
            main.DATABASE, "postgresql://postgres:postgres@localhost:5432/postgres"
        )

    def test_empty_app_token(self):
        original_env = dict(os.environ)

        os.environ["TOKEN"] = ""

        main = Main()

        self.assertEqual(main.TOKEN, "")

        os.environ.clear()
        os.environ.update(original_env)

    def test_custom_values(self):
        original_env = dict(os.environ)

        os.environ["HOST"] = "http://34.95.34.5"
        os.environ["TOKEN"] = "eVBfQyhwtj"
        os.environ["TICKETS"] = "10"
        os.environ["T_MAX"] = "40"
        os.environ["T_MIN"] = "5"
        os.environ[
            "DATABASE"
        ] = "postgresql://postgres:postgres@localhost:5432/postgres"

        main = Main()

        self.assertEqual(main.HOST, "http://34.95.34.5")
        self.assertEqual(main.TOKEN, "eVBfQyhwtj")
        self.assertEqual(main.TICKETS, "10")
        self.assertEqual(main.T_MAX, "40")
        self.assertEqual(main.T_MIN, "5")
        self.assertEqual(
            main.DATABASE, "postgresql://postgres:postgres@localhost:5432/postgres"
        )

        os.environ.clear()
        os.environ.update(original_env)


if __name__ == "__main__":
    unittest.main()
