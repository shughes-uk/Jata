from utils.flagging import GetFlagList, Flag

class BaseScene(object):
    def __init__(self):
        self.finished = False
        self.name = 'BaseScene'
        self.drawables = []
        self.triggers = []
        self.current_event = None
        self.elapsed_time = 0


    def Tick(self, dx):
        self.elapsed_time += dx
        GetFlagList().AddFlag(Flag(self.name + '_time', self.elapsed_time))
        self.triggers = [trigger for trigger in self.triggers if not trigger.done]
        for trigger in self.triggers:
            trigger.Check()

    def Teardown(self):
        print 'Scene_%s teardown not implemented' % self.name


class BaseTrigger(object):
    def __init__(self, parentscene):
        self.done = False
        self.name = self.__class__.__name__
        self.flag_conditions = []
        self.parent_scene = parentscene

    def Check(self):
        met = True
        for fcondition in self.flag_conditions:
            if isinstance(fcondition, list):
                for condition in fcondition:
                    if not self.CheckCondition(condition):
                        met = False
            else:
                if not self.CheckCondition(fcondition):
                    met = False
        if met:
            self.Trigger()


    def CheckCondition(self, condition):
        flag = GetFlagList().GetFlag(condition['name'])
        if flag:
            if 'payload' in condition:
                if 'op' in condition['payload']:
                    if condition['payload']['op'] == '>=':
                        if flag.payload >= condition['payload']['val']:
                            return True
                    elif condition['payload']['op'] == '<=':
                        if flag.payload <= condition['payload']['va']:
                            return True
                    elif condition['payload']['op'] == '<':
                        if flag.payload < condition['payload']['val']:
                            return True
                    elif condition['payload']['op'] == '>':
                        if flag.payload > condition['payload']['val']:
                            return True
                    else:
                        return False
                else:
                    if flag.payload == condition['payload']:
                        return True
                    else:
                        return False
            else:
                return True
        else:
            return False

    def Trigger(self):
        print 'Scene_%s_Event_%s.Trigger not implemented' % (self.parent_scene.name, self.name)

