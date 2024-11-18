from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def read_root():
    return "<html><body><h1>Este es el docker de fastAPI para mas info ve a /info</h1></body></html>"

@app.get("/info",response_class=HTMLResponse)
def read_info()->str:
    return """
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;">
        <h1>FastAPI</h1>
        
        <p>FastAPI es un moderno y rápido framework web para construir APIs con Python 3.7+ basado en estándares abiertos para APIs. Aquí tienes una visión general de sus características principales:</p>
        
        <h2>Rendimiento</h2>
        <p>FastAPI ofrece un rendimiento muy alto, comparable al de NodeJS y Go, gracias a que está construido sobre Starlette y Pydantic. Esto lo hace uno de los frameworks Python más rápidos disponibles.</p>
        
        <h2>Facilidad de uso</h2>
        <ul>
            <li><strong>Intuitivo y fácil de aprender:</strong> FastAPI está diseñado para ser fácil de usar y aprender, con una sintaxis clara y concisa.</li>
            <li><strong>Menos errores:</strong> Reduce la posibilidad de errores humanos al proporcionar validación de datos y serialización automática.</li>
        </ul>
        
        <h2>Características avanzadas</h2>
        <ul>
            <li><strong>Basado en estándares:</strong> Utiliza y es totalmente compatible con los estándares abiertos para APIs, como OpenAPI (anteriormente conocido como Swagger) y JSON Schema.</li>
            <li><strong>Documentación automática:</strong> Genera automáticamente documentación interactiva de API (con Swagger UI) y esquemas JSON alternativos.</li>
            <li><strong>Validación de datos:</strong> Proporciona validación automática de datos de solicitud y respuesta.</li>
            <li><strong>Anotaciones de tipo:</strong> Aprovecha las anotaciones de tipo de Python para la validación, serialización y documentación.</li>
        </ul>
        
        <h2>Desarrollo rápido</h2>
        <ul>
            <li><strong>Rápido de codificar:</strong> Aumenta la velocidad de desarrollo al reducir alrededor del 40% de los errores humanos inducidos por desarrolladores.</li>
            <li><strong>Autocompletado:</strong> Ofrece soporte completo para editores con autocompletado en todas partes.</li>
        </ul>
        
        <h2>Producción lista</h2>
        <ul>
            <li><strong>Basado en Starlette:</strong> Incluye todas las características de Starlette, como WebSocket support, GraphQL, tareas en segundo plano, sesiones, pruebas basadas en pytest, CORS, Cookie Sessions, y más.</li>
            <li><strong>Basado en Pydantic:</strong> Utiliza Pydantic para la validación de datos, serialización y documentación (como esquemas OpenAPI).</li>
        </ul>
        
        <h2>Extensibilidad</h2>
        <p>FastAPI es altamente extensible, permitiendo la integración con muchas bibliotecas y herramientas del ecosistema Python.</p>
        
        <h2>Comunidad y soporte</h2>
        <p>FastAPI tiene una comunidad activa y creciente, con abundante documentación y recursos disponibles para los desarrolladores.</p>
        
        <p>FastAPI se ha vuelto cada vez más popular para el desarrollo de APIs en Python debido a su combinación de rendimiento, facilidad de uso y características avanzadas. Es especialmente adecuado para proyectos que requieren APIs rápidas y robustas con un tiempo de desarrollo reducido.</p>
    </body>
    </html>
    """