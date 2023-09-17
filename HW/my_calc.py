def my_calc(num1, num2, operator):
    result = 0
    if str(operator) in "+-**//%" and str(num1).isdigit() and str(num2).isdigit():
        if int(num2) == 0 and (str(operator) == "/" or str(operator) == "//" or str(operator) == "%"):
            return "You can't divide by zero!"
        else:
            if str(operator) == "+":
                result = {int(num1) + int(num2)}
            elif str(operator) == "-":
                result = {int(num1) - int(num2)}
            elif str(operator) == "*":
                result = {int(num1) * int(num2)}
            elif str(operator) == "**":
                result = {int(num1) ** int(num2)}
            elif str(operator) == "/":
                result = {int(num1) / int(num2)}
            elif str(operator) == "//":
                result = {int(num1) // int(num2)}
            else:
                result = {int(num1) % int(num2)}
            return f"{num1} {operator} {num2} = {result}"
    else:
        return "Enter valid data"