from enum import IntEnum

import pygame

from game.JSONStatistics import save_statistics_to_json, load_statistics_from_json
import game.scenes.Game
import game.scenes.Gameover
import game.scenes.Statistics
import system.Display


class InstanceState(IntEnum):
    none = 0
    game = 1
    stats = 2
    upgrades = 3
    gameover = 4


class Instance:

    def __init__(self):
        pygame.init()
        self.display = system.Display(720, 720, "bulonais-5")
        self.display.set_icon("assets/sprites/WIP32x32.png")
        self.display.frames = 60

        self.statistics = self.load()

        self.actualState = InstanceState.none
        self.previousState = InstanceState.none

        self.scenes = []
        self.scenes.append(game.scenes.Game(self.display))
        self.scenes.append(game.scenes.Statistics(self.display, self.statistics))
        self.scenes.append(game.scenes.Upgrades(self.display, self.statistics))
        self.scenes.append(game.scenes.Gameover(self.display))

    def load(self):
        result = load_statistics_from_json()
        if result is None:
            result = load_statistics_from_json(extension=".dat.bkp")
            if result is None:
                return game.GameStatistics()
        return result

    def save_and_exit(self):
            save_statistics_to_json(self.statistics)
            pygame.quit()

    def update_instance_states(self, new_state):
        self.previousState = self.actualState
        self.actualState = new_state

    def loop(self):
        while pygame.get_init():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_and_exit()
                    return

            self.display.clear()

            actual_scene = None
            previous_scene = None
            if self.actualState != InstanceState.none:
                actual_scene = self.scenes[self.actualState - 1]
            if self.previousState != InstanceState.none:
                previous_scene = self.scenes[self.previousState - 1]

            # there will be "only one" element updated exclusively beyond actual scene
            if self.actualState != InstanceState.none and self.actualState != InstanceState.gameover:
                self.statistics.update()

            match self.actualState:
                case InstanceState.none:
                    self.update_instance_states(InstanceState.game)
                    self.scenes[self.actualState - 1].set(self.statistics)
                case InstanceState.game:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    match actual_scene.update():
                        case 2:
                            self.update_instance_states(InstanceState.stats)
                        case 3:
                            self.update_instance_states(InstanceState.upgrades)
                        case 4:
                            self.save_and_exit()
                            return
                        case 0:
                            self.update_instance_states(InstanceState.gameover)
                            self.scenes[self.actualState - 1].set(self.statistics)
                            pass
                        case _:
                            pass
                    actual_scene.render()
                case InstanceState.stats | InstanceState.upgrades:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    if actual_scene.update():
                        self.update_instance_states(InstanceState.game)
                    previous_scene.render()
                    actual_scene.render()
                case InstanceState.gameover:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    match actual_scene.update():
                        case 1:
                            self.update_instance_states(InstanceState.game)
                            self.statistics.set()
                        case -1:
                            pygame.quit()
                            return
                        case _:
                            pass
                    previous_scene.render()
                    actual_scene.render()
                case _:
                    pass

            self.display.display_and_wait()

        pygame.quit()

