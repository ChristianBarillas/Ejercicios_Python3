ingresos_mensuales = 2000
gastos_mensuales = 2500

if ingresos_mensuales > 400:
    if ingresos_mensuales - gastos_mensuales < 0:
        print ("estas en perdida")
    elif ingresos_mensuales - gastos_mensuales > 1000:
        print("estamos bien")
    else:
        print("estas gastando mucho")

elif ingresos_mensuales > 100:
    print("estas bien en cualquier parte del mundo")
    
else:
    print("sos pobre")