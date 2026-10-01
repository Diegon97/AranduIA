# Arquitectura Técnica General — AranduIA

## 1. Visión Global del Sistema

AranduIA está concebido como una plataforma modular con capas desacopladas:

```text
┌───────────────────────────────────────────────────────────────┐
│               CAPA DE INTERFAZ Y ACCESO                      │
│   • PWA Web Offline-First (Móvil / Escritorio)                │
│   • Gateway WhatsApp (Micro-mensajería comunitaria)           │
├───────────────────────────────┬───────────────────────────────┤
│       MÓDULO DOCENTE          │       MÓDULO ESTUDIANTE       │
│    "El Copiloto del Aula"     │    "El Tutor Socrático"       │
│ • Planes de Lección MEC       │ • Diálogo Socrático Guiado    │
│ • Adaptación Curricular TEA   │ • Modo TEA & Pictogramas      │
│ • Rúbricas y Evaluaciones     │ • Soporte Bilingüe Jopara     │
├───────────────────────────────┴───────────────────────────────┤
│               MOTOR PEDAGÓGICO Y LINGÜÍSTICO                  │
│ • Motor Socrático (EduCrate spec) • Léxico Jopara            │
│ • Evaluador de Privacidad & Minimización (Ley 7593/2025)      │
├───────────────────────────────────────────────────────────────┤
│               CAPA DE INFERENCIA IA (AGNOSTIC)                │
│ • Inferencia Local (Ollama, llama.cpp, SLMs cuantizados)      │
│ • Conectores API externos cifrados (Fallback opcional)        │
├───────────────────────────────────────────────────────────────┤
│               INFRAESTRUCTURA Y ALMACENAMIENTO                │
│ • SQLite local / IndexedDB en navegador                       │
│ • Sincronización ligera intermitente (Offline-First)          │
│ • Compatibilidad con Servidor Escolar Kolibri / Raspberry Pi  │
└───────────────────────────────────────────────────────────────┘
```

## 2. Pila Tecnológica Elegida

* **Backend:** Python 3.10+ con **FastAPI** y **Pydantic v2**. Liviano, asíncrono, con bajo consumo de memoria.
* **Frontend:** PWA nativa con HTML5 semántico, CSS responsivo con modo de alto contraste y soporte de dislexia, y JavaScript moderno sin frameworks pesados para garantizar compatibilidad con navegadores antiguos.
* **Persistencia:** SQLite local para el backend y almacenamiento IndexedDB en el cliente.
* **Modelos de Lenguaje:** Interfaz agnóstica (`LLMProvider`) preparada para correr modelos pequeños como Phi-3 Mini (3.8B), Gemma-2 (2B), Llama-3 (8B) o Qwen-2.5 en hardware local, o consultar endpoints remotos cuando hay conexión.
