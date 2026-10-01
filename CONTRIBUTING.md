# CONTRIBUTING.md — Guía para Contribuidores (Humanos e IA)

¡Gracias por tu interés en hacer de **AranduIA** una realidad para las escuelas y familias de Paraguay! Este es un proyecto de código abierto comunitario y voluntario.

---

## 🤖 Para Asistentes de IA y Agentes Autónomos

1. **Lectura Obligatoria:** Antes de escribir una sola línea, procesá [`AI_CONTEXT.md`](AI_CONTEXT.md) y [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md).
2. **Código Completo:** Prohibido dejar marcadores de posición (`TODO`, `pass` silenciosos o stubs incompletos).
3. **Tests:** Todo cambio funcional debe incluir su correspondiente test en `tests/`.

---

## 👩‍🏫 Para Docentes y Especialistas Pedagógicos

No necesitás saber programar para contribuir a AranduIA. Tu ayuda es vital en:
* Revisar que los planes de lección y rúbricas correspondan con los programas oficiales del MEC.
* Corregir el vocabulario pedagógico en Guaraní Jopara.
* Proponer ejercicios y dinámicas efectivas para estudiantes con TEA / neurodivergencias.
* Podés abrir un issue en GitHub usando la plantilla de **Mejora de Documentación** o escribir en la sección de **Discussions**.

---

## 💻 Para Desarrolladores

### 1. Configuración del Entorno Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/Diegon97/AranduIA.git
cd AranduIA

# 2. Crear entorno virtual
python -m venv venv
# Activar (Windows):
.\venv\Scripts\activate
# Activar (Linux/Mac):
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables
cp .env.example .env
```

### 2. Convención de Commits

Seguimos la especificación de [Conventional Commits](https://www.conventionalcommits.org/es/):
* `feat:` Nueva funcionalidad (ej: `feat(tutor): agregar modo visual con pictogramas para TEA`)
* `fix:` Corrección de errores (ej: `fix(jopara): corregir tildes nasales en glosario`)
* `docs:` Documentación (ej: `docs(readme): agregar instrucciones de ejecución offline`)
* `test:` Tests automatizados (ej: `test(docente): agregar validación de planes de clase`)
* `refactor:` Mejoras internas sin cambio funcional
* `style:` Formateo o estilos visuales

### 3. Flujo de Trabajo (Git Flow)

1. Creá una rama descriptiva a partir de `main`: `git checkout -b feature/nombre-mejora`
2. Hacé tus commits siguiendo la convención.
3. Asegurate de que los tests pasen con éxito: `pytest`
4. Hacé push y abrí un Pull Request en GitHub completando la plantilla requerida.
