from renderer.renderer import GetRenderer


class Drawable(object):
    show = False

    def __init__(self):
        GetRenderer().AddDrawable(self)

