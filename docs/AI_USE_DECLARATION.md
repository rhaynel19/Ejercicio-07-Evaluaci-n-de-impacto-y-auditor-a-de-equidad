# Declaración de uso de IA

## Herramienta y finalidad
Se utilizó un asistente de IA en VS Code para revisar la estructura del proyecto, ejecutar las auditorías LAB12 y la evaluación de puertas LAB13, ejecutar pruebas existentes y preparar el borrador del expediente U04.E07.

## Contenido asistido
La asistencia afectó el informe y documentos de apoyo, el registro cualitativo de riesgos/interesados y la validación/generación del reporte LAB11. Se reforzó `score_risks` para validar escala 1–4, identificadores y niveles residuales, y se añadieron pruebas de esas validaciones. No se modificaron el algoritmo del modelo, los datos sintéticos ni las puertas de configuración. Las métricas se generaron con los scripts del proyecto y se contrastaron con los JSON/CSV resultantes.

## Decisiones y valores humanos
El autor eligió falsos negativos como daño prioritario, República Dominicana como jurisdicción para revisar y limitar el uso a priorización de revisión humana, sin uso operacional con personas reales. A petición del autor, la IA propuso el análisis de interesados y el registro de riesgos, incluidas valoraciones ordinales de probabilidad, impacto y riesgo residual basadas en los artefactos sintéticos. Son juicios preliminares del ejercicio, no frecuencias observadas ni evaluaciones validadas por una institución; el autor debe revisarlos y ratificarlos antes de presentar el trabajo.

## Verificaciones, errores y correcciones
Se ejecutaron `scripts/lab12_audit.py` para los modelos `logistic` y `tree`, `scripts/lab13_governance.py`, `scripts/validate_lab12_decision.py`, `scripts/lab11_impact.py` y la suite completa de pytest: 12 pruebas pasaron. También pasó la comprobación de entorno/dataset. El resultado técnico `GO` de LAB13 se separó explícitamente de la decisión humana restrictiva. La primera invocación del ejecutor integrado no descubrió los tests; se verificaron con pytest desde el entorno del proyecto. No se usaron datos reales. La Ley 172-13 se contrastó en el registro oficial de legislación de la Consultoría Jurídica del Poder Ejecutivo y el AI RMF en el sitio de NIST; no se emite una opinión legal.

## Verificación pendiente del autor
El autor debe revisar todas las métricas e interpretaciones, ratificar las valoraciones cualitativas de riesgo, comprobar la aplicabilidad legal con asesoría competente, validar los controles y corregir cualquier error antes de entregar. El informe incluye el enlace al repositorio asignado; este se encontraba vacío antes de la primera publicación de los artefactos.
