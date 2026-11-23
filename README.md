# NexusReal — Plataforma Web de Gestión y Búsqueda Inmobiliaria (Módulo I)

## Descripción del Proyecto
* **Problema:** Los asesores inmobiliarios suelen gestionar y buscar propiedades a través de múltiples grupos y chats de WhatsApp, lo que genera pérdida de tiempo, información desactualizada y dificultad para filtrar inmuebles según las necesidades reales de un cliente.
* **Solución:** **NexusReal** es una aplicación web centralizada que organiza el catálogo de propiedades en un solo entorno estructurado, permitiendo búsquedas rápidas por criterios clave y controlando el acceso mediante roles y privilegios bien definidos.

---

## Metodología de Desarrollo en V (Rama Descendente)

Para el desarrollo de este proyecto, se ha implementado la metodología de desarrollo en V, centrándonos inicialmente en la **Fase de Verificación** (rama descendente). Este proceso asegura que cada etapa de construcción esté basada en una definición previa, clara y trazable.

### Etapas de la Fase Descendente:

1. **Análisis de Requisitos (Requirement Gathering):**
   En esta etapa se definieron las necesidades operativas de los asesores y usuarios finales, estableciendo las funcionalidades esenciales del sistema: registro e inicio de sesión, gestión centralizada de inmuebles, filtrado de propiedades y control de acceso por niveles de privilegio (**Administrador**, **Gestor**, **Usuario** y **Visitante**).
2. **Análisis del Sistema (System Analysis):**
   Se definió el comportamiento general del software, estableciendo cómo interactúan los datos, el flujo de navegación y las responsabilidades de cada rol dentro de la arquitectura funcional de NexusReal:
   * **Administrador:** Control total del sistema, gestión de cuentas, asignación de roles y administración de tablas desde Django Admin.
   * **Gestor:** Publicación, edición y actualización del estado de disponibilidad de las propiedades.
   * **Usuario:** Consulta y filtrado del catálogo de inmuebles disponibles para atender requerimientos de clientes.
   * **Visitante:** Acceso a la vista pública general de la plataforma sin privilegios internos de gestión.
3. **Diseño de Software / Arquitectura (Software Design):**
   Se seleccionó el stack tecnológico (**Python**, **Django**, **Docker**, **Vite.js** y **GitHub**) y se definieron los componentes principales: el backend en Django para la lógica de negocio y persistencia, el frontend estructurado con Vite.js y plantillas dinámicas (`templates`) según el rol activo, y la contenerización mediante Docker para garantizar un entorno reproducible.
4. **Diseño de Módulos (Module Design):**
   Se detalló la lógica interna de cada aplicación del proyecto (`core` y `usuarios`), definiendo los modelos de datos para perfiles de usuario, roles y propiedades, así como las vistas y reglas de permisos necesarias para la ejecución de cada tarea.

**Punto de Inflexión → Codificación (Coding):** Una vez completadas y validadas las etapas de diseño anteriores, se procede a la **Codificación**, iniciando la construcción real del código fuente mediante la configuración del entorno Docker, la creación del proyecto y aplicaciones en Django, el módulo de autenticación, la configuración de Django Admin y las plantillas diferenciadas por rol.

---

## Estructura del Proyecto y Entorno
* **Stack:** Python, Django, Vite.js, Docker y GitHub.
* **Módulos principales:**
  * `usuarios/`: Registro, inicio de sesión, gestión de roles y configuración en Django Admin.
  * `core/`: Vistas principales, lógica del sistema y enrutamiento por nivel de privilegio.
  * `templates/`: Plantillas HTML adaptadas para Administrador, Gestor, Usuario y Visitante.
  * `frontend/`: Base de interfaz con Vite.js.
* **Ejecución con Docker:**
  ```bash
  docker-compose up --build