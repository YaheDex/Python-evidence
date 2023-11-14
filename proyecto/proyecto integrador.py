#Proyecto integrador
#Autores: Aleydis Xalli Jiménez Rendón, Carol Fernanda Reyes García, Yahel Alejandro Jiménez Fernández
#Fecha: 08/09/2022
import time
import random
import math
dibujo_vidas=['''
  *** ***    *** ***    *** ***
 *********  *********  *********
  *******    *******    *******
    ***        ***        ***''','''
  *** ***    *** ***    * *  **
 *********  *********  **  *   *
  *******    *******    * *   *
    ***        ***         **''','''
  *** ***    **   **    * *  **
 *********  *   **  *  **  *   *
  *******    * *   *    * *   *
    ***        * *         **''','''
  *   *      **   **    * *  **
 * * *  **  *   **  *  **  *   *
  ***  **    * *   *    * *   *
    **         * *         **''']
file=open("instrucciones1.txt","r") #Sección de instrucciones de introducción para entender el funcionamiento del programa, con tiempos de espera para permitir al usuario leer
print(file.read())
file.close
nick=str(input("Danos el nombre de tu pequeño gamer\n"))
print("De ahora en más, cada que se despliegue el programa, saluderamos a",nick)
time.sleep(2)
print("Hablando del despliegue, explicaremos cómo funciona:")
time.sleep(2)
print("Cuando",nick,"ingrese a un videojuego de la lista, el programa se desplegará")
time.sleep(2)
file2=open("instrucciones2.txt","r")
print(file2.read())
file2.close
time.sleep(3)
print("Al completar el test, se evaluará el puntaje.\nCabe destacar que, de no alcanzar el puntaje,el launcher bloqueará el acceso al juego y se le\nredirigirá a",nick,"al menú inicio, además se le mostrara su puntaje y una pequeña retroalimentación.")
time.sleep(4)
file3=open("instrucciones3.txt","r")
print(file3.read())
file3.close
time.sleep(3)
print("Usted cuenta con las siguientes opciones para usar el launcher:")
time.sleep(2)
print("Jugar: escoger la app a ejecutar")
time.sleep(3)
print("Añadir: le permite añadir apps al launcher sin añadirlas a la lista de apps restringidas")
time.sleep(3)
print("Agregar: le permite añadir una app a la lista de las cuales requieren\nresponder algún test.\n*No hay necesidad de añadirlas primero al launcher")
time.sleep(3)
print("Eliminar: permite eliminar una app de la lista de las cuales requieren\nresponder algún test")
time.sleep(3)
print("Suprimir: elimina la app por completo del launcher")
time.sleep(3)
print("Consultar: consulta las apps dentro del launcher")
time.sleep(3)
print("Salir: cierra el programa")
time.sleep(3)
lista_test=["Ortografía","Gramática","Lectura"]

