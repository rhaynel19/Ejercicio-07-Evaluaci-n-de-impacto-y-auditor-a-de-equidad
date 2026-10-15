# INF-8239 · Unidad 04 · Gobernanza y DSS responsable

Proyecto base acumulativo para LAB11–13. El estudiante completa archivos pequeños en `student_inputs/`, ejecuta scripts y concentra su esfuerzo en interpretar y justificar decisiones.

## Inicio
```bash
uv sync --frozen
uv run pytest -q
uv run python scripts/check_environment.py
```

## Ruta
```bash
uv run python scripts/lab11_impact.py
uv run python scripts/lab12_audit.py --model logistic
uv run python scripts/lab13_governance.py
uv run streamlit run app.py
```

Los datos son sintéticos y didácticos. El sistema no autoriza decisiones automáticas sobre personas.

## Ejercicio 07 · Expediente

- [Informe editable (borrador)](reports/ejercicio07/INFORME_EJERCICIO07.html)

LAB11–LAB13 se ejecutaron con datos sintéticos y las evidencias reproducibles están en `reports/`. El expediente incluye análisis de interesados, registro de riesgos, model card, declaración de uso de IA y runbook. Las valoraciones ordinales de riesgo requieren ratificación del autor; la recomendación excluye el uso operacional con personas reales. Revisa y aprueba el informe editable antes de entregarlo.

Repositorio GitHub indicado para el ejercicio: [Ejercicio 07 · Evaluación de impacto y auditoría de equidad](https://github.com/rhaynel19/Ejercicio-07-Evaluaci-n-de-impacto-y-auditor-a-de-equidad).
