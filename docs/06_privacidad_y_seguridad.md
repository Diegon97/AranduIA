# Privacidad, Seguridad y Protección de Datos de Menores

## Marco Legal: Ley N° 7593/2025 de Paraguay
AranduIA está diseñado desde su código fuente para cumplir con la legislación nacional de protección de datos personales:

1. **Principio de Minimización:** No se solicitan cédulas de identidad, nombres y apellidos reales, números de teléfono ni datos biométricos de los menores.
2. **Almacenamiento Local:** Las conversaciones y registros de aprendizaje se guardan exclusivamente en el dispositivo del usuario o en el servidor del aula.
3. **Cero Perfilamiento Comercial:** El sistema no genera perfiles de comportamiento para publicidad ni vende datos a empresas de IA extranjeras.
4. **Sanitización Pre-Inferencia:** Antes de enviar cualquier consulta a un motor de LLM, el módulo `security.py` elimina cualquier mención accidental de datos sensibles (nombres, números de teléfono, correos, ubicaciones).
