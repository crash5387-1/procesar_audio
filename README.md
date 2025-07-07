# Optimizador de Audio con Python 🔊

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Una herramienta de línea de comandos simple y potente, diseñada para procesar archivos de audio en lote. El script limpia el ruido de fondo, estandariza el formato y mejora la claridad general, ideal para pre-procesar grabaciones de voz, podcasts o cualquier fuente de audio que requiera una mejora.

---

## ✨ Características Principales

* **Procesamiento por Lotes**: Coloca todos los archivos que necesites en la carpeta `input` y el script los procesará todos de una sola vez.
* **Estandarización de Audio**: Convierte automáticamente todos los audios a un formato consistente:
    * Frecuencia de muestreo: **44100 Hz**
    * Canales: **Mono**
* **Reducción de Ruido**: Utiliza `noisereduce` para analizar y eliminar el ruido de fondo estacionario (zumbidos, siseos, aire acondicionado).
* **Soporte Multiformato**: Gracias a `pydub`, puede leer una gran variedad de formatos de audio como `.mp3`, `.wav`, `.flac`, `.ogg` y más (siempre que tengas **FFmpeg** instalado).
* **Salida Organizada**: Guarda los archivos procesados en formato `.wav` de alta calidad en la carpeta `output`, con nombres secuenciales (`audio_0001.wav`, `audio_0002.wav`, etc.).

---

## 🛠️ Primeros Pasos

Sigue estas instrucciones para tener el proyecto funcionando en tu máquina local.

### Prerrequisitos

Asegúrate de tener lo siguiente instalado:

* **Python 3.8 o superior**.
* **pip** (el gestor de paquetes de Python).
* **(Recomendado) FFmpeg**: Para que `pydub` pueda manejar formatos de audio como `.mp3` y `.m4a`. Puedes descargarlo desde [su sitio web oficial](https://ffmpeg.org/download.html).

### Instalación

1.  **Clona o descarga este repositorio** en tu máquina local.

2.  **Crea la estructura de carpetas**. Dentro del directorio del proyecto, asegúrate de que existan las carpetas `input` y `output`.
    ```bash
    mkdir input output
    ```

3.  **Instala las dependencias**. Navega hasta la carpeta del proyecto en tu terminal y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Modo de Uso

El uso del script es muy sencillo:

1.  **Añade tus audios**: Copia todos los archivos de audio que quieras procesar dentro de la carpeta `input/`.
2.  **Ejecuta el script**: Abre una terminal en el directorio del proyecto y ejecuta el siguiente comando:
    ```bash
    python procesar_audio.py
    ```
3.  **Recoge los resultados**: El script comenzará a procesar cada archivo, mostrando el progreso en la terminal. Una vez finalizado, encontrarás todos los audios limpios y estandarizados en la carpeta `output/`.

---

## ⚙️ Flujo de Procesamiento

Para cada archivo de audio, el script sigue un riguroso pipeline de 3 pasos:

1.  **Carga y Estandarización**: El archivo se carga en memoria y se convierte a un formato de trabajo estándar (44.1kHz, mono). Esto asegura que los siguientes pasos funcionen de manera consistente.

2.  **Reducción de Ruido**: El corazón del proceso. El audio se convierte en un array numérico con `NumPy`, y la biblioteca `noisereduce` se encarga de identificar el perfil de ruido y restarlo del audio original, dejando la voz o el sonido principal más claro.

3.  **Exportación**: El audio procesado, ya limpio, se exporta como un archivo `.wav` sin comprimir para garantizar la máxima calidad. Se guarda en la carpeta `output` con un nombre de archivo numérico y secuencial.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar la herramienta, por favor, abre un *issue* para discutir el cambio o envía directamente una *pull request*.

1.  Haz un Fork del proyecto.
2.  Crea tu rama de funcionalidad (`git checkout -b feature/AmazingFeature`).
3.  Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`).
4.  Haz push a la rama (`git push origin feature/AmazingFeature`).
5.  Abre una Pull Request.

---

## 📄 Licencia

Este proyecto está distribuido bajo la Licencia MIT.