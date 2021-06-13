#API

POST /api/v1/team
Obtiene los jugadores de un equipo sin importar si se escribe en minúscula o mayúscula.
Ejemplo de request:
```
{
    “Name” : “real madrid”,
    “Page” : 1
}
```
Ejemplo de response:
```
{
    “Page”: 1,
    “totalPages: 2
    “Items”: 10,
    “totalItems”:20,
    “Players” : [
        { name: “Marcelo”, “position”: “LB”, “nation” : “Brazil” },
        ...
    ]
}
```

GET /api/v1/players
Busca los jugadores que contengan el String en los campos del nombre del jugador, ya sea una coincidencia parcial o total, y sin importar si es mayúscula o minúscula.
El order puede ser asc o desc y define el orden a partir del nombre alfabéticamente, por default sera asc (si no se recibe en la url).

Ejemplo: /api/v1/players?search=cristi&order=asc&page=1

Respuesta:
```
{
    “Page”: 1,
    “totalPages:1,
    “Items”: 10,
    “totalItems”:10,
    “Players” : [
    {name: “Cristiano Ronaldo”, “position”: “ST”, “nation” : “Portugal” ,   “team”: “Juventus” },
    ...
    ]
}
```

##Ejecutar aplicación

Crear archivo .env con el siguiente contenido ajustando según configuración local

```
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
DEBUG= # True or False
API_KEY=
```

Levantar api por primera vez:
```docker-compose up --build```

Ejecutar migraciones:
```make migrate```

Cargar fixtures:

```make load_fixtures```

Consultar api de fifa para llenar base de datos local:

```make populate_db```

Ejecutar tests:

```make test```

