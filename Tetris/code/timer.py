from settings import *

class Timer:
    def __init__(self, duration, repeated=False, func=None):
        self.repeated = repeated
        self.func = func
        self.duration = duration
        
        self.start_time = 0
        self.active = False
        
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
        
    def update(self):
        curr_time = pygame.time.get_ticks()
        if curr_time - self.start_time >= self.duration and self.active:
            pass