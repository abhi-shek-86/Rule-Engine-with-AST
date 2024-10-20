document.getElementById('createRuleButton').onclick = async function () {
    const ruleString = document.getElementById('ruleInput').value;
    const response = await fetch('http://localhost:8000/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_string: ruleString }),
    });

    const result = await response.json();
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);
};

document.getElementById('combineRulesButton').onclick = async function () {
    const ast1 = JSON.parse(document.getElementById('ast1').value);
    const ast2 = JSON.parse(document.getElementById('ast2').value);
    const operator = document.getElementById('operator').value;

    const response = await fetch('http://localhost:8000/combine_rules', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ast1, ast2, operator }),
    });

    const result = await response.json();
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);
};

document.getElementById('evaluateRuleButton').onclick = async function () {
    const data = JSON.parse(document.getElementById('dataInput').value);
    const ruleAst = JSON.parse(document.getElementById('ast1').value); // Assuming you use the first AST

    const response = await fetch('http://localhost:8000/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rule_ast: ruleAst, data }),
    });

    const result = await response.json();
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);
};
