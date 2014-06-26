import pkgutil
import Queue

import pyglet

import scenes
from renderer.renderer import GetRenderer


pyglet.font.add_file('clacon.ttf')


class Game():
    def __init__(self):
        self.scenes = Queue.Queue()
        self.current_scene = None

    def LoadScenes(self):
        unsorted = []
        for importer, modname, ispkg in pkgutil.iter_modules(scenes.__path__):
            if modname != "baseclasses":
                print "Loading scene %s" % modname
                scene = __import__("scenes." + modname, fromlist="hook")
                unsorted.append(scene.Scene())
        sorted_scenes = sorted(unsorted, key=lambda scene: scene.name)
        for scene in sorted_scenes:
            self.scenes.put(scene)
        print "Scenes loaded"


    def Start(self):
        pyglet.clock.schedule_interval(self.Tick, 0.1)
        self.current_scene = self.scenes.get()

    def Tick(self, dx):
        if not self.current_scene.finished:
            self.current_scene.Tick(dx)
            return
        elif self.current_scene.finished and self.scenes.empty():
            self.finished = True
            return
        elif self.current_scene.finished:
            self.current_scene.Teardown()
            self.current_scene = self.scenes.get()
            return


if __name__ == '__main__':
    renderer = GetRenderer()
    game = Game()
    game.LoadScenes()
    game.Start()
    pyglet.app.run()