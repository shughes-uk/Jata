import pyglet

import baseclasses


class Console(baseclasses.Drawable):
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