#lista de frases aleatorias para hacer amigable al programa, contiene algunas chistosas
random_frases=["¿Ya repasaste gramática? Recuerda hacerlo a menudo para progresar","Espero tengas éxito al jugar y al aprender","¿Tienes tiempo libre? Lee un ratitooo","Tú puedes aprender mucho, yo sólo sé las pocas cosas que me enseñaron Yahel, Xalli y Carol","Me gustan los shooter, ¿ya viste que van a sacar Warzone Mobile? ¡QUE ÉPICO!", "Incluso en tus temas de interés puedes seguir apreniendo, yo leo foros de videojuegos y así me entretengo\n pero mantengo lenguaje enriquecido","Ojalá el equipo que me programó obtenga 10 en su calificación, ah, ¡y tú también en tu próximo test!","¿Ya tomaste agua? Recuerda que una buena hidratación mantiene las ideas fluyendo más eficientemente","Si no apruebas la siguiente ocasión, secuestraré a tu mascota, ah, espera, no soy Duolingo jaja, olvídalo","¿Amaneciste bien? Recuerda que la salud e inteligencia emocional son de lo más importante para que todo al rededor se mantenga en armonía"]
#a continuación están todas las funciones que actúan conforme a la opción elegida por el usuario
def jugar(a,la,ab,au,nick): #función que contiene la opción de jugar, que en base a si la app está restringida o no, desplegará un test aleatorio
    #sección de listas de preguntas y respuestas de cada test
    p_ortg=["1.- Identifica las palabras homófonas usadas de manera CORRECTA.","2.- Hace falta una palabra, identifícala:\nPedro        su jardín.","3.- Hace falta una palabra, identifícala:\nYo siempre       bien la masa antes de hornear.","4.-Hace falta una palabra, identifícala:\nEl avión no     podido despegar por las fallas en el motor.","5.-Hace falta una palabra, identifícala:\nTodos quedamos       de tanta comida.","6.- Hace falta una palabra, identifícala:\nTodos deberíamos actuar con  "]
    r_ortg_correcta=[1,1,2,3,1,3]
    r_ortg_1=open("respuestas_ortg_1.txt","r")
    r_ortg=r_ortg_1.readlines()
    r_ortg_1.close()
    r_ortg_2=open("respuestas_ortg_2.txt","r")
    r_ortg2=r_ortg_2.readlines()
    r_ortg_2.close()
    r_ortg_3=open("respuestas_ortg_3.txt","r")
    r_ortg3=r_ortg_3.readlines()
    r_ortg_3.close()
    r_ortg_4=open("respuestas_ortg_4.txt","r")
    r_ortg4=r_ortg_4.readlines()
    r_ortg_4.close()
    r_ortg_5=open("respuestas_ortg_5.txt","r")
    r_ortg5=r_ortg_5.readlines()
    r_ortg_5.close()
    r_ortg_6=open("respuestas_ortg_6.txt","r")
    r_ortg6=r_ortg_6.readlines()
    r_ortg_6.close()
    no=3
    
    p_gra=["1. Sam esta a punto de tener a su      hijo.","2. Ella fue la        en llegar a la cita","3. Estamos en el       piso.","4. Es: aguda, grave o esdrújula: camión.","5. Es: aguda, grave o esdrújula: equipo.","6. Es: aguda, grave o esdrújula: semilla","7. Es: aguda, grave o esdrújula: sábado.","7. Ingresa la palabra en el tiempo gramátical que corresponda:\nPlaneo       con la organización del evento de graduación.","8. Ingresa la palabra en el tiempo gramátical que corresponda:\nMariana y Lily       examen de matemáticas la semana pasada.","9. Ingresa la palabra en el tiempo gramátical que corresponda:\nHe ido a visitarte todas las noches y tu mamá me ha       que llego muy tarde por que siempre te duermes temprano."]
    r_gra_correcta=[2,1,1,1,2,2,3,1,2,3]
    r_gra_1=open("respuestas_gra.txt","r")
    r_gra=r_gra_1.readlines()
    r_gra_1.close()
    r_gra_2=open("respuestas_gra2.txt","r")
    r_gra2=r_gra_2.readlines()
    r_gra_2.close()
    r_gra_3=open("respuestas_gra3.txt","r")
    r_gra3=r_gra_3.readlines()
    r_gra_3.close()
    r_gra_4=open("respuestas_gra4.txt","r")
    r_gra4=r_gra_4.readlines()
    r_gra_4.close()
    r_gra_5=open("respuestas_gra5.txt","r")
    r_gra5=r_gra_5.readlines()
    r_gra_5.close()
    r_gra_6=open("respuestas_gra6.txt","r")
    r_gra6=r_gra_6.readlines()
    r_gra_6.close()
    r_gra_7=open("respuestas_gra7.txt","r")
    r_gra7=r_gra_7.readlines()
    r_gra_7.close()
    r_gra_8=open("respuestas_gra8.txt","r")
    r_gra8=r_gra_8.readlines()
    r_gra_8.close()
    r_gra_9=open("respuestas_gra9.txt","r")
    r_gra9=r_gra_9.readlines()
    r_gra_9.close()
    ng=3
    
    p_lec=["1. ¿Cómo se describe a los duendes en este cuento?","2. ¿Cómo era la situación de los zapateros?","3. ¿Cómo notaron los zapateros quién los ayudó?","4. ¿Por qué la esposa del zapatero les hizo ropa a los duendes?","5. ¿De qué manera beneficiaron los duendes a la pareja?","6. Con base a las acciones de los duendes podemos inferir que sus intenciones eran:"]
    r_lec_correcta=[2,1,2,1,3,3]
    r_lec_1=open("respuestas_lec.txt","r")
    r_lec=r_lec_1.readlines()
    r_lec_1.close()
    r_lec_2=open("respuestas_lec2.txt","r")
    r_lec2=r_lec_2.readlines()
    r_lec_2.close()
    r_lec_3=open("respuestas_lec3.txt","r")
    r_lec3=r_lec_3.readlines()
    r_lec_3.close()
    r_lec_4=open("respuestas_lec4.txt","r")
    r_lec4=r_lec_4.readlines()
    r_lec_4.close()
    r_lec_5=open("respuestas_lec5.txt","r")
    r_lec5=r_lec_5.readlines()
    r_lec_5.close()
    r_lec_6=open("respuestas_lec6.txt","r")
    r_lec6=r_lec_6.readlines()
    r_lec_6.close()
    nl=3
    #funciones de cada test, funcionan similar pero fueron modificadas en base al número de preguntas, ajustando los nombres de las variables
    def ortografia(p,r,rc,n,nick):
        print("Bienvenido",nick+", deberás contestar correctamente",n,"de las 6 preguntas para poder acceder a la app seleccionada.")
        time.sleep(2.5)
        print(dibujo_vidas[0])
        print("Contarás con solo 3 vidas para pasar todo el test.\n¡Mucho éxito!\n")
        time.sleep(3)
        i_ortg=open("instrucciones_orgt.txt","r")
        print(i_ortg.read())
        i_ortg.close()
        time.sleep(7)
        n_p=6
        vidas=3
        acertadas=0
        while True:
            for i in range(n_p):
                print(p_ortg[i]+"\n")
                if i==0:
                    for j in range (len(r_ortg)):
                        print(r_ortg[j])
                elif i==1:
                    for k in range (len(r_ortg2)):
                        print(r_ortg2[k])
                elif i==2:
                    for z in range(len(r_ortg3)):
                        print(r_ortg3[z])
                elif i==3:
                    for y in range(len(r_ortg4)):
                        print(r_ortg4[y])
                elif i==4:
                    for w in range(len(r_ortg5)):
                        print(r_ortg5[w])
                elif i==5:
                    for q in range(len(r_ortg6)):
                        print(r_ortg6[q])
                        
                r_inicial=int(input("\nEscoge la respuesta correcta "))
                if r_inicial==rc[i]:
                    print("Respuesta correcta!! Felicidades, vamos a la que sigue!\n")
                    acertadas=acertadas+1
                    time.sleep(2)
                else:
                    vidas=vidas-1
                    if vidas==0:
                        print("Te has quedado sin vidas ∩(︶▽︶)∩")
                        if acertadas>=n:
                            print("¡Aprobaste! Muchas felicidades",nick,"diviértete mucho y estudia mucho\nNos vemos (◕‿-)")
                            return acertadas
                        else:
                            print("Estudia e inténtalo de nuevo, ¡ánimo!")
                            return acertadas
                    else:
                        print("\nRespuesta incorrecta, te quedan:",str(vidas),"vidas, ¡intenta de nuevo!\n")
                        print(dibujo_vidas[3-vidas])
                        time.sleep(3)
                    
            if i==5:
                print("Terminaste todo el test, ¡felicidades!",nick)
                return acertadas
            
    def gramatica(p,r,rc,ng,nick):
        print("Bienvenido",nick+", deberás contestar correctamente",ng,"de las 6 preguntas para poder acceder a la app seleccionada.")
        time.sleep(2.5)
        print(dibujo_vidas[0])
        print("Contarás con solo 3 vidas para pasar todo el test.\n¡Mucho éxito!\n")
        time.sleep(3)
        n_p=6
        vidas=3
        acertadas=0
        while True:
            for i in range(n_p):
                print(p_gra[i]+"\n")
                if i==0:
                    for j in range (len(r_gra)):
                        print(r_gra[j])
                elif i==1:
                    for k in range (len(r_gra2)):
                        print(r_gra2[k])
                elif i==2:
                    for z in range(len(r_gra3)):
                        print(r_gra3[z])
                elif i==3:
                    for y in range(len(r_gra4)):
                        print(r_gra4[y])
                elif i==4:
                    for w in range(len(r_gra5)):
                        print(r_gra5[w])
                elif i==5:
                    for q in range(len(r_gra6)):
                        print(r_gra6[q])
                elif i==6:
                    for s in range(len(r_gra7)):
                        print(r_gra7[s])
                elif i==7:
                    for t in range(len(r_gra8)):
                        print(r_gra8[t])
                elif i==8:
                    for h in range(len(r_gra9)):
                        print(r_gra9[h])
                        
                r_inicial=int(input("\nEscoge la respuesta correcta "))
                if r_inicial==rc[i]:
                    print("Respuesta correcta!! Felicidades, vamos a la que sigue!\n")
                    acertadas=acertadas+1
                    time.sleep(2)
                else:
                    vidas=vidas-1
                    if vidas==0:
                        print("Te has quedado sin vidas ∩(︶▽︶)∩")
                        if acertadas>=n:
                            print("¡Aprobaste! Muchas felicidades",nick,"diviértete mucho y estudia mucho\nNos vemos (◕‿-)")
                            return acertadas
                        else:
                            print("Estudia e inténtalo de nuevo, ¡ánimo!")
                            return acertadas
                    else:
                        print("\nRespuesta incorrecta, te quedan:",str(vidas),"vidas, ¡intenta de nuevo!\n")
                        print(dibujo_vidas[3-vidas])
                        time.sleep(3)
                    
            if i==8:
                print("Terminaste todo el test, ¡felicidades!",nick)
                return acertadas
                    
    def lectura(p,r,rc,nl,nick):
        print("Bienvenido",nick+", deberás contestar correctamente",nl,"de las 6 preguntas para poder acceder a la app seleccionada.")
        time.sleep(2.5)
        print(dibujo_vidas[0])
        print("Contarás con solo 3 vidas para pasar todo el test.\n¡Mucho éxito!\n")
        time.sleep(3)
        i_lec=open("lectura.txt","r")
        print(i_lec.read())
        i_lec.close()
        time.sleep(7)
        n_p=6
        vidas=3
        acertadas=0
        while True:
            for i in range(n_p):
                print(p_lec[i]+"\n")
                if i==0:
                    for j in range (len(r_lec)):
                        print(r_lec[j])
                elif i==1:
                    for k in range (len(r_lec2)):
                        print(r_lec2[k])
                elif i==2:
                    for z in range(len(r_lec3)):
                        print(r_lec3[z])
                elif i==3:
                    for y in range(len(r_lec4)):
                        print(r_lec4[y])
                elif i==4:
                    for w in range(len(r_lec5)):
                        print(r_lec5[w])
                elif i==5:
                    for q in range(len(r_lec6)):
                        print(r_lec6[q])
                
                r_inicial=int(input("\nEscoge la respuesta correcta "))
                if r_inicial==rc[i]:
                    print("Respuesta correcta!! Felicidades, vamos a la que sigue!\n")
                    acertadas=acertadas+1
                    time.sleep(2)
                else:
                    vidas=vidas-1
                    if vidas==0:
                        print("Te has quedado sin vidas ∩(︶▽︶)∩")
                        if acertadas>=n:
                            print("¡Aprobaste! Muchas felicidades",nick,"diviértete mucho y estudia mucho\nNos vemos (◕‿-)")
                            return acertadas
                        else:
                            print("Estudia e inténtalo de nuevo, ¡ánimo!")
                            return acertadas
                    else:
                        print("\nRespuesta incorrecta, te quedan:",str(vidas),"vidas, ¡intenta de nuevo!\n")
                        print(dibujo_vidas[3-vidas])
                        time.sleep(3)
                    
            if i==5:
                print("Terminaste todo el test, ¡felicidades!",nick)
                return acertadas
    #sección de la función jugar donde se decide el test a aplicar en base a si la aplicación está o no bloqueada
    if a in ab:
        print("\tEsta app está restringida",nick+", a continuación se\ndesplegará un test y una vez respondido, podrás continuar en la app")
        test=random.choice(lista_test)
        if test=="Ortografía":
           print("Se ha escogido el test de ortografía")
           time.sleep(2)
           if ortografia(p_ortg,r_ortg,r_ortg_correcta,no,nick)>=no:
               print("Muchas muchas felicidades",nick,"aprobaste, espero te diviertas mucho, recuerda cuidar tu vista.\nNos vemos (◕‿-)")
               no=no+1
           else:
               print("Lo siento",nick+", no aprobaste, Estudia esta retroalimentación e inténtalo de nuevo, ¡ánimo!")
               retro_ortg=open("retroalimentación ortografia.txt","r")
               print(retro_ortg.read())
               retro_ortg.close()
        elif test=="Gramática":
            print("Se ha escogido el test de gramática")
            time.sleep(2)
            if gramatica(p_gra,r_gra,r_gra_correcta,ng,nick)>=ng:
                print("Muchas muchas felicidades",nick,"aprobaste, espero te diviertas mucho, recuerda cuidar tu vista.\nNos vemos (◕‿-)")
                ng=ng+1
            else:
                print("Lo siento",nick+", no aprobaste, Estudia esta retroalimentación e inténtalo de nuevo, ¡ánimo!")
                retro_gra=open("retroalimentación gramática.txt","r")
                print(retro_gra.read())
                retro_gra.close()
        elif test=="Lectura":
            print("Se ha escogido el test de lectura")
            time.sleep(2)
            if lectura(p_lec,r_lec,r_lec_correcta,ng,nick)>=nl:
                print("Muchas muchas felicidades",nick,"aprobaste, espero te diviertas mucho, recuerda cuidar tu vista.\nNos vemos (◕‿-)")
                nl=nl+1
            else:
                print("Lo siento",nick+", no aprobaste, Estudia esta retroalimentación e inténtalo de nuevo, ¡ánimo!")
                retro_lec=open("Retroalimentación comprensión lectora.txt","r")
                print(retro_lec.read())
                retro_lec.close()
    elif a in au:
        print("Parece que",a,"no está restringida, disfruta un buen rato y recuerda estudiar a menudo",nick+"(◕‿-)")
       
