# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the settings scene

from scene import *
import ui
import time
import config
import sound

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        
        self.test_counter = 1
        
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.PNG',
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
        
        
        #sound label
        sound_label_position = Vector2()
        sound_label_position.x = self.size.x - 850
        sound_label_position.y = self.size.y - 270
        self.sound_label = LabelNode(text = "Sound",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = sound_label_position)
        
        
        # sound slider
        sound_slider_position = Vector2()
        sound_slider_position.x = self.size.x - 650
        sound_slider_position.y = self.size.y - 260
        self.sound_slider = SpriteNode('./assets/sprites/yes_no_slider.PNG',
                                  position = sound_slider_position,
                                  parent = self,
                                  scale = 0.2,
                                  alpha = 0.7)
        
        
        # cursor for sound slider
        self.sound_slider_cursor_position = Vector2()
        self.sound_slider_cursor_position.x = self.size.x - 690
        self.sound_slider_cursor_position.y = self.size.y - 275
        self.sound_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                         parent = self,
                                         position = self.sound_slider_cursor_position,
                                         scale = 0.15,
                                         alpha = 0.8)
        
        
        #characters
        characteroptions_label_position = Vector2()
        characteroptions_label_position.x = self.size.x - 710
        characteroptions_label_position.y = self.size.y - 410
        self.characteroptions_label = LabelNode(text = "Character options:",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = characteroptions_label_position)
        
        
        # classic ninja
        classic_ninja_label_position = Vector2()
        classic_ninja_label_position.x = self.size.x / 5
        classic_ninja_label_position.y = 50
        classic_ninja_label = LabelNode(text = "Classic Ninja",
                                        font = ('ChalkboardSE-Light', 30),
                                        parent = self,
                                        position = classic_ninja_label_position)
        
        classic_ninja_position = Vector2()
        classic_ninja_position.x = self.size.x / 4
        classic_ninja_position.y = classic_ninja_label_position.y + 150
        self.classic_ninja = SpriteNode('./assets/sprites/classic_ninja/c1.PNG',
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.11)
        
        
        # ginger ninja
        ginger_ninja_label_position = Vector2()
        ginger_ninja_label_position.x = self.size.x / 2
        ginger_ninja_label_position.y = 50
        ginger_ninja_label = LabelNode(text = "Ginger Ninja",
                                        font = ('ChalkboardSE-Light', 30),
                                        parent = self,
                                        position = ginger_ninja_label_position)
        
        ginger_ninja_position = Vector2()
        ginger_ninja_position.x = ginger_ninja_label_position.x
        ginger_ninja_position.y = ginger_ninja_label_position.y + 150
        self.ginger_ninja = SpriteNode('./assets/sprites/ginger_ninja/g1.PNG',
                                    parent = self,
                                    position = ginger_ninja_position,
                                    scale = 0.1)
        
        
        # bat ninja
        bat_ninja_label_position = Vector2()
        bat_ninja_label_position.x = self.size.x * 4 / 5
        bat_ninja_label_position.y = 50
        bat_ninja_label = LabelNode(text = "Bat Ninja",
                                        font = ('ChalkboardSE-Light', 30),
                                        parent = self,
                                        position = bat_ninja_label_position)
        
        bat_ninja_position = Vector2()
        bat_ninja_position.x = self.size.x * 3 / 4
        bat_ninja_position.y = bat_ninja_label_position.y + 150
        self.bat_ninja = SpriteNode('./assets/sprites/bat_ninja/b1.PNG',
                                    parent = self,
                                    position = bat_ninja_position,
                                    scale = 0.1)
        
        
        # back button
        back_arrow_button_position = Vector2()
        back_arrow_button_position.x = 120
        back_arrow_button_position.y = self.size.y - 100
        self.back_arrow_button = SpriteNode('./assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_arrow_button_position,
                                       size = self.size / 8)
        
        
        # test animating
        test_ninja_position = Vector2()
        test_ninja_position.x = self.size.x - 100
        test_ninja_position.y = self.size.y - 100
        self.test_ninja = SpriteNode('./assets/sprites/classic_ninja/c1.PNG',
                                       parent = self,
                                       position = test_ninja_position,
                                       scale = 0.05)
        
        turtle_test_position = Vector2()
        turtle_test_position.x = self.size.x - 200
        turtle_test_position.y = self.size.y - 100
        self.turtle_test = SpriteNode('./assets/sprites/bigboi.GIF',
                                      parent = self,
                                      position = turtle_test_position,
                                      scale = 0.2)
        
        
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        #pass
        
        # if sound is off, cursor for slider should be on the right side
        if config.sound_setting == False:
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
        
        # if sound is on, cursor for slider should be on the left side
        if config.sound_setting == True:
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
        
        # show which ninja is selected for the game by showing it kicking and the others running
        
        if config.character_setting == 'classic':
            self.classic_ninja_kick()
        else:
            self.classic_run()
        
        if config.character_setting == 'ginger':
            self.ginger_ninja_kick()
        else:
            self.ginger_run()
        
        if config.character_setting == 'bat':
            self.bat_ninja_kick()
        else:
            self.bat_run()
        
        
    
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
            if config.sound_setting == True:
                config.sound_setting = False
                sound.stop_effect(config.background_music)
            elif config.sound_setting == False:
                config.sound_setting = True
                config.background_music = sound.play_effect('./assets/sounds/backgroundMusic.mp3',
                                                            volume = 0.2)
        
        # changing characters options and animating them but only for 1 cycle
        if self.classic_ninja.frame.contains_point(touch.location):
            config.character_setting = 'classic'
        if self.ginger_ninja.frame.contains_point(touch.location):
            config.character_setting = 'ginger'
            #print(config.character_setting)
        if self.bat_ninja.frame.contains_point(touch.location):
            config.character_setting = 'bat'
            #print(config.character_setting)
        
        
        
        
        # testing animation: this works
        if self.test_ninja.frame.contains_point(touch.location):
            print(self.test_counter)
            self.test_animating(self.test_counter)
            self.test_counter = self.test_counter + 1
            if self.test_counter > 8:
                self.test_counter = 1
        
        
