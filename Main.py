from MaquinaExpendedora import maquina, reporte_productos, comprar_producto, reporte_dinero, cantidades_dinero, agregar_dinero, dinero_total, retirar_dinero, agregar_producto;

salida = True;
admin = "administrador";
password = "12345";
maquina();

while salida:
    print("\n---------- Bienvenido a la Maquina Expendedora ----------");
    print("\nPor favor ingrese el numero correspondiente a la opcción:\n");
    print("1• Comprar");
    print("2• Aministrador");
    print("3• Ver productos");
    print("4• Salir");
    
    try: 
        
        eleccion = int(input("\nIngresa el numero de tu elección: "));
        
        if eleccion == 1:
            
            print("\n--------- Productos Disponibles ---------\n");
            reporte_productos();
            
            dinero = int(input("\nIngrese el Dinero: "));
            producto = int(input("Id del producto: "));
            comprar_producto(dinero, producto);
                
        elif eleccion == 2:
            
            print("\n-------- Administrador -------\n");
            salida_admin = True;
            user = input("Ingrese el usuario: ");
            
            if user == admin:
                contra = input("Ingrese la contraseña: ");
                if contra == password:
                    
                    while salida_admin:
                        print("\n------- Bienvenido de Vuelta Admin -------\n");
                        print("1) Introducir Dinero a la Maquina");
                        print("2) Agregar Productos");
                        print("3) Retirar Dinero de la Maquina");
                        print("4) Reporte de Productos");
                        print("5) Reporte del Dinero Disponible");
                        print("6) Salir del administrador");

                        
                        eleccion_admin = int(input("\nIngresa el numero de tu elección: "));
                        
                        if eleccion_admin == 1:
                            print("\n----- Ingreso de Dinero a la maquina  -----\n");
                            cantidades = [];
                            
                            for i in range(9):
                                cantidad = int(input(f"Ingresa la cantidad de Billetes/Monedas de {cantidades_dinero[i]} pesos: "));
                                cantidades.append(cantidad);
                            
                            agregar_dinero(cantidades);
                            print(f"Ahora hay {dinero_total()} pesos en la Maquina =D");
                            
                            
                        elif eleccion_admin == 2:
                            lista_produc = [];
                            print("------- Agregar Producto ------");
                            nombre = str(input("Ingresa el nombre del producto: "));
                            precio = int(input("Precio del producto: "));
                            cantidad = int(input("Ingrese la cantidad de unidades del producto: "));
                            agregar_producto(nombre,precio,cantidad);
                            
                        elif eleccion_admin == 3:
                            print("\n------ Retirar dinero de la Maquina ------\n");
                            cantida = int(input("Ingrese el valor que desea retirar de la maquina: "));
                            print(f"\n------ Dinero Retirado ------\n");
                            retirar_dinero(cantida);
                            
                            
                        elif eleccion_admin == 4:
                            print("\n-------- Reporte de los Productos Disponibles --------\n");
                            reporte_productos();
                            
                        elif eleccion_admin == 5:
                            print("\n-------- Reporte del Dinero Disponible en la Maquina --------\n");
                            reporte_dinero();
                            
                            
                        elif eleccion_admin == 6:
                            print("\nHasta la proxima Admin :D\n");
                            salida_admin = False;
                            
                        else:
                            print("Por favor ingresa un entero!");
                    
                else:
                    print("\nContraseña incorrecta pri :(\n");
            else:
                print("\nUsuario incorrecto pri :(\n");
            
        elif eleccion == 3:
            
            print("\n--------- Productos disponibles en la máquina ---------\n");
            reporte_productos();
            
        elif eleccion == 4:
            
            print("\nQue tengas un buen dia!");
            salida = False;

        elif 1 > eleccion > 4 :
            
            print("Por favor ingrese un numero disponible! :D");
            
    except ValueError:
        print("Por favor ingresa un entero!");