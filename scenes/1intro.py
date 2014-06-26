import baseclasses
import drawables.Console


class Scene(baseclasses.BaseScene):
    def __init__(self):
        super(Scene, self).__init__()
        self.events.put(Opening())


class Opening(baseclasses.BaseEvent):
    def Do(self, parent_scene, time):
        if time > 1:
            parent_scene.drawables.append(drawables.Console.Console())
            self.finished = True
