# tic-tac-toe-Python-Test
Technical test for Python Developer job.

The project consist in develop an API that lets you play the tic-tac-toe game,
validate the board and return the winner, a message saying it was a tie, or an error if
there was some kind of problem with the input data.

## Run Locally

The version of python that the project is using is 3.9 so lets create a virtual enviroment 

Clone the project.
```bash
git clone https://github.com/facuvegaa/tic-tac-toe-Python-Test.git
```

Go to the project directory.
```bash
cd tic-tac-toe-Python-Test
```

The version of python that the project is using is 3.9 so lets create a virtual enviroment. I use Pyenv and Pyenv-virtualenv to do it, in order to install this tools check the links, anyways you can use any tool to create your own Virtual Enviroment.
```
https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv-virtualenv
```

Build images from application and database.
```bash
  docker-compose build
```

Run the migrations
```bash
  docker-compose run web python manage.py migrate
```

Run the generated images.
```bash
  docker-compose up
```

