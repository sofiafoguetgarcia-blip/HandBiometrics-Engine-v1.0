# HandBiometrics-Engine-v1.0
Análisis biométrico y estimación de morfología dactilar en tiempo real.
## Descripción
HandBiometrics Engine es una aplicación de visión artificial desarrollada en Python que permite la detección de puntos clave (landmarks) de la mano y la extracción de métricas biométricas en tiempo real. El sistema utiliza modelos de aprendizaje profundo para procesar flujos de vídeo, permitiendo el cálculo de distancias dactilares y la clasificación morfológica basada en proporciones óseas.

### Requisitos de Hardware
Cámara web con resolución mínima de 640x480.

Procesador con soporte para instrucciones SSE4.1 o superior.

### Requisitos de Software y Dependencias
Para garantizar el correcto funcionamiento del algoritmo, es estrictamente necesario utilizar Python 3.11. Versiones superiores como Python 3.12 presentan incompatibilidades conocidas con las compilaciones actuales de la biblioteca MediaPipe.

### Librerías necesarias
Las dependencias exactas que deben estar presentes en el archivo requirements.txt son:

    mediapipe==0.10.9: Motor de inferencia para la detección de la malla de la mano.
    
    opencv-python: Gestión de la interfaz de vídeo y procesamiento de imagen.
    
    numpy: Operaciones matriciales y cálculos de álgebra lineal.

## Instrucciones de Instalación
### 1. Preparación del Entorno Virtual
Se recomienda el uso de un entorno virtual aislado para evitar conflictos de librerías en el sistema:

PowerShell
#### Crear entorno virtual con Python 3.11
    uv venv --python 3.11

#### Activación del entorno (Windows)
    .venv\Scripts\activate
### 2. Instalación de Dependencias
Una vez activado el entorno, proceda con la instalación de los paquetes mediante el gestor de su preferencia:

Uso de uv (Recomendado):

    PowerShell
    uv pip install -r requirements.txt
    
Uso de pip:

    PowerShell 
    pip install mediapipe==0.10.9 opencv-python numpy

### Arquitectura de Funcionamiento
El sistema opera bajo los siguientes módulos funcionales:

Módulo de Medición: Transforma las coordenadas normalizadas de MediaPipe (0.0 a 1.0) en valores de píxeles basados en la resolución activa de la ventana.

Módulo de Estimación de Género: Implementa la teoría antropológica del Ratio 2D:4D. Evalúa la relación entre la longitud del dedo índice y el anular, junto con el índice de robustez de la palma, para determinar una clasificación morfológica.

Módulo de Visualización: Renderiza una capa superior (HUD) que muestra las distancias calculadas y la envolvente convexa (Convex Hull) de la mano detectada.

## Ejecución del Sistema
Para iniciar el análisis, ejecute el script principal desde la terminal:

    PowerShell
    python main.py
Finalización del proceso: Presione la tecla Q para liberar los recursos de la cámara y cerrar las ventanas de procesamiento de forma segura.

## Imagen Demostración Código

<img width="1920" height="1080" alt="demo_mano" src="https://github.com/user-attachments/assets/78970702-84a4-4caa-a1f0-c5dbab83c5c0" />


## Consideraciones Legales y Técnicas
Este software ha sido diseñado con fines de investigación y aprendizaje técnico. Las estimaciones de género se basan en medias estadísticas de antropometría y no constituyen un método de identificación fehaciente. La precisión de las mediciones en píxeles depende de la distancia del sujeto respecto a la lente y de la distorsión óptica de la misma.
