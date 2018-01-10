# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the settings scene

from scene import *
import ui
import time

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        self.sound_setting = True
        self.display_slider_setting = True
        self.character_setting = 'classic'
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.JPG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        # page title
        settings_label_position = self.CENTRE_OF_SCREEN
        settings_label_position.y = self.size.y - 100
        self.settings_label = LabelNode(text = "Settings",
                                            font = ('ChalkboardSE-Light', 100),
                                            parent = self,
                                            position = settings_label_position)
        #sound
        sound_label_position = self.CENTRE_OF_SCREEN
        sound_label_position.x = self.size.x - 850
        sound_label_position.y = self.size.y - 270
        self.sound_label = LabelNode(text = "Sound",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = sound_label_position)
        sound_slider_position = self.CENTRE_OF_SCREEN
        sound_slider_position.x = self.size.x - 650
        sound_slider_position.y = self.size.y - 260
        self.sound_slider = SpriteNode('./assets/sprites/yes_no_slider.PNG',
                                  position = sound_slider_position,
                                  parent = self,
                                  scale = 0.2,
                                  alpha = 0.7)
        self.sound_slider_cursor_position = self.CENTRE_OF_SCREEN
        self.sound_slider_cursor_position.x = self.size.x - 690
        self.sound_slider_cursor_position.y = self.size.y - 275
        self.sound_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                         parent = self,
                                         position = self.sound_slider_cursor_position,
                                         scale = 0.15,
                                         alpha = 0.8)
        #display slider
        displayslider_label_position = self.CENTRE_OF_SCREEN
        displayslider_label_position.x = self.size.x - 760
        displayslider_label_position.y = self.size.y - 340
        self.displayslider_label = LabelNode(text = "Display slider",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = displayslider_label_position)
        display_slider_position = self.CENTRE_OF_SCREEN
        display_slider_position.x = self.size.x - 500
        display_slider_position.y = self.size.y - 330
        self.display_slider = SpriteNode('./assets/sprites/yes_no_slider.PNG',
                                  position = display_slider_position,
                                  parent = self,
                                  scale = 0.2,
                                  alpha = 0.7)
        self.display_slider_cursor_position = self.CENTRE_OF_SCREEN
        self.display_slider_cursor_position.x = self.size.x - 540
        self.display_slider_cursor_position.y = self.size.y - 345
        self.display_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                         parent = self,
                                         position = self.display_slider_cursor_position,
                                         scale = 0.15,
                                         alpha = 0.8)
        #characters
        characteroptions_label_position = self.CENTRE_OF_SCREEN
        characteroptions_label_position.x = self.size.x - 710
        characteroptions_label_position.y = self.size.y - 410
        self.characteroptions_label = LabelNode(text = "Character options:",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = characteroptions_label_position)
        classicgingerbat_label_position = self.CENTRE_OF_SCREEN
        classicgingerbat_label_position.x = self.size.x - 520
        classicgingerbat_label_position.y = self.size.y - 700
        self.classicgingerbat_label = LabelNode(text = "Classic Ninja      Ginger Ninja      Bat Ninja",
                                    font = ('ChalkboardSE-Light', 40),
                                    parent = self,
                                    position = classicgingerbat_label_position)
        
        # classic ninja
        classic_ninja_position = self.CENTRE_OF_SCREEN
        classic_ninja_position.x = 200
        classic_ninja_position.y = 200
        self.classic_ninja = SpriteNode('./assets/sprites/classic_ninja/c1.PNG',
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.1)
        # ginger ninja
        ginger_ninja_position = self.CENTRE_OF_SCREEN
        ginger_ninja_position.x = 540
        ginger_ninja_position.y = 200
        self.ginger_ninja = SpriteNode('./assets/sprites/ginger_ninja/g1.PNG',
                                    parent = self,
                                    position = ginger_ninja_position,
                                    scale = 0.1)
        # bat ninja
        bat_ninja_position = self.CENTRE_OF_SCREEN
        bat_ninja_position.x = self.size.x - 210
        bat_ninja_position.y = 200
        self.bat_ninja = SpriteNode('./assets/sprites/bat_ninja/b1.PNG',
                                    parent = self,
                                    position = bat_ninja_position,
                                    scale = 0.1)
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
        #pass
        if self.sound_setting == False:
            # change sound setting slider to off
            #print("sound off")
            self.sound_slider_cursor.remove_from_parent()
            self.sound_slider_cursor_position.x = self.size.x - 610
            self.sound_slider_cursor_position.y = self.size.y - 275
            self.sound_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                                  parent = self,
                                                  position = self.sound_slider_cursor_position,
                                                  scale = 0.15,
                                                  alpha = 0.8)
        if self.sound_setting == True:
            # change sound setting slider to on
            #print("sound on")
            self.sound_slider_cursor.remove_from_parent()
            self.sound_slider_cursor_position.x = self.size.x - 690
            self.sound_slider_cursor_position.y = self.size.y - 275
            self.sound_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                                  parent = self,
                                                  position = self.sound_slider_cursor_position,
                                                  scale = 0.15,
                                                  alpha = 0.8)
        if self.display_slider_setting == False:
            # change display slider setting to off
            self.display_slider_cursor.remove_from_parent()
            self.display_slider_cursor_position.x = self.size.x - 460
            self.display_slider_cursor_position.y = self.size.y - 345
            self.display_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                                  parent = self,
                                                  position = self.sound_slider_cursor_position,
                                                  scale = 0.15,
                                                  alpha = 0.8)
        if self.display_slider_setting == True:
            # change display slider setting to on
            self.display_slider_cursor.remove_from_parent()
            self.display_slider_cursor_position.x = self.size.x - 540
            self.display_slider_cursor_position.y = self.size.y - 345
            self.display_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                                  parent = self,
                                                  position = self.sound_slider_cursor_position,
                                                  scale = 0.15,
                                                  alpha = 0.8)
        
    
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
            
        # sound slider
        if self.sound_slider.frame.contains_point(touch.location):
            #print("sound slider clicked")
            if self.sound_setting == True:
                self.sound_setting = False
            elif self.sound_setting == False:
                self.sound_setting = True
        
        # display slider
        if self.display_slider.frame.contains_point(touch.location):
            #print("display slider pressed")
            if self.display_slider_setting == True:
                self.display_slider_setting = False
            elif self.display_slider_setting == False:
                self.display_slider_setting = True
        
        # changing characters options and animating them but only for 1 cycle
        if self.classic_ninja.frame.contains_point(touch.location):
            self.character_setting = 'classic'
            print(self.character_setting)
            classic_counter = 1
            while classic_counter <= 8:
                self.animate_classic_ninja(classic_counter)
                time.sleep(0.1)
                classic_counter = classic_counter + 1
        if self.ginger_ninja.frame.contains_point(touch.location):
            self.character_setting = 'ginger'
            print(self.character_setting)
        if self.bat_ninja.frame.contains_point(touch.location):
            self.character_setting = 'bat'
            print(self.character_setting)
        
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
    
    def animate_classic_ninja(self, classic_count):
        # animates the classic ninja
        #pass
        print(classic_count)
        # takes out existing sprite
        self.classic_ninja.remove_from_parent()
        # shows next sprite
        classic_ninja_file = "./assets/sprites/classic_ninja/c" + str(classic_count) + ".PNG"
        classic_ninja_position = self.CENTRE_OF_SCREEN
        classic_ninja_position.x = 200
        classic_ninja_position.y = 200
        self.classic_ninja = SpriteNode(classic_ninja_file,
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.1)
        
