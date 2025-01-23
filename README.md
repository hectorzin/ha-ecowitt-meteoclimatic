# Ecowitt-Meteoclimatic Home Assistant Add-on

## Descripción

Este complemento se basa en el código que publicó @tonicb en el foro meteoclimatic. A partir de ese código yo he creado este complemento para Home Asistant, para hacer mucho más fácil en la mayoría de los casos la integración con Home Assistant

El complemento **Ecowitt-Meteoclimatic** permite integrar tu estación meteorológica **Ecowitt** con **Home Assistant** y, al mismo tiempo, enviar datos a **Meteoclimatic**, una red de estaciones meteorológicas. Esto te permitirá registrar y visualizar los datos de tu estación tanto localmente como en la plataforma de Meteoclimatic.

El complemento es altamente configurable, soporta múltiples arquitecturas y es ideal para quienes deseen centralizar la gestión de datos meteorológicos.

---

## Características principales

- Recibe datos de estaciones **Ecowitt** mediante webhooks.
- Envía los datos recibidos a **Home Assistant** para su visualización y análisis.
- Integra con **Meteoclimatic** para compartir tus datos meteorológicos con la comunidad.
- Modo de depuración para registrar logs detallados.

---

## Instalación

1. Dirígete a la sección **Supervisor** en tu instalación de Home Assistant.
2. Haz clic en la pestaña **Complementos** y selecciona la opción para agregar un repositorio.
3. Ingresa la URL del repositorio de este complemento:  
   👉 [Repositorio en GitHub](https://github.com/hectorzin/ecowitt-meteoclimatic/tree/main/ha-addon)
4. Busca el complemento **Ecowitt-Meteoclimatic** en la lista e instálalo.
5. Una vez instalado, configúralo y asegúrate de iniciarlo.

---

## Configuración

El complemento se configura desde la interfaz de Home Assistant. Accede a la sección del complemento y completa los campos en la pestaña de configuración:

### Parámetros de configuración:

| **Parámetro**             | **Descripción**                                                                                  | **Requerido** |
|---------------------------|--------------------------------------------------------------------------------------------------|---------------|
| `home_assistant_server`   | Nombre del servidor o dirección IP de tu instalación de Home Assistant.                         | Sí            |
| `home_assistant_port`     | Puerto del servidor de Home Assistant (normalmente 8123).                                       | Sí            |
| `path`                    | Ruta del webhook para recibir datos de la estación, la proporciona la integración Ecowitt.      | Sí            |
| `station_code`            | Código de tu estación meteorológica registrado en Meteoclimatic.                                | Sí            |
| `send_to_meteoclmatic`    | Deshabilitarlo si temporalmente no quieres enviar datos a meteoclimatic.                        | Sí            |
| `api_key`                 | Clave API proporcionada por Meteoclimatic.                                                      | Sí            |
| `debug`                   | Activa el modo de depuración para ver logs detallados.                                          | No            |

---

### Ejemplo de configuración

```yaml
home_assistant_server: "homeassistant.local"
home_assistant_port: 8123
path: "/api/webhook/1aa4aab46e90718090c094xxxxxxxxxx"
station_code: "ESCAT0800000XXXXXX"
api_key: "504xxxxx-xx82-1xxf-a9xx-02xxxxxxxxxx"
debug: true
```

---

## Cómo funciona

1. Configura tu estación Ecowitt para enviar datos a la IP de Home Assistant usando el puerto configurado (por defecto, 8120) y en path debes poner /api/data.
2. El complemento recibirá los datos y los procesará de la siguiente manera:
   - **Home Assistant**: Los datos se enviarán al webhook configurado en tu servidor de Home Assistant.
   - **Meteoclimatic**: Si está configurado, los datos también se enviarán a la plataforma Meteoclimatic.

---

## Notas importantes

- Meteoclimatic requiere un código de estación y una clave API válidos para aceptar datos.

---

## Contribuciones

Si encuentras un problema o tienes sugerencias, por favor crea un **issue** o un **pull request** en el repositorio oficial:  
👉 [Repositorio en GitHub](https://github.com/hectorzin/ecowitt-meteoclimatic/tree/main/ha-addon)

---

## Licencia

Este complemento está disponible bajo la licencia MIT. Consulta el archivo [LICENSE](https://github.com/hectorzin/ecowitt-meteoclimatic/blob/main/LICENSE) para más detalles.
