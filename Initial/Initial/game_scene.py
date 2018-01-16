# Created by: Jenny Trac
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
import time
import sound
import config
from numpy import random
from copy import deepcopy
from pause_scene import *
from game_over_scene import *

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        self.SCREEN_SIZE = deepcopy(self.size)
        self.slider_scale_size = 0.4
        self.asteroids = []
        self.slider_used = False
        self.asteroid_speed = 8.0
        self.asteroid_create_rate = 1
        self.kick_start_time = time.time()
        self.kick_button_enabled = True
        
        # add space background
        self.background = SpriteNode('./assets/sprites/space_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.SCREEN_SIZE)
        
        
        # slider
        slider_position = self.CENTRE_OF_SCREEN
        slider_position.x = 65
        self.slider = SpriteNode('./assets/sprites/slider.PNG',
                                 position = slider_position,
                                 parent = self,
                                 alpha = 0.5,
                                 scale = self.slider_scale_size)
        
        
        # slider cursor
        self.slider_cursor_position = self.CENTRE_OF_SCREEN
        self.slider_cursor_position.y = self.SCREEN_SIZE.y / 2
        self.slider_cursor_position.x = 63
        self.slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                        position = self.slider_cursor_position,
                                        parent = self,
                                        scale = 0.2,
                                        alpha = 0.6)
        
        
        # kick button
        kick_button_position = self.CENTRE_OF_SCREEN
        kick_button_position.x = self.SCREEN_SIZE.x - 110
        kick_button_position.y = 70
        self.kick_button = SpriteNode('./assets/sprites/kick_button.PNG',
                                      parent = self,
                                      position = kick_button_position,
                                      scale = 0.25,
                                      alpha = 0.7)
        
        
        # pause button
        #pause_button_position = self.CENTRE_OF_SCREEN
        #pause_button_position.x = self.SCREEN_SIZE.x - 60
        #pause_button_position.y = self.SCREEN_SIZE.y - 60
        #self.pause_button = SpriteNode('./assets/sprites/pause_button.PNG',
        #                               parent = self,
        #                               position = pause_button_position,
        #                               scale = 0.4,
        #                               alpha = 0.5)
        
        
        # ninja
        self.ninja_choice = self.ninja_file(config.character_setting)
        #print(self.ninja_choice)
        ninja_position = self.CENTRE_OF_SCREEN
        ninja_position.x = 200
        ninja_position.y = self.SCREEN_SIZE.y / 2
        self.ninja = SpriteNode('./assets/sprites/' + self.ninja_choice + '.PNG',
                                parent = self,
                                position = ninja_position,
                                scale = 0.09)
        
        
        # score
        score_label_position = self.size
        score_label_position.x = self.size.x - 250
        score_label_position.y = self.size.y - 60
        self.score_label = LabelNode(text = "Score: 0",
                                           font = ('ChalkboardSE-Light', 50),
                                           parent = self,
                                           position = score_label_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        #pass
        
        # check if game is over
        if config.game_over == True:
            self.dismiss_modal_scene()
        
        
        # check if new asteroid should be created
        asteroid_create_chance = (random.randint(1, 40)) - (config.score / 10)
        if asteroid_create_chance <= self.asteroid_create_rate:
            self.add_asteroid()
        
        
        # check if any asteroid is off the screen and delete
        for asteroid in self.asteroids:
            if asteroid.position.x < 1:
                asteroid.remove_from_parent()
                self.asteroids.remove(asteroid)
        
        
        # check if kick ninja has been displayed for half a second, then change back to running
        if (time.time() - self.kick_start_time) > 0.5:
            self.ninja_back_to_running(self.ninja_choice)
        
        
        # disable kick button for 1 second after it has been clicked
        if (time.time() - self.kick_start_time) > 1:
            self.kick_button_enabled = True
        
        
        # check if ninja is kicking an asteroid and remove it
        if (time.time() - self.kick_start_time) <= 0.5:
            if len(self.asteroids) > 0:
                for asteroid_kicked in self.asteroids:
                    if asteroid_kicked.frame.intersects(self.ninja.frame):
                        if config.sound_setting == True:
                            sound.play_effect('./assets/sounds/asteroidKicked.mp3')
                        asteroid_kicked.remove_from_parent()
                        self.asteroids.remove(asteroid_kicked)
                        config.score = config.score + 1
        
        
        # check if running ninja is touching an asteroid and he dies
        if (time.time() - self.kick_start_time) > 0.5:
            if len(self.asteroids) > 0:
                for asteroid_touched in self.asteroids:
                    if asteroid_touched.frame.intersects(self.ninja.frame):
                        self.ninja.remove_from_parent()
                        self.present_modal_scene(GameOverScene())
        
        
        # update score
        self.score_label.text = "Score: " + str(config.score)
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        #pass
        
        # check if user is using the slider
        if self.slider.frame.contains_point(touch.location):
            self.slider_used = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        #pass
        
        # if user is using slider, make cursor and ninja move
        if self.slider_used == True:
            # move cursor
            cursor_position = self.SCREEN_SIZE
            cursor_position.x = 63
            cursor_position.y = touch.location.y
            cursorMoveAction = Action.move_to(cursor_position.x, cursor_position.y)
            self.slider_cursor.run_action(cursorMoveAction)
            # move ninja
            ninja_position = self.SCREEN_SIZE
            ninja_position.x = 200
            ninja_position.y = touch.location.y
            ninjaMoveAction = Action.move_to(ninja_position.x, ninja_position.y)
            self.ninja.run_action(ninjaMoveAction)
    
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #pass
        
        #if self.pause_button.frame.contains_point(touch.location):
        #    self.present_modal_scene(PauseScene())
            
        # ensures that user uses slider and not a random part of screen
        #self.slider_used = False # not using this feature because game play becomes choppy
        
        # kick button
        if self.kick_button.frame.contains_point(touch.location) and self.kick_button_enabled == True:
            self.kick_start_time = time.time()
            self.ninja_kick(config.character_setting)
            self.kick_button_enabled = False
            if config.sound_setting == True:
                sound.play_effect('./assets/sounds/ninjaKick.mp3')
    
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
    
    def add_asteroid(self):
        # creates new asteroid to move across screen
        
        # assign random start position for asteroid on right side of screen
        asteroid_start_position = Vector2()
        asteroid_start_position = deepcopy(self.SCREEN_SIZE)
        asteroid_start_position.x = self.size.x
        asteroid_start_position.y = random.randint(100, self.size.y - 99)
        
        
        # assign end position for asteroid on left side of screen
        asteroid_end_position = deepcopy(self.SCREEN_SIZE)
        asteroid_end_position.x = 0
        asteroid_end_position.y = asteroid_start_position.y
        
        
        # choose which asteroid to show (there are 4 options)
        asteroid_variation = random.randint(1, 5)
        asteroid_file = "./assets/sprites/asteroids/a" + str(asteroid_variation) + ".PNG"
        
        
        # create the asteroid and add it to array of asteroids
        self.asteroids.append(SpriteNode(asteroid_file,
                                         position = asteroid_start_position,
                                         parent = self,
                                         scale = 0.28,
                                         alpha = 0.9))
        
        
        # make asteroid move across the screen
        asteroidMoveAction = Action.move_to(asteroid_end_position.x,
                                            asteroid_end_position.y,
                                            self.asteroid_speed)
        self.asteroids[len(self.asteroids)-1].run_action(asteroidMoveAction)
    
    def ninja_kick(self, character):
        # shows ninja kicking
        
        # save ninja's location
        kick_ninja_position = self.ninja.position
        
        
        # take out running ninja
        self.ninja.remove_from_parent()
        
        
        # check which ninja character is being used
        ninja_kick_file = './assets/sprites/classic_ninja/ckick.PNG'
        kick_ninja_scale = 0.1
        
        if character == 'ginger':
            ninja_kick_file = './assets/sprites/ginger_ninja/gkick.PNG'
            kick_ninja_scale = 0.11
        elif character == 'bat':
            ninja_kick_file = './assets/sprites/bat_ninja/bkick.PNG'
            kick_ninja_scale = 0.12
        
        
        # show kicking ninja
        self.ninja = SpriteNode(ninja_kick_file,
                                parent = self,
                                position = kick_ninja_position,
                                scale = kick_ninja_scale)
        
    
    def ninja_back_to_running(self, ninja_name):
        # back to running ninja after half a second
        
        # save the ninja's currents position
        running_ninja_position = self.ninja.position
        
        
        # remove the kicking ninja
        self.ninja.remove_from_parent()
        
        
        # show the running ninja again
        self.ninja = SpriteNode('./assets/sprites/' + ninja_name + '.PNG',
                                parent = self,
                                position = running_ninja_position,
                                scale = 0.09)
        
    
    def ninja_file(self, character_choice):
        # chooses which ninja to display
        
        the_ninja_file = ' '
        if character_choice == 'classic':
            the_ninja_file = 'classic_ninja/c1'
        elif character_choice == 'ginger':
            the_ninja_file = 'ginger_ninja/g1'
        elif character_choice == 'bat':
            the_ninja_file = 'bat_ninja/b1'
        
        return the_ninja_file
    
    def pause_game(self):
        # saves all data and stops all sprites from moving
        pass
