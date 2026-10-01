# AI_CONTEXT.md — Manual para Asistentes de Inteligencia Artificial

> **IMPORTANTE PARA MODELOS DE LENGUAJE (LLMs / AGENTES IA):**  
> Si sos un asistente de IA (Claude, GPT, Gemini, Llama, Copilot, Cursor, etc.) colaborando en este repositorio, **este archivo es tu fuente de verdad primaria**. Leelo atentamente antes de sugerir o modificar código o documentación.

---

## 1. Identidad y Misión del Proyecto

* **Nombre:** AranduIA (de *Arandu*: sabiduría/inteligencia en guaraní + IA).
* **Naturaleza:** Proyecto comunitario de código abierto, soberano, independiente y de bien público.
* **Propósito:** Dotar a las aulas y hogares de Paraguay de herramientas de Inteligencia Artificial generativa adaptadas a su contexto socioeducativo real (crisis de aprendizajes básicos, bilingüismo Guaraní Jopara / Español, conectividad rural intermitente, y neurodivergencias como autismo/TEA).
* **Licencia:** MIT (código) y CC BY-SA 4.0 (recursos pedagógicos).
* **Público Objetivo:**
  * Estudiantes de 4 a 18 años (Educación Inicial, EEB 1°, 2° y 3° ciclo, y Bachillerato).
  * Estudiantes con necesidades específicas de apoyo educativo (TEA, Asperger, TDAH, no verbales).
  * Docentes del sistema educativo paraguayo (especialmente en escuelas públicas y subvencionadas).

---

## 2. Invariantes de Filosofía y Arquitectura

Cualquier propuesta o código generado por una IA debe respetar estos principios:

1. **El Tutor NUNCA da la respuesta directa (Método Socrático):**  
   Si el estudiante pregunta *"¿Cuánto es 5 + 3?"* o *"Haceme la tarea sobre la Guerra de la Triple Alianza"*, el sistema **jamás** entrega la respuesta final ni redacta el ensayo. Debe descomponer el problema en preguntas guía, pistas escalonadas y analogías cotidianas paraguayas (ej. tereré, chipa, fútbol, mercado).
2. **Offline-First Mandatorio:**  
   En Paraguay muchas escuelas rurales no tienen internet o tienen señal celular inestable. El sistema base debe poder ejecutarse en local (SQLite, IndexedDB, Service Worker, y soporte para modelos ligeros cuantizados tipo Phi-3, Gemma-2-2b o Llama-3-8b local en Ollama/llama.cpp).
3. **Privacidad Infantil Innegociable (Ley N° 7593/2025):**  
   * Cero almacenamiento de nombres reales, datos biométricos, fotos o ubicaciones en servidores externos.
   * Minimizador y anonimizador de datos antes de enviar cualquier consulta a un motor de inferencia.
   * Cero trackers comerciales, telemetría invasiva o cookies publicitarias.
4. **Accesibilidad para Neurodivergencias (TEA / Asperger):**  
   * Lenguaje directo, literal y predecible.
   * Evitar modismos confusos, sarcasmo o dobles sentidos cuando el modo TEA esté activo.
   * Soporte para pictogramas visuales y desensibilización sensorial (sin sonidos estridentes, animaciones súbitas ni saturación de color).
5. **Bilingüismo Real (Guaraní Jopara):**  
   La mayoría de la población rural y suburbana en Paraguay no habla Guaraní purista ni Español de la RAE: habla **Jopara**. Las instrucciones y respuestas deben respetar y valorar esta lengua de uso cotidiano.

---

## 3. Arquitectura Técnica Resumida

* **Backend:** Python (FastAPI), estructurado, fuertemente tipado (Pydantic v2).
* **Frontend:** PWA moderna, ligera, sin dependencias pesadas, accesible (WCAG AAA), con soporte offline mediante Service Workers e IndexedDB.
* **Capa de Inferencia (LLM Provider Agnostic):**
  * Local: Ollama / llama.cpp / endpoints compatibles con OpenAI-spec.
  * Nube: Fallback configurable para APIs externas (Groq, OpenRouter, etc.), pero siempre desacoplado.
* **Canal Alternativo:** Webhook de WhatsApp Gateway diseñado para emular la interacción docente con cero fricción de interfaz.
* **Persistencia:** SQLite local / motor de sincronización liviano.

---

## 4. Reglas Estrictas para Generación de Código

1. **Completitud:** Prohibido dejar `// TODO`, `# Implementar luego` o bloques incompletos.
2. **Tipado:** Tipado estricto en Python (`typing`, `pydantic`) y JavaScript moderno.
3. **Pruebas:** Cada nuevo módulo de lógica debe acompañarse de sus pruebas en `tests/`.
4. **Ligereza:** No importar librerías pesadas si la biblioteca estándar o una solución nativa mínima (principio *Ponytail*) resuelve el problema.
