# Simulación de incidente (ejercicio de mesa)

Este documento describe un escenario simulado; no registra un incidente real ni
una notificación enviada a personas.

- Marca temporal de la simulación (UTC): 2026-10-15T01:05:54.071078+00:00
- Señal: el modelo tree registró una brecha de recall de 0.181, por encima del umbral configurado de 0.160.
- Clasificación: fallo de puerta de equidad en una prueba con datos sintéticos.
- Contención recomendada: no usar el modelo para uso operacional; volver a revisión manual sin puntuación.
- Evidencia: `reports/lab12/tree/global_metrics.json` y `configs/governance.yml`.
- Comunicación: ninguna enviada; el escenario es exclusivamente académico y no contiene personas reales.
- Acción correctiva: revisar la causa de la brecha, repetir auditorías globales y por grupo y mantener suspendido el apoyo del modelo hasta que se aprueben los controles.
- Responsable institucional: sin designar; asignar antes de cualquier uso operacional.
- Estado: simulación completada; aprobación de reanudación no aplica.
