# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the credits

from scene import *
import ui

class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add background image
        self.background = SpriteNode('./assets/sprites/space_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        
        
        # page title
        credits_label_position = self.CENTRE_OF_SCREEN
        credits_label_position.y = self.size.y - 100
        self.credits_label = LabelNode(text = "Credits",
                                            font = ('ChalkboardSE-Light', 100),
                                            parent = self,
                                            position = credits_label_position)
        
        
        # developer, teacher, school, artwork and sound
        developer_label_position = self.CENTRE_OF_SCREEN
        developer_label_position.x = self.size.x - 700
        developer_label_position.y = self.size.y - 270
        self.developer_label = LabelNode(text = "Developer: Jenny Trac",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = developer_label_position)
        
        
        teacher_label_position = self.CENTRE_OF_SCREEN
        teacher_label_position.x = self.size.x - 730
        teacher_label_position.y = self.size.y - 350
        self.teacher_label = LabelNode(text = "Teacher: Mr. Coxall",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = teacher_label_position)
        
        
        school_label_position = self.CENTRE_OF_SCREEN
        school_label_position.x = self.size.x - 510
        school_label_position.y = self.size.y - 430
        self.school_label = LabelNode(text = "School: St. Mother Teresa High School",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = school_label_position)
        
        
        artwork_label_position = self.CENTRE_OF_SCREEN
        artwork_label_position.x = self.size.x - 490
        artwork_label_position.y = self.size.y - 510
        self.artwork_label = LabelNode(text = "Artwork: Becca Schroer and Jenny Trac",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = artwork_label_position)
        
        
        sound_label_position = self.CENTRE_OF_SCREEN
        sound_label_position.x = 240
        sound_label_position.y = self.size.y - 590
        self.sound_label = LabelNode(text = "Sound: iMovie",
                                     font = ('ChalkboardSE-Light', 50),
                                     parent = self,
                                     position = sound_label_position)
        
        
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
        
        #back button
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
    
