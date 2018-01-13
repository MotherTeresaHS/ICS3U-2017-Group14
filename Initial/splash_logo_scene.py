# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the splash scene with the game logo

from scene import *
import ui
import time
from main_menu_scene import *

class SplashLogoScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.JPG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        
        
        # add logo to centre of screen
        logo_position = self.CENTRE_OF_SCREEN
        logo_position.y = self.CENTRE_OF_SCREEN.y - 50
        self.space_ninja_logo = SpriteNode('./assets/sprites/space_ninja_logo.PNG',
                                           parent = self,
                                           position = logo_position,
                                           size = self.size)
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScene())
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
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
    
