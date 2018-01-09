# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
from pause_scene import *

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        self.slider_scale_size = 0.4
        
        # add space background
        self.background = SpriteNode('./assets/sprites/space_background.JPG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        # slider
        slider_position = self.CENTRE_OF_SCREEN
        slider_position.x = 65
        self.slider = SpriteNode('./assets/sprites/slider.PNG',
                                 position = slider_position,
                                 parent = self,
                                 alpha = 0.5,
                                 scale = self.slider_scale_size)
        self.slider_cursor_position = self.CENTRE_OF_SCREEN
        self.slider_cursor_position.y = self.size.y / 2
        self.slider_cursor_position.x = 63
        self.slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                        position = self.slider_cursor_position,
                                        parent = self,
                                        scale = 0.2,
                                        alpha = 0.6)
        # kick button
        kick_button_position = self.CENTRE_OF_SCREEN
        kick_button_position.x = self.size.x - 110
        kick_button_position.y = 70
        self.kick_button = SpriteNode('./assets/sprites/kick_button.PNG',
                                      parent = self,
                                      position = kick_button_position,
                                      scale = 0.25,
                                      alpha = 0.7)
        # pause button
        pause_button_position = self.CENTRE_OF_SCREEN
        pause_button_position.x = self.size.x - 60
        pause_button_position.y = self.size.y - 60
        self.pause_button = SpriteNode('./assets/sprites/pause_button.PNG',
                                       parent = self,
                                       position = pause_button_position,
                                       scale = 0.4,
                                       alpha = 0.5)
        
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
        if self.pause_button.frame.contains_point(touch.location):
            self.present_modal_scene(PauseScene())
    
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
    
