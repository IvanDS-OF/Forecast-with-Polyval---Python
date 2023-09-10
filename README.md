# Forecast-with-Polyfit---Python
This code pretends to obtain a simple forecast with Polyval function - PYTHON
Este es un código que pretende obtener un pronóstico simple usando la función Polyval en Python. 

## Pronóstico / Forecast
El pronóstico es una previsión de eventos futuros del comportamiento de un sistema en base a datos pasados comprobables registrados. Podemos encontrar un ejemplo sencillo del pronóstico en las noticias a la hora de las presentaciones del clima, en donde se presenta un pronóstico del tiempo. 


## Polyfit
Polyfit es una función de ls librería de **numpy** y la podemos mandar a llamar de la siguente manera: 

```
import numyp as np
np.polyval(x, y, grado)
```
Los argumentos que son obligatorios introducir son:

x == array : Representa los valores en el eje de las X, en caso de ser aplicado a una serie temporal podemos poner al vector de tiempo.
y == array : Representa los valores del eje de las y's, en caso de ser aplicado a una serie temporal podemos poner al vector de la información
grado == int 

Recordemos de forma rápida la ecuación de la función polyval, lo que la función hace es minimizar el error cuadrado mediante la siguiente ecuación:


$$ E = \sum_{j=0}^k [p (x_j) - y]^2 $$

De igual forma podemos encontrar más información [en el siguiente link](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) que pertenece a la documentación oficial de la librería. 


## Código / Code
El código genera un pronóstico usando la función polyval, al mismo tiempo que la base de datos es posible que el usuario la llene en tiempo real introduciendo valores desde la terminal. 

Primero es necesario importar las librerías necesarias para el funcionamiento del programa como son: 

```
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import time
```
Posteriormente creamos dos vectores vacíos con valores flotantes usando la forma de _list cmoprehension_

Luego inicializamos la figura en donde vamos a plotear la figura e inicializamos tanto una variable que será iterada de forma infinita y un ciclo **while True**.

Dentro del ciclo infinito podemos encontrar que primero vamos a fijar los ejes superiores e inferiores para mayor estabilidad la animación y al mismo tiempo colocamos una instrucción para que los ejes laterales se vayan actualizando cada que se agregue un nuevo valor a la lista.


> Nota: Los valores no son almacenados en ninguna base de datos, solamente serán visibles y utilizados en cada iteración del programa. 

Después de fijar los ejes correspondientes, creamos un vector de tiempo que nos servirá para poder plotear correctamente la figura completa en los últimos 20 espacios. 

Luego creamos la variable llamada **coef** que utilizará el método **polyfit** de la librería **numpy** y que nos entregará a la slida una lista de dos valores. 


Posteriormente, se crea un ciclo for que nos servirá para poder aplicar la función que nos dará un pronóstico aproximado dado el comportamiento de los últimos 20 datos registrados (que igual son los que se muestran en la gráfica).

Se tiene que realizar en un ciclo for ya que el método polyval de numpy solamente evalua con un argumento unitario y nos devuelve igual un valor unitario. 

Luego creamos una lista llamada **vector_pronostico** que se irá actualizando cada iteración. Esta lista nos ayudará para ubicar de mejor manera al vector que nos arroja la predicción.

Finalmente, mandamos a plotear todos los datos, usando la sintaxis que se definió previamente con la definición de la figura. Los datos mostrados son los siguientes: 

```
Medición -> Azul
Pronóstico -> Rojo
```

Después del ploteo inicial, le pedimos al usuario ingresar un valor para ser tomado como un valor más de la medición.

Al final, mandamos a limpiar tanto nuestro vector de predicción como nuestra figura con la función **cla()** de matplotlib 



## Simulación / Simulation

La simulación inicia cuando el programa es ejecutado. De primera instancia podemos ver que se abre una figura de matplotlib que muestra los valores iniciales en 0 de la medición al igual que muestra los valores de la predicción que igual son 9. También se le pide al usuario que ingrese un valor flotante desde la terminal. 

Una vez sea ingresado este valor flotante desde la terminar, la gráfica se actualizará mostrando el valor que fue introducido dentro del apartado de las mediciones y también se actualizan los valores de la predicción que tienen un comportamiento de tendencia final al comportamiento actual de los datos de medición.




Gracias :D