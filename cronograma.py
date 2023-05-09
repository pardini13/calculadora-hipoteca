def mostrar_cronograma(principal, tasa_anual, plazo, pago_mensual):
    tasa_mensual = tasa_anual / 12 / 100
    saldo = principal
    for pago in range(1, plazo * 12 + 1):
        interes_pago = saldo * tasa_mensual
        principal_pago = pago_mensual - interes_pago
        saldo -= principal_pago
        print(f"Pago {pago}: Interés: {interes_pago:.2f}, Principal: {principal_pago:.2f}")
