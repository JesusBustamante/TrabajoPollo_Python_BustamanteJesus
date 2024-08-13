# MoliPollito

Sistema que gestiona pedidos de mesas de un restaurante

# Índice

1. [Estado del proyecto](#id1)
2. [Descripción del Proyecto](#id2)
3. [Tecnologías Utilizadas](#id3)
4. [Estructura del proyecto](#id4)
5. [Características](#id5)
6. [Diseño](#id6)
7. [Instrucciones](#id7)
8. [Personas Desarrolladoras del Proyecto](#id8)


# Estado del Proyecto<a name="id1"></a>

En desarrollo

# Descripción del Proyecto<a name="id2"></a>

El aplicativo debe cumplir con las siguiente especificaciones:

- Permitir la creación de pedidos para un cliente añadiendo los platos que solicite separándolos por entradas, platos fuertes y bebidas. Los pedidos serán almacenados en un archivo tipo JSON.
- Leer los archivos JSON (su contenido será encontrado al final de este documento y tendrá que ser respetado) con la información del menú para dar las opciones a la hora de tomar pedido.
- Los pedidos pueden agregar tantos platos y opciones como se soliciten, permitiendo la repetición de los mismos.
- Al finalizar la selección de platos del pedido se debe mostrar la orden completa y solo guardar en pedidos si se confirma la misma.
- Registrar los pagos hechos por pedido en formato JSON. El pedido deberá contener la información si fue pagado o no, el pago se puede realizar en cualquier momento. Al pagarse debe registrar en un archivo la fecha de pago, el valor total (que en ese momento deberá ser calculado) y el identificador del cliente línea a línea sin eliminar nunca ningún registro.
- Cambiar de estado los pedidos. Los estados son Creado --> preparacion --> servido o el estado especial cancelado, el cambio de estado debe hacerse por un estado diferente al actual o uno posterior, no puede devolverse. Y solo se podrá pasar a estado servido si y solo si ya fue pagado.
- Permitir la modificación de pedidos si y sólo si se encuentra en estado creado.
- Permitir cancelar pedido, el estado cancelado solo podrá ser asignado si el estado es creado y no ha sido pagado.
- Permitir realizar consultas a los pedidos realizados.

# Tecnologías utilizadas<a name="id3"></a>

* Python

# Estructura del Proyecto



# Características<a name="id5"></a>


# Diseño<a name="id6"></a>

* Solo puede ser visto y usado en consola

# Instrucciones<a name="id7"></a>

1. Clonar el repositorio
~~~
https://github.com/JesusBustamante/Filtro_python_BustamanteJesus.git
~~~

2. Si es clonado en Visual Studio Code, descargue la extensión de Python.

3. También descargue python desde un navegador web o la microsoft store.

3. Ejecuta el programa en la terminal de GitBash de la siguiente forma: 
~~~ 
python main.py 
~~~

# Personas Desarrolladoras del Proyecto<a name="id8"></a>

Este proyecto fue desarrollado por Jesús Leonardo Bustamante Ramírez, estudiante de Campuslands, como trabajo requerido para el módulo de Git.