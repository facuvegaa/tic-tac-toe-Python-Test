# tic-tac-toe-Python-Test
Technical test for Python Developer job.

The project consist in develop an API that lets you play the tic-tac-toe game,
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

Build images from application and database.
```bash
docker-compose build
```

Make and run the migrations
```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Run the generated images.
```bash
docker-compose up
```

## API Reference


#### Create a game

```http
  POST localhost:8000/api/create_game/
```

| Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `player1` | `array` | **Required** |
| `player2` | `array` | **Required** |
| `next_turn` | `sring` | **Required** |

Returns a response with the data of the game:
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
Returns a response with all the games:
```JSON
{
[
    {
        "id": 1,
        "player1": [
            "Facu",
            "P"
        ],
        "player2": [
            "Benja",
            "T"
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
    },
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
]
}
```
  
#### Delete a game

```http
  DELETE localhost:8000/api/delete_game/{id}
```
Delete the game by id.
  

#### Retrive a game

```http
  DELETE localhost:8000/api/delete_game/{id}
```
Retrive a game by id:

```JSON
    {
        "id": 1,
        "player1": [
            "Facu",
            "P"
        ],
        "player2": [
            "Benja",
            "T"
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

#### Update a game
```http
  POST localhost:8000/api/update_game/{id}
```
| Parameters | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `player` | `string` | **Required** |
| `row` | `string` | **Required** |
| `column` | `sring` | **Required** |

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
    "next_turn": "Pedro",
    "movements_played": 1,
    "winner": "",
    "board": [
        [
            "O",
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