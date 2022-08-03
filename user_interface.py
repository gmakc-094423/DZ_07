import rational_numbers as rn
import complex_numbers as cn
import view_result as vr
import logger as log


def button_click():
    marker = 3
    is_OK = True
    while is_OK:
        marker = vr.input_data(
            "Press 1 if rational numbers\npress 2 if complex numbers\npress 3 if watch log\npress 4 if exit\n: "
        )
        log.logger("User klick", marker)
        if marker == "1":
            formula = vr.input_data("Input rational formula (exampe: (2+2)*2):  ")
            log.logger("Inputed rational formula", formula)
            vr.view("Result = ", rn.calc(formula))
            log.logger("Result", rn.calc(formula))
            is_OK = True
        elif marker == "2":
            z1 = vr.input_data("Input 1-st complex number (exampe: -1+3i):   ")
            z2 = vr.input_data("Input 2-nd complex number (exampe: 3-4i):   ")
            sign = vr.input_data(
                "Input sign operation on complex number (exampe: + - * / ):   "
            )
            formula = z1, z2, sign
            log.logger("Inputed complex formula", formula)
            vr.view("Result = ", cn.calc(formula))
            log.logger("Result", cn.calc(formula))
            is_OK = True
        elif marker == "3":
            vr.log_viev("log.csv")
            is_OK = True
        elif marker == "4":
            log.logger("Programm close", "")
            is_OK = False
        else:
            log.logger("User loss", "")
            is_OK = True
