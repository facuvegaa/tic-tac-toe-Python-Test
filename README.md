# tic-tac-toe-Python-Test
Technical test for Python Developer job.

The project consist on develop an API that lets you play the tic-tac-toe game,
validate the board and return the winner, a message saying it was a tie, or an error if
there was some kind of problem with the input data.

## Run Locally

Clone the project.
```bash
git clone https://github.com/facuvegaa/tic-tac-toe-Python-Test.git
```

Go to the project directory.
```bash
cd tic-tac-toe-Python-Test
```

Build images from the application and database.
```bash
docker-compose build
```

Run the generated images.
```bash
docker-compose up
```

CTRL+C to stop and run the migrations.
```bash
docker-compose run web python manage.py migrate
```

Run the tests.
```bash
docker-compose run web python manage.py test
```

Run the generated images again.
```bash
docker-compose up
```


## API Reference


#### Create a game

```http
  POST localhost:8000/api/create_game/
```

| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `player1` | `array` | ["Facu", "X"] | **Required** |
| `player2` | `array` | ["Benja", "O"] | **Required** |
| `next_turn` | `sring` | "Benja" | **Required** |

Returns a response with the data of the created game:
```JSON
{
    "id": 1,
    "player1": [
        "Facu",
        "X"
    ],
    "player2": [
        "Benja",
        "O"
    ],
    "next_turn": "Benja",
    "movements_played": 0,
    "winner": "",
    "board": [
        [
            null,
            null,
            null
        ],
        [
            null,
            null,
            null
        ],
        [
            null,
            null,
            null
        ]
    ],
    "is_finished": false
}
```

#### Get all games

```http
  GET localhost:8000/api/get_all_games/
```
Returns a response with all the games.

#### Get finished games

```http
  GET localhost:8000/api/get_finished_games/
```
Returns a response with all the finished games.

#### Get active games
```http
  GET localhost:8000/api/get_active_games/
```
Returns a response with all the active game. 

#### Delete a game

```http
  DELETE localhost:8000/api/delete_game/{id}
```
Delete the game by id.
  

#### Retrive a game

```http
  GET localhost:8000/api/delete_game/{id}
```
Retrive a game by id

#### Update a game
```http
  POST localhost:8000/api/update_game/{id}
```
| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `player` | `string` | "Pedro" | **Required** |
| `row` | `string` | "0" | **Required** |
| `column` | `sring` | "0" | **Required** |

The squares of the board are counted as in computer science, for example the square of the first row on the left would be row="0" and column="0"

Update the state of the game:
```JSON
{
    "id": 2,
    "player1": [
        "Pedro",
        "X"
    ],
    "player2": [
        "Pablo",
        "O"
    ],
    "next_turn": "Pablo",
    "movements_played": 1,
    "winner": "",
    "board": [
        [
            "X",
            null,
            null
        ],
        [
            null,
            null,
            null
        ],
        [
            null,
            null,
            null
        ]
    ],
    "is_finished": false
}
```
## Tech Stack

**Language:**
- Python

**Database:**
- PostgresSQL

**Others:**
- Docker Compose

  
## Author

- [@FacundoVega](https://github.com/facuvegaa)