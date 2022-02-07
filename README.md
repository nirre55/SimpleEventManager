## SimpleEventManager
### Introduction
* SimpleEventManager est une api crée avec Flask (Un micro framework open-source de développement web en Python.)
* Les données sont enregistré dans fichier JSON qui sera crée avec la class Event (src/main/python/package/api/event.py)
* Le fortmat du fichier JSON est comme suit : 
```JSON
{
    "events": [
        {
            "id": 0,
            "title": "Festival de music",
            "content": "Lancement du plus grand festivale de music",
            "start_date": "2023/01/01 15:00:00",
            "end_date": "2023/01/30 15:00:00",
            "timezone": "CET"
        },
        {
            "id": 1,
            "title": "Festival de music 1",
            "content": "Lancement du plus grand festivale de music 1",
            "start_date": "2023/01/01 15:00:00",
            "end_date": "2023/01/30 15:00:00",
            "timezone": "CET"
        },
        {
            "id": 2,
            "title": "Festival de music 2",
            "content": "Lancement du plus grand festivale de music 2",
            "start_date": "2023/01/01 15:00:00",
            "end_date": "2023/01/30 15:00:00",
            "timezone": "CET"
        }
    ]
}
```
* Chaque Event a un identifiant qui est incrémenté automatiquement et une timezone pour chaque utilisateur(créateur de l'événement).
* Lors du lancement (src/main/python/package/api/api_event.py) Flask vas crée un serveur de developpement en local sur le port 5000 (par défaut) : http://127.0.0.1:5000

### Les endpoints crée sont: 
Verbes HTTP  | Endpoints  |  Request Parameters  |   Request Body   
------------- | ------------- | ------------- | -------------
POST  | /api/v1/resources/events   |  //   | obligatoire
PUT  | /api/v1/resources/events/{id}  | obligatoire ex : /events?id=12  |  obligatoire
GET  | /api/v1/resources/events/{id}  | obligatoire ex : /events?id=47  |  //
DELETE  | /api/v1/resources/events/{id}  | obligatoire ex : /events?id=25  |  //
 

exmple de body a ajouté pour une requete POST : 
 ```JSON
{
"title": "First Event",
"content": "The a content of first event"
"start_date": "2023/01/01 15:00:00",
"end_date": "2023/01/30 15:00:00",
}
```


