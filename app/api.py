from fastapi import APIRouter
from app.ast import parse_rule, combine_rules, evaluate_rule
from app.models import RuleCreateRequest, RuleCombineRequest, RuleEvaluateRequest

api_router = APIRouter()

@api_router.post("/create_rule")
async def create_rule(request: RuleCreateRequest):
    ast = parse_rule(request.rule_string)
    return {"AST": ast}

@api_router.post("/combine_rules")
async def combine_rules_endpoint(request: RuleCombineRequest):
    combined_ast = combine_rules(request.ast1, request.ast2, request.operator)
    return {"combined_AST": combined_ast}

@api_router.post("/evaluate_rule")
async def evaluate_rule_endpoint(request: RuleEvaluateRequest):
    result = evaluate_rule(request.rule_ast, request.data)
    return {"result": result}
