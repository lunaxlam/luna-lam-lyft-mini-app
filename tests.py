"Tests for Luna Lam's lyft mini app"

import unittest
from server import app


class AppTests(unittest.TestCase):
    """Tests for lyft mini app"""

    def setUp(self):
        """Run before every test"""

        self.client = app.test_client()
        app.config["TESTING"] = True
    

    def test_homepage(self):
        """Check to see if the correct content renders on the homepage"""

        result = self.client.get("/")
        self.assertIn(b"Please enter a string and we will cut it for you for no additional charge:", result.data)
    

    def test_result(self):
        """Test to see if the correct results render"""

        result = self.client.post("/test", 
                                data={"string_to_cut": "iamyourlyftdriver"})

        self.assertIn(b"return_string", result.data)
        self.assertIn(b"muydv", result.data)




if __name__ == "__main__":
    unittest.main()


    

    