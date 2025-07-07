# procesar_audio.py - v1.1

import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# --- Configuración de Carpetas ---
ruta_base = os.path.dirname(os.path.abspath(__file__))
carpeta_input = os.path.join(ruta_base, "input")
carpeta_output = os.path.join(ruta_base, "output")

# --- Funciones de Procesamiento ---
def procesar_audio(ruta_archivo, ruta_salida):
    """
    Carga un archivo de audio, lo convierte a 44100Hz, mono y lo guarda.
    """
    try:
        print(f"Cargando archivo: {os.path.basename(ruta_archivo)}")
        audio = AudioSegment.from_file(ruta_archivo)

        print("Convirtiendo a mono...")
        audio = audio.set_channels(1)

        print("Cambiando frecuencia a 44100 Hz...")
        audio = audio.set_frame_rate(44100)
        
        print(f"Guardando archivo procesado en: {ruta_salida}")
        audio.export(ruta_salida, format="wav")
        print("¡Procesamiento básico completado con éxito! ✅")
        return True # Devuelve True si el procesamiento fue exitoso

    except CouldntDecodeError:
        print(f"Error: No se pudo decodificar el archivo {os.path.basename(ruta_archivo)}. Puede que el formato no sea compatible o el archivo esté corrupto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado procesando {os.path.basename(ruta_archivo)}: {e}")
    return False # Devuelve False si hubo un error

# --- Lógica Principal ---
def main():
    """
    Función principal que recorre la carpeta de entrada y procesa los archivos.
    """
    print("--- Iniciando el Procesador de Audio v1.1 ---")
    
    if not os.path.exists(carpeta_output):
        print(f"Creando carpeta de salida en: {carpeta_output}")
        os.makedirs(carpeta_output)

    archivos_en_input = os.listdir(carpeta_input)
    
    if not archivos_en_input:
        print("La carpeta 'input' está vacía. Coloca archivos de audio para procesar.")
        return

    # --- NUEVO: Inicializamos el contador de archivos ---
    contador_archivos_guardados = 1

    for nombre_archivo in sorted(archivos_en_input): # Usamos sorted() para procesar en orden alfabético
        ruta_completa_input = os.path.join(carpeta_input, nombre_archivo)
        
        if os.path.isfile(ruta_completa_input):
            # --- MODIFICADO: Generamos el nuevo nombre de archivo ---
            # El formato {:04d} asegura que el número tenga 4 dígitos (ej: 0001, 0002)
            nombre_archivo_salida = f"audio_{contador_archivos_guardados:04d}.wav"
            ruta_completa_output = os.path.join(carpeta_output, nombre_archivo_salida)

            # Procesamos el audio y solo incrementamos el contador si fue exitoso
            if procesar_audio(ruta_completa_input, ruta_completa_output):
                contador_archivos_guardados += 1 # Incrementamos el contador
            
            print("-" * 20)

    print("--- Todos los archivos han sido procesados. ---")

if __name__ == "__main__":
    main()