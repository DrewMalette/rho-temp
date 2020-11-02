# fader.py:

import pygame

class Fader: # TODO make a white version
    def __init__(self, uid, size):
        self.uid = uid	
        self.curtain = pygame.Surface(size)
        self.curtain.fill((0,0,0))
        self.opacity = 0
        self.curtain.set_alpha(self.opacity)
        
        self.speed = 0
        self.velocity = -self.speed
        self.faded_in = False # as in a cycle
        self.faded_out = False
        self.fading = False
        
        print("fader initialized")
    
    def fade_out(self, speed=6):	
        self.speed = speed
        self.opacity = 0
        self.curtain.set_alpha(self.opacity)
        self.fading = True
        self.velocity = self.speed
        self.game.script = self.game.fade_loop
        
    def fade_in(self, speed=6):		
        self.speed = speed
        self.opacity = 255
        self.curtain.set_alpha(self.opacity)
        self.fading = True
        self.velocity = -self.speed
        self.game.script = self.game.fade_loop
        
    def update(self, signals, fc):
        if self.faded_in:
            self.faded_in = False
        if self.faded_out:
            self.faded_out = False
        
        if self.fading:
            self.opacity += self.velocity
            
            if self.opacity <= 0:
                self.opacity = 0
                self.faded_in = True
            elif self.opacity >= 255:
                self.opacity = 255
                self.faded_out = True
            
            self.curtain.set_alpha(self.opacity)

            if self.faded_in or self.faded_out:
                self.fading = False
                
            signals.append("fading")
                
    def render(self, surface):
        surface.blit(self.curtain,(0,0))
