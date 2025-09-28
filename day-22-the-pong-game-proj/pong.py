"""
Complete Pong Game using Python Turtle Graphics with Sound Effects
Features:
- Single player vs AI mode
- Two player local multiplayer mode
- Simple menu system
- Score tracking and win conditions
- Sound effects for all game events
"""

import turtle
import random
import sys

# Import sound module based on platform
try:
    if sys.platform.startswith('win'):
        import winsound
        SOUND_AVAILABLE = True
    else:
        # For Linux/Mac, try to import playsound or use os.system
        try:
            import playsound
            SOUND_AVAILABLE = True
        except ImportError:
            import os
            SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("Sound effects not available on this system")


class SoundManager:
    """Handle sound effects for the game"""
    
    @staticmethod
    def play_paddle_hit():
        """Play sound when ball hits paddle"""
        if SOUND_AVAILABLE:
            try:
                if sys.platform.startswith('win'):
                    # High-pitched beep for paddle hit
                    winsound.Beep(800, 100)  # 800 Hz for 100ms
                else:
                    # For Linux/Mac - use system beep or tone
                    os.system('echo -e "\a"')  # System beep
            except:
                pass  # Silently fail if sound doesn't work
    
    @staticmethod
    def play_wall_hit():
        """Play sound when ball hits wall"""
        if SOUND_AVAILABLE:
            try:
                if sys.platform.startswith('win'):
                    # Medium-pitched beep for wall hit
                    winsound.Beep(600, 80)  # 600 Hz for 80ms
                else:
                    os.system('echo -e "\a"')
            except:
                pass
    
    @staticmethod
    def play_score():
        """Play sound when player scores"""
        if SOUND_AVAILABLE:
            try:
                if sys.platform.startswith('win'):
                    # Lower-pitched beep for scoring
                    winsound.Beep(400, 200)  # 400 Hz for 200ms
                else:
                    os.system('echo -e "\a"')
            except:
                pass
    
    @staticmethod
    def play_win():
        """Play sound when game is won"""
        if SOUND_AVAILABLE:
            try:
                if sys.platform.startswith('win'):
                    # Victory melody - three ascending tones
                    winsound.Beep(500, 150)
                    winsound.Beep(600, 150)  
                    winsound.Beep(700, 300)
                else:
                    # Multiple beeps for victory
                    for _ in range(3):
                        os.system('echo -e "\a"')
            except:
                pass


class Paddle:
    def __init__(self, x, y, width, height):
        """Initialize a paddle at the given position"""
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(x, y)
        
        # Stretch the paddle to desired size
        self.turtle.shapesize(stretch_wid=height/20, stretch_len=width/20)
        
        self.speed = 5
        
    def set_ai_speed(self, speed):
        """Set different speed for AI paddle"""
        self.speed = speed
        
    def move_up(self):
        """Move paddle up"""
        y = self.turtle.ycor()
        if y < 250:  # Keep paddle on screen
            self.turtle.sety(y + self.speed)
            
    def move_down(self):
        """Move paddle down"""
        y = self.turtle.ycor()
        if y > -250:  # Keep paddle on screen
            self.turtle.sety(y - self.speed)


