while True:
    print('')
    print('NIVELES DE ANESTESIA PARA LAS RATAS')
    print('')
    peso = int(input('Ingrese el peso en gramos '))
    print('')
    keta = (peso*80)/1000
    ketamina = keta/50
    xilo = (peso*10)/1000
    xilocaina = (xilo/100)
    print('Ketamina a colocar ', ketamina, ' ml')
    print('')
    print('Xilacina a colocar ',xilocaina,' ml')
    print('')
    print('COLOCAR CON DISCRESION O SE MUEREN')
    print('')
    repeticion = int(input('Si desea calcular una nueva dosis, ingrese 1, de lo contrario, ingrese 0 '))
    
    if repeticion == 1:
        continue
    else:
        break
