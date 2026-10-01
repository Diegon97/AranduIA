# Estrategia de Gateway de WhatsApp para Docentes

## La Paradoja de la Conectividad en Paraguay
Muchas familias y docentes no tienen saldo para navegar libremente por internet, pero cuentan con **paquetes de WhatsApp ilimitado** ofrecidos por las operadoras móviles locales (Tigo, Personal, Claro).

---

## Estrategia de Dos Vías

### Fase Piloto: Gateway Ligero (Evolution API / Baileys)
* Para las primeras escuelas y pruebas de bajo volumen, se utiliza un conector open source que permite a los docentes interactuar con el copiloto mediante un número de WhatsApp comunitario.
* Cero costo de mensajes para el proyecto durante la validación temprana.

### Fase de Escala: API Oficial de Meta Cloud
* Migración a números verificados con la API Cloud de WhatsApp cuando el volumen crezca y se disponga de fondos comunitarios para cubrir los costos por conversación de servicio.
* Implementación de colas y rate-limiting (máximo 1 respuesta cada 2-3 segundos) para proteger la experiencia del usuario.
