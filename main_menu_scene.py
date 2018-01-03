# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from instructions_scene import *
from game_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.JPG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        # add logo to top of screen
        logo_position = self.CENTRE_OF_SCREEN
        logo_position.y = self.size.y - 170
        self.space_ninja_logo = SpriteNode('./assets/sprites/space_ninja_logo.PNG',
                                           parent = self,
                                           position = logo_position,
                                           size = self.size / 1.5)
        #add play label
        play_label_position = self.CENTRE_OF_SCREEN
        play_label_position.y = self.size.y - 300
        self.play_label = LabelNode(text = "Play",
                                    font = ('ChalkboardSE-Light', 70),
                                    parent = self,
                                    position = play_label_position)
        #add settings label
        settings_label_position = self.CENTRE_OF_SCREEN
        settings_label_position.y = self.size.y - 400
        self.settings_label = LabelNode(text = "Settings",
                                        font = ('ChalkboardSE-Light', 70),
                                        parent = self,
                                        position = settings_label_position)
        # add instructions label
        instructions_label_position = self.CENTRE_OF_SCREEN
        instructions_label_position.y = self.size.y - 500
        self.instructions_label = LabelNode(text = "Instructions",
                                            font = ('ChalkboardSE-Light', 70),
                                            parent = self,
                                            position = instructions_label_position)
        # add credits label
        credits_label_position = self.CENTRE_OF_SCREEN
        credits_label_position.y = self.size.y - 600
        self.credits_label = LabelNode(text = "Credits",
                                       font = ('ChalkboardSE-Light', 70),
                                       parent = self,
                                       position = credits_label_position)
        # add all 4 arrow buttons
        play_arrow_button_position = self.CENTRE_OF_SCREEN
        play_arrow_button_position.x = 350
        play_arrow_button_position.y = self.size.y - 300
        self.play_arrow_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                       parent = self,
                                       position = play_arrow_button_position,
                                       size = self.size / 10)
        settings_arrow_button_position = self.CENTRE_OF_SCREEN
        settings_arrow_button_position.x = 285
        settings_arrow_button_position.y = self.size.y - 400
        self.settings_arrow_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                       parent = self,
                                       position = play_arrow_button_position,
                                       size = self.size / 10)
        instructions_arrow_button_position = self.CENTRE_OF_SCREEN
        instructions_arrow_button_position.x = 220
        instructions_arrow_button_position.y = self.size.y - 500
        self.instructions_arrow_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                       parent = self,
                                       position = instructions_arrow_button_position,
                                       size = self.size / 10)
        credits_arrow_button_position = self.CENTRE_OF_SCREEN
        credits_arrow_button_position.x = 290
        credits_arrow_button_position.y = self.size.y -600
        self.credits_arrow_button = SpriteNode('./assets/sprites/arrow_button.PNG',
                                       parent = self,
                                       position = credits_arrow_button_position,
                                       size = self.size / 10)
        
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
        if self.play_arrow_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        if self.instructions_arrow_button.frame.contains_point(touch.location):
            self.present_modal_scene(InstructionsScene())
        # pass
    
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
    
