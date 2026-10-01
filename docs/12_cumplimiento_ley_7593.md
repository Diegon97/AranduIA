# Cumplimiento de la Ley N° 7593/2025 de Protección de Datos

Documento de conformidad técnica con la **Ley N° 7593/2025** de la República del Paraguay:

1. **Datos de Menores de Edad:** El artículo de tutela reforzada para menores se cumple mediante el diseño de **Cero Registro Identificable**. Los estudiantes pueden usar el tutor sin proporcionar su identidad real ni vincular correos personales.
2. **Cifrado y Anonimización:** Todo almacenamiento local en SQLite está aislado, y las consultas procesadas pasan por un filtro regex en `src/core/security.py` que remueve números de teléfono, correos y nombres propios.
3. **No Cesión a Terceros:** No existe cesión, venta ni transferencia internacional de bases de datos de estudiantes paraguayos.
