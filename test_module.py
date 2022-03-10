import unittest
import requests

@unittest.skipIf(requests.get('https://api.kauri.finance').status_code != 200,
                            "API is not currently available")
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.good_data ={
                        "password": "1234bR#",
                        "username": "string",
                        "email": "string@gmail.com"
                        }

    def test_invalid_password(self):
        for bad_password in (["1234bR#"], ('1234bR#'), {1234:1234}):
            self.good_data["password"] = bad_password
            actual = requests.post('https://api.kauri.finance/api/v1/user/create',
                                    data = self.good_data).status_code
            unexpected = 201
            self.assertNotEqual(actual, unexpected, 'Expected failing the creation \
                             with wrong password')

    def test_invalid_username(self):
        for bad_username in (("string"), 12345, ["string"]):
            self.good_data["username"] = bad_username
            actual = requests.post('https://api.kauri.finance/api/v1/user/create',
                                    data = self.good_data).status_code
            unexpected = 201
            self.assertNotEqual(actual, unexpected, 'Expected failing the creation \
                             with wrong username')

    def test_invalid_email(self):
        for bad_email in ("str13@gmail.com", ["str1@gmail.com"], {"str1@gmail.com":1234}, ("str1@gmail.com")):
            self.good_data["email"] = bad_email
            actual = requests.post('https://api.kauri.finance/api/v1/user/create',
                                    data = self.good_data).status_code
            unexpected = 201
            self.assertNotEqual(actual, unexpected, 'Expected failing the creation\
                             with wrong email')



if __name__ == "__main__":
    unittest.main()
