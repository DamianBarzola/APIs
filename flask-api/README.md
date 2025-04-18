app/**init**.py: inicializa la app Flask, configura extensiones y registra blueprints.

config.py: configuración por entorno (desarrollo, producción).

models/: definición de los modelos de base de datos (SQLAlchemy).

routes/: controladores/blueprints que definen los endpoints.

services/: lógica de negocio (separada de los controladores).

schemas/: serialización y validación (por ejemplo, con Marshmallow).

utils/: funciones auxiliares (ej: autenticación, manejo de errores).

extensions.py: inicialización de cosas como SQLAlchemy, JWT, CORS, etc.

migrations/: para manejar cambios en la base de datos.

tests/: pruebas unitarias o de integración.

run.py: corre la app (puede llamarse también main.py si preferís).
