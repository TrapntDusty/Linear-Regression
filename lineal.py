#EL IDE ES VISUAL STUDIO CODE 
#en este ejemplo usamos una data de dos columbas de experiencia y salario


#Primero importamos las librerias para el analisis
#Numpy para las calculaciones matematicas
import numpy as np
#Pandas para almacenar y manipular los datos del csv 
import pandas as pd
#matplot para graficar todos los datos
import matplotlib.pyplot as plt


#Cargamos el excel y asignamos en X la columna llamada Experiencia y en Y Salario 
#para este ejemplo usaremos a X para predecir a Y asi que la variable dependiente sera la Y y la independiente la X
data = pd.read_csv('Datos_Empleo.csv')
x = data['Experiencia']
y = data['Salario']
#Imprimimos una vista de los datos para ver la informacion que este correcta, lo cual solo nos mostrara las primeras filas
print(data.head())

#Para evitar intentar adivinar la pendiente e interseccion de la regresional usaremos las formula generales para encontrar la pendiente e inteseccion 
def linear_regression(x, y):   
    #usamos la funcion len para conseguir el numero de observaciones en los dato y ponerlo en la variable N, luego calculamos la mean de x y Y con su propia funcion
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()
    #Claculamos la pendiente , para acortar la longitud primero calculamos numeroados y denominador de la formula de la pendiente
    #luego dividimos el numerador por el denominador y asignamos a una variable llamada B1
    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean)**2).sum()
    B1 = B1_num / B1_den
    #ahora que tenemos la pendiente usamos la formula para la interseccion 
    B0 = y_mean - (B1*x_mean)
    #aqui ponemos el formato en como estara la variable reg_line siendo y = interseccion + pendiente redondeada por 3 decimales
    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))
    #Regresamos la pendiente , la interseccion y la variable reg_line
    return (B0, B1, reg_line)


#calculamos que tan bien se ajusta la linea de regresion, para determinarlo calculamos el coeficiente de correlacion, conocido como R y el de Determinacion como R^2
#R^2 o coeficiente de determinacion es el porcentaje de varianza explicado por la variable independiente con valor entre 0 y 1 
#por ejemplo si r^2 = .82 indica que x explica el 81% de la varianza de y , tambien conocida como la bondad de ajuste
#R o coeficiente de correlacion es el glado de relacion entre dos variables, puede variar de -1 a 1 con valores iguales a 1 , que significan correlacion psotivia o negativa
#para usar la formula de coeficiente de correlacion tendremos que almacenar el numero de observaciones ( filas en datos ) en la variable N de nuevo, a continuacion
#dividimos la formula de correlacion en 2 ,denominador y numerador , y asi devolveremos el coeficiente de correlacion
def corr_coef(x, y):
    N = len(x)
    
    num = (N * (x*y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x**2).sum() - x.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    return R


#A los balores B0 B1 y Reg_line le damos lo que conseguimos de la funcion lineal_regression con datos X y Y 
B0, B1, reg_line = linear_regression(x, y)
#Imprimimos la regresion Lineal
print('Regresion Lineal: ', reg_line)
#Almacenamos en R el coeficiente de correlacion que sacamos de la funcion con los datos X y Y
R = corr_coef(x, y)
#Imprimimos cual es el coeficiente de correlacion y la bondad de ajuste con el dato de R y R^2
print('coeficiente de correlacion: ', R)
print('"bondad de ajuste": ', R**2)

#Finalmente graficamos los datos usando PLT 
plt.figure(figsize=(12,5))
plt.scatter(x, y, s=300, linewidths=1, edgecolor='black')
text = '''X Significa: {} Años
Y Significa: ${}
R: {}
R^2: {}
y = {} + {}X'''.format(round(x.mean(), 2), 
                       round(y.mean(), 2), 
                       round(R, 4), 
                       round(R**2, 4),
                       round(B0, 3),
                       round(B1, 3)) # el texto muestra que significa cada dato redondeado 
plt.text(x=1, y=100000, s=text, fontsize=12, bbox={'facecolor': 'grey', 'alpha': 0.2, 'pad': 10})
plt.title('Como la Experiencia Afecta el salario')
plt.xlabel('Años de Experiencia', fontsize=15)
plt.ylabel('Salario', fontsize=15)
plt.plot(x, B0 + B1*x, c = 'r', linewidth=5, alpha=.5, solid_capstyle='round')
plt.scatter(x=x.mean(), y=y.mean(), marker='*', s=10**2.5, c='r') # punto medio
plt.show()