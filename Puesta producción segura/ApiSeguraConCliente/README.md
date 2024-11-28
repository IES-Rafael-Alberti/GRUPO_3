# API web con CORS, seguridad (JWT) y cliente (React o Vue)

## Indice

1. Aegurar la API (CORS y Token JWT)

- JWT:

  Función que crea los tokens a los usuarios con JWT ([utils.py](peticiones-fastAPI\utils\utils.py))

      def create_access_token(data: dict, expires_delta: timedelta = None):
          to_encode = data.copy()
          if expires_delta:
              expire = datetime.utcnow() + expires_delta
          else:
              expire = datetime.utcnow() + timedelta(minutes=60)
          to_encode.update({"exp": expire})
          encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
          return encoded_jwt

- CORS

  Implementacion CORS ([main.py](peticiones-fastAPI\main.py))

      app.add_middleware(
          CORSMiddleware,
          allow_origins=["https://fastapi-client.netlify.app"],
          allow_credentials=True,
          allow_methods=["*"],
          allow_headers=["*"],
      )

2.  Desarrollo del cliente (Vue)

Estructura del cliente:

        |-- src
            |-- assets (CSS e imagenes)
            |-- components
                |-- Header.vue (Componente del header de la página)
                |-- Footer.vue (Componente del footer de la página)
            |-- router
                |-- index.js (no se ni pa que lo he puesto si solo es una pagina XD)
            |-- stores
                |-- userStore.js (Donde se guarda la info del usuario que tiene la sesion iniciada, lo mas importante el token)
            |-- views
                |-- HomeView.vue (Vista de la página, donde esta el html y toda la logica)
        main.js (js que Vue usa para montar la app)
        App.vue (archivo principal donde de agrupa todo: Header, RouterView (en este caso solo la vista del home) y Footer)

### Hecho por:

- Víctor Jiménez
- Israel Valderrama
- Alejandro Seoane
