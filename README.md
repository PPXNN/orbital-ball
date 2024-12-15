# Orbital Ball   :
This is a game where a player can jump across platforms, avoid balls, and gain score points. 
---
## Project description:

- **Platform Jumping:**  
   The player jumps between platforms to avoid falling balls.  
- **Score Points:**  
   Earn points by successfully landing on platforms.  
- **Progressive Levels:**  
   The game gets harder with more falling balls and platform movement as you on the next level. 

### Feature:
- **Character Movement:**  
   - Move left using the **`a`** key.  
   - Move right using the **`d`** key.  
   - Jump using the **`space`** key.  

- **Dynamic Environment:**  
   - Randomly generated platforms for each level.  
   - Falling balls with increasing speed based on time and level.  

- **Game Progression:**  
   - Track your score with successful landings.  
   - New levels appear when you reach the top of the screen.  
   - Platforms start moving randomly from level 8.

- **Summary Screen:**  
   - Show your final score.  
   - Includes **Play Again** and **Quit** buttons.  

---

## How to install and run the project:

### Requirement:
    -Python 3.7+
- Libraries:  
  - **`turtle`**  
  - **`tkinter`**  
  - **`random`**

### Step to run:
1. Clone or download this project:  
   If you want to clone the repository, use the following command:  
   ```bash  
   git clone https://github.com/PPXNN/orbital-ball.git  
   ```  

2. Go to the `orbital-ball` folder or use the following command:  
   ```bash  
   cd orbital-ball  
   ```  

3. Run the game on the folder or use the following command:  
   ```bash  
   python game.py  
   ```  
4. The gameplay instructions:  
   - **Press `a`** to move left.  
   - **Press `d`** to move right.  
   - **Press `space`** to jump.  

---

## Usage:

- **Open the Game:**  
   Start at the bottom of the screen as the player. 

- **Control:**  
   Use the **`a`**, **`d`**, and **`space`** keys to move and jump. 

- **Score Points:**  
   Land on platforms successfully to gain points.  

- **Avoid Falling Balls:**  
   Dodge the balls, which fall randomly and speed up over time and levels.  

- **Game Over:**  
   The game ends if the player is hit by a ball. A summary screen will display your score.  

---

### Demo Video:
[**Watch on YouTube**](https://www.youtube.com/watch?v=_D0tETIOY_8) 

---

## Project design and implementation:

### UML Diagram:  
![UML Diagram](UML%20DIAGRAM.png)  

### Class Player:
- Represents the player character.  
- Allows left/right movement and jumping.  
- **Interaction:**  
  - Interacts with `Platform` objects when landing.  
  - Interacts with `Ball` objects when hit.  

### Class Platform:
- Represents platforms where the player can jump and land.  
- Platforms can move randomly from level 8 and up.  
- **Interaction:**  
  - Allows `Player` to jump and land. 

### Class Ball:
- Represents falling balls.  
- Balls bounce horizontally and fall at increasing speed.  
- **Interaction:**  
  - Ends the game if `Player` comes too close. 

### Class Game:
- Controls all gameplay elements, including player, platforms, and balls.  
- Handles score updates, level changes, and game-over conditions.  
- **Interaction:**  
  - Manages interactions between `Player`, `Platform`, and `ball`.  

---

### How I use/extend/modify the provided baseline code:
1. Modifying ball to make it random falling and bouncing side to side.
2. Modifying paddle to make it able to jump on and make it move.

---

### Known Bugs:
- **Quit Button Issue:** Sometimes, clicking the "Quit" button on the summary screen may cause an error. 

--- 

## Project Sophistication Level  

**Self-Rated Sophistication Level:** 90  
    





