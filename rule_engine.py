import json
import re
from ast import Node
from database import get_existing_rules

class RuleEngine:
    def __init__(self):
        self.rules = []

    def create_rule(self, rule_string):
        # Validate the rule string
        if not self._validate_rule_string(rule_string):
            raise ValueError("Invalid rule string format.")
        
        # Check for existing rules and modify if necessary
        existing_rule = self._check_existing_rule(rule_string)
        if existing_rule:
            print(f"Rule already exists: {existing_rule}")
            return existing_rule  # Return existing rule

        try:
            # Convert rule string to AST Node
            return self._parse_rule(rule_string)
        except Exception as e:
            raise ValueError(f"Error parsing rule: {e}")

    def combine_rules(self, rules):
        # Combine multiple rules into a single AST
        combined_ast = None
        for rule in rules:
            try:
                ast = self.create_rule(rule)
                if combined_ast is None:
                    combined_ast = ast
                else:
                    combined_ast = Node("operator", left=combined_ast, right=ast, value="AND")
            except ValueError as e:
                print(f"Error combining rules: {e}")
                continue  # Skip invalid rules
        return combined_ast

    def evaluate_rule(self, rule_ast, data):
        # Validate the data format
        if not self._validate_data(data):
            raise ValueError("Invalid data format.")

        try:
            # Evaluate the AST against the provided data
            return self._evaluate_node(rule_ast, data)
        except Exception as e:
            raise ValueError(f"Error evaluating rule: {e}")

    def _validate_rule_string(self, rule_string):
        # Simple regex to validate rule structure (e.g., "age > 30")
        pattern = r"^\s*\(\s*(\w+\s*(>|<|=|!=)\s*\d+)\s*(AND|OR)\s*(\w+\s*(>|<|=|!=)\s*\d+)\s*\)\s*$"
        return bool(re.match(pattern, rule_string))

    def _check_existing_rule(self, rule_string):
        existing_rules = get_existing_rules()
        for rule in existing_rules:
            if rule['rule'] == rule_string:
                return rule
        return None

    def _validate_data(self, data):
        # Implement logic to validate data attributes against a catalog
        required_attributes = {"age", "department", "salary", "experience"}
        return all(attr in data for attr in required_attributes)

    def _parse_rule(self, rule_string):
        # Implement a simple parser to convert rule string to AST
        # This is a stub for your parsing logic.
        return Node("operator", left=Node("operand", value="age"), right=Node("operand", value=30), value=">")  # Example only

    def _evaluate_node(self, node, data):
        if node.type == "operand":
            return data[node.value]  # Just an example, needs more logic for comparison
        elif node.type == "operator":
            left_value = self._evaluate_node(node.left, data)
            right_value = self._evaluate_node(node.right, data)
            if node.value == ">":
                return left_value > right_value
            # Add more operator logic (AND, OR, etc.)
        return False  # Default case
