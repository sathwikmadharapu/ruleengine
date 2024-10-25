from flask import Flask, request, jsonify
from rule_engine import RuleEngine

app = Flask(__name__)
engine = RuleEngine()

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    try:
        rule_node = engine.create_rule(rule_string)
        return jsonify({'rule': rule_node.__dict__}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rules = request.json.get('rules')
    combined_ast = engine.combine_rules(rules)
    return jsonify({'combined_rule': combined_ast.__dict__})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_ast = request.json.get('rule_ast')
    data = request.json.get('data')
    try:
        result = engine.evaluate_rule(rule_ast, data)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
