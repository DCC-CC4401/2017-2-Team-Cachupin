# Tarea N°3

## Lo que debemos implementar

En esta iteración deben desarrollar los requisitos asociados a los dos siguientes tipos de usuarios:  
1) representante de una municipalidad, y 
2) persona natural.

Por desarrollar, nos referimos a diseñar e implementar el modelo de datos, captar y procesar los datos ingresados por los usuarios a través de las interfaces, etc. El uso de Git y GitHub es obligatorio para esta tarea, en conjunto con las metodologías de desarrollo vistas en clases auxiliares (git-flow, kanban, issues y milestones).

Interfaces (__deben ser *responsive*__):

1. Landing page para personas naturales: en vez de un mapa funcional, _**DEBEN** utilizar un screenshot de un mapa_.
Pueden definir un image map sobre esta imagen para linkear al resto de las interfaces (para más información, ver
https://www.w3schools.com/tags/tag_map.asp).
2. Ficha del animal
3. Ficha de la denuncia
4. Ficha de la municipalidad

## Sobre los requisitos

Requisitos que deben implementar en forma completa: **1-3, 5, 12-14, 29, 31-33**. También deben implementar los requisitos
_4 y 6_, pero como en esta entrega usaremos un mapa estático, deben usar un valor dummy como ubicación, en vez de la
posición real del usuario.
En el caso de las interfaces que no son parte de esta entrega, usen links estáticos a los mockups definidos para estas
interfaces. Especialmente en el caso de los requisitos _4, 6, 7-11_.

## Entregables

1. Un informe. Este informe debe incluir al menos la siguiente información:
  - Resumen del cumplimiento de los requisitos: cuales requisitos están satisfechos/parcialmente satisfechos/no
satisfechos
  - Descripción de la metodología seguida por el equipo: herramientas usadas, frecuencia de reuniones, planificación
del trabajo, etc.
  - Descripción de su modelo de datos, donde indican la trazabilidad con las interfaces
2. Una presentación, en las clases del 24 y 26 de octubre. Tienen __15 minutos__ para esta presentación, y las diapositivas
se entregan el 23 de octubre con el informe. Sus presentaciones deben tener un inicio y un fin, no deben ser solo
una demo de la funcionalidad implementada. También deben hacer una reflexión acerca del trabajo realizado. Solo
presenta una persona, _elegida al azar de los que aun no presentan_.
Ambos entregables deben estar en _formato PDF_, y asegúrense de que los diagramas en ambos entregables sean legibles.
Deben hacer entrega de ambos documentos por U-Cursos, la __fecha de entrega es 23 de octubre @ 23:59__.

# Requisitos

## Generales

1. __Completo__ El sistema debe permitir la autentificación de usuarios.
2. __Completo__ El sistema debe considerar 4 tipos de usuarios: administrador, representante de una
municipalidad, representante de una ONG, persona natural (hace denuncias, busca
animales para adoptar, etc.).
3. __Completo__ El sistema debe permitir que personas naturales reporten casos de maltrato.
4. Las denuncias creadas en el sistema deben estar geo-localizadas (*valor __dummy__*). (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
5. __Completo__ El sistema debe considerar los siguientes tipos de maltrato: abandono en la calle,
exposición a temperaturas extremas, falta de agua, falta de comida, violencia y venta
ambulante.

## Landing page para personas naturales:

6. El sistema debe mostrar un mapa centrado en la posición actual del usuario (*valor __dummy__*), sin
importar si hay un usuario autentificado. (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
7. El sistema debe mostrar las posiciones de las ONG con animales por adoptar, sin
importar si hay un usuario autentificado.  (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
8. Si el usuario se ha autentificado como persona natural, el sistema también debe mostrar
las posiciones de las ONG favoritas del usuario.  (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
9. Se debe usar iconos distintos para las ONG favoritos/no favoritos.  (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
10. Cuando un usuario presiona el icono de una ONG en el mapa, el sistema debe mostrar
la ficha de esta ONG.  (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)
11. En el caso de personas naturales, el sistema debe permitir buscar animales en adopción
en el mapa, mostrando solo las ONG que tienen animales que cumplen con los criterios
de búsqueda especificadas por el usuario (sin importar si hay un usuario autentificado). 
Inicialmente, deben considerar los siguientes criterios: tipo de animal, y edad estimada
de este.  (_link estatico_ a mockup definido para interfaz que no es parte de la entrega)

## Ficha de Municipalidad (vista por representante municipal):

12. __Completo__ El sistema debe mostrar el nombre y foto de perfil de la municipalidad.
13. __Completo__ El sistema debe mostrar un listado de las denuncias recibidas dentro de la comuna.
Desde este resumen se puede navegar a las fichas de las denuncias individuales.
14. __Completo__ El sistema debe generar estadísticas básicas de las denuncias por comuna. Se debe
poder filtrar por estado de la denuncia (reportadas, consolidadas, verificadas, cerradas y
desechadas).

## Ficha de ONG (vista por persona natural):

15. El sistema debe mostrar el nombre y foto de perfil de la ONG.
16. El sistema debe mostrar cuántos usuarios lo han seleccionado como “favorito”.
17. El sistema debe mostrar un resumen de los animales actualmente en adopción. Desde
este resumen se puede navegar a las fichas de los animales individuales.
18. El sistema debe permitir que los usuarios de tipo persona natural registren a ONGs
como “favorito”.

## Ficha de ONG (vista por representante municipal):

19. El sistema debe mostrar el nombre y foto de perfil de la ONG.
20. El sistema debe mostrar cuántos usuarios lo han seleccionado como “favorito”.
21. El sistema debe generar estadísticas básicas de las adopciones gestadas por la ONG.
22. El sistema debe generar estadísticas básicas de las esterilizaciones realizadas por la
ONG.

## Ficha de ONG (vista por representante ONG):

23. El sistema debe permitir gestionar el nombre y foto de perfil de la ONG.
24. El sistema debe permitir gestionar las fichas de los animales actualmente bajo su
cuidado.
25. El sistema debe permitir ver las solicitudes de adopción de los animales bajo su
cuidado.
26. El sistema debe mostrar cuántos usuarios lo han seleccionado como “favorito”.
27. El sistema debe generar estadísticas básicas de las adopciones gestadas esta ONG.
28. El sistema debe generar estadísticas básicas de las esterilizaciones realizadas por esta
ONG.

## Ficha de animal

29. __Completo__ El sistema debe mostrar la siguiente información para un animal: 
*nombre
*tipo de animal 
*foto 
*sexo
*edad estimada
*cuánto tiempo lleva en adopción.
30. En el caso de las ONG, el sistema debe permitir gestionar la información de un animal.
31. __Completo__ En el caso de una persona natural, el sistema debe permitirle al usuario indicar que
quiere adoptar el animal.

## Ficha de denuncia

32. __Completo__ El sistema debe mostrar la siguiente información para una denuncia: estado de la
denuncia, lugar de la denuncia, tipo de animal, sexo, color general, y si este se
encuentra herido.
33. __Completo__ En el caso de las municipalidades, el sistema debe permitir gestionar la información de
una denuncia.

## Interfaces de administración (solo para usuarios de tipo administrador)

34. El sistema debe permitir la gestión (creación, modificación y eliminación) de
representantes municipales.
35. El sistema debe permitir la gestión (creación, modificación y eliminación) de
representantes ONG.
