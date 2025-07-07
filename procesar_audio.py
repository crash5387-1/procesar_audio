# procesar_audio.py - v1.0

import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# --- Configuración de Carpetas ---
# Define la ruta de la carpeta actual donde se ejecuta el script
ruta_base = os.path.dirname(os.path.abspath(__file__))
# Define la ruta para las carpetas de entrada y salida
carpeta_input = os.path.join(ruta_base, "input")
carpeta_output = os.path.join(ruta_base, "output")

# --- Funciones de Procesamiento ---
def procesar_audio(ruta_archivo, ruta_salida):
    """
    Carga un archivo de audio, lo convierte a 44100Hz, mono y lo guarda.
    """
    try:
        # 1. Cargar el archivo de audio
        print(f"Cargando archivo: {os.path.basename(ruta_archivo)}")
        audio = AudioSegment.from_file(ruta_archivo)

        # 2. Convertir a mono
        print("Convirtiendo a mono...")
        audio = audio.set_channels(1)

        # 3. Cambiar la frecuencia de muestreo a 44100 Hz
        print("Cambiando frecuencia a 44100 Hz...")
        audio = audio.set_frame_rate(44100)
        
        # 4. Exportar el archivo procesado en formato WAV
        # Usamos WAV para mantener la calidad máxima después del procesamiento
        print(f"Guardando archivo procesado en: {ruta_salida}")
        audio.export(ruta_salida, format="wav")
        print("¡Procesamiento básico completado con éxito! ✅")

    except CouldntDecodeError:
        print(f"Error: No se pudo decodificar el archivo {os.path.basename(ruta_archivo)}. Puede que el formato no sea compatible o el archivo esté corrupto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado procesando {os.path.basename(ruta_archivo)}: {e}")

# --- Lógica Principal ---
def main():
    """
    Función principal que recorre la carpeta de entrada y procesa los archivos.
    """
    print("--- Iniciando el Procesador de Audio v1.0 ---")
    
    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_output):
        print(f"Creando carpeta de salida en: {carpeta_output}")
        os.makedirs(carpeta_output)

    # Listar archivos en la carpeta de entrada
    archivos_en_input = os.listdir(carpeta_input)
    
    if not archivos_en_input:
        print("La carpeta 'input' está vacía. Coloca archivos de audio para procesar.")
        return

    for nombre_archivo in archivos_en_input:
        ruta_completa_input = os.path.join(carpeta_input, nombre_archivo)
        
        # Solo procesar si es un archivo
        if os.path.isfile(ruta_completa_input):
            # Definir el nombre del archivo de salida
            nombre_base, _ = os.path.splitext(nombre_archivo)
            nombre_archivo_salida = f"{nombre_base}_procesado.wav"
            ruta_completa_output = os.path.join(carpeta_output, nombre_archivo_salida)

            procesar_audio(ruta_completa_input, ruta_completa_output)
            print("-" * 20) # Separador para el siguiente archivo

    print("--- Todos los archivos han sido procesados. ---")

if __name__ == "__main__":
    main()