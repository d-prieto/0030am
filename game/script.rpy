# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define b = Character("Bruna", color="#554949")
define a = Character("Aurora",color="#a1b69f")
define au = "Aurora"
define br = "Bruna"

# Variables de la Historia
default ignorarTelefonoUnaVez = False

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg habitacion osc1

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # show eileen happy

    # Presenta las líneas del diálogo.

    "Que sueño, mejor me voy a acostar"

    scene black
    with dissolve

    "zzzzz"
    # aqui suena sonido
    play sound "audio/Message tone.mp3"
    scene bg habitacion osc2
    with dissolve

    "¿Qué suena a esta hora?"

    menu:

        "Acaba de sonar un mensaje ¿lo reviso?"

        "A ver qué dice":
            jump conversacionTelefono

        "Nah, mañana lo miro que tengo mucho sueño":
            jump suenaOtraVezElMensaje

label suenaOtraVezElMensaje:
    $ ignorarTelefonoUnaVez = True
    scene bg habitacion osc1
    with dissolve
    "No voy a leerlo porque es muy tarde"
    play sound "audio/Message tone.mp3"
    pause 0.8
    "Suena de nuevo otro mensaje"
# Aquí debería ir un sonido
    scene bg habitacion osc2
    with dissolve
    "Jumm, otro mensaje"
    menu:
        "Acaba de sonar OTRO mensaje ¿lo reviso?"

        "Toca silenciar el celu o apagarlo":
            jump ignorarloTodo

        "Bueno... a ver qué dice":
            jump conversacionTelefono

label ignorarloTodo:
    scene bg habitacion osc1
    with dissolve
    "Apago el celu y voy a dormir"
    #(Final se le cae el celu en la cara)
    scene bg final dormir
    with dissolve
    pause
    "{b}Fin{/b}."
    return

label conversacionTelefono:


    call phone_start(0) from _call_phone_start
    #aquí hay una cosa fea y es que poniendo el scene puedo puedes poner el teléfono directamente.
    #El teléfono está puesto 2 veces, una vez haciendo la animación integrada y luego con la mano como fondo
    scene bg habitacion tel1
    $ phone_too = " " #Si no se pone esta variable el programa falla.
    call mensaje(br, "¿Aurora? Ping?Holo?") from _call_mensaje
    if ignorarTelefonoUnaVez:
        call mensaje(br, "¿hay alguien ahí?") from _call_mensaje_1
    call mensaje("yo", "Hola Bruna…") from _call_mensaje_2
    call mensaje(br, "¿Estás despierta?") from _call_mensaje_3
    call mensaje("yo", "No, bueno ahora sí pero antes no.") from _call_mensaje_4
    call mensaje(br, "La noche está super rara.") from _call_mensaje_5
    call mensaje("yo", "Sí, yo también me di cuenta hay mucho silencio") from _call_mensaje_6
    call mensaje(br, "A esta hora ya tienen la media fiesta aquí al lao") from _call_mensaje_7
    call mensaje("yo", "Se fueron pal norte el otro día.") from _call_mensaje_8
    call mensaje(br, "ahh si pu.") from _call_mensaje_9
    call mensaje("yo", "Si pu") from _call_mensaje_10
    call mensaje(br, "¿y qué estás haciendo?") from _call_mensaje_11
    call mensaje("yo", "Durmiendo pu, tú lo sabes, jjajaaja ya dime ¿qué quieres?") from _call_mensaje_12
    call mensaje(br, "Sabía que me ibas a contestar.") from _call_mensaje_13
    call mensaje("yo", "Siempre te contesto.") from _call_mensaje_14
    call mensaje(br, "Uta que tengo sueño, ya dime.") from _call_mensaje_15
    call mensaje("yo", "Dime tú.") from _call_mensaje_16
    call mensaje(br, "Pero si tú me hablaste.") from _call_mensaje_17
    call mensaje("yo", "No, tú me mandaste el mensaje.") from _call_mensaje_18
    call mensaje(br, "No, tú me mandaste el mensaje.") from _call_mensaje_19
    call mensaje("yo", "No, sí, yo... ¿te mande el mensaje?") from _call_mensaje_20
    call mensaje(br, "Que bueno que me contestaste.") from _call_mensaje_21
    #primera elección
    call screen phone_reply("Tengo mucho sueño","suenyo1","Quiero conversar","seguir1")

