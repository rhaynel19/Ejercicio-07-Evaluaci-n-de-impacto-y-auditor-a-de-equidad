Markdown
# INF-8239 · Unidad 04 · Gobernanza y DSS responsable

Repositorio del proyecto acumulativo para los laboratorios **LAB11–LAB13** y el **Ejercicio 07 (U04.E07): Evaluación de impacto y auditoría de equidad** de la asignatura **Ciencia de Datos II** (Universidad Autónoma de Santo Domingo - UASD).

> **Aviso importante:** Este repositorio utiliza datos sintéticos y didácticos. El sistema está concebido estrictamente como un Sistema de Apoyo a la Decisión (DSS) orientado a la revisión humana y **no autoriza decisiones automáticas, de elegibilidad o intervenciones sobre personas reales**.

---

## 🚀 Inicio y Configuración del Entorno

El proyecto gestiona sus dependencias mediante `uv`. Para sincronizar el entorno y verificar que todo funcione correctamente, ejecuta:

```bash
uv sync --frozen
uv run pytest -q
uv run python scripts/check_environment.py
🛠️ Ruta de Ejecución de Laboratorios
Para reproducir el pipeline analítico, las auditorías de equidad, las evaluaciones de impacto y los controles de gobernanza, utiliza la siguiente secuencia:

Bash
# 1. Evaluación de impacto y actores (LAB11)
uv run python scripts/lab11_impact.py

# 2. Auditoría de equidad y análisis por grupos (LAB12)
uv run python scripts/lab12_audit.py --model logistic
uv run python scripts/lab12_audit.py --model tree

# 3. Gobernanza, validación de puertas y decisión de despliegue (LAB13)
uv run python scripts/lab13_governance.py

# 4. Interfaz interactiva de visualización (Streamlit)
uv run streamlit run app.py
📁 Estructura y Artefactos del Expediente (Ejercicio 07)
El expediente técnico e informes consolidados se encuentran organizados dentro de los siguientes directorios:

Informes y Síntesis:

PDF de Síntesis Académica: reports/U04_E07_Informe_Final.pdf (o reports/U04_E07_Informe_Final_2.pdf)

Borrador / Informe editable: reports/ejercicio07/INFORME_EJERCICIO07.html

Artefactos de Auditoría y Gobernanza:

Auditoría Modelo Logístico: reports/lab12/logistic/

Auditoría Modelo de Árbol: reports/lab12/tree/

Decisión de Despliegue (JSON): reports/lab13/deployment_decision.json

Entradas del Estudiante:

Matriz de Riesgos y Stakeholders: student_inputs/

⚖️ Consideraciones Éticas y Normativas
Marco de Riesgo: Estructurado bajo los lineamientos voluntarios del NIST AI RMF 1.0 (Govern, Map, Measure, Manage).

Jurisdicción y Cumplimiento: El análisis normativo hipotético contempla la Constitución de la República Dominicana (art. 44) y la Ley núm. 172-13 de protección integral de datos personales, aplicables únicamente bajo el principio de cautela y separación estricta frente a datos sintéticos.

Decisión Final (Operacional): STOP. Se prioriza la revisión manual sin puntuación automatizada para cualquier escenario con personas reales, prevaleciendo el criterio humano sobre los resultados técnicos automatizados ("GO").

Autor: Fraimel Trinidad · Asignatura: INF-8239 Ciencia de Datos II · UASD (2026)
