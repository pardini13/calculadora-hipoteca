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
