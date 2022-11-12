#-----------librerias----------------
import os

#--------------------variables---------------------------
#vector para almacenar los usuarios Organizadores
vectorOrganizadores=[]

#----------------------Funciones-----------------------
def llenarVecOrganizadores():
    #este metodo llena el vector de organizadores con los usuarios que estan en el archivo usersOrga.txt
    #siempre y cuando el archivo exista
    #si existe entonces se abre el archivo y se lee linea por linea y se guarda en el vector
    if os.path.exists("usersOrga.txt"):
        file=open("usersOrga.txt","r")
        for linea in file:
            vectorOrganizadores.append(linea.strip())
        file.close()
    
def gestionUsuarios():
    #---se piden los datos para crear usuario---
    print("COMPLETE LO SOLICITADO PARA REGISTRAR UN USUARIO 👤: ")
    nomCom=input("Nombre completo👤 : ")
    mail=input("Correo electrónico 📧:  ")
    username=input("Nombre de usuario: ")
    
    #username no puede tener mas de 10 caracteres
    while len(username)>10:
        print("El nombre de usuario no puede tener mas de 10 caracteres")
        username=input("Nombre de usuario: ")
    rol=int(input("Rol: 1=Asesor ||  2=Organizador: "))
    
    if(rol==1):#----Si el rol que se digita es 1, entonces se le asigna el rol de asesor
        
        rol="Asesor"
        #---guardar en archivo
        file=open("usuariosAsesor.txt","a") #"a" escribir sin borrar
        file.write("Nombre: "+nomCom+" || Correo: "+mail+" || Username: "+username+" || Rol: "+rol+"\n")#se guarda en el archivo
        file.close()#se cierra el archivo
    else:#----Si el rol que se digita es 2, entonces se le asigna el rol de organizador
        
        rol="Organizador"
        file=open("usuariosOrganizador.txt","a") #"a" escribir sin borrar
        file.write("Nombre: "+nomCom+" || Correo: "+mail+" || Username: "+username+" || Rol: "+rol+"\n")#---guardar en archivo
        file.close()#se cierra el archivo
        
        ##---se guarda en eltxt  de organizadores
        file=open("usersOrga.txt","a") #"a" escribir sin borrar
        file.write(username+"\n "  )#---guardar en archivo
        file.close()#se cierra el archivo
        
    print("Usuario tipo: "+rol+", registrado con éxito 👍")
    
