from flask import Flask, render_template, request, jsonify
import ast
import operator

app = Flask(__name__)


ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod
}


def evaluate(expr):
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise Exception("Invalid")

    node = ast.parse(expr, mode='eval').body
    return _eval(node)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data["expression"]

    try:
        result = evaluate(expression)
        return jsonify({"result": str(result)})
    except:
        return jsonify({"result": "Error"})


if __name__ == "__main__":
    app.run(debug=True)