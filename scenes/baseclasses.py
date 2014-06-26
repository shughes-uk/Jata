import Queue


class BaseScene(object):
    def __init__(self):
        self.finished = False
        self.name = self.__class__.__name__
        self.drawables = []
        self.events = Queue.Queue()
        self.current_event = None
        self.elapsedtime = 0

    def Start(self):
        self.current_event = self.events.get()

    def Tick(self, dx):
        self.elapsedtime += dx
        if not self.current_event.finished:
            self.current_event.Do(self, self.elapsedtime)
            return
        elif self.current_event.finished and self.events.empty():
            self.finished = True
            return
        elif self.current_event.finished:
            self.current_event = self.events.get()
            return

    def Teardown(self):
        print 'Scene_%s teardown not implemented' % self.name


class BaseEvent(object):
    def __init__(self):
        self.finished = False
        self.name = self.__class__.__name__

    def Do(self, parent_scene, dx):
        print 'Scene_%s_Event_%s.Do not implemented' % (parent_scene.name, self.name)