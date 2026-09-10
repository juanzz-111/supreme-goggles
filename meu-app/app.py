from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")

@app.route("/resultado", methods=["POST"])
def resultado():

    numero1 = float(request.form["numero1"])
    numero2 = float(request.form["numero2"])
    operacao = request.form["operacao"]

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "*":
        resultado = numero1 * numero2

    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "Aqui tem como não rapaz, IMPOSSÍVEL divisível por zero"

    return render_template("resultado.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)