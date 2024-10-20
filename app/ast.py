from typing import Dict, Any

# Parse rule string into AST (Abstract Syntax Tree)
def parse_rule(rule_string: str) -> Dict[str, Any]:
    if "AND" in rule_string:
        left, right = rule_string.split("AND")
        return {
            "type": "AND",
            "left": {"type": "condition", "value": left.strip()},
            "right": {"type": "condition", "value": right.strip()}
        }
    elif "OR" in rule_string:
        left, right = rule_string.split("OR")
        return {
            "type": "OR",
            "left": {"type": "condition", "value": left.strip()},
            "right": {"type": "condition", "value": right.strip()}
        }
    else:
        return {"type": "condition", "value": rule_string.strip()}

# Combine two AST rules
def combine_rules(ast1: Dict[str, Any], ast2: Dict[str, Any], operator: str = "AND") -> Dict[str, Any]:
    return {
        "type": operator,
        "left": ast1,
        "right": ast2
    }

# Evaluate the rule AST against provided data
def evaluate_rule(rule_ast: Dict[str, Any], data: Dict[str, Any]) -> bool:
    rule_type = rule_ast.get("type")

    if rule_type == "AND":
        return evaluate_rule(rule_ast["left"], data) and evaluate_rule(rule_ast["right"], data)
    elif rule_type == "OR":
        return evaluate_rule(rule_ast["left"], data) or evaluate_rule(rule_ast["right"], data)
    elif rule_type == "condition":
        condition = rule_ast["value"]
        key, operator, value = condition.split()
        key = key.strip()
        value = value.strip().replace("'", "")  # Clean up value for strings
        if operator == ">":
            return data.get(key) > int(value)
        elif operator == "<":
            return data.get(key) < int(value)
        elif operator == "=":
            return data.get(key) == value
        else:
            raise ValueError("Unsupported operator")
    else:
        raise ValueError("Invalid rule type")
