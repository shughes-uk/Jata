import weakref

import pyglet

pyglet.font.add_file('clacon.ttf')
renderer = None


def GetRenderer():
    return renderer


class Drawable(object):
    show = False

    def __init__(self):
        GetRenderer().AddDrawable(self)

    def __del__(self):
        GetRenderer().RemoveDrawable(self)


class Renderer(pyglet.window.Window):
    def __init__(self):
        super(Renderer, self).__init__()
        self.render_list = []

    def on_draw(self):
        self.clear()
        self.render_list = [ref for ref in self.render_list if ref()]
        for render in self.render_list:
            render.draw()

    def AddDrawable(self, drawable):
        self.render_list.append(weakref.ref(drawable))

    def RemoveDrawable(self, drawable):
        self.render_list.remove(drawable)


class Console(Drawable):
    def __init__(self):
        super(Console, self).__init__()
        self.lines = []
        first = pyglet.text.Label('>Hello',
                                  font_name='Classic Console',
                                  font_size=20,
                                  x=0, y=0,
                                  anchor_x='left', anchor_y='bottom')
        self.lines.append(first)

    def draw(self):
        for line in self.lines:
            line.draw()


renderer = Renderer()
console = Console()
pyglet.app.run()