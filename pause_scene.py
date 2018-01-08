# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the pause screen.

from scene import *
import ui
from game_scene import *
from main_menu_scene import *

class PauseScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add space background
        self.background = SpriteNode('./assets/sprites/dark_space_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        # paused title
        paused_label_position = self.CENTRE_OF_SCREEN
        paused_label_position.y = self.size.y - 100
        self.paused_label = LabelNode(text = "Paused",
                                      font = ('ChalkboardSE-Light', 120),
                                      parent = self,
                                      position = paused_label_position)
        # resume game label
        resume_game_label_position = self.CENTRE_OF_SCREEN
        resume_game_label_position.y = self.size.y - 350
        self.resume_game_label = LabelNode(text = "Resume game",
                                           font = ('ChalkboardSE-Light', 70),
                                           parent = self,
                                           position = resume_game_label_position)
        # resume game button
        resume_game_button_position = self.CENTRE_OF_SCREEN
        resume_game_button_position.x = 220
        resume_game_button_position.y = resume_game_label_position.y
        self.resume_game_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                             position = resume_game_button_position,
                                             parent = self,
                                             scale = 0.15)
        # return to main menu label
        main_menu_label_position = self.CENTRE_OF_SCREEN
        main_menu_label_position.x = self.size.x / 2
        main_menu_label_position.y = self.size.y - 450
        self.main_menu_label = LabelNode(text = "Main menu",
                                           font = ('ChalkboardSE-Light', 70),
                                           parent = self,
                                           position = main_menu_label_position)
        # return to main menu button
        main_menu_button_position = self.CENTRE_OF_SCREEN
        main_menu_button_position.x = 260
        main_menu_button_position.y = main_menu_label_position.y
        self.main_menu_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                             position = main_menu_button_position,
                                             parent = self,
                                             scale = 0.15)
        
        
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
        if self.resume_game_button.frame.contains_point(touch.location) or self.resume_game_label.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        #if self.main_menu_button.frame.contains_point(touch.location):
        #    self.dismiss_modal_scene()
        #    self.dismiss_modal_scene() # somehow return to main menu? still need to figure this out
    
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
    
