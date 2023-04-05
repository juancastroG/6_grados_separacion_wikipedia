# Wikipedia Conexiones

Este proyecto es un algoritmo que busca en la página de Wikipedia de un usuario dado como entrada, y realiza un webscraping para buscar contactos de la primera persona y la relación entre ellos a través de sus conocidos, apoyándose en la teoría de los 6 grados.

## Teoría de los 6 grados

La teoría de los 6 grados se refiere a la hipótesis de que cualquier persona en el mundo puede estar conectada con cualquier otra persona a través de una cadena de conocidos que no tiene más de seis intermediarios. En otras palabras, todos estamos conectados entre sí a través de un número muy reducido de personas. Esta teoría fue popularizada por el juego "Six Degrees of Kevin Bacon", que desafía a los participantes a encontrar una conexión de película a película entre cualquier actor y Kevin Bacon en seis pasos o menos

## Web Scraping

El Web Scraping es la técnica de extracción de datos de sitios web. En este proyecto, se realiza Web Scraping en la página de Wikipedia para extraer información relevante de la persona de entrada y sus conocidos.

## Biblioteca Spacy

Spacy es una biblioteca de procesamiento de lenguaje natural de código abierto en Python. Se utiliza en este proyecto para procesar el texto extraído de Wikipedia y extraer la información relevante.

## Requisitos
Los requisitos necesarios para ejecutar el programa son:

- spacy
- bs4
- urlopen
- requests
- re

## Uso

Para ejecutar el programa, simplemente ejecute el archivo 'wikipediaConexiones.py'. En la línea 59 del código, puede cambiar el nombre de las personas si es necesario. Tenga en cuenta que el proceso de extracción de información puede ser demorado.

## Autoría y Licencia

Este proyecto fue desarrollado por Juan Carlos Castro Guevara y se distribuye sin ninguna restricción de licencia.


