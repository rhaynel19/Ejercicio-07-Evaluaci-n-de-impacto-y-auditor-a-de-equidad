# Registro de decisión — U04.E07

## Alcance y responsables

- Propósito: Ejercicio académico para evaluar si un DSS con datos sintéticos puede priorizar casos para revisión humana; no es una herramienta operativa.
- Responsable académico: Responsable académico del expediente: Edwin Ramón José Nolasco. No existe un propietario institucional u operativo designado.
- Responsable institucional/operacional: sin designar; el uso operacional no está autorizado.
- Decisión asistida: Orden de revisión de casos sintéticos; una persona conserva la decisión y puede ignorar la puntuación.
- Daño prioritario seleccionado por el autor: Falsos negativos: casos relevantes que no se priorizan. Esta prioridad fue elegida por el autor del expediente.

## Evidencia y umbrales

- Métrica principal y tolerancias: Recall global y por grupo protegido; revisar conjuntamente la brecha de recall y la tasa de falsos positivos (FPR) para evitar ocultar trade-offs.; Usar las puertas ya configuradas, sin ajustarlas a posteriori: recall >= 0.68; brecha entre grupos de recall <= 0.16; brecha entre grupos de FPR <= 0.16. Son umbrales didácticos del proyecto, no estándares legales ni una aceptación de riesgo real.
- Artefactos de evidencia: reports/lab12/logistic/global_metrics.json; reports/lab12/logistic/fairness_by_group.csv; reports/lab12/logistic/fairness_intersectional.csv; reports/lab12/tree/global_metrics.json; reports/lab12/tree/fairness_by_group.csv; reports/lab12/tree/fairness_intersectional.csv; reports/lab13/deployment_decision.json.
- Estado de medición: completada
- Limitación: Prueba temporal sintética de 160 filas; intersecciones pequeñas (mínimo n=8); no hay intervalos de confianza, validación externa, consulta a afectados ni demostración de validez en una población real.

## Priorización de riesgos

La probabilidad y el impacto son valoraciones cualitativas provisionales de 1
a 4; la prioridad es su producto, no una probabilidad estimada empíricamente.
Los niveles residuales son juicios cualitativos y requieren revisión del autor
y de la institución antes de cualquier uso operacional.

| Riesgo | Prioridad inherente | Nivel residual | Responsable |
|---|---:|---|---|
| R01 | 12 | high | Academic owner (risk assessment); institutional service owner unassigned. |
| R03 | 12 | high | Academic owner (risk assessment); institutional fairness owner unassigned. |
| R04 | 12 | high | Academic owner (risk assessment); independent evaluator unassigned. |
| R02 | 9 | medium | Academic owner (risk assessment); operational reviewer owner unassigned. |
| R06 | 9 | medium | Academic owner for exercise; operational service owner unassigned. |
| R07 | 8 | high | Academic owner for exercise; institutional governance owner unassigned. |
| R08 | 6 | medium | Academic owner for exercise; MLOps/monitoring owner unassigned. |
| R05 | 4 | medium | Academic owner for this exercise; institutional privacy officer unassigned. |

## Decisión

Modificar y limitar a priorización de casos sintéticos para revisión humana dentro del ejercicio. No desplegar ni usar con personas o datos reales; conservar revisión manual sin modelo como alternativa segura.

Esta es la decisión restrictiva del autor para el ejercicio y no autoriza
despliegue. Si una propuesta futura incumple un umbral configurado, carece de
evidencia representativa o controles aprobados, o se sale del alcance, se debe
suspender la priorización asistida y usar la alternativa manual no predictiva.
