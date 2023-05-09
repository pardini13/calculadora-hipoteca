def calcular_pago_mensual(principal, tasa_anual, plazo):
    tasa_mensual = tasa_anual / 12 / 100
    num_pagos = plazo * 12
    pago_mensual = principal * (tasa_mensual * (1 + tasa_mensual)**num_pagos) / ((1 + tasa_mensual)**num_pagos - 1)
    return pago_mensual

def calcular_monto_total(pago_mensual, plazo):
    num_pagos = plazo * 12
    monto_total = pago_mensual * num_pagos
    return monto_total

def calcular_interes_total(monto_total, principal):
    interes_total = monto_total - principal
    return interes_total

def mostrar_cronograma(principal, tasa_anual, plazo, pago_mensual):
    tasa_mensual = tasa_anual / 12 / 100
    saldo = principal
    for pago in range(1, plazo * 12 + 1):
        interes_pago = saldo * tasa_mensual
        principal_pago = pago_mensual - interes_pago
        saldo -= principal_pago
        print(f"Pago {pago}: Interés: {interes_pago:.2f}, Principal: {principal_pago:.2f}")

def main():
    principal = float(input("Ingrese el monto del préstamo: "))
    tasa_anual = float(input("Ingrese la tasa de interés anual (porcentaje): "))
    plazo = int(input("Ingrese el plazo del préstamo en años: "))

    pago_mensual = calcular_pago_mensual(principal, tasa_anual, plazo)
    monto_total = calcular_monto_total(pago_mensual, plazo)
    interes_total = calcular_interes_total(monto_total, principal)

    print(f"Pago mensual: {pago_mensual:.2f}")
    print(f"Monto total a pagar: {monto_total:.2f}")
    print(f"Interés total pagado: {interes_total:.2f}")

    mostrar_cronograma(principal, tasa_anual, plazo, pago_mensual)

if __name__ == "__main__":
    main()