#función para la opción de agregar, agrega la app a la lista de apps del launcher y a la lista de apps restringidas        
def agregar(a,la,ab,au):
    if a in la:
        print(a,"fue restringida correctamente")
    la.append(a)
    ab.append(a)
    if a in au:
        au.remove(a)
    else:
        print(a,"ha sido agregada correctamente al launcher y a la lista de apps restringidas")
#función eliminar, para sacar una app de la lista de apps restringidas y dejarla en la de apps libres, pero la mantiene dentro del launcher    
def eliminar(a,la,ab,au):
    au.append(a)
    ab.remove(a)
    print("Su app fue exitosamente retirada de la lista de apps restringidas")
#función añadir, que permite añadir apps al launcher sin restringirlas, es decir, las deja en la lista apps_unlocked o apps libres
def añadir(a,la,au):
    au.append(a)
    la.append(a)
    print("Su app fue añadida correctamente sin restricción inmediata al launcher")
#función suprimir, para borrar una app completamente del launcher, independientemente si está bloqueada o no
def suprimir(a,la,ab,au):
    la.remove(a)
    if a in ab:
        ab.remove(a)
    elif a in au:
        au.remove(a)
    print(a,"fue removida con éxito del launcher")
#menú de inicio    
print("\t𝔹𝕀𝔼ℕ𝕍𝔼ℕ𝕀𝔻𝕆 𝔸 𝕃𝔼 𝔾𝔸𝕄𝕀ℕ𝔾")
option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')

