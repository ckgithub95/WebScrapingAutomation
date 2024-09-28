import unittest
from login import login_function  # Assuming your login function is defined here

class TestLogin(unittest.TestCase):
    
    def test_successful_login(self):
        """Test successful login with valid credentials."""
        username = "valid_user"
        password = "valid_password"
        result = login_function(username, password)  # Call your login function
        self.assertTrue(result)  # Assuming the function returns True on success

    def test_failed_login(self):
        """Test failed login with invalid credentials."""
        username = "invalid_user"
        password = "invalid_password"
        result = login_function(username, password)
        self.assertFalse(result)  # Assuming the function returns False on failure

if __name__ == '__main__':
    unittest.main()
