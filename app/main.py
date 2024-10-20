from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; adjust for production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods; adjust as necessary
    allow_headers=["*"],  # Allows all headers; adjust as necessary
)

# Define your data models
class Rule(BaseModel):
    rule_string: str

class CombineRequest(BaseModel):
    ast1: Dict[str, Any]
    ast2: Dict[str, Any]

class EvaluateRequest(BaseModel):
    ast: Dict[str, Any]
    data: Dict[str, Any]

# A function to parse the rule and return an AST
def parse_rule(rule_string: str) -> Dict[str, Any]:
    # Example parsing logic
    if ">" in rule_string:
        field, value = rule_string.split(">")
        return {"type": "condition", "field": field.strip(), "operator": ">", "value": value.strip()}
    return {"type": "condition", "field": rule_string.strip(), "operator": "=", "value": "true"}

# An endpoint to create rules
@app.post("/create_rule")
def create_rule(rule: Rule):
    ast = parse_rule(rule.rule_string)  # Parse the rule string to AST
    return {"AST": ast}

# A function to combine two ASTs
def combine_rules(ast1: Dict[str, Any], ast2: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "AND",
        "left": ast1,
        "right": ast2,
    }

# An endpoint to combine two rules
@app.post("/combine_rules")
def combine_rules_endpoint(request: CombineRequest):
    combined_ast = combine_rules(request.ast1, request.ast2)
    return {"combined_AST": combined_ast}

# A function to evaluate the rule
def evaluate_rule(ast: Dict[str, Any], data: Dict[str, Any]) -> bool:
    # Example evaluation logic
    if ast['operator'] == '>':
        return data[ast['field']] > int(ast['value'])
    return False

# An endpoint to evaluate a rule
@app.post("/evaluate_rule")
def evaluate_rule_endpoint(request: EvaluateRequest):
    result = evaluate_rule(request.ast, request.data)
    return {"evaluation_result": result}

# Run the application (this is just for local testing, usually done in the terminal)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
