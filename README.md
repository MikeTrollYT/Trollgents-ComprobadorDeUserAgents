# Comprobador de User Agents

## Descripción

Este proyecto es un script en Python para comprobar user agents. El script verifica si los user agents listados en un archivo de texto son funcionales o si están obsoletos, y los clasifica en archivos separados para user agents funcionales y obsoletos.

## Características

- Verifica la funcionalidad de user agents enviando solicitudes HTTP a un sitio web especificado.
- Muestra el estado de cada user agent en la consola con colores: verde para user agents funcionales y rojo para obsoletos.
- Guarda los resultados en archivos de texto separados para user agents funcionales y obsoletos.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- Python 3.6 o superior
- Paquetes Python:
  - `requests`

## Instalación

1. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt

## Uso

1. Prepara el archivo de user agents:
- El archivo `user_agents.txt` debe contener una lista de user agents, uno por línea.
- Puedes encontrar user agents en el siguiente sitio web: [MikeTroll - User Agents](https://miketrollyt.github.io/MikeTroll/user-agents/)
2. Ejecuta el script:
- Ejecuta el script `main.py` desde la línea de comandos. El script te pedirá que ingreses la URL del sitio web para probar los user agents.
  ```bash
   python main.py
3. Ingresar la URL del sitio web:
- Ingresa la URL del sitio web que deseas usar para verificar los user agents (por ejemplo, `https://www.google.com`).
4. Revisa los resultados:
  - El script generará dos archivos de salida:
    - `user_agents_funcionales.txt`: Contiene user agents que funcionan.
    - `user_agents_obsoletos.txt`: Contiene user agents que no funcionan.
   
## Notas

- Asegúrate de que el archivo de user agents no contenga líneas vacías ni formatos incorrectos.
- Si el archivo de user agents tiene un formato incorrecto, el script puede arrojar errores.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Agradecimientos

- Requests - Biblioteca para realizar solicitudes HTTP.
