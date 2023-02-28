# Clases y objetos
Python soporta la programación orientada a objetos. Esto quiere decir que podemos definir entidades agrupando (encapsulando) sus atributos y comportamiento (métodos) en clases.

La definición de una clase en Python se hace de la siguiente manera:

```python
class Persona: 
	# atributos
	nombre = "Josune"
	edad = 24 
	
	# metodos
	def camina(self):
		print(self.nombre + " está caminando")
```	    

Una clase es como una plantilla o modelo para crear a partir de ella objetos. Esta plantilla contiene la información para definir cómo serán los objetos, es decir, qué atributos y métodos tendrán.

A partir de una clase se pueden crear tantos **objetos** como se desee. Los objetos de una clase se conocen como **instancias**. Cada objeto **contiene los atributos y métodos de la clase** y podrá asignar a esos atributos unos valores concretos. Esto se conoce como el **estado de un objeto**.

```python
p1 = Persona() # la variable p1 contiene un objeto de la clase Persona
p1.camina()
print(p1.nombre)  
print(p1.edad)
```


## Método especial __init__ de la clase

El método __init__ es una función especial con el objetivo de inicializar los atributos del objeto que creamos.

Implementar este método tiene varias ventajas como son:

- Es el primer método en ejecutarse al crear un objeto.
- Podemos asegurarnos de que siempre se va a llamar al crear un objeto.

Una función dentro de una clase se conoce como **método**. Las clases contienen el método especial `__init__` conocido como **constructor** y que sirve para inicializar un objeto. Al crear un objeto siempre se llama al constructor. Una diferencia importante con otros lenguajes como Java es que solo se puede definir un único constructor.

```python
class Persona:  
	def __init__(self, nombre, apellidos, edad):  
		self.nombre= nombre
		self.apellidos = apellidos 
		self.edad = edad 
	
	def camina(self):
		print(self.nombre + " está caminando")
```

En la creación del objeto es necesario indicar los argumentos del constructor:

```python
p1 = Persona("Mike", "Mendiola", 25)
p1.camina()
print(p1.nombre)  
print(p1.edad)
```

El parámetro `self` de los métodos es una referencia a la propia instancia y se utiliza para acceder a las variables que pertenecen a la clase. Si no se define un constructor, la clase hereda uno que únicamente recibe el argumento `self`.


## Método especial __str__
Al igual que podíamos convertir una variable de tipo entero, float, etc… en una de tipo string con la función str(), podemos utilizar un método en una clase para retornar un string.

## Atributos de clase vs Atributos de instancia
Los atributos definidos dentro del constructor se conocen como **atributos de instancia**, por lo tanto, los atributos definidos dentro de la clase pero fuera del constructor se conocen como **atributos de clase**.

La principal diferencia es que un atributto de clase puede ser accedido aunque no existan instancias de la clase. Además, si se modifica su valor, se modificará el valor en todas las instancias existentes de dicha clase.

```python
class Demo:
	atrib_estatico = 123 # compartido por todos los objetos
	def __init__(self,numero):
		self.atrib_instancia = numero # específico de cada objeto

c1 = Demo(456)
c2 = Demo(789)

# Valor inicial
print(f"C1: Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}")
# output: C1: Estatico 123 - Instancia: 456
print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# output: C2: Estatico 123 - Instancia: 789

Demo.atrib_estatico = -1
 
print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# output: C2: Estatico -1 - Instancia: 456
print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# output: C2: Estatico -1 - Instancia: 789

c1.atrib_instancia = 999
  
print(f"C1: Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}")
# output: C1: Estatico -1 - Instancia: 999

print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# output: C2: Estatico -1 - Instancia: 789
```

Es importante remarcar que para acceder a los atributos de instancia se debe utilizar la palabra reservada `self`, la cual hace referencia al objeto actual. En Python no podemos utilizar `self` en cualquier momento, para utilizarlo hay que indicarlo en los métodos cómo el primer parámetro recibido.

