# AranduIA 🇵🇾🧠

> **Ecosistema Abierto, Soberano y Offline-First de Inteligencia Artificial para la Educación Paraguaya**  
> *Arandu (sabiduría / inteligencia en guaraní) + IA. Herramientas pedagógicas libres para docentes y estudiantes de 4 a 18 años, con adaptación bilingüe (Guaraní Jopara / Español) y diseño inclusivo para estudiantes con TEA y neurodivergencias.*

[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Offline First](https://img.shields.io/badge/arquitectura-Offline--First-orange.svg)](#arquitectura-offline-first)
[![Privacidad](https://img.shields.io/badge/privacidad-Ley%207593%2F2025-blueviolet.svg)](docs/12_cumplimiento_ley_7593.md)
[![Inclusión](https://img.shields.io/badge/inclusi%C3%B3n-TEA%20%7C%20Neurodivergencias-teal.svg)](docs/04_modulo_estudiante.md)
[![Bilingüe](https://img.shields.io/badge/idioma-Espa%C3%B1ol%20%7C%20Guaran%C3%AD%20Jopara-yellow.svg)](docs/02_arquitectura_tecnica.md)

---

## 🎯 ¿Qué es AranduIA?

**AranduIA** es una iniciativa de código abierto creada desde y para la realidad de las aulas y hogares de Paraguay. Nace como respuesta comunitaria e independiente para cerrar la brecha de aprendizaje diagnosticada en pruebas nacionales e internacionales (PISA/SNEPE), donde el 85% de los estudiantes no alcanza los niveles mínimos de competencia en matemáticas y lectoescritura, y los docentes soportan una sobrecarga administrativa asfixiante.

AranduIA no busca reemplazar al maestro ni ser una enciclopedia pasiva: **es un copiloto pedagógico para el docente y un tutor socrático interactivo para el estudiante**, diseñado para funcionar con o sin conexión a internet, en computadoras escolares de bajos recursos, servidores comunitarios (Raspberry Pi) o celulares vía WhatsApp y PWA.

---

## 🧩 Los Dos Módulos Principales

### 1. 👩‍🏫 Módulo Docente: "El Copiloto del Aula"
Reduce drásticamente las horas de carga administrativa del docente para que pueda enfocarse en enseñar:
* **Generador de Planes de Lección:** Alineado a las capacidades y mallas curriculares del MEC (Educación Inicial, EEB 1°, 2° y 3° ciclo, y Bachillerato).
* **Adaptación Curricular para Neurodivergencias (TEA/Asperger/TDAH):** Generación automática de Ajustes Curriculares Individualizados (ACI) y rúbricas diferenciadas según la Ley de Educación Inclusiva N° 5136/2013 y PLANATEA.
* **Materiales Didácticos Bilingües:** Explicaciones, ejercicios y lecturas en Español formal y Guaraní Jopara natural.
* **Acceso Multicanal:** Interfaz Web PWA y Gateway liviano vía WhatsApp (para docentes con datos limitados).

### 2. 🧑‍🎓 Módulo Estudiante: "El Tutor que No Da la Respuesta"
Un tutor inteligente guiado por el método socrático que acompaña al alumno a razonar:
* **Interrogación Guiada:** Si el alumno pregunta *"¿Cuánto es 7 x 8?"*, AranduIA no le da el número; le pregunta: *"¿Te acordás de cuánto es 7 x 7? Sumale 7 más, ¿cuánto te da?"*.
* **Modo Adaptativo TEA & Sensorial:**
  * Interfaz limpia sin estímulos distractores (cero sobrecarga sensorial).
  * Apoyo con pictogramas universales y lenguaje visual para estudiantes no verbales o en espectro autista.
  * Respuestas en lenguaje directo, sin ambigüedades, metáforas confusas ni ironías.
* **Refuerzo en Áreas Críticas:** Foco especial en Lectoescritura comprensiva y Pensamiento Matemático.

---

## 🛡️ Principios Innegociables

1. **Soberanía y Privacidad Estricta (Ley N° 7593/2025):**  
   Cero venta de datos y cero telemetría invasiva. Los datos de estudiantes y docentes nunca salen a nubes corporativas no autorizadas. Procesamiento local o con proveedores cifrados.
2. **Offline-First Real:**  
   Funciona 100% desconectado en un aula rural del Chaco o San Pedro. Sincroniza de forma liviana cuando hay señal esporádica (Starlink rural o WiFi escolar).
3. **Hardware Democrático:**  
   Optimizado para correr en computadoras reacondicionadas (4 GB RAM sin GPU dedicada) o placas Raspberry Pi 4/5 locales.
4. **Respeto a la Identidad Lingüística:**  
   Comprensión y generación natural en **Guaraní Jopara**, el idioma real hablado por la mayoría de las familias paraguayas.

---

## 🚀 Inicio Rápido (Desarrollo Local)

### Prerrequisitos
* Python 3.10 o superior
* Git

### Instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/Diegon97/AranduIA.git
cd AranduIA

# 2. Crear y activar entorno virtual
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env

# 5. Ejecutar la suite de tests
pytest

# 6. Iniciar el servidor interactivo
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Abrí tu navegador en `http://localhost:8000` para acceder a la PWA interactiva con el Tutor Socrático y el Copiloto Docente.

### Ejecución con Docker
```bash
docker compose up -d
```

---

## 📂 Estructura del Repositorio

```text
AranduIA/
├── .github/                       # Plantillas de issues, PRs y modelo de funding
├── docs/                          # Documentación ejecutiva, técnica y legal (14 capítulos)
│   ├── 00_vision_y_mision.md
│   ├── 01_problema_y_contexto.md
│   ├── 02_arquitectura_tecnica.md
│   ├── 03_modulo_docente.md
│   ├── 04_modulo_estudiante.md
│   ├── 05_infraestructura_offline.md
│   ├── 06_privacidad_y_seguridad.md
│   ├── 07_hoja_de_ruta.md
│   ├── 08_barreras_y_soluciones.md
│   ├── 09_guia_para_ia.md
│   ├── 10_sostenibilidad_y_donaciones.md
│   ├── 11_whatsapp_gateway_strategy.md
│   ├── 12_cumplimiento_ley_7593.md
│   └── 13_plan_contingencia_ban.md
├── src/                           # Código fuente del sistema
│   ├── main.py                    # Servidor FastAPI y montaje de PWA
│   ├── core/                      # Motores: Tutor Socrático, Docente, Jopara, Privacidad
│   ├── api/                       # Endpoints REST (Tutor, Docente, WhatsApp, Sync)
│   └── static/                    # Frontend PWA interactivo y accesible (WCAG AAA)
├── tests/                         # Tests unitarios automatizados
├── AI_CONTEXT.md                  # Manual crítico para Asistentes de IA
├── PROJECT_BRIEF.md               # Alcance formal y filosofía del proyecto
├── CONTRIBUTING.md                # Guía de contribución para personas y agentes IA
└── LICENSE                        # Licencia MIT permisiva
```

---

## 🤝 Cómo Contribuir

¡Toda contribución es bienvenida! Necesitamos:
* **Docentes paraguayos:** Validación pedagógica, rúbricas y planes de aula.
* **Especialistas en Neurodivergencias (TEA/Asperger):** Auditoría de lenguaje directo y pictogramas.
* **Hablantes y lingüistas de Guaraní:** Enriquecimiento del léxico Jopara educativo.
* **Desarrolladores:** Optimización de modelos locales (SLMs cuantizados), PWA offline y conectores.

Consultá [`CONTRIBUTING.md`](CONTRIBUTING.md) para detalles del flujo de trabajo y [`AI_CONTEXT.md`](AI_CONTEXT.md) si usás asistentes de IA para colaborar.

---

## 💖 Apoyá el Proyecto

AranduIA es un bien público digital, sin fines de lucro, que sobrevive gracias al apoyo de su comunidad. Tu aporte sostiene servidores de prueba, pruebas en escuelas piloto rurales y equipamiento para aulas de escasos recursos.

* [Open Collective: AranduIA](https://opencollective.com/aranduia)
* [Ko-fi: AranduIA](https://ko-fi.com/aranduia)
* Conocé más en [`docs/10_sostenibilidad_y_donaciones.md`](docs/10_sostenibilidad_y_donaciones.md) y [`SPONSORS.md`](SPONSORS.md).

---

## 📜 Licencia

* **Código Fuente:** Licencia [MIT](LICENSE).
* **Materiales y Guías Educativas:** Licencia [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
