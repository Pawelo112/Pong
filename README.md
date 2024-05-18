# 🎮 Pong
![Screenshot from the game.](https://github.com/Pawelo112/Pong/assets/121107616/608fcbc5-12d2-4bb7-8388-ff69568b2c20)

## 📖 Description and rules
This is a classic Pong game that I made in Python using Turtle module, during **100 days of code** Python course.

The rules are the same as in classic legendary Pong:
+ 🕹️Left paddle is controlled by the W and S; and the right paddle is controlled by ⬆️ and ⬇️ keys - the best way to play is to play with friend🙋‍♂️, each one of you controls one paddle.
+ ⏬You can either hold or click the buttons to move the paddle up or down.
+ 🏅Your goal is to block the incoming ball with the paddle and make it bounce to the other side.
+ ⏩Velocity of the ball increases after each bounce.
+ ➖1️⃣ **When ball goes out of bounds (behind your paddle) you lose a point.**
+ ❌If you want to exit the game just close the app window.

## 📁 Files description
+ **[main.py](https://github.com/Pawelo112/Pong/blob/main/main.py)** - Main file of the app. Here the objects for paddle, ball and screen are being created and collision is being detected. From the important things you can edit screen size here or change how much the ball should speed up after each bounce.
  
+ **[ball.py](https://github.com/Pawelo112/Pong/blob/main/ball.py)** - Here the ball object is being represented. You can change the shape or the color of the ball and add any new ball behaviour that you want.
  
+ **[scoreboard.py](https://github.com/Pawelo112/Pong/blob/main/scoreboard.py)** - This file contains all methods connected to the scoreboard like updating score and displaying it at the top of the screen. You can change the font or displayed text here.
  
+ **[paddle.py](https://github.com/Pawelo112/Pong/blob/main/paddle.py)** - This file collects all methods and things connected to the paddle. Here you can change paddle size or where it is located. You can also change by how many pixels paddle moves up or down (25 by default).

## 🖥️ Usage
You can find the latest release here: [releases](https://github.com/Pawelo112/Pong/releases)  
You can download exe file to play and test the game or whole source code to edit this game on your own 🤓.  

Unfortunately windows defender and other anti-viruses detects **Pong.exe** file as a virus because it was made with pyinstaller and it is known issue with exe files made with it and there isn't much that I can do about it at the moment.

## 📝 License

Copyright © 2024 [Paweł Marcinkowski](https://github.com/Pawelo112).  
This project is [MIT](https://github.com/Pawelo112/Pong/blob/main/LICENSE) licensed.
