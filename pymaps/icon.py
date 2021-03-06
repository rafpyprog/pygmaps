SHAPES = ['pin', 'airport', 'hospital', 'home', 'dot', 'start', 'heart',
          'flag']

COLORS = {
    'amber'     : ('FFC107', 'FF6F00'),
    'blakwhite' : ('000000', 'FFFFFF'),
    'blue'      : ('2196F3', '0D47A1'),
    'bluewhite' : ('0277BD', 'FFFFFF'),
    'cyan'      : ('00BCD4', '006064'),
    'deeppurple': ('673AB7', '311B92'),
    'deeporange': ('FF5722', 'BF360C'),
    'gray'      : ('9E9E9E', '212121'),
    'green'     : ('4CAF50', '1B5E20'),
    'indigo'    : ('3F51B5', '1A237E'),
    'lightblue' : ('03A9F4', '01579B'),
    'lightgreen': ('8BC34A', '33691E'),
    'lime'      : ('CDDC39', '827717'),
    'orange'    : ('FF9800', 'E65100'),
    'pink'      : ('E91E63', '880E4F'),
    'purple'    : ('9C27B0', '4A148C'),
    'red'       : ('ea4335', '960a0a'),
    'teal'      : ('009688', '004D40'),
    'yellow'    : ('FFEB3B', 'F57F17'),
    }

def url_picker(icon_name):
    google = 'http://www.google.com/maps/vt/icon/name=assets/icons'
    pinlet = '/poi/tactile/pinlet_shadow-1-small.png,assets/icons/poi/tactile/pinlet-1-small.png,assets/icons/poi/quantum/pinlet/'
    icons = {
        'pin': google + '/spotlight/spotlight_pin_v2_shadow-1-small.png,assets/icons/spotlight/spotlight_pin_v2-1-small.png,assets/icons/spotlight/spotlight_pin_v2_dot-1-small.png,assets/icons/spotlight/spotlight_pin_v2_accent-1-small.png&highlight=FF00FF,{},{},FF00FF&color=FF00FF?scale={}',
        'airport': google + pinlet + 'airport_pinlet-1-small.png&highlight=ff000000,{},{}&color=ff000000?scale={}',
        'hospital': google + pinlet + 'hospital_H_pinlet-1-small.png&highlight=ff000000,{},{}&color=ff000000?scale={}',
        'home': google + pinlet + 'home_pinlet-1-small.png&highlight=ffffff,{},{}&color=ff000000?scale={}',
        'dot': google + pinlet + 'dot_pinlet-1-small.png&highlight=ff000000,{},{}&color=ff000000?scale={}',
        'start': google + pinlet + 'constellation_star_pinlet-1-small.png&highlight=ff000000,{},{},ffffff&color=ff000000?scale={}',
        'heart': google + pinlet + 'heart_pinlet-1-small.png&highlight=ff000000,{},{},ffffff&color=ff000000?scale={}',
        'flag': google + pinlet + 'nickname_pinlet-1-small.png&highlight=ff000000,{},{},ffffff&color=ff000000?scale={}'
    }
    return icons[icon_name]


def color_picker(color, shape):
    if color is None:
        if shape == 'pin':
            pick = COLORS['red']
        else:
            pick = COLORS['bluewhite']
    else:
        if isinstance(color, (list, tuple)):
            pick = [i.replace('#', '') for i in color]
        else:
            pick = COLORS.get(color, COLORS['red'])
    return pick


class Icon():
    def __init__(self, name='pin', color=None, size=1):
        self.name = name
        self.color = color_picker(color, name)
        self.size = size

    @property
    def url(self):
        url = url_picker(self.name)
        return url.format(*self.color, self.size)
