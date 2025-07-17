# Diagnóstico Médico con Redes Bayesianas

Este proyecto es un sistema de apoyo al diagnóstico médico que utiliza **redes bayesianas** para estimar la probabilidad de diversas enfermedades respiratorias a partir de síntomas ingresados por el usuario.

## 🚀 Tecnologías utilizadas
- **Python 3.11**
- **FastAPI** (backend y API REST)
- **pgmpy** (modelado de redes bayesianas)
- **Uvicorn** (servidor ASGI)
- **HTML, CSS, JavaScript** (frontend simple)
- **Docker** (opcional para despliegue)

## 🩺 ¿Cómo funciona?
El usuario selecciona síntomas en la interfaz web. El frontend envía estos datos al backend, que utiliza una red bayesiana para calcular la probabilidad de enfermedades como COVID-19, Bronquitis, Faringitis, Neumonía y Tuberculosis. El resultado se muestra de forma clara y ordenada.

## 📦 Instalación y ejecución local

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/DiagnosticoRB.git
   cd DiagnosticoRB
   ```
2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```
3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicia el servidor:**
   ```bash
   python app.py
   ```

## 🌐 Cómo abrir la interfaz web

Puedes abrir la interfaz gráfica de usuario de dos formas:

### Opción 1: Usando la extensión **Live Server** de VSCode
1. Instala la extensión "Live Server" en Visual Studio Code.
2. Haz clic derecho sobre el archivo `index.html` y selecciona **"Open with Live Server"**.
3. Se abrirá tu navegador en una dirección como `http://127.0.0.1:5500/index.html` y podrás interactuar con la app.

### Opción 2: Abrir directamente el archivo
- También puedes abrir `index.html` haciendo doble clic sobre él, pero algunas funciones pueden no funcionar correctamente si el navegador restringe las peticiones locales. Se recomienda usar Live Server o cualquier servidor local.

## 🐳 Despliegue con Docker

1. **Construye la imagen:**
   ```bash
   docker build -t diagnostico-rb .
   ```
2. **Ejecuta el contenedor:**
   ```bash
   docker run -p 8000:8000 diagnostico-rb
   ```
3. **Accede a la API:**
   - [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI para pruebas)
   - Abre `index.html` para la interfaz web.

## 🧪 Pruebas de la API
Puedes probar el endpoint `/infer` desde Swagger UI o usando herramientas como Postman, Insomnia o cURL. Ejemplo de JSON de entrada:

```json
{
  "evidence": {
    "Fiebre": 1,
    "Tos": 1,
    "Dolor_de_garganta": 0,
    "Dificultad_respiratoria": 0,
    "Dolor_en_el_pecho": 0,
    "Fatiga": 0,
    "Sudores_nocturnos": 0,
    "Perdida_de_peso": 0,
    "Hemoptisis": 0
  }
}
```

## 📋 Notas
- Este sistema es solo una herramienta de apoyo y **no reemplaza el diagnóstico médico profesional**.
- Puedes modificar la red bayesiana en `models.py` para adaptarla a otros escenarios.

---

**Desarrollado por [Tu Nombre o Usuario de GitHub]**
