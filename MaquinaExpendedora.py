productos = [];
cantidades_dinero = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100];
dinero_disp = [];
codigo = 0;
denominacion = {};
denominaciones = False;
produc = False;

#Funcion que lee el archivo de texto para realizar las acciones
def config_inicial():
    archivo = open( 'Configuracion.txt', 'r');
    lineas = archivo.readlines();
    archivo.close();
    return lineas;

#Funcion que devuelve todo el dinero del cajero
def dinero_total():
    total = 0;
    for i in range(len(dinero_disp)):
        total += dinero_disp[i]*cantidades_dinero[i];
        
    return total;

#funcion para agregar un producto a la lista de los productos que hay
def agregar_producto_archivo(string):
    datos = string.split(",");
    ultimos_datos = [int(datos[-2]), int(datos[-1])];
    lista_datos = datos[:-2] + ultimos_datos;
    productos.append(lista_datos);
    return lista_datos;

def agregar_producto(nombre, precio, cantidad):
    lista_produc = [];
    lista_produc.append(nombre);
    lista_produc.append(precio);
    lista_produc.append(cantidad);
    productos.append(lista_produc);
    print(productos);
    return print("El producto fue agregado exitosamente :D");

#Funcion que elimina el producto de la lista productos de acuerdo al codigo
#de ese respectivo producto
def eliminar_producto(codigo):
    
    for producto in productos:
        
        if producto.codigo == codigo:
            productos.remove(producto);
            break;

#Funcion para comprar el productos
def comprar_producto(monto, id):
    
    if monto >= productos[id-1][1]:
        print(f"\n---- Compraste {productos[id-1][0]} :D\n");
        monto -= productos[id-1][1];
        productos[id-1][2] -= 1;
        
    elif monto < productos[id-1][1]:
        print("\nNo tienes suficiente dinero :( \n");
        
    if monto != 0:
        print(f"------ Devuelta ------\n");
        retirar_dinero(monto);
    elif monto == 0:
        print("---- Ya no tienes dinero :( -----");
    

def agregar_dinero( list ):
    
    for i in range(len(dinero_disp)):
        dinero_disp[i] += list[i];
        
    print("\nHas Agregado el Dinero Exitosamente :D");
    

def retirar_dinero(cantidad):
    
    cambio = [];

    for denominacion in cantidades_dinero:
        
        cantidad_a_retirar = min(dinero_total(), cantidad // denominacion);
        
        if cantidad_a_retirar > 0:
            cambio.append([denominacion, cantidad_a_retirar]);
            cantidad -= cantidad_a_retirar * denominacion;
    
    for i in cambio:
        print(f"Billetes/Monedas de {i[0]} pesos: {i[1]}");
            
    if cantidad == 0:
        
        for denominacion, cantidad_en_maquina in cambio:
            
            for i in range(len(dinero_disp)):
                if cantidades_dinero[i] == denominacion:
                    dinero_disp[i] -= cantidad_en_maquina;
                    break;
    else:
        cambio = [];
    
    return cambio;


def reporte_productos():
    
    total_valor = 0;
    
    for i in range(len(productos)):

        print(f"{i+1}) Nombre: {productos[i][0]} ------ Precio: {productos[i][1]} ------ Cantidad Disponible:{productos[i][2]}");
        total_valor += productos[i][1];
        
    return print(f"\nValor total de los productos: {total_valor} pesos");


def reporte_dinero():
    
    total_valor = 0;
    
    for i in  range(len(dinero_disp)):
        print(f"- {dinero_disp[i]} billetes/monedas de {cantidades_dinero[i]} pesos");
        total_valor +=  cantidades_dinero[i] * dinero_disp[i];
        
    return print(f"\nValor total del dinero_disp: {total_valor} pesos\n");
    
    
def lista_enteros(lista):
    cantidad = int(lista.split(",")[1]);
    return cantidad;


def maquina():
    
    archivo = config_inicial();
    aux = "";
    global denominaciones;
    global produc;
    
    for i in archivo:
        
        aux = i;
        palabra = aux.split("\n")[0];
        
        if palabra == "Denominaciones":
            denominaciones = True;
            produc = False;
        elif palabra == "Productos":
            denominaciones = False;
            produc = True;
        
        if denominaciones == True:
            if palabra != "Denominaciones":
                dinero_disp.append(lista_enteros(aux));
                
        elif produc == True:
            if palabra != "Productos":
                agregar_producto_archivo(aux);
                
                
            