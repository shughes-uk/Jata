def GetFlagList():
    return flaglist


class FlagList(object):
    def __init__(self):
        self.flags = {}

    def AddFlag(self, flag):
        self.flags[flag.name] = flag

    def GetFlag(self, flag_name):
        if flag_name in self.flags:
            return self.flags[flag_name]
        else:
            return None

    def Reset(self):
        self.flags.clear()


class Flag(object):
    def __init__(self, name, payload=None):
        self.name = name
        self.payload = payload


flaglist = FlagList()