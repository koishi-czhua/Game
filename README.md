# PlaneGame
#### Video Demo:  <https://youtu.be/AXnYCZr_t9A>
#### Description:This project is a simple 2D game based on Pygame. Players need to control an aircraft and keep their health points alive for as long as possible by avoiding enemy aircraft and bullets from enemy aircraft. The design concept of this game is simple and fun, so that players can enjoy the game in a short time.

#### In the game, the movement of the aircraft is a very important part. Players can use the up, down, left and right arrow keys to control the movement of the aircraft to avoid collisions with enemy aircraft and bullets. In order to increase the challenge of the game, the aircraft cannot fly outside the screen, which requires players to control the movement of the aircraft more precisely.

#### The generation of enemy aircraft is also a major feature of the game. There are two types of enemy aircraft in the game, ordinary enemy aircraft and Benemy enemy aircraft. They cycle across the screen and have randomly varying movement speeds. When the enemy planes reach the bottom of the screen, they will be refreshed at the top of the screen, thus forming a continuous loop of enemy planes, providing players with a continuous challenge.

#### The firing of bullets is the main attack method of Benemy enemy aircraft. In the game, the Benemy enemy will fire bullets at a certain frequency, and players need to dodge these bullets to maintain the health of the aircraft. This design increases the tension and challenge of the game.

#### The aircraft's health and invincibility are important mechanisms to protect players. The aircraft has a certain health value, and every time it collides with an enemy aircraft or bullet, the health value will be reduced. In order to prevent players from losing lives due to continuous collisions in a short period of time, a period of invincibility is designed. During this period, the aircraft will not receive any damage.

#### The game's menu and game end interface are the entrance and exit of the game. When the game starts, a menu is displayed and the player can choose to start or quit the game. When the game is over, a game over interface will be displayed, and the player can choose to return to the main menu. The design of these two interfaces makes the beginning and end of the game smoother and more friendly.

#### The structure of the project mainly consists of two parts: the main loop and the class definition. The main loop is the core of the game. It continuously detects user input and various events, and executes corresponding logic based on the status of the game (menu, game in progress, game over). Class definition is the basis of the game, including Bullet class, Enemy class and Benermy class. The Bullet class manages the properties and behavior of bullets, the Enemy class manages the properties and behavior of enemy aircraft, including position reset, and the Benermy class is a subclass of the Enemy class, which has additional bullet launching logic.

#### The game's screen drawing uses the Pygame library. Through Pygame, we can easily draw game elements such as aircraft, enemy aircraft, bullets, and health points, making the visual effects of the game richer and more vivid.

#### Although this project is a simple aircraft shooting game framework, it has a lot of room for expansion and optimization. For example, we could add multiple enemy types and boss types, each with unique behaviors and attacks. We can also introduce more game elements, such as bonus items, level systems, etc., to enhance the depth and interest of the game. In addition, we can also optimize graphics and animation effects to enhance the visual experience of the game.

#### All in all, this project is a starting point for me as a coding beginner. I have learned a lot during the project production process. At the same time, I hope my works can also give you some inspiration.
