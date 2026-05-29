import math


from flask import render_template, request




def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)
    if operacao == "bhaskara":
        num3_valor = request.form.get("num3", "").strip()
        if not num3_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num3 = float(num3_valor)
        
    else:

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        if operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"
            else:
                resultado = "Erro"
                etapas = "Erro: Divisão por zero não é permitida."
        elif operacao == "**" or operacao == "^":
            resultado = num1 ** num2
            etapas = f"{num1} elevado a {num2} = {resultado}"
        elif operacao == "raiz":
            if num1 >= 0:
                resultado = math.sqrt(num1)
                etapas = f"raiz_quadrada({num1}) = {resultado}"
            else:
                resultado = "Erro"
                etapas = "Erro: Não existe raiz real de número negativo."
        elif operacao == "log":
            if num1 > 0 and num2 > 0 and num2 != 1:
                resultado = math.log(num1, num2)
                etapas = f"log de {num1} na base {num2} = {resultado}"
            else:
                resultado = "Erro"
                etapas = "Erro: Argumentos do logaritmo inválidos."
        elif operacao == "bhaskara":
            a = num1
            b = num2
            c = num3
            delta = (b ** 2) - (4 * a * c)
    
            if a == 0:
                resultado = "Erro"
                etapas = "Erro: 'a' não pode ser zero em uma equação de 2º grau."
            elif delta < 0:
                resultado = "Sem raízes reais"
                etapas = f"Delta = {delta}. Como delta é negativo, não existem raízes reais."
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                resultado = (x1, x2)
                etapas = f"Delta = {delta}\nx1 = (-({b}) + √{delta}) / (2 * {a}) = {x1}\nx2 = (-({b}) - √{delta}) / (2 * {a}) = {x2}"

                
    return render_template("calculadora.html",etapas=etapas,resultados=resultado)
