from pydantic import BaseModel

# Request model for creating a rule (convert rule string to AST)
class RuleCreateRequest(BaseModel):
    rule_string: str

# Request model for combining two AST rules
class RuleCombineRequest(BaseModel):
    ast1: dict
    ast2: dict
    operator: str = "AND"

# Request model for evaluating a rule against data
class RuleEvaluateRequest(BaseModel):
    rule_ast: dict
    data: dict
