# En un juego de preguntas a las que se responde “Si” o “No” gana quien
# responda correctamente las tres preguntas. Si se responde mal a cualquiera de
# ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
# 1. Colon descubrió América?
# 2. La independencia de Colombia fue en el año 1810?
# 3. The Doors fue un grupo de rock Americano?

def ResponderPreguntas (pregunta):
    if pregunta == 'Si':
        return True
    elif pregunta == 'No':
        return False

def Jugar ():
        if ResponderPreguntas (input ('¿Colon descubrio america?:')):
            if ResponderPreguntas (input ('¿La independencia de Colombia fue en el año 1810?:')):
                if ResponderPreguntas (input ('¿The Doors fue un grupo de rock Americano?:')):
                    print ('¡Gano el juego!')
        else:
            print ('Perdio el juego')
        
Jugar ()