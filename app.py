from flask import Flask, render_template, request  

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            number1 = float(request.form["number1"])
            number2 = float(request.form["number2"])
            operation = request.form["operation"]

            if operation == "add":
                result = number1 + number2

            elif operation == "subtract":
                result = number1 - number2

            elif operation == "multiply":
                result = number1 * number2

            elif operation == "divide":
                if number2 == 0:
                    error = "Cannot divide by zero"
                else:
                    result = number1 / number2

        except ValueError:
            error = "Please enter valid numbers"

    return render_template(
        "index.html",
        result=result,
        error=error
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
