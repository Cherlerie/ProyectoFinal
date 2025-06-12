# Bienvenido a RDexperience

Una página web de reservas turísticas. Este proyecto integra **diseño web moderno**, y **base de datos MySQL**, permitiendo a los usuarios **buscar**, **conocer** y **reservar** experiencias turísticas.

---

## 📌 Descripción del Proyecto

El objetivo principal del proyecto es proporcionar una **plataforma web funcional y atractiva** para la gestión de reservas turísticas. Incluye:

- **Página de Inicio**: búsqueda, ofertas turísticas, y contacto.
- **Página de Descripción**: información detallada de las actividades.
- **Página de Reservas**: formulario para reservar, con contacto y detalles de pago.
- **Base de Datos MySQL**: almacenamiento seguro de las reservas.

---

## 📁 Estructura del Proyecto
├── .states/ # Estados del frontend
├── .web/ # Archivos de interfaz web
├── assets/ # Recursos estáticos (imágenes, íconos, etc.)
├── turismo_app/ # Aplicación principal
│ ├── init.py
│ ├── database.py
│ ├── descripcion_acuario_nacional.py
│ ├── descripcion_bahiaAguilas.py
│ ├── descripcion_cayolevantado.py
│ ├── descripcion_cuevaspomier.py
│ ├── descripcion_islacatalina.py
│ ├── descripcion_PlayaElValle.py
│ ├── descripcion.py
│ ├── lista.py
│ ├── reservas_acuario_nacional.py
│ ├── reservas_admin.py
│ ├── reservas_bahia_de_las_aguilas.py
│ ├── reservas_cayo_levantado.py
│ ├── reservas_cuecas_pomier.py
│ ├── reservas_isla_catalina.py
│ ├── reservas_playa_el_valle.py
│ ├── reservas.py
│ └── turismo_app.py
├── venv/ # Entorno virtual de Python
├── .gitignore
├── README.md
├── requirements.txt # Dependencias del proyecto
└── rxconfig.py # Configuración Reflex

## ▶️ Ejecución

Clonar el repositorio con :
```bash
git clone https://github.com/tuusuario/reflex-reservas.git
```

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

Por ultimo, ejecuta el servidor con:
```bash
reflex run