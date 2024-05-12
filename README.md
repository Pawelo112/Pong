# 🎮 Pong
![Screenshot from the game.](https://github.com/Pawelo112/Pong/assets/121107616/608fcbc5-12d2-4bb7-8388-ff69568b2c20)

## 📖 Description and rules
This is a classic Pong game that I made in Python using Turtle module, during **100 days of code** Python course.

The rules are the same as in classic legendary Pong:
+ 🕹️Left paddle is controlled by the W and S; and the right paddle is controlled by ⬆️ and ⬇️ keys - the best way to play is to play with friend🙋‍♂️, each one of you controls one paddle.
+ ⏬You can either hold or click the buttons to move the paddle up or down.
+ 🏅Your goal is to block the incoming ball with the paddle and make it bounce to the other side.
+ ⏩Velocity of the ball increases after each bounce.
+ ➖1️⃣**When the ball goes out of boud (behind your paddle) you lose a point.**
+ ❌If you want to exit the game just close the app window.

## 📁 Files description
+ **[main.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/main.py)** - Main file of the app. Here the objects for food, snake, scoreboard and screen are created and collision is being detected. From the important things you can edit screen size here or change the speed of the game.
  
+ **[food.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/food.py)** - Here the food object is being represented and its position and color is being randomized. You can add any colors to the colors list as long as Turtle module supports it.
  
+ **[scoreboard.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/scoreboard.py)** - This file contains all methods connected to the scoreboard like updating score and displaying **GAME OVER** screen.
  
+ **[snake.py](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/snake.py)** - This file collects all methods and things connected to the snake object like creating small snake at the start and adding new "segments" of it, which is used after eating one piece of food by snake.

## 📝 License

Copyright © 2024 [Paweł Marcinkowski](https://github.com/Pawelo112).  
This project is [MIT](https://github.com/Pawelo112/Simple-snake-game-in-Python/blob/main/LICENSE) licensed.