def moduloServicios():
    op=0
    while op!=5:
        print("Bienvenido al módulo de servicios 📚 \n1.Servicios Food Truck🚚 \n2.Parrillada\n3.Eventos\n5.Salir\n")
        op=int(input("Digite una opción: "))
        ##--Servicios food truck--
        if op==1: 
            print("-----Servicios Food Truck🚚-----\nDigite lo solicitado: \n")
            #--ingreso de datos
            nombreContacto=input("Nombre completo del contacto: ")
            while len(nombreContacto)<30:
                print("El nombre del contacto no puede tener menos de 30 caracteres")
                nombreContacto=input("Nombre completo del contacto: ")
            
            numeroContacto=input("Número de contacto: ")
            while len(numeroContacto)!=8 and numeroContacto.isdigit()==False:
                print("El número de contacto debe tener 10 dígitos")
                numeroContacto=input("Número de contacto: ")

            mailContacto=input("Correo de contacto: ")
            fechaEvento=input("Fecha del evento  'dd/mm/aaaa:' ")
            direccionEvento=input("Dirección del evento: ")
            horaEvento=input("Hora del evento:  hh:mm am\pm")
            #--guardar en archivo
            file=open("serviciosFoodTruck.txt","a") #"a" escribir sin borrar
            file.write("Nombre del contacto: "+nombreContacto+"\nNúmero de contacto: "+numeroContacto+"\nCorreo de contacto: "+mailContacto+" \nFecha del evento: "+fechaEvento+"\nDirección del evento: "+direccionEvento+"\nHora del evento: "+horaEvento+"\n--------------\n")#se guarda en el archivo
            file.close()#se cierra el archivo
            print ("Servicio solicitado con éxito 👍")
        #--fin servicios food truck--
        ##--Servicio parrillada--
        elif op==2: 
            print("------Servicios Parrillada🍗-------\nDigite lo solicitado: \n")
            #--ingreso de datos
            nombreContacto=input("Nombre completo del contacto: ")
            while len(nombreContacto)<30:
                print("El nombre del contacto no puede tener menos de 30 caracteres")
                nombreContacto=input("Nombre completo del contacto: ")
            
            numeroContacto=input("Número de contacto: ")
            while len(numeroContacto)!=8 and numeroContacto.isdigit()==False:
                print("El número de contacto debe tener 10 dígitos")
                numeroContacto=input("Número de contacto: ")
            
            mailContacto=input("Correo de contacto: ")
            fechaEvento=input("Fecha del evento  'dd/mm/aaaa:' ")
            direccionEvento=input("Dirección del evento: ")
            cantidadPersonas=int(input("Digite la Cantidad de personas: "))
            #no acepta numeros negativos
            while cantidadPersonas < 0:
                print("La cantidad de personas no puede ser negativa")
                cantidadPersonas=int(input("Digite la Cantidad de personas: "))
            #--calculos de costos--
            totalBruto=(cantidadPersonas*3200)
            iva=totalBruto*0.13
            totalNeto=totalBruto+iva
            #--guardar en archivo
            file=open("serviciosParrillada.txt","a")
            file.write("Nombre del contacto: "+nombreContacto+"\nNúmero de contacto: "+numeroContacto+"\nCorreo de contacto: "+mailContacto+" \nFecha del evento: "+fechaEvento+"\nDirección del evento: "+direccionEvento+"\nCantidad de personas: "+str(cantidadPersonas)+"\nTotal a pagar: "+str(totalNeto)+"\n--------------\n")#se guarda en el archivo
            file.close()#se cierra el archivo
            print ("Servicio solicitado con éxito 👍")
        #--fin servicio parrillada--
        ##--Servicios eventos--
        elif op==3: 
            print("------Bienvenido al modulo de Eventos\n")
            op=0
            while op!=5:
                op=int(input("Digite una opción: \n1.Bodas \n2.Otros(Organizacionales): \n5.Salir \n"))
                ##--Servicios bodas--
                if op==1:
                    print("------Servicios Bodas👰🤵-------\nDigite lo solicitado: \n")
                    #--se solicitas datos
                    nombreContacto=input("Nombre completo del contacto: ")
                    while len(nombreContacto)<30:
                        print("El nombre del contacto no puede tener menos de 30 caracteres")
                        nombreContacto=input("Nombre completo del contacto: ")
                    
                    numeroContacto=input("Número de contacto: ")
                    while len(numeroContacto)!=8 and numeroContacto.isdigit()==False:
                        print("El número de contacto debe tener 10 dígitos")
                        numeroContacto=input("Número de contacto: ")
                    mailContacto=input("Correo de contacto: ")
                    
                    #---calculos 
                    cantidadAdultos=int(input("Digite la Cantidad de adultos: "))
                    totalBrutoAdultos=(cantidadAdultos*8000)
                    totalNetoAdultos=totalBrutoAdultos*0.13
                    cantidadNinos=int(input("Digite la Cantidad de niños: "))
                    totalBrutoNinos=(cantidadNinos*4000)
                    totalNetoNinos=totalBrutoNinos*0.13
                    
                    #--guardar en archivo
                    file=open("serviciosBodas.txt","a")
                    file.write("Nombre del contacto: "+nombreContacto+"\nNúmero de contacto: "+numeroContacto+"\nCorreo de contacto: "+mailContacto+" \nCantidad de adultos: "+str(cantidadAdultos)+"\nCantidad de niños: "+str(cantidadNinos)+"\nTotal a pagar: "+str(totalNetoAdultos+totalNetoNinos)+"\n--------------\n")#se guarda en el archivo
                    file.close()#se cierra el archivo
                    
                    print ("Servicio solicitado con éxito 👍")
                #--fin servicios bodas--
                ##--Servicios otros--
                elif op==2:
                    print("------Servicios Organizacionales📝-------\nDigite lo solicitado: \n")
                    #--ingreso de datos
                    nombreContacto=input("Nombre completo del contacto: ")
                    while len(nombreContacto)<30:
                        print("El nombre del contacto no puede tener menos de 30 caracteres")
                        nombreContacto=input("Nombre completo del contacto: ")
                    
                    numeroContacto=input("Número de contacto: ")
                    while len(numeroContacto)!=8 and numeroContacto.isdigit()==False:
                        print("El número de contacto debe tener 10 dígitos")
                        numeroContacto=input("Número de contacto: ")
                    
                    mailContacto=input("Correo de contacto: ")
                    fechaEvento=input("Fecha del evento  'dd/mm/aaaa:' ")
                    direccionEvento=input("Dirección del evento: ")
                    cantidadPersonas=int(input("Digite la Cantidad de personas: "))
                    #no acepta numeros negativos
                    while cantidadPersonas < 0:
                        print("La cantidad de personas no puede ser negativa")
                        cantidadPersonas=int(input("Digite la Cantidad de personas: "))
                    nombreEmpresa=input("Nombre de la empresa: ")
                    
                    #--calculos de costos--
                    totalBruto=(cantidadPersonas*4500)
                    iva=totalBruto*0.13
                    totalNeto=totalBruto+iva
                    
                    #--guardar en archivo
                    file=open("serviciosOrganizacionales.txt","a")
                    file.write("Nombre del contacto: "+nombreContacto+"\nNúmero de contacto: "+numeroContacto+"\nCorreo de contacto: "+mailContacto+" \nFecha del evento: "+fechaEvento+"\nDirección del evento: "+direccionEvento+"\nCantidad de personas: "+str(cantidadPersonas)+"\nNombre de la empresa: "+nombreEmpresa+"\nTotal a pagar: "+str(totalNeto)+"\n--------------\n")#se guarda en el archivo
                    file.close()#se cierra el archivo
                    print ("Servicio solicitado con éxito 👍")
                #-fin servicios otros--
                elif op==5:
                    print("Saliendo del modulo de eventos...")
                else:
                    print("Opción no válida")
        #-- fin servicio eventos--
        elif op==5:## Salir
            print("Saliendo del módulo de servicios")
        else:
            print("Opción no válida")

