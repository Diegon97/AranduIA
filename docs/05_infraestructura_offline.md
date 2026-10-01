# Infraestructura Offline-First y Despliegue en Escuelas

## La Realidad de las Aulas Paraguayas
Muchas escuelas públicas no cuentan con conectividad a internet en sus salas de clase. AranduIA adopta una arquitectura donde **el acceso a internet es una mejora opcional, no un requisito funcional**.

---

## Modos de Operación

### 1. Modo Local Autónomo (Monopuesto)
* La aplicación corre en una computadora común del aula (Windows 10/11 o Linux).
* Almacena datos en SQLite local.
* La PWA corre en el navegador y puede sincronizar en caché todo el contenido educativo.

### 2. Modo Servidor de Aula (Raspberry Pi / Mini PC)
* Una Raspberry Pi 4 (4GB/8GB) o mini PC actúa como servidor local emitiendo una red Wi-Fi sin salida a internet (Access Point local).
* Todos los celulares y netbooks de los estudiantes y docentes se conectan al Wi-Fi del aula y abren `http://arandu.local`.
* Se integra con plataformas como **Kolibri** para servir videos y lecturas offline.

### 3. Sincronización Intermitente
* Cuando una escuela dispone de enlace Starlink o señal móvil temporal:
  * Envía telemetría anónima de uso (si la escuela lo autoriza).
  * Descarga actualizaciones de modelos, mallas curriculares y planes de lección comunitarios.
