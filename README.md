# Rule Engine Web Application

This is a simple web-based Rule Engine application that allows users to create, combine, and evaluate rules. The backend is built using **FastAPI**, and the frontend uses **HTML, CSS, and JavaScript** for interaction with the API.

## Features

- **Create Rule**: Input a rule (e.g., `age > 30`), and it generates an Abstract Syntax Tree (AST) for the rule.
- **Combine Rules**: Combine two ASTs (e.g., `age > 30 AND salary > 50000`).
- **Evaluate Rule**: Evaluate the AST against a dataset (e.g., `{ "age": 35, "salary": 60000 }`).

## Technology Stack

### Frontend
- HTML5, CSS3, and JavaScript
- Asynchronous fetch requests to interact with the FastAPI backend

### Backend
- FastAPI for rule parsing, combining, and evaluation
- CORS Middleware for cross-origin requests

## Setup Instructions

### Prerequisites
- Python 3.x
- FastAPI
- Uvicorn (for running FastAPI)
  
### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/rule-engine-app.git
    cd rule-engine-app
    ```

2. **Install dependencies**:

    First, create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

    Then install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```

3. **Run the FastAPI server**:

    Start the FastAPI server with Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    The backend will be available at `http://127.0.0.1:8000`.

4. **Open the Frontend**:

    Simply open the `index.html` file in your browser. The web page will allow you to interact with the FastAPI backend to create, combine, and evaluate rules.

## API Endpoints

- **Create Rule**: `POST /create_rule`
  - Request Body: `{ "rule_string": "age > 30" }`
  - Response: `{"AST": {...}}`

- **Combine Rules**: `POST /combine_rules`
  - Request Body: `{ "ast1": {...}, "ast2": {...} }`
  - Response: `{"combined_AST": {...}}`

- **Evaluate Rule**: `POST /evaluate_rule`
  - Request Body: `{ "ast": {...}, "data": { "age": 35 } }`
  - Response: `{"evaluation_result": true/false}`

 ## OVERALL OUTPUT
 ![OUTPUT](https://github.com/abhi-shek-86/Rule-Engine-with-AST/blob/master/Output.png)
 ![OUTPUT - INPUT](https://github.com/abhi-shek-86/Rule-Engine-with-AST/blob/master/Output%20-%20Input.png)


## Example Usage

1. **Create a rule**: Input a rule like `age > 30` and click the "Create Rule" button.
2. **Combine two rules**: Combine two ASTs by inputting them as JSON and clicking "Combine Rules."
3. **Evaluate rule**: Input an AST and a dataset to evaluate whether the rule is true for the given data.

## Screenshots
)
### Create Rule Page
![Create Rule](https://github.com/abhi-shek-86/Rule-Engine-with-AST/blob/master/Create%20Rule.png)

### Combine Rules Page
![Combine Rule](https://github.com/abhi-shek-86/Rule-Engine-with-AST/blob/master/Combine%20Rule.png)


### Evaluate Rule Page
![Evaluate Rule](https://github.com/abhi-shek-86/Rule-Engine-with-AST/blob/master/Evalute%20Rule.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **FastAPI**: For providing a fast and easy-to-use web framework.
- **Uvicorn**: For providing an ASGI server to run the FastAPI app.

