# -*- coding: utf-8 -*-
def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print("calculadora de divisas peso mexicano/peso colombiano")

    ammount = float(input("igresa el monto a convertir"))

    result = foreign_exchange_calculator(ammount)

    print("${} pesos mexicanos son ${} pesos colombianos ".format(ammount, result))

if __name__ == "__main__":
    run()