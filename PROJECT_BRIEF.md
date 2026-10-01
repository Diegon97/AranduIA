# PROJECT_BRIEF.md — Propósito, Alcance y Filosofía

## 1. Visión

Una educación paraguaya equitativa y soberana donde cada docente cuente con un copiloto pedagógico para aliviar su carga administrativa, y cada niño o adolescente disponga de un tutor socrático paciente e interactivo que estimule su pensamiento crítico, sin importar su condición socioeconómica, su lengua materna o sus capacidades cognitivas.

---

## 2. Misión

Construir de forma abierta y comunitaria un ecosistema tecnológico de IA generativa de bien público, libre de ataduras burocráticas o licencias comerciales prohibitivas, específicamente calibrado para la realidad curricular, lingüística y tecnológica de Paraguay.

---

## 3. Alcance del Proyecto

### Fase 1: Fundaciones y Núcleo de Aula (Actual)
* **Usuarios:** Docentes de aula y estudiantes de Educación Escolar Básica (EEB 1°, 2° y 3° ciclo, 6 a 15 años).
* **Áreas Prioritarias:**
  * **Pensamiento Matemático:** Comprensión de operaciones, fracciones, lógica y resolución de problemas.
  * **Lectoescritura:** Comprensión lectora, vocabulario bilingüe y producción de textos guiada.
* **Módulo Docente:**
  * Generación de planes de clase alineados a los programas de estudio del MEC.
  * Rúbricas de evaluación cualitativa y cuantitativa.
  * Ajustes Curriculares Individualizados (ACI) para estudiantes con TEA o dificultades de aprendizaje.
* **Módulo Estudiante:**
  * Tutoría Socrática adaptativa.
  * Selector de Modo Sensorial / TEA con pictogramas y lenguaje no ambiguo.
* **Infraestructura:**
  * PWA Offline-First y servidor local ligero (FastAPI + SQLite).
  * Soporte de traducción y generación en Español y Guaraní Jopara.

### Fase 2: Expansión e Integración Comunitaria (Próximos 6 a 12 meses)
* Incorporación de Ciencias de la Naturaleza y Ciencias Sociales.
* Módulo de Comunicación Aumentativa y Alternativa (CAA) con síntesis de voz offline para estudiantes no verbales.
* Gateway de WhatsApp automatizado para zonas de nula conectividad web pero con planes móviles patrocinados.
* Paquetes de distribución listos para servidores escolares Kolibri y Starlink rural.

---

## 4. Lo que NO es AranduIA (No-Goals)

1. **NO es un generador de tareas para copiar y pegar:** AranduIA nunca escribe tareas completas a los alumnos ni reemplaza el proceso de aprendizaje activo.
2. **NO es un reemplazo del docente:** La tecnología potencia la labor pedagógica del maestro, devolviéndole tiempo para la mediación humana.
3. **NO es una plataforma extractiva de datos:** No vende perfiles de usuarios ni entrena modelos cerrados con datos de menores de edad paraguayos.
4. **NO es un producto burocrático:** Es una herramienta creada desde las bases comunitarias que demuestra su valor en el aula diaria sin esperar decretos oficiales.

---

## 5. Principios de Diseño

* **Simplicidad Radiactiva:** Si un docente no puede usarlo en 60 segundos sin manual, la interfaz falló.
* **Resiliencia Extrema:** Si se corta la luz o internet en una tormenta, el trabajo local no se pierde y la PWA sigue respondiendo con datos en caché.
* **Inclusión Universal:** Accesibilidad visual, contraste WCAG AAA, tipografía apta para dislexia y soporte de pictogramas estandarizados.
