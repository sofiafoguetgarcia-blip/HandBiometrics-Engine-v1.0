# Proyecto webcam: medidas de la mano y edad orientativa

Proyecto simple en Python que usa la webcam del portátil para:

- detectar una mano en tiempo real,
- calcular medidas básicas en píxeles,
- dibujar los puntos de la mano,
- mostrar un contorno aproximado,
- y estimar una edad solo de forma orientativa con una heurística sencilla.

## Importante

La parte de edad no es científica ni fiable.
No usa un modelo entrenado con un dataset de edades reales.
Es solo una demostración educativa de visión por computador.

## Tecnologías

- Python
- OpenCV
- MediaPipe
- NumPy

## Instalación con uv

```bash
uv venv
uv pip install -r requirements.txt
```

## Ejecutar

```bash
uv run main.py
```

## Uso

1. Ejecuta el programa.
2. Acepta permisos de cámara si el sistema lo pide.
3. Coloca una mano abierta frente a la webcam.
4. En pantalla verás:
   - ancho de palma,
   - alto de palma,
   - longitud aproximada de varios dedos,
   - edad orientativa.

## Controles

- Q para salir.

## Qué calcula

El programa usa los landmarks de la mano para medir:

- ancho de palma,
- alto de palma,
- pulgar,
- índice,
- dedo medio,
- anular,
- meñique.

Todas las medidas se muestran en píxeles.

## Limitaciones

- Solo analiza una mano.
- Las medidas no están en centímetros.
- La estimación de edad es una heurística muy simple.
- La luz, la distancia a cámara y la calidad de la webcam afectan al resultado.

## Posibles mejoras

- calibración real en centímetros usando un objeto de referencia,
- guardar capturas,
- exportar medidas a CSV,
- mejorar la heurística,
- reemplazar la edad orientativa por clasificación de tamaño de mano.

## Imagen demostración

<img width="1920" height="1080" alt="demo_mano" src="https://github.com/user-attachments/assets/27905098-e523-4519-bdfb-fd93ee245df6" />