class Ball:
    def __init__(self, speed=1.5):
        """Initialize the ball with configurable speed"""
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(0, 0)

        # Set initial random direction with configurable speed
        self.base_speed = speed
        self.dx = random.choice([-self.base_speed, self.base_speed])
        self.dy = random.choice([-self.base_speed, self.base_speed])

    def set_speed(self, speed):
        """Update ball speed while maintaining direction"""
        # Calculate current direction (normalized)
        current_dir_x = 1 if self.dx > 0 else -1
        current_dir_y = 1 if self.dy > 0 else -1

        # Apply new speed with same direction
        self.base_speed = speed
        self.dx = current_dir_x * self.base_speed
        self.dy = current_dir_y * self.base_speed

    def move(self):
        """Move the ball"""
        new_x = self.turtle.xcor() + self.dx
        new_y = self.turtle.ycor() + self.dy
        self.turtle.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse vertical direction"""
        self.dy *= -1

    def bounce_x(self):
        """Reverse horizontal direction"""
        self.dx *= -1

    def reset_position(self):
        """Reset ball to center with random direction"""
        self.turtle.goto(0, 0)
        self.dx = random.choice([-self.base_speed, self.base_speed])
        self.dy = random.choice([-self.base_speed, self.base_speed])


class PongGame:
    def __init__(self):
        # Game settings
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.PADDLE_WIDTH = 20
        self.PADDLE_HEIGHT = 100
        self.BALL_SIZE = 20
        self.WINNING_SCORE = 5

        # Ball speed settings (configurable)
        self.BALL_SPEED_SLOW = 1.0
        self.BALL_SPEED_NORMAL = 1.5  # Default
        self.BALL_SPEED_FAST = 2.0
        self.BALL_SPEED_VERY_FAST = 2.5
        self.current_ball_speed = self.BALL_SPEED_NORMAL
        
        # Game state
        self.game_mode = None  # "single", "two_player", or None (menu)
        self.player1_score = 0
        self.player2_score = 0
        self.game_running = False
        self.frame_count = 0  # For periodic focus checks

        # Key state tracking for continuous movement
        self.keys_pressed = {
            'w': False, 'W': False,
            's': False, 'S': False,
            'Up': False, 'Down': False
        }

        # Focus management tracking
        self.last_focus_check = 0
        self.focus_recovery_attempts = 0
        
        # Initialize screen FIRST (without keyboard bindings)
        self.setup_screen_basic()
        
        # Initialize game objects AFTER screen
        self.paddle1 = Paddle(-350, 0, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.paddle2 = Paddle(350, 0, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.paddle2.set_ai_speed(7)  # Make AI paddle faster than player
        self.ball = Ball(self.current_ball_speed)
        
        # Score display
        self.score_turtle = turtle.Turtle()
        self.score_turtle.speed(0)
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(0, 260)
        
        # NOW setup keyboard bindings after all objects exist
        self.setup_keyboard_bindings()
        
    def setup_screen_basic(self):
        """Initialize the basic game screen with Turtle graphics"""
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.screen.tracer(0)  # Turn off animation for better performance
        
        # Try to bring window to front
        try:
            self.screen.getcanvas().winfo_toplevel().lift()
            self.screen.getcanvas().winfo_toplevel().attributes('-topmost', True)
            self.screen.getcanvas().winfo_toplevel().attributes('-topmost', False)
        except:
            pass  # If this fails, continue anyway
        
        # Set coordinate system
        self.screen.setworldcoordinates(-self.SCREEN_WIDTH//2, -self.SCREEN_HEIGHT//2,
                                       self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)

    # Key press/release handlers for continuous movement
    def key_pressed(self, key):
        """Handle key press events"""
        if key in self.keys_pressed:
            self.keys_pressed[key] = True

    def key_released(self, key):
        """Handle key release events"""
        if key in self.keys_pressed:
            self.keys_pressed[key] = False

    def handle_continuous_movement(self):
        """Handle continuous paddle movement based on pressed keys"""
        if hasattr(self, 'paddle1') and self.paddle1:
            # Player 1 movement (W/S - both cases for CapsLock)
            if self.keys_pressed['w'] or self.keys_pressed['W']:
                self.paddle1.move_up()
            if self.keys_pressed['s'] or self.keys_pressed['S']:
                self.paddle1.move_down()

        if hasattr(self, 'paddle2') and self.paddle2 and self.game_mode == "two_player":
            # Player 2 movement (only in two player mode)
            if self.keys_pressed['Up']:
                self.paddle2.move_up()
            if self.keys_pressed['Down']:
                self.paddle2.move_down()

    # Ball speed control methods
    def set_ball_speed_slow(self):
        """Set ball speed to slow"""
        self.current_ball_speed = self.BALL_SPEED_SLOW
        if hasattr(self, 'ball') and self.ball:
            self.ball.set_speed(self.current_ball_speed)

    def set_ball_speed_normal(self):
        """Set ball speed to normal"""
        self.current_ball_speed = self.BALL_SPEED_NORMAL
        if hasattr(self, 'ball') and self.ball:
            self.ball.set_speed(self.current_ball_speed)

    def set_ball_speed_fast(self):
        """Set ball speed to fast"""
        self.current_ball_speed = self.BALL_SPEED_FAST
        if hasattr(self, 'ball') and self.ball:
            self.ball.set_speed(self.current_ball_speed)

    def set_ball_speed_very_fast(self):
        """Set ball speed to very fast"""
        self.current_ball_speed = self.BALL_SPEED_VERY_FAST
        if hasattr(self, 'ball') and self.ball:
            self.ball.set_speed(self.current_ball_speed)

    def emergency_focus_recovery(self):
        """Emergency focus recovery when keyboard stops responding"""
        try:
            self.focus_recovery_attempts += 1
            print(f"Attempting focus recovery #{self.focus_recovery_attempts}")

            # Force window to front aggressively
            canvas = self.screen.getcanvas()
            root = canvas.winfo_toplevel()

            # Multiple recovery strategies
            root.deiconify()  # Ensure window is not minimized
            root.lift()       # Bring to front
            root.focus_force()  # Force focus to window
            canvas.focus_force()  # Force focus to canvas

            # Re-establish all keyboard bindings
            self.setup_keyboard_bindings()

            # Clear any stuck key states
            for key in self.keys_pressed:
                self.keys_pressed[key] = False

            print("Focus recovery completed")
            return True

        except Exception as e:
            print(f"Focus recovery failed: {e}")
            return False

    def setup_keyboard_bindings(self):
        """Setup keyboard controls based on current game mode"""
        self.screen.listen()

        # Menu controls (always available) - CapsLock independent
        self.screen.onkey(self.start_single_player, "1")
        self.screen.onkey(self.start_two_player, "2")
        self.screen.onkey(self.quit_game, "q")
        self.screen.onkey(self.quit_game, "Q")  # CapsLock support
        self.screen.onkey(self.return_to_menu, "m")
        self.screen.onkey(self.return_to_menu, "M")  # CapsLock support

        # Ball speed controls (during game) - avoid conflict with menu keys
        self.screen.onkey(self.set_ball_speed_slow, "z")
        self.screen.onkey(self.set_ball_speed_slow, "Z")
        self.screen.onkey(self.set_ball_speed_normal, "x")
        self.screen.onkey(self.set_ball_speed_normal, "X")
        self.screen.onkey(self.set_ball_speed_fast, "c")
        self.screen.onkey(self.set_ball_speed_fast, "C")
        self.screen.onkey(self.set_ball_speed_very_fast, "v")
        self.screen.onkey(self.set_ball_speed_very_fast, "V")

        # Emergency focus recovery key (F key)
        self.screen.onkey(self.emergency_focus_recovery, "f")
        self.screen.onkey(self.emergency_focus_recovery, "F")

        # Continuous movement with key press/release (CapsLock independent)
        if hasattr(self, 'paddle1') and self.paddle1:
            # Player 1 controls - both uppercase and lowercase for CapsLock
            self.screen.onkeypress(lambda: self.key_pressed('w'), "w")
            self.screen.onkeyrelease(lambda: self.key_released('w'), "w")
            self.screen.onkeypress(lambda: self.key_pressed('W'), "W")
            self.screen.onkeyrelease(lambda: self.key_released('W'), "W")

            self.screen.onkeypress(lambda: self.key_pressed('s'), "s")
            self.screen.onkeyrelease(lambda: self.key_released('s'), "s")
            self.screen.onkeypress(lambda: self.key_pressed('S'), "S")
            self.screen.onkeyrelease(lambda: self.key_released('S'), "S")

        if hasattr(self, 'paddle2') and self.paddle2:
            # Player 2 controls (only in two player mode)
            if self.game_mode == "two_player":
                self.screen.onkeypress(lambda: self.key_pressed('Up'), "Up")
                self.screen.onkeyrelease(lambda: self.key_released('Up'), "Up")
                self.screen.onkeypress(lambda: self.key_pressed('Down'), "Down")
                self.screen.onkeyrelease(lambda: self.key_released('Down'), "Down")
            elif self.game_mode == "single":
                # Disable Player 2 controls in single player mode (AI controlled)
                self.screen.onkeypress(None, "Up")
                self.screen.onkeyrelease(None, "Up")
                self.screen.onkeypress(None, "Down")
                self.screen.onkeyrelease(None, "Down")

        # Ensure window has keyboard focus for gameplay
        try:
            self.screen.getcanvas().focus_set()
            self.screen.getcanvas().focus_force()
        except:
            pass  # If focus setting fails, continue anyway
        
    def show_menu(self):
        """Display the main menu"""
        self.screen.clear()
        self.screen.bgcolor("black")
        
        # Create menu text turtle
        menu_turtle = turtle.Turtle()
        menu_turtle.hideturtle()
        menu_turtle.color("white")
        menu_turtle.penup()
        menu_turtle.speed(0)
        
        # Display title
        menu_turtle.goto(0, 150)
        menu_turtle.write("PONG GAME", align="center", font=("Arial", 32, "bold"))
        
        # Display menu options
        menu_turtle.goto(0, 50)
        menu_turtle.write("1 - Single Player (vs AI)", align="center", font=("Arial", 16, "normal"))
        
        menu_turtle.goto(0, 10)
        menu_turtle.write("2 - Two Player Mode", align="center", font=("Arial", 16, "normal"))
        
        menu_turtle.goto(0, -30)
        menu_turtle.write("Q - Quit Game", align="center", font=("Arial", 16, "normal"))
        
        # Display controls
        menu_turtle.goto(0, -80)
        menu_turtle.write("Controls:", align="center", font=("Arial", 14, "bold"))
        menu_turtle.goto(0, -110)
        menu_turtle.write("Player 1 (Left): W/S keys (CapsLock independent)", align="center", font=("Arial", 12, "normal"))
        menu_turtle.goto(0, -130)
        menu_turtle.write("Player 2 (Right): Arrow Up/Down keys", align="center", font=("Arial", 12, "normal"))
        menu_turtle.goto(0, -150)
        menu_turtle.write("Hold keys for continuous movement", align="center", font=("Arial", 11, "italic"))
        
        # Game rules
        menu_turtle.goto(0, -170)
        menu_turtle.write("Game Rules:", align="center", font=("Arial", 14, "bold"))
        menu_turtle.goto(0, -200)
        menu_turtle.write(f"First to {self.WINNING_SCORE} points wins!", align="center", font=("Arial", 12, "normal"))
        menu_turtle.goto(0, -220)
        menu_turtle.write("During game: Press M to return to menu", align="center", font=("Arial", 12, "normal"))

        # Ball speed controls
        menu_turtle.goto(0, -245)
        menu_turtle.write("Ball Speed: Z=Slow, X=Normal, C=Fast, V=Very Fast", align="center", font=("Arial", 11, "normal"))

        # Focus recovery help
        menu_turtle.goto(0, -265)
        menu_turtle.write("If controls stop working: Press F to fix focus", align="center", font=("Arial", 10, "italic"))

        # Sound effects info
        if SOUND_AVAILABLE:
            menu_turtle.goto(0, -290)
            menu_turtle.write("🔊 Sound effects enabled", align="center", font=("Arial", 10, "normal"))
        else:
            menu_turtle.goto(0, -290)
            menu_turtle.write("🔇 Sound effects not available", align="center", font=("Arial", 10, "normal"))
        
        # Re-establish keyboard bindings after screen.clear() reset them
        self.setup_keyboard_bindings()

        # Ensure screen has focus for keyboard input (especially important on Windows)
        try:
            self.screen.getcanvas().focus_force()
        except:
            pass  # If this fails, continue anyway

        # Force screen update
        self.screen.update()
        
    def start_single_player(self):
        """Start single player mode"""
        self.game_mode = "single"
        self.reset_scores()
        self.game_running = True
        self.setup_game()
        self.game_loop()
        print("Starting Single Player Mode")
        
    def start_two_player(self):
        """Start two player mode"""
        self.game_mode = "two_player"
        self.reset_scores()
        self.game_running = True
        self.setup_game()
        self.game_loop()
        print("Starting Two Player Mode")
        
    def setup_game(self):
        """Setup the game screen for playing"""
        self.screen.clear()
        self.screen.bgcolor("black")
        
        # Draw center line
        center_line = turtle.Turtle()
        center_line.speed(0)
        center_line.color("white")
        center_line.penup()
        center_line.hideturtle()
        center_line.goto(0, 300)
        center_line.setheading(270)
        center_line.pendown()
        for _ in range(15):
            center_line.forward(20)
            center_line.penup()
            center_line.forward(20)
            center_line.pendown()
            
        # Recreate all game objects after screen.clear() destroyed them
        self.paddle1 = Paddle(-350, 0, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.paddle2 = Paddle(350, 0, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.paddle2.set_ai_speed(7)  # Make AI paddle faster than player
        self.ball = Ball(self.current_ball_speed)

        # Recreate score display
        self.score_turtle = turtle.Turtle()
        self.score_turtle.speed(0)
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(0, 260)

        # Re-establish keyboard bindings with new paddle objects
        self.setup_keyboard_bindings()

        # Reset ball position and update score display
        self.ball.reset_position()
        self.update_score_display()
        
    def ai_move_paddle(self):
        """Improved AI for paddle 2 in single player mode"""
        if self.game_mode == "single":
            ball_x = self.ball.turtle.xcor()
            ball_y = self.ball.turtle.ycor()
            paddle_y = self.paddle2.turtle.ycor()
            
            # Only move when ball is coming towards AI paddle
            if self.ball.dx > 0:  # Ball moving right towards AI
                # More responsive AI - smaller dead zone
                if ball_y > paddle_y + 10:
                    self.paddle2.move_up()
                elif ball_y < paddle_y - 10:
                    self.paddle2.move_down()
            else:
                # When ball moving away, move towards center slowly
                center_y = 0
                if paddle_y > center_y + 30:
                    self.paddle2.move_down()
                elif paddle_y < center_y - 30:
                    self.paddle2.move_up()
                
    def game_loop(self):
        """Main game loop"""
        if self.game_running:
            self.ball.move()
            self.check_ball_collision()
            self.ai_move_paddle()

            # Handle continuous paddle movement
            self.handle_continuous_movement()

            # Aggressive focus management (every 0.5 seconds = 30 frames at 60 FPS)
            self.frame_count += 1
            if self.frame_count % 30 == 0:
                try:
                    # Multiple focus methods for better reliability
                    canvas = self.screen.getcanvas()
                    canvas.focus_set()
                    canvas.focus_force()

                    # Also try to bring window to front
                    root = canvas.winfo_toplevel()
                    root.lift()
                    root.attributes('-topmost', True)
                    root.attributes('-topmost', False)

                    # Re-establish screen listening (in case it got disconnected)
                    self.screen.listen()

                except Exception as e:
                    # If standard focus fails, try alternative methods
                    try:
                        self.screen.getcanvas().focus()
                        self.screen.listen()
                    except:
                        pass  # If all focus methods fail, continue anyway

            # Emergency focus recovery every 5 seconds (300 frames)
            if self.frame_count % 300 == 0:
                print(f"Performing emergency focus recovery at frame {self.frame_count}")
                self.emergency_focus_recovery()

            self.screen.update()
            self.screen.ontimer(self.game_loop, 16)  # ~60 FPS for smoother movement
        
    def quit_game(self):
        """Quit the game"""
        self.screen.bye()
        
    def reset_scores(self):
        """Reset player scores"""
        self.player1_score = 0
        self.player2_score = 0
        
    def update_score_display(self):
        """Update the score display"""
        self.score_turtle.clear()
        score_text = f"Player 1: {self.player1_score}  |  Player 2: {self.player2_score}"
        self.score_turtle.write(score_text, align="center", font=("Arial", 16, "normal"))
        
    def check_ball_collision(self):
        """Check ball collisions with walls and paddles"""
        ball_x = self.ball.turtle.xcor()
        ball_y = self.ball.turtle.ycor()
        
        # Ball collision with top and bottom walls
        if ball_y > 290 or ball_y < -290:
            self.ball.bounce_y()
            SoundManager.play_wall_hit()  # Play wall hit sound
            
        # Ball collision with paddles
        # Left paddle collision
        if (ball_x < -330 and ball_x > -350 and 
            ball_y < self.paddle1.turtle.ycor() + 50 and 
            ball_y > self.paddle1.turtle.ycor() - 50):
            self.ball.bounce_x()
            SoundManager.play_paddle_hit()  # Play paddle hit sound
            
        # Right paddle collision  
        if (ball_x > 330 and ball_x < 350 and
            ball_y < self.paddle2.turtle.ycor() + 50 and 
            ball_y > self.paddle2.turtle.ycor() - 50):
            self.ball.bounce_x()
            SoundManager.play_paddle_hit()  # Play paddle hit sound
            
        # Ball goes past left paddle - Player 2 scores
        if ball_x < -400:
            self.player2_score += 1
            self.ball.reset_position()
            self.update_score_display()
            SoundManager.play_score()  # Play score sound
            self.check_win_condition()
            
        # Ball goes past right paddle - Player 1 scores
        if ball_x > 400:
            self.player1_score += 1
            self.ball.reset_position()
            self.update_score_display()
            SoundManager.play_score()  # Play score sound
            self.check_win_condition()
            
    def check_win_condition(self):
        """Check if someone won"""
        if self.player1_score >= self.WINNING_SCORE:
            self.end_game("Player 1 Wins!")
        elif self.player2_score >= self.WINNING_SCORE:
            self.end_game("Player 2 Wins!")
            
    def end_game(self, winner_text):
        """End the game and show winner"""
        self.game_running = False
        
        # Play victory sound
        SoundManager.play_win()
        
        # Display winner
        winner_turtle = turtle.Turtle()
        winner_turtle.hideturtle()
        winner_turtle.color("yellow")
        winner_turtle.penup()
        winner_turtle.goto(0, 0)
        winner_turtle.write(winner_text, align="center", font=("Arial", 24, "bold"))
        
        # Show return to menu option
        winner_turtle.goto(0, -50)
        winner_turtle.color("white")
        winner_turtle.write("Press M to return to menu", align="center", font=("Arial", 14, "normal"))
        
        # Add return to menu key binding
        self.screen.onkey(self.return_to_menu, "m")
        
    def return_to_menu(self):
        """Return to the main menu"""
        self.game_mode = None
        self.game_running = False
        self.show_menu()


if __name__ == "__main__":
    try:
        # Start the game
        print("Starting Pong Game...")
        game = PongGame()
        print("Game object created successfully.")
        
        game.show_menu()
        print("Menu displayed. Pong Game initialized!")
        print("Press 1 for Single Player, 2 for Two Player, Q to quit.")
        print("If you don't see a game window, try clicking on the Python icon in your taskbar.")
        print("Window should be visible now - check your taskbar or try Alt+Tab")
        
        # Keep the game running
        game.screen.mainloop()
    except Exception as e:
        print(f"Error running the game: {e}")
        import traceback
        traceback.print_exc()