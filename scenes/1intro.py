import baseclasses


class Scene(baseclasses.BaseScene):
    def __init__(self):
        super(Scene, self).__init__()
        self.name = '1intro'
        self.triggers.append(Opening(self))


class Opening(baseclasses.BaseTrigger):
    def __init__(self, parentscene):
        super(Opening, self).__init__(parentscene)
        self.flag_conditions.append({'name': '1intro_time', 'payload': {'op': '>', 'val': 5}})
