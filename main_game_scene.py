# Created by : Sidney Kang
# Created on : 11 Oct. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_07
# This scene displays the main game scene

from scene import * 
import ui

class MainGameScene(Scene):
    def setup(self):
        # This method is called when user moves to this scene
        
        self.missiles = []
        self.aliens = []
          
        self.center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.ship_move_speed = 20.0
         
        # Add background
        self.background = SpriteNode('./assets/sprites/star_background.PNG',
                                      position = self.size/2, 
                                      parent = self,
                                      size = self.size)

        spaceship_position = self.center_of_screen
        spaceship_position.y = 100                                           
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                     parent = self,
                                     position = spaceship_position)
                                  
        left_button_position = self.center_of_screen
        left_button_position.y = 100
        left_button_position.x = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.5)
        
        right_button_position = self.center_of_screen
        right_button_position.y = 100
        right_button_position.x = 300
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                        parent = self,
                                        position = right_button_position,
                                        alpha = 0.5) 
                                                                                                 
        red_button_position = self.size
        red_button_position.y = 100
        red_button_position.x =  red_button_position.x - 100
        self.red_button = SpriteNode('./assets/sprites/red_button.PNG',
                                      parent = self,
                                      position = red_button_position,
                                      alpha = 0.5) 
                                                                     
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # Move spaceship if button pressed
        if self.left_button_down == True :
            self.spaceship.run_action(Action.move_by(-1*self.ship_move_speed, 0.0, 0.1))
        if self.right_button_down == True :
            self.spaceship.run_action(Action.move_by(self.ship_move_speed, 0.0, 0.1))	   
              
    
    def touch_began(self, touch):
              # This method is called, when user touches the screen
              
        # Check if left or right button was pressed
        if self.left_button.frame.contains_point(touch.location):
           self.left_button_down = True
                 
        if self.right_button.frame.contains_point(touch.location):
           self.right_button_down = True
            
    def touch_ended(self, touch):
    # this method is called, when user releases a finger from the screen
    
    # If finger is removed then no matter what, spaceship should not move
        self.left_button_down = False
        self.right_button_down = False
        
    # If red button pressed new missile is fired
        if self.red_button.frame.contains_point(touch.location):
           self.create_new_missile()
           
    def create_new_missile(self):
        # When user presses red button
        
        missile_start_position = self.spaceship.position
        missile_start_position.y = 150
        
        missile_end_position = self.size
        missile_end_position.x = missile_start_position.x
        
        self.missiles.append(SpriteNode('./assets/sprites/missiles.PNG',
                                        position = missile_start_position,
                                        parent = self))
                                        
        # Make missiles move forwards
        missileMoveAction = Action.move_to(missile_end_position.x, 
                                       missile_end_position.y + 100,
                                       5.0)               
                                       
        self.missiles[len(self.missiles)-1].run_action(missileMoveAction)
