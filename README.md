# PlaneGame
#### Video Demo:  <https://youtu.be/AXnYCZr_t9A>
#### Description:My project is a 2D shooter written in Python and the Pygame library. In this game, players need to control a plane, dodge enemy attacks, and survive as long as possible.

#### My game contains the following features

#### Player Controls: Players can use the direction keys to control the movement of the aircraft. The plane cannot fly off screen

#### Enemies: There are two types of enemies in the game, one is a red ordinary enemy, and the other is a purple enemy called "benermy", which can shoot bullets. The total number of all enemies is fixed at 5, but the flying speed of each enemy aircraft is random within a range, and will be refreshed above after flying out of the screen.

#### Collision Detection: The game detects if the aircraft collides with enemies or bullets. If the aircraft hits an enemy or a bullet, the aircraft's health will be reduced. At the same time, in order to prevent continuous damage after encountering the enemy aircraft, I added an invincibility time effect. The invincibility time was activated at the moment of encountering the enemy aircraft and lasted for about two seconds to avoid continuous collision determination.

#### Game state: The game has three states, namely "menu", "playing" and "game_over". Players can click "start" in the menu to start the game and "quit" to exit the game. They can also click "menu" after the "Game over" pops up after the aircraft's health value returns to zero to return to the menu interface.
