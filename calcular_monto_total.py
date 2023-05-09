def calcular_monto_total(pago_mensual, plazo):
    num_pagos = plazo * 12
    monto_total = pago_mensual * num_pagos
    return monto_total
