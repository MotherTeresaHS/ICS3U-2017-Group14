# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the instructions.

from scene import *
import ui

class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        
        
        # page title
        instructions_label_position = self.CENTRE_OF_SCREEN
        instructions_label_position.y = self.size.y - 100
        self.instructions_label = LabelNode(text = "Instructions",
                                            font = ('ChalkboardSE-Light', 100),
                                            parent = self,
                                            position = instructions_label_position)
        
        
        # how to instructions
        howtoplay_label_position = self.CENTRE_OF_SCREEN
        howtoplay_label_position.x = self.size.x - 800
        howtoplay_label_position.y = self.size.y - 270
        self.howtoplay_label = LabelNode(text = "How to play:",
                                    font = ('ChalkboardSE-Light', 60),
                                    parent = self,
                                    position = howtoplay_label_position)
        
        
        howtoslider_label_position = self.CENTRE_OF_SCREEN
        howtoslider_label_position.x = self.size.x - 510
        howtoslider_label_position.y = self.size.y - 400
        self.howtoslider_label = LabelNode(text = "Use slider on the left side to move ninja up and down.",
                                    font = ('ChalkboardSE-Light', 40),
                                    parent = self,
                                    position = howtoplay_label_position)
        
        
        howtoasteroids_label_position = self.CENTRE_OF_SCREEN
        howtoasteroids_label_position.x = self.size.x - 500
        howtoasteroids_label_position.y = self.size.y - 470
        self.howtoasteroids_label = LabelNode(text = "When meteors appear, either kick them or avoid them.",
                                    font = ('ChalkboardSE-Light', 40),
                                    parent = self,
                                    position = howtoasteroids_label_position)
        
        
        # back button
        back_arrow_button_position = self.CENTRE_OF_SCREEN
        back_arrow_button_position.x = 120
        back_arrow_button_position.y = self.size.y - 100
        self.back_arrow_button = SpriteNode('./assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_arrow_button_position,
                                       size = self.size / 8)
        
    
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
        
        # back button
        if self.back_arrow_button.frame.contains_point(touch.location):
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
    