label suenyo1:
    call mensaje("yo", "Creo que tengo mucho sueño.") from _call_mensaje_22
    call mensaje(br, "Creo que estoy soñando.") from _call_mensaje_23
    call mensaje("yo", "Yo también, mejor me duermo.") from _call_mensaje_24
    call mensaje(br, "¿se puede dormir dentro de un sueño?") from _call_mensaje_25
    call mensaje("yo", "no se... ") from _call_mensaje_26
    hide screen phone_message4
    call mensaje(br, "Si una de las dos está despierta creo que sí.") from _call_mensaje_27

    call phone_end(0) from _call_phone_end
        #(Final se le cae el celu en la cara)
    pause 0.2
    play sound "audio/celucayendo.mp3"
    scene bg final plop
    pause
    "{b}Fin{/b}."
return

label seguir1:
    call mensaje("yo", "Yo también, pero quiero conversar.") from _call_mensaje_28
    call mensaje(br, "Por eso te mandé el mensaje, hablemos.") from _call_mensaje_29
    call mensaje("yo", "¿Qué?... pero que mierda") from _call_mensaje_30
    call mensaje(br, "Te acordai cuando estaba en la playa y vino tremenda ola,") from _call_mensaje_31
    call mensaje("yo", "me dio tremendas vueltas, quedé llena de arena.") from _call_mensaje_32
    call mensaje(br, "Tenía arena hasta en el pelo.") from _call_mensaje_33
    call mensaje("yo", "Igual después me volví a meter al agua.") from _call_mensaje_34
    call mensaje(br, "Hacía frío igual que ahora") from _call_mensaje_35
    #segunda elección
    #Aquí bifurcación  si pregunta dónde está, se llega al final del dibujo con coneja mirando. Si pregunta qué sigue adelante.
    call screen phone_reply("¿Dónde estás?","creepy1","¿Qué haces?","seguir2")

label creepy1:
#(imagen del final con sombra)
    call mensaje("yo", "¿Dónde estás?") from _call_mensaje_36
    call mensaje(br, "En la cama, con el celu y tú?") from _call_mensaje_37
    call mensaje("yo", "En la cama con el celu y… me llego tu mensaje.") from _call_mensaje_38
    call mensaje(br, "...") from _call_mensaje_39
    call mensaje("yo", "¿Estás bien?") from _call_mensaje_40
    call phone_end(0) from _call_phone_end_1
    scene bg final creepy
    pause
    "{b}Fin{/b}."
return

label seguir2:
#Aquí sigue si se escoge decir qué haces?
    call mensaje("yo", "¿Qué haces?") from _call_mensaje_41
    call mensaje(br, "Aburrirme… ser noctámbula es aburrido.") from _call_mensaje_42
    call mensaje(br, "¿cómo vives de día?") from _call_mensaje_43
    call mensaje("yo", "Me pregunto lo mismo contigo") from _call_mensaje_44
    call mensaje(br, "Yo también me lo pregunto.") from _call_mensaje_45
    call mensaje("yo", "Pero tu querías ser vampira.") from _call_mensaje_46
    call mensaje(br, "Y tú bruja… estoy preocupada, tengo miedo.") from _call_mensaje_47
    hide screen phone_message4
    call mensaje(br, "Por eso no aguanté escribirte.") from _call_mensaje_48
    call mensaje("yo", "¿Qué te preocupa?") from _call_mensaje_49
    call mensaje(br, "¿Seguiremos siendo hermanas después de esto?") from _call_mensaje_50
    call mensaje("yo", "Obvio") from _call_mensaje_51
    hide screen phone_message4
    call mensaje("yo", "No importa pa que lado nos hayamos ido. Igual nos complementamos") from _call_mensaje_52
    call mensaje(br, "Siempre sabes que decir pa hacerme sentir mejor.") from _call_mensaje_53
    call mensaje("yo", "Ajummmm si que tengo sueño… ¿hablamos mañana?") from _call_mensaje_54
    call mensaje(br, "Te llamaré más temprano.") from _call_mensaje_55
    call mensaje("yo", "Ánimos con tu nueva fase… ajumm") from _call_mensaje_56
    call phone_end(0) from _call_phone_end_2

    scene bg final hermanas
    pause
    "{b}Fin{/b}."
return
