def calcular_pago_mensual(principal, tasa_anual, plazo):
    tasa_mensual = tasa_anual / 12 / 100
    num_pagos = plazo * 12
    pago_mensual = principal * (tasa_mensual * (1 + tasa_mensual)*num_pagos) / ((1 + tasa_mensual)*num_pagos - 1)
    return pago_mensual
