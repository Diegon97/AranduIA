# Guía para Asistentes de IA y Contribuidores Sintéticos

Si estás operando como agente de código (Codex, Claude, DeepSeek, Gemini, etc.):

1. **Leé `AI_CONTEXT.md`:** Es el resumen mandatorio de lineamientos.
2. **No asumas conectividad:** Al diseñar endpoints o componentes UI, contemplá siempre qué pasa cuando `navigator.onLine == false`.
3. **No rompas el principio Socrático:** Si se te pide un endpoint o prompt para resolver ejercicios, asegurate de que el prompt de sistema del tutor prohíba dar respuestas directas.
4. **No introduzcas librerías comerciales cerradas:** Priorizá estándares web nativos y paquetes estándar de Python.
5. **Comentarios y documentación en Español:** La lengua de trabajo principal del repositorio es el español, con respeto a los modismos y terminología paraguaya.