```python
class Persona:  
	def __init__(self, nombre, apellidos, edad):  
		self.nombre= nombre
		self.apellidos = apellidos 
		self.edad = edad 
	
	def camina(self): # es necesario indicar 'self' como primer argumento
		print(self.nombre + " está caminando")

p1 = Persona("Mike", "Mendiola", 25) # no hay que pasarle 'self'
p1.camina() # no hay que pasarle 'self'
print(p1.nombre)  
print(p1.edad)
```

## Private y protected
A diferencia de otros lenguajes de Programación Orientada a Objetos, todos los métodos y atributos en Python son públicos. Es decir, **no es posible definir una variable como** `private` o `protected`. 

Existe una convención de añadir como prefijo un **guión bajo** (`_`) a los atributos que consideramos como **protected** y dos guiones bajos (__) a las variables que consideramos private.

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # atributo protected 
        self.__edad = edad # atributo private
```

## Coding time!

### Ejercicio 1
Crea la clase Coche que contenga las siguientes propiedades:

- `matrícula` (string)
- `marca` (string)
- `kilometros_recorridos` (float)
- `gasolina` (float)

La clase tendrá un método llamado `avanzar()` que recibirá como argumento el número de kilómetros a conducir y sumará los kilómetros recorridos al valor de la propiedad `kilometros_recorridos`. El método también restará al valor de `gasolina` el resultado de los kilómetros multiplicado por 0'1.
La clase también contendrá otro método llamado `repostar()` que recibirá como argumento los litros introducidos que deberán sumarse a la variable `gasolina`.
Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario repostar para recorrer la cantidad indicada de kilómetros".

Ejemplo:

 - `avanzar(50)` # gasolina = 50
 - `avanzar(100)` # kilometros_recorridos = 100, gasolina = 40
 - `avanzar(40)` # kilometros_recorridos = 140, gasolina = 36
 - `avanzar(180)` # kilometros_recorridos = 320, gasolina = 18

### Ejercicio 2
Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá realizar los siguientes movimientos:
- Avanzar hacia adelante (A)
- Retroceder (R)
- Avanzar hacia la izquierda (I) o hacia la derecha (D)

El robot tendrá un método llamado `mueve()` que recibirá la orden como parámetro y otro método, `posicion_actual()`,  que indicará su posición en las coordenadas X e Y. Al crear el robot este se inicializará a las coordenadas (0,0).

Puedes utilizar el siguiente código para probar la clase creada:

```python
miRobot = Robot()
orden = "A"
while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    print(miRobot.posicion_actual())
```

Ejemplo:

```
>> Introduce la orden: A
Posición actual: 1,0
>> Introduce la orden: A
Posición actual: 2,0
>> Introduce la orden: I
Posición actual: 2,-1
>> Introduce la orden: A
Posición actual: 3,-1
>> Introduce la orden: I
Posición actual: 3,-2
>> Introduce la orden: D
Posición actual: 3,-1
>> Introduce la orden: R
Posición actual: 2,-1
>> Introduce la orden: fin
```

### Ejercicio 3
Crea la clase Triangulo que almacene la longitud de cada uno de sus lados. Deberá contener los siguientes métodos:
- `area()`: devuelve el área del triángulo
- `forma()`: indica si se trata de un triángulo equilátero, isósceles o irregular.
- `perímetro()`: devuelve el perímetro del triángulo.


## Herencia

La herencia es una técnica de la Programación Orientada a Objetos en la que una clase (conocida como **clase hija** o **subclase**) hereda todos los métodos y propiedades de otra clase (conocida como **padre** o **clase base**).

La sintaxis para definir una clase que herede de otra es la siguiente:

```python
class ClaseBase:
	# código de la clase base

class Subclase(BaseClass):
	# código de la subclase
```

### Demostración
````py
class SerVivo():
    sentidos = ["olfato","vista","oido","gusto","tacto"]

class Persona(SerVivo):
    def __init__(self,nombre):
        self.nombre = nombre
    

p1 = Persona("felipe")
print(p1.sentidos)
````

### Ejercicios:

1.  Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
    1.  mostrar(): Muestra los datos de la cuenta.
    2.  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    3.  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
2. Ejercicios de servivo, pero que los metodos heredados sean diferentes, en vez de caminar, correr, en vez de hablar, ladrar o maullar.
3. 