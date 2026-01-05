# Sistema Experto - Diagnóstico de Fallas en Computadoras

Sistema experto web para diagnóstico técnico de fallas en computadoras con una base de conocimientos de 500 reglas.

## Características

- 🔍 **Búsqueda inteligente** por síntomas y condiciones
- 📊 **Filtrado avanzado** por categoría y nivel de certeza
- 🎯 **500 reglas** de diagnóstico organizadas por categorías
- 💡 **Interfaz moderna** y responsiva
- 📱 **Diseño responsive** para móviles y tablets

## Categorías de Diagnóstico

1. **Fuente de Poder** (50 reglas)
2. **Motherboard / Placa Madre** (60 reglas)
3. **Procesador / CPU** (40 reglas)
4. **Memoria RAM** (50 reglas)
5. **Almacenamiento - HDD/SSD** (60 reglas)
6. **Tarjeta Gráfica / GPU** (60 reglas)
7. **Refrigeración / Cooling** (40 reglas)
8. **Sistema Operativo y Software** (50 reglas)
9. **Red y Conectividad** (40 reglas)
10. **Periféricos** (40 reglas)
11. **Portátiles / Laptops** (30 reglas)
12. **Mantenimiento, Prevención y Varios** (20 reglas)

## Instalación

### Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**
```bash
python app.py
```

4. **Abrir en el navegador:**
```
http://127.0.0.1:5000
```

## Uso

### Búsqueda Básica

1. Escribe síntomas o condiciones en el campo de búsqueda (ej: `computadora_no_enciende`, `pantalla_azul`)
2. Presiona Enter o haz clic en "Buscar"
3. Las reglas que coincidan se mostrarán ordenadas por relevancia

### Filtros

- **Por Categoría:** Selecciona una categoría específica para filtrar resultados
- **Por Certeza:** Ajusta el slider para mostrar solo reglas con certeza mínima deseada

### Ver Detalles

Haz clic en cualquier tarjeta de regla para ver información detallada en un modal.

## Estructura del Proyecto

```
proyect/
├── app.py                 # Servidor Flask principal
├── knowledge_base.py      # Base de conocimientos (500 reglas)
├── requirements.txt       # Dependencias Python
├── README.md              # Este archivo
├── templates/
│   └── index.html        # Interfaz HTML
└── static/
    ├── css/
    │   └── style.css     # Estilos CSS
    └── js/
        └── app.js        # Lógica JavaScript
```

## API Endpoints

- `GET /` - Página principal
- `GET /api/rules` - Obtener todas las reglas
- `POST /api/search` - Buscar reglas por condiciones
- `GET /api/rules/<id>` - Obtener regla específica
- `GET /api/categories` - Obtener todas las categorías
- `GET /api/filter` - Filtrar reglas

## Ejemplo de Búsqueda

**Búsqueda:** `computadora_no_enciende pantalla_negra`

**Resultado:** Reglas relacionadas con problemas de encendido y video, ordenadas por relevancia y certeza.

## Notas

- El sistema busca coincidencias parciales en las condiciones
- Los resultados se ordenan por porcentaje de coincidencia y nivel de certeza
- Las reglas con mayor certeza (≥80%) son más confiables

## Desarrollo

Para desarrollo local con recarga automática:

```bash
export FLASK_ENV=development
python app.py
```

## Licencia

Este proyecto es para uso educativo y técnico.

## Autor

Sistema Experto - Electivo II Sistemas Expertos

