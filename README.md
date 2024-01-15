# Preentrega 3 Comisión 56060

## Nombre

- Eduardo Cadin

## Resumen del proyecto

- Proyecto de página de Personal Trainer

## Pasos para ejecutar el proyecto

Link de github - https://github.com/educadin19/TuPrimeraPaginaEduCadin.git

1) Inicializar un repositorio

```
git init
```

2) Clonar el repositorio 
```
get clone https://github.com/educadin19/TuPrimeraPaginaEduCadin.git
```
3)  Crear entorno virtual en Sistema operativo Windows

```
python -m venv .venv
```

4)  Activar entorno virtual

```
.\.venv\Scripts\activate
```

5)  Instalar django

```
pip install django
```
6) Inicicar el servidor
```
py .\manage.py runserver
```

## Secciones

1)  Página de inicio - Vista general de la página con introducción de las actividades propuestas. 

2) Admin - Acceso al panel de control de Django.

3) Profesores - Se presenta una lista de los profesores disponibles y las clases que imparte cada uno y un botón para acceder al registro de profesores. Se completa Nombre, Apellido y se seleecciona la clase de interés.

4) Clases - Se presenta una lista de las clases disponibles con su duiración y un botón para acceder al registro de clases. Se completa Nombre y duración de la nueva clase.

5) Usuarios - Se presenta una lista de los usuarios inscriptosy un botón para acceder al registro de usuarios y las clases a las que asiste cada uno. Se completa Nombre, Apellido y se seleecciona la clase de interés.
