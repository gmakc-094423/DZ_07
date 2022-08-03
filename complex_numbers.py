import re


def tuple_formula(formula):
    return tuple(re.findall(r"[-+i]?[^-+i]+", formula))


def calc(formula):
    z1, z2, sign = formula
    z1 = tuple_formula(z1)
    z2 = tuple_formula(z2)

    a1 = z1[0]
    a2 = z2[0]
    b1 = z1[1]
    b2 = z2[1]

    match sign:
        case "+":
            return str(eval(a1 + "+" + a2)) + "+" + str(eval(b1 + "+" + b2)) + "i"
        case "-":
            return str(eval(a1 + "-" + a2)) + "+" + str(eval(b1 + "-" + b2)) + "i"
        case "*":
            return (
                str(eval(a1 + "*" + a2 + "-" + b1 + "*" + b2))
                + "+"
                + str(eval(a1 + "*" + b2 + "+" + a2 + "*" + b1))
                + "i"
            )
        case "/":
            return (
                str(
                    eval(
                        "("
                        + a1
                        + "*"
                        + a2
                        + "+"
                        + b1
                        + "*"
                        + b2
                        + ")"
                        + "/"
                        + "("
                        + a2
                        + "**2"
                        + "+"
                        + b2
                        + "**2"
                        + ")"
                    )
                )
                + "+"
                + str(
                    eval(
                        "("
                        + a2
                        + "*"
                        + b1
                        + "+"
                        + a1
                        + "*"
                        + b2
                        + ")"
                        + "/"
                        + "("
                        + a2
                        + "**2"
                        + "+"
                        + b2
                        + "**2"
                        + ")"
                    )
                )
                + "i"
            )


# formula = "-2+3i", "6-2i", "*"

# print(calc(formula))
