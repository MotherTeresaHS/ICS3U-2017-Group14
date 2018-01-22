# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the gave over screen.

from scene import *
import ui
import config
from game_scene import *
from main_menu_scene import *

class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add space background
        self.background = SpriteNode('./assets/sprites/dark_space_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        
        
        # paused title
        game_over_label_position = self.CENTRE_OF_SCREEN
        game_over_label_position.y = self.size.y - 100
        self.game_over_label = LabelNode(text = "Game Over",
                                      font = ('ChalkboardSE-Light', 120),
                                      parent = self,
                                      position = game_over_label_position)
        
        
        # main menu label
        main_menu_label_position = self.size / 2
        self.main_menu_label = LabelNode(text = "Main menu",
                                         position = main_menu_label_position,
                                         parent = self,
                                         font = ('ChalkboardSE-Light', 80))
        
        
        # main menu game button
        main_menu_button_position = Vector2()
        main_menu_button_position.x = 220
        main_menu_button_position.y = self.size.y / 2
        self.main_menu_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                             position = main_menu_button_position,
                                             parent = self,
                                             scale = 0.15)
        
        
        # score
        score_label_position = Vector2()
        score_label_position.x = self.size.x / 4
        score_label_position.y = self.size.y - 260
        self.score_label = LabelNode("Score: " + str(config.score),
                                     position = score_label_position,
                                     parent = self,
                                     font = ('ChalkboardSE-Light', 60))
        
        
        # highscore
        if config.score > config.high_score:
            config.high_score = config.score
        
        
        # highscore label
        highscore_label_position = Vector2()
        highscore_label_position.x = (self.size.x * 3 / 4) - 50
        highscore_label_position.y = self.size.y - 260
        self.highscore_label = LabelNode("Highscore: " + str(config.high_score),
                                         position = highscore_label_position,
                                         parent = self,
                                         font = ('ChalkboardSE-Light', 60))
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #pass
        
        # main menu button
        if self.main_menu_button.frame.contains_point(touch.location) or self.main_menu_label.frame.contains_point(touch.location):
            # change game status to over then close scene
            config.game_over = True
            self.dismiss_modal_scene()
        
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
