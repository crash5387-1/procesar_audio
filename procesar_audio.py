# procesar_audio.py - v1.2

import os
import numpy as np
import noisereduce as nr
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# --- Configuración de Carpetas ---
ruta_base = os.path.dirname(os.path.abspath(__file__))
carpeta_input = os.path.join(ruta_base, "input")
carpeta_output = os.path.join(ruta_base, "output")

# --- Funciones de Procesamiento ---
def procesar_audio(ruta_archivo, ruta_salida):
    """
    Carga un archivo de audio, lo convierte, reduce el ruido y lo guarda.
    """
    try:
        # 1. Cargar el archivo de audio
        print(f"Cargando archivo: {os.path.basename(ruta_archivo)}")
        audio = AudioSegment.from_file(ruta_archivo)

        # 2. Convertir a mono y 44100 Hz (requisito para el procesamiento)
        print("Convirtiendo a mono y 44100 Hz...")
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(44100)
        
        # --- NUEVO: Reducción de Ruido ---
        print("Aplicando reducción de ruido...")
        
        # 3. Convertir el audio de pydub a un array de NumPy
        # Los datos se normalizan a flotantes entre -1 y 1 para el procesamiento
        muestras = np.array(audio.get_array_of_samples()).astype(np.float32)
        
        # 4. Aplicar la reducción de ruido
        # El algoritmo usa la primera parte del audio como perfil de ruido por defecto
        muestras_reducidas = nr.reduce_noise(y=muestras, sr=audio.frame_rate)
        
        # 5. Volver a crear un objeto AudioSegment desde los datos procesados
        # Es importante convertir de nuevo al tipo de dato original de las muestras
        audio_procesado = audio._spawn(muestras_reducidas.astype(audio.array_type))
        # --- FIN DE LA SECCIÓN DE REDUCCIÓN DE RUIDO ---

        print(f"Guardando archivo procesado en: {ruta_salida}")
        audio_procesado.export(ruta_salida, format="wav")
        print("¡Reducción de ruido completada con éxito! ✅")
        return True

    except CouldntDecodeError:
        print(f"Error: No se pudo decodificar el archivo {os.path.basename(ruta_archivo)}.")
    except Exception as e:
        print(f"Ocurrió un error inesperado procesando {os.path.basename(ruta_archivo)}: {e}")
    return False

# --- Lógica Principal (sin cambios) ---
def main():
    """
    Función principal que recorre la carpeta de entrada y procesa los archivos.
    """
    print("--- Iniciando el Procesador de Audio v1.2 ---")
    
    if not os.path.exists(carpeta_output):
        print(f"Creando carpeta de salida en: {carpeta_output}")
        os.makedirs(carpeta_output)

    archivos_en_input = os.listdir(carpeta_input)
    
    if not archivos_en_input:
        print("La carpeta 'input' está vacía. Coloca archivos de audio para procesar.")
        return

    contador_archivos_guardados = 1
    for nombre_archivo in sorted(archivos_en_input):
        ruta_completa_input = os.path.join(carpeta_input, nombre_archivo)
        
        if os.path.isfile(ruta_completa_input):
            nombre_archivo_salida = f"audio_{contador_archivos_guardados:04d}_2.wav"
            ruta_completa_output = os.path.join(carpeta_output, nombre_archivo_salida)

            if procesar_audio(ruta_completa_input, ruta_completa_output):
                contador_archivos_guardados += 1
            
            print("-" * 20)

    print("--- Todos los archivos han sido procesados. ---")

if __name__ == "__main__":
    main()