apps_blocked=[] #lista de apps restringidas
apps_unlocked=[]  #lista de apps no restringidas o libres
apps=[]  #lista de apps dentro del launcer
while True:
    if option1.lower()=="jugar": #si el usuario teclea "jugar" sin importar las mayúsculas, operará la función jugar
        print("Selecciona una de tus apps",nick)
        option2=input()
        option2_real=option2.lower()
        if option2_real in apps:
            jugar(option2_real,apps,apps_blocked,apps_unlocked,nick)
            frase_hoy=random.choice(random_frases)
            print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?(◕_◕)")
            option1=input()
        else:
            print("No se encuentra esa app, asegúrate de haberla añadido")  #opción en caso de que la app no esté en el launcher
            option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')
        
    elif option1.lower()=="agregar":   #si el usuario teclea "agregar" sin importar las mayúsculas, operará la función agregar
        option3=input("Escribe el nombre de la app a agregar\n")
        option3_real=option3.lower()
        if option3_real in apps_blocked:
            print("Esa app ya está restringida",nick) #en caso de que la app ya esté restringida, el programa infiere que ya está en el launcher también, por tanto, despliega este texto
            option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')
        else:
            agregar(option3_real,apps,apps_blocked,apps_unlocked)
            frase_hoy=random.choice(random_frases)
            print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?∩(︶▽︶)∩")
            option1=input()
    elif option1.lower()=="eliminar":  #si el usuario teclea "eliminar" sin importar las mayúsculas, operará la función eliminar
        option4=input("Escribe el nombre de la app a eliminar\n")
        option4_real=option4.lower()
        if option4_real in apps_blocked:
            eliminar(option4_real,apps,apps_blocked,apps_unlocked)
            frase_hoy=random.choice(random_frases)
            print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?∩(︶▽︶)∩")
            option1=input()
        else:
            print("Esa app aún no está en el launcher o no está restringida")  #en caso que la app no esté en el launcher o sí esté pero no restringida, el programa imprimirá esto
            option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')
    elif option1.lower()=="añadir":  #si el usuario teclea "añadir" sin importar las mayúsculas, operará la función añadir
        option5=input("Escribe el nombre de la app para añadirla al launcher\n")
        option5_real=option5.lower()
        if option5_real in apps:
            print("Esa app ya está en el launcher")  #en dado caso que la app ya esté en alguna lista, el programa lo dirá
            option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')
        else:
            añadir(option5_real,apps,apps_unlocked)
            frase_hoy=random.choice(random_frases)
            print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?∩(︶▽︶)∩")
            option1=input()
    elif option1.lower()=="suprimir":  #si el usuario teclea "suprimir" sin importar las mayúsculas, operará la función suprimir
        option6=input("Escribe el nombre de la app para suprimirla del launcher\n")
        option6_real=option6.lower()
        if option6_real in apps:
            suprimir(option6_real,apps,apps_blocked,apps_unlocked)
            frase_hoy=random.choice(random_frases)
            print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?∩(︶▽︶)∩")
            option1=input()
        else:
            print("No se encuentra esa app en el launcher")  #si nunca se añadió la app tecleada, se detectará y notificará
            option1=input('''
------██۞█████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃
   ▂▄▅█████████▅▄▃▂ 
   ██████████████].¿Qué quieres hacer hoy?
   ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..''')
    elif option1.lower()=="consultar":  ##si el usuario teclea "consultar" sin importar las mayúsculas, imprimirá todas las apps en forma de lista, en dado caso que olvidase cómo añadió alguna
        print("Estas son las aplicaciones que se encuentran en el launcher")
        for i in range(len(apps)):
            print(apps[i])
        frase_hoy=random.choice(random_frases)
        print(frase_hoy,"\nEn fin, ¿Qué quieres hacer hoy?∩(︶▽︶)∩")
        option1=input()
    elif option1.lower()=="salir":  #cierra el programa por completo, rompiendo el while true y despidiendo al usuario
        print("Recuerda seguir estudiando, hoy eres la mejor versión de ti, mañana serás una mejor versión que hoy...\nHasta pronto!(◕‿-)")
        break
    else:  #para en dado caso que el usuario introduzca alguna opción inexistente, el programa le recordará las que tiene disponibles
        option1=input("(╯°□°)--︻╦╤─ - - -\n\t¡Esa opción no existe! Prueba de nuevo\nPro tip: recuerda que tus opciones son: Jugar, agregar, añadir, eliminar, suprimir, consultar o salir\n")
