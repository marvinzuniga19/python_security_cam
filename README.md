## Explicación del código en español:

**Importaciones:**

- `import cv2`: Importa la biblioteca OpenCV para tareas de visión artificial como procesamiento de imágenes y captura de video.
- `import time`: Proporciona funciones para manejar operaciones relacionadas con el tiempo.
- `import datetime`: Ofrece herramientas para trabajar con fechas y horas.

**Configuración:**

- `DETECTION_THRESHOLD = 1`: Define el umbral mínimo de detecciones (caras o cuerpos) para iniciar la grabación.
- `SECONDS_TO_RECORD_AFTER_DETECTION = 5`: Duración de la grabación después de la última detección.
- `FRAME_WIDTH = 640` y `FRAME_HEIGHT = 480`: Dimensiones deseadas para los fotogramas de video.
- `VIDEO_FOURCC = cv2.VideoWriter_fourcc(*"mp4v")`: Códec de video para la grabación, configurado en formato MP4.

**Clasificadores:**

- `face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")`: Carga el clasificador de cascada preentrenado para la detección de rostros del directorio de datos de OpenCV.
- `body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")`: Carga el clasificador de cascada preentrenado para la detección de cuerpos del directorio de datos de OpenCV.

**Funciones:**

- `get_video_capture()`: Inicializa un objeto de captura de video usando la cámara predeterminada (índice 0).
- `detect_faces_and_bodies(gray_frame)`: Toma un fotograma en escala de grises como entrada y devuelve dos listas: rostros detectados usando el clasificador de cascada de rostros y cuerpos detectados usando el clasificador de cascada de cuerpos.
- `start_recording(current_time)`: Crea un objeto de escritura de video para comenzar a grabar video con la marca de tiempo en el nombre del archivo e imprime un mensaje para indicar el inicio de la grabación.
- `stop_recording()`: Libera el objeto de escritura de video, deteniendo la grabación e imprime un mensaje para indicar la finalización de la grabación.
- `write_frame_to_video(frame)`: Escribe el fotograma dado en el archivo de video si la grabación está activa.
- `display_frame(frame)`: Muestra el fotograma dado en una ventana titulada "Cámara".

**Función principal:**

- `main()`:

    1. **Inicialización:**
        - Declara la variable global `out` para almacenar el objeto de escritura de video.
        - Captura video usando `get_video_capture()`.
        - Inicializa variables para rastrear el estado de detección, el tiempo de parada y el estado del temporizador.

    2. **Bucle principal:**
        - Lee un fotograma de la captura de video.
        - Convierte el fotograma a escala de grises para la detección.
        - Detecta rostros y cuerpos usando los clasificadores cargados.
        - Cuenta el número total de detecciones.

        3. **Lógica de detección:**
            - Si las detecciones superan el umbral y no hay una grabación en curso:
                - Inicia la grabación con el nombre del archivo con marca de tiempo y configura `detection` como True.
            - Si hay detecciones y la grabación está en curso:
                - Si el temporizador no ha comenzado:
                    - Inicia el temporizador y establece `detection_stopped_time`.
                - Si el temporizador ha comenzado y ha pasado el tiempo después de la última detección:
                    - Detiene la grabación, configura `detection` como False y reinicia el temporizador.

        4. **Escritura y visualización de fotogramas:**
            - Escribe el fotograma en el archivo de video si la grabación está activa.
            - Muestra el fotograma en la ventana "Cámara".

        5. **Salida:**
            - Sale del bucle si se presiona la tecla "q".
            - Libera la captura de video y destruye todas las ventanas.
