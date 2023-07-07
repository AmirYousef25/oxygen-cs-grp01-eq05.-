## To Implement
import unittest
from src.main import Main
import os


class MainTests(unittest.TestCase):
    def test_default_values(self):
        main = Main()
        self.assertEqual(main.HOST, "http://34.95.34.5")
        self.assertEqual(main.TICKETS, "1")
        self.assertEqual(main.T_MAX, "35")
        self.assertEqual(main.T_MIN, "10")
        self.assertEqual(
            main.DATABASE, "postgresql://postgres:postgres@localhost:5432/postgres"
        )

    def test_empty_app_token(self):
        # Save original environment variables to restore them later
        original_env = dict(os.environ)

        # Set the environment variable APP_TOKEN as an empty string for testing
        os.environ["TOKEN"] = ""

        # Initialize the main class
        main = Main()

        # Test if the APP_TOKEN is an empty string
        self.assertEqual(main.TOKEN, "")

        # Reset environment variables to original state
        os.environ.clear()
        os.environ.update(original_env)

            
    def test_custom_values(self):
        # Save original environment variables to restore them later
        original_env = dict(os.environ)

        # Set the environment variables with custom values for testing
        os.environ["HOST"] = "http://34.95.34.5"
        os.environ["TOKEN"] = "eVBfQyhwtj"
        os.environ["TICKETS"] = "10"
        os.environ["T_MAX"] = "40"
        os.environ["T_MIN"] = "5"
        os.environ[
            "DATABASE"
        ] = "postgresql://postgres:postgres@localhost:5432/postgres"

        # Initialize the main class
        main = Main()

        # Test the custom values
        self.assertEqual(main.HOST, "http://34.95.34.5")
        self.assertEqual(main.TOKEN, "eVBfQyhwtj")
        self.assertEqual(main.TICKETS, "10")
        self.assertEqual(main.T_MAX, "40")
        self.assertEqual(main.T_MIN, "5")
        self.assertEqual(
            main.DATABASE, "postgresql://postgres:postgres@localhost:5432/postgres"
        )

        # Reset environment variables to original state
        os.environ.clear()
        os.environ.update(original_env)


if __name__ == "__main__":
    unittest.main()