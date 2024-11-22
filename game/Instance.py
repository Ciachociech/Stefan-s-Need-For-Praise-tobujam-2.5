from enum import Enum

import pygame

import system.Display


class InstanceState(Enum):
    none = 0
    # add more states like title-screen, menu, game and game-over


class Instance:
    def __init__(self):
        pygame.init()
        self.display = system.Display(1280, 720, "pygame Template")
        self.display.set_icon("assets/sprites/WIP32x32.png")
        self.display.frames = 60
        self.actualState = InstanceState.none
        self.previousState = InstanceState.none
        self.scenes = []
        '''
        load scenes like:
        self.scenes.append(Scene("tag", self.display))
        '''

    '''
    after updating call this like:
    self.update_instance_states(new_state)
    '''
    def update_instance_states(self, new_state):
        self.previousState = self.actualState
        self.actualState = new_state

    def loop(self):
        while pygame.get_init():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.display.clear()

            if self.actualState == InstanceState.none:
                '''
                # scene process input like:
                scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick, pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                # scene update
                scene.update()
                # scene(s) render
                scene.render()
                '''
                pass

            self.display.display_and_wait()

        pygame.quit()
