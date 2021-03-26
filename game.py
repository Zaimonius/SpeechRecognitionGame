import math
import time
import pygame
from pygame.locals import *
from itertools import chain
import random
import pyaudio
import wave
import train
import tile
import settings

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             

def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                         
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account."""
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

class Game:
    def __init__(self, display_width, display_height, grid_size):
        pygame.init()
        pygame.font.init()
        self.grid_size = grid_size
        self.display_width = display_width
        self.display_height = display_height
        self.screen = pygame.display.set_mode((display_width, display_height))
        #clock
        self.clock = pygame.time.Clock()
        #set font
        self.font = pygame.font.SysFont('Arial', 32)
        self.grid = [ [ None for i in range(grid_size) ] for j in range(grid_size) ]
        self.grid_types = [tile.Forest, tile.Mountain, tile.River, tile.Plain]
        self.create_grid()
        self.directions = {
                            'up' : pygame.Vector2(int(0),int(-1)),
                            'down' : pygame.Vector2(int(0),int(1)),
                            'left'  : pygame.Vector2(int(-1),int(0)),
                            'right'  : pygame.Vector2(int(1),int(0))
                           }
        self.position = pygame.Vector2(int(self.grid_size/2), int(self.grid_size/2))
        self.position_image = pygame.image.load('assets/position.png')
        self.current_action = self.grid[int(self.position.x)][int(self.position.y)].root
        self.set_current_text(self.current_action.description)
        #sound input vars
        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.stream = self.p.open(format=settings.sample_format,
        channels=settings.channels,
        rate=settings.fs,
        frames_per_buffer=settings.chunk,
        input=True)
        self.frames = []  # Initialize array to store frames
        self.trainer = train.Trainer(file_path="librispeechmodel.txt", epochs=0, batch_size=1)
        self.current_command = ''
        self.spoken_letters = ''

    def __del__(self):
        self.p.terminate()
        print("shutting down")

    def random_tile(self, position):
        return self.grid_types[random.randint(0,len(self.grid_types)-1)](position)

    def create_grid(self):
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                self.grid[i][j] = self.random_tile((i,j))

    def draw_map(self):
        rect = pygame.Rect(pygame.Vector2(700, 20), (500, 300))
        pygame.draw.rect(self.screen, settings.white, rect)
        for i in range(0, self.grid_size):
            for j in range(0, self.grid_size):
                self.screen.blit(self.grid[i][j].image, pygame.Vector2(700 + (32*i), 20 + (32*j)))

    def draw_textlog(self):
        rect = pygame.Rect(pygame.Vector2(20, 20), (650, 400))
        pygame.draw.rect(self.screen, settings.white, rect)
        for i, line in enumerate(self.strlst):
            text = self.font.render(line, True, settings.black)
            self.screen.blit(text,(rect.x + 5, rect.y + i*32 + 5))

    def draw_actions(self):
        rect = pygame.Rect(pygame.Vector2(20, 450), (650, 250))
        pygame.draw.rect(self.screen, settings.white, rect)
        actions = ""
        for action in self.available_actions:
            actions = actions + "  " + action
        if len(actions) > 0:
            actions = wrap_multi_line(actions, self.font, 650)
            for i, line in enumerate(actions):
                text = self.font.render(line, True, settings.black)
                self.screen.blit(text,(rect.x + 5, rect.y + i*32 + 5))

    def set_available_actions(self):
        self.available_actions = []
        if self.current_action.move_node:
            for string, direction in self.directions.items():
                if self.inbounds(self.position + direction):
                    self.available_actions.append(string)
        for node in self.current_action.children:
            self.available_actions.append(node.data)

    def draw_newest_letters(self):
        rect = pygame.Rect(pygame.Vector2(700, 550), (512, 150))
        pygame.draw.rect(self.screen, settings.white, rect)
        text = self.font.render(self.spoken_letters, True, settings.black)
        self.screen.blit(text,(rect.x + 5, rect.y + 5))

    def inbounds(self, position):
        if position.x > self.grid_size or position.y > self.grid_size:
            return False
        elif position.y < 0 or position.y < 0:
            return False
        else:
            return True

    def draw_position(self):
        self.screen.blit(self.position_image, pygame.Vector2(700 + (32*self.position[0]), 20 + (32*self.position[1])))

    def set_current_text(self, text):
        self.strlst = wrap_multi_line(text, self.font, 650)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                #escape
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                #begin speech
                if event.key == pygame.K_t:
                    self.stream = self.p.open(format=settings.sample_format,
                    channels=settings.channels,
                    rate=settings.fs,
                    frames_per_buffer=settings.chunk,
                    input=True)
                    self.frames = []  # Initialize array to store frames
                    data = self.stream.read(settings.chunk)
                    self.frames.append(data)
            currently_pressed = pygame.key.get_pressed()
            if currently_pressed[pygame.K_t] > 0:
                    data = self.stream.read(settings.chunk)
                    self.frames.append(data)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    # Stop and close the streams and save wav file
                    self.stream.stop_stream()
                    self.stream.close()
                    wf = wave.open(settings.filename, 'wb')
                    wf.setnchannels(settings.channels)
                    wf.setsampwidth(self.p.get_sample_size(settings.sample_format))
                    wf.setframerate(settings.fs)
                    wf.writeframes(b''.join(self.frames))
                    wf.close()
                    new_action = self.trainer.speech_to_text('./output.wav')[0]
                    self.spoken_letters = new_action
                    self.current_command = new_action
                    self.current_command = self.check_action(self.current_command)
                    if self.current_command in self.directions.keys():
                        self.position = self.position + self.directions[self.current_command]
                        self.current_action = self.grid[int(self.position.x)][int(self.position.y)].root
                        self.set_current_text(self.current_action.description)
                    else:
                        for i, action in enumerate(self.current_action.children):
                            if action.data == self.current_command:
                                self.current_action = self.current_action.children[i]
                                self.set_current_text(self.current_action.description)

    def check_action(self, new_action):
        probability_list = []
        for action in self.available_actions:
            probability_list.append(self.count(new_action, action))
        max_val = max(probability_list)
        for i, action in enumerate(probability_list):
            if action == max_val:
                return self.available_actions[i]

    def count(self, str1, str2):  
        c, j = 0, 0
        for i in str1:     
            if str2.find(i)>= 0 and j == str1.find(i):  
                c += 1
            j += 1
        return c

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(settings.FPS)
            self.set_available_actions()
            self.handle_events()
            pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
            self.screen.fill(settings.darkgray)
            self.draw_textlog()
            self.draw_map()
            self.draw_position()
            self.draw_actions()
            self.draw_newest_letters()
            pygame.display.flip()
