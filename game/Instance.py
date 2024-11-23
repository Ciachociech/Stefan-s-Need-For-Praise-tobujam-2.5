from enum import IntEnum

import pygame

import game.scenes.Game
import game.scenes.Statistics
import system.Display


class InstanceState(IntEnum):
    none = 0,
    game = 1,
    stats = 2
    # add more states like title-screen, menu, game and game-over


class Instance:
    def __init__(self):
        pygame.init()
        self.display = system.Display(720, 720, "bulonais-5")
        self.display.set_icon("assets/sprites/WIP32x32.png")
        self.display.frames = 60
        self.actualState = InstanceState.none
        self.previousState = InstanceState.none
        self.scenes = []
        self.scenes.append(game.scenes.Game(self.display))
        self.scenes.append(game.scenes.Statistics(self.display, self.scenes[0].stefan.statistics))

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

            actual_scene = None
            previous_scene = None
            if self.actualState != InstanceState.none:
                actual_scene = self.scenes[self.actualState - 1]
            if self.previousState != InstanceState.none:
                previous_scene = self.scenes[self.previousState - 1]

            match self.actualState:
                case InstanceState.none:
                    self.update_instance_states(InstanceState.game)
                case InstanceState.game:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    match actual_scene.update():
                        case 2:
                            self.update_instance_states(InstanceState.stats)
                        case 3:
                            pass
                        case 4:
                            pygame.quit()
                            return
                        case _:
                            pass
                    actual_scene.render()
                case InstanceState.stats:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    if actual_scene.update():
                        self.update_instance_states(InstanceState.game)
                    previous_scene.render()
                    actual_scene.render()
                case _:
                    pass

            self.display.display_and_wait()

        pygame.quit()
