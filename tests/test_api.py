import unittest
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_rule_valid(self):
        response = self.app.post('/create_rule', json={'rule_string': 'age > 30'})
        self.assertEqual(response.status_code, 201)

    def test_create_rule_invalid(self):
        response = self.app.post('/create_rule', json={'rule_string': 'invalid rule'})
        self.assertEqual(response.status_code, 400)

    def test_combine_rules(self):
        response = self.app.post('/combine_rules', json={'rules': ['age > 30', 'salary > 50000']})
        self.assertEqual(response.status_code, 200)

    def test_evaluate_rule_valid(self):
        response = self.app.post('/evaluate_rule', json={'rule_ast': {}, 'data': {'age': 35}})
        self.assertEqual(response.status_code, 200)

    def test_evaluate_rule_invalid(self):
        response = self.app.post('/evaluate_rule', json={'rule_ast': {}, 'data': {'invalid_key': 35}})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
