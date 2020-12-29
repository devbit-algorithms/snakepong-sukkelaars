# SnakePONG™®

## Intro

We present you, SnakePONG™®! A mix between the legendary games,
Snake (1997) and Pong (1972)! If that doesn't sound like a recipe for epicness, we don't know what will.

---

## The Rules

You, the player, will play as the snake and try to score into the computer's "goal".

**_BUT_** there is a _twist_ !

You can also try and eat some delicious candy while playing which will increase the length of your snake.

Watch out though, while it might make it easier to hit the ball, you will get tangled up more quickly and possibly **LOSE** the game!

---

## Features

1. **_Unparalleled gameplay_**
2. **_Fully controllable snake_**
3. **:candy: _LOTS OF CANDY_ :candy:**

---

## Installation

To install this project and make sure you can enjoy the full SnakePONG™® experience as intended by its creators, please follow the steps below precisely.

1. Clone into the GitHub repository

You can easily clone into the GitHub repository or classroom called *snakepong-sukkelaars* with the commands below.
The GitHub Classroom is called the way it is because the creators of the game used to be real programming *sukkelaars*, but have become real professionals!

```bash
git clone [the password-protected SSH key/the web URL - goes here]
```

2. Installing the necessary libraries

Use the commands below to install the necessary libraries for running the game in its full madness. 
Please make sure you are using the latest version of *pip* and *python* to run these commands, you can check this [here](https://pip.pypa.io/en/stable/installing/)!

```bash
pip install pygame pygame-menu collision
```

After you have succeeded in installing everything correctly you can head over to the next item on the list: **How to actually play the game?**

## How to play

Playing this is game is as easy as passing the exams of mister Cordemans at the Vives Hogeschool in Bruges - but wait ... Which mister Cordemans and which exams are we talking about :o

Nevermind let's not get sidetracked here because starting up the game is rather easy, but is playing the game as easy? Only time will tell - ay guess that's life, not?

To play the game simply open up the the location of the repo in any CLI (PowerShell or Windows Terminal are confirmed to be working) and use the command below to fire up the game!

```bash
python ./src/main.py
```

## Components

### Main.py

The first step of our code. We simply call for the menu to be opened

### Menus.py

Launching the game first takes you to our neat menu, here you can change the settings, your name or press "play" to begin enjoying the new GOTY of Python games.

![snakepong Menu](images/snakepong_menu.png)

#### Settings

If you were to go into the settings, you can change a bunch of stuff.

Want to play with a friend? That's possible! Just click on the "Players" option to increase the player count to 2!

Had enough of the funky soundtrack or the sound effects? Disable them by the click of a button!

We would've liked to also implement difficulty levels and different playing fields but due to time strain and other assignments we had to cut our losses. Still, we are very happy how our game ended up looking!

![snakepong Settings](images/settings.png)

### Playfield.py

The name says it all, here we made our playingfield including the borders.

### Entities.py

Here we have programmed all our interactive objects, how the ball moves and bounces, how our :candy: spawns, how our snake is made and controlled and how the paddle moves on its own!

**_FUN FACT: For our snake we've used a corrupted DLL file!_**

#### The snake

![snakepong Game](images/snake.png)

#### The paddle

![snakepong Game](images/paddle.png)

#### The candy

![snakepong Game](images/candy.png)

#### The ball

![snakepong Game](images/ball.png)

### Game.py

This is where the main game loop takes place and where all our code comes together in one nice little package.

![snakepong Game](images/snakepong_game.png)

---

## Trajectory

==Done== | ==Feature== | ==Difficulty==
:---: | ---- | ----
 ✔️ | Playing Field | :star:
 ✔️ | Snake | :star::star:
 ✔️ | Candy | :candy::candy:
 ✔️ | Ball | :star::star::star:
 ✔️ | Menu | :star:
 ✔️ | AI | :star::star::star:
  