def listaPedidos():
    llenarVecOrganizadores() ##ejecucios del metodo para ver los organizadores
    
    user=""
    while user!="salir":
        user=input("Ingrese un usuario 'Oranizador' o escriba 'salir' para salir: ")
        if user in vectorOrganizadores: ##verifica si el usuario esta en el vector de organizadores, si esta, entra al modulo de lista de pedidos
            
            op=0
            while op!=5:
                print("------Bienvenido "+user+" al modulo de lista de pedidos------\n")
                op=int(input("Digite una opción: \n1.Food Truck \n2.Parrillada \n3.Eventos \n5.Salir \n"))
                if op==1:
                    print("------Food Truck------\n")
                    #si el archivo existe, se abre y se lee linea por linea
                    if os.path.exists("serviciosFoodTruck.txt"):
                        file=open("serviciosFoodTruck.txt","r")
                        print(file.read())
                        file.close()
                    else: ## si no existe el archivo, muestra un mensaje de que no hay pedidos
                        print("No hay pedidos")
                        
                elif op==2:
                    print("------Parrillada------\n")
                    #si el archivo existe, se abre y se lee linea por linea
                    if os.path.exists("serviciosParrillada.txt"):
                        file=open("serviciosParrillada.txt","r")
                        print(file.read())
                        file.close()
                    else: ## si no existe el archivo, muestra un mensaje de que no hay pedidos
                        print("No hay pedidos")
                elif op==3:
                    print("------Eventos------\n")
                    op2=0
                    while op2!=5:
                        op2=int(input("Que desea ver? 1.Bodas \n2.Otros \n5.salir \n"))
                        if op2==1:
                            #si el archivo existe, se abre y se lee linea por linea
                            if os.path.exists("serviciosBodas.txt"):
                                file=open("serviciosBodas.txt","r")
                                print(file.read())
                                file.close()
                            else:
                                ## si no existe el archivo, muestra un mensaje de que no hay pedidos
                                print("No hay pedidos")
                        elif op2==2:
                            #si el archivo existe, se abre y se lee linea por linea
                            if os.path.exists("serviciosOrganizacionales.txt"):
                                file=open("serviciosOrganizacionales.txt","r")
                                print(file.read())
                                file.close()
                            else:
                                ## si no existe el archivo, muestra un mensaje de que no hay pedidos
                                print("No hay pedidos")
                        elif op2==5:
                            print("Saliendo del modulo de eventos...")
                        else:
                            print("Opción no válida")
        else: ## si el usuario no esta en el vector de organizadores, se le notifica que no esta registrado
            print("Usuario no encotrado o no registrado")
    #hola
    print("MODULO NO DISPONIBLE")

#---------------------------MENU PRINCIPAL---------------------
#definir variable int 
op=0

while op!=5:
    print("--------Bienvenido al sistema de Comidas 🍗---------")
    op=int (input("Digite la opcion\n1.Gestion de usuarios👤\n2.Modulo Servicios🛍️🛒\n3.Lista de pedidos🛒\n5.Salir❌\n "))
    
    if(op==1):
        gestionUsuarios()
    elif(op==2):
        moduloServicios()
    elif(op==3):
        listaPedidos()
    elif(op==5):
        print("Hasta pronto")
    else:
        print("Opcion no valida")