#        # testing animation: this does not work
#        if self.test_ninja.frame.contains_point(touch.location):
#            while self.test_counter <= 8:
#                print(self.test_counter)
#                self.test_animating(self.test_counter)
#                self.test_counter = self.test_counter + 1
#                
#            self.test_counter = 1
        
        
        
    
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
    
    def classic_ninja_kick(self):
        # shows ninja kicking
        
        # take out running ninja
        self.classic_ninja.remove_from_parent()
        
        #kicking ninja properties
        c_ninja_kick_file = './assets/sprites/classic_ninja/ckick.PNG'
        kick_c_ninja_scale = 0.13
        classic_ninja_position = Vector2()
        classic_ninja_position.x = self.size.x / 4
        classic_ninja_position.y = 200
        
        # reassign ninja
        self.classic_ninja = SpriteNode(c_ninja_kick_file,
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = kick_c_ninja_scale)
    
    def ginger_ninja_kick(self):
        # shows ninja kicking
        
        # take out running ninja
        self.ginger_ninja.remove_from_parent()
        
        #kicking ninja properties
        g_ninja_kick_file = './assets/sprites/ginger_ninja/gkick.PNG'
        kick_g_ninja_scale = 0.13
        ginger_ninja_position = Vector2()
        ginger_ninja_position.x = self.size.x / 2
        ginger_ninja_position.y = 200
        
        # reassign ninja
        self.ginger_ninja = SpriteNode(g_ninja_kick_file,
                                       parent = self,
                                       position = ginger_ninja_position,
                                       scale = kick_g_ninja_scale)
        
    def bat_ninja_kick(self):
        # shows ninja kicking
        
        # take out running ninja
        self.bat_ninja.remove_from_parent()
        
        #kicking ninja properties
        b_ninja_kick_file = './assets/sprites/bat_ninja/bkick.PNG'
        kick_b_ninja_scale = 0.13
        bat_ninja_position = Vector2()
        bat_ninja_position.x = self.size.x * 3 / 4
        bat_ninja_position.y = 200
        
        # reassign ninja
        self.bat_ninja = SpriteNode(b_ninja_kick_file,
                                       parent = self,
                                       position = bat_ninja_position,
                                       scale = kick_b_ninja_scale)
        
    def classic_run(self):
        # shows ninja running
        
        # take out kicking ninja
        self.classic_ninja.remove_from_parent()
        
        # ninja properties
        classic_ninja_position = Vector2()
        classic_ninja_position.x = self.size.x / 4
        classic_ninja_position.y = 200
        self.classic_ninja = SpriteNode('./assets/sprites/classic_ninja/c1.PNG',
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.11)
        
    def ginger_run(self):
        # shows ninja running
        
        # take out kicking ninja
        self.ginger_ninja.remove_from_parent()
        
        # ninja properties
        ginger_ninja_position = Vector2()
        ginger_ninja_position.x = self.size.x / 2
        ginger_ninja_position.y = 200
        self.ginger_ninja = SpriteNode('./assets/sprites/ginger_ninja/g1.PNG',
                                    parent = self,
                                    position = ginger_ninja_position,
                                    scale = 0.1)
        
    def bat_run(self):
        # shows ninja running
        
        # take out kicking ninja
        self.bat_ninja.remove_from_parent()
        
        # ninja properties
        bat_ninja_position = Vector2()
        bat_ninja_position.x = self.size.x * 3 / 4
        bat_ninja_position.y = 200
        self.bat_ninja = SpriteNode('./assets/sprites/bat_ninja/b1.PNG',
                                    parent = self,
                                    position = bat_ninja_position,
                                    scale = 0.1)
        
    
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
                                        scale = 0.11)



    def test_animating(self, test_count):
        # testing animating so I dont mess up the rest of my code
        #pass
        
        self.test_ninja.remove_from_parent()
        
        test_ninja_position = Vector2()
        test_ninja_position.x = self.size.x - 100
        test_ninja_position.y = self.size.y - 100
        
        test_ninja_file = "./assets/sprites/classic_ninja/c" + str(test_count) + ".PNG"
        
        self.test_ninja = SpriteNode(test_ninja_file,
                                     parent = self,
                                     position = test_ninja_position,
                                     scale = 0.05)
        
        
        
    
