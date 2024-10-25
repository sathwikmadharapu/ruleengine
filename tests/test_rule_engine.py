import unittest
from rule_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RuleEngine()

    def test_create_rule_valid(self):
        rule = "age > 30"
        ast = self.engine.create_rule(rule)
        self.assertIsNotNone(ast)

    def test_create_rule_invalid(self):
        with self.assertRaises(ValueError):
            self.engine.create_rule("invalid rule format")

    def test_combine_rules(self):
        rules = ["age > 30", "salary > 50000"]
        combined_ast = self.engine.combine_rules(rules)
        self.assertIsNotNone(combined_ast)

    def test_evaluate_rule_valid(self):
        rule = "age > 30"
        ast = self.engine.create_rule(rule)
        data = {"age": 35}
        result = self.engine.evaluate_rule(ast, data)
        self.assertTrue(result)

    def test_evaluate_rule_invalid(self):
        rule = "age > 30"
        ast = self.engine.create_rule(rule)
        data = {"invalid_key": 35}
        with self.assertRaises(ValueError):
            self.engine.evaluate_rule(ast, data)

if __name__ == '__main__':
    unittest.main()
