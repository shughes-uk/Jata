import weakref

import pyglet


def GetRenderer():
    return renderer


class Renderer(pyglet.window.Window):
    def __init__(self):
        super(Renderer, self).__init__()
        self.render_list = []

    def on_draw(self):
        self.clear()
        self.render_list = [ref for ref in self.render_list if ref()]
        for weakref in self.render_list:
            weakref().draw()

    def AddDrawable(self, drawable):
        self.render_list.append(weakref.ref(drawable))


renderer = Renderer()