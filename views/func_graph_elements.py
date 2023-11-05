def diode_bridge(x, y, name):
    return (r'''\draw ''' + f'({x + 10}, {y}) to[diode] ({x}, {y - 10}) to[diode] ({x - 10}, {y});' + '''
    \draw ''' + f'({x + 10}, {y}) to[diode] ({x}, {y + 10}) to[diode] ({x - 10}, {y});' + '''
    \draw ''' + f'({x}, {y}) node {{${name}$}};\n' +
            f'\draw ({x-10}, {y}) node [below left] {{$+$}};\n' +
            f'\draw ({x+10}, {y}) node [below left] {{$-$}};\n' +
            f'\draw ({x}, {y+10}) node [above left] {{$~$}};\n' +
            f'\draw ({x}, {y - 10}) node [below left] {{$~$}};\n')


def contact_no(x: int, y:int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 10}, {y}) -- ({x+20}, {y+5});\n' +
            f'\\draw ({x+20},{y}) -- ({x+30}, {y});\n' +
            f'\draw ({x+15}, {y+7}) node [above, align=center] {{${name}$}};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{${x_name}$}};\n' +
            f'\draw ({x+30}, {y}) node [below, align=center] {{${y_name}$}};\n')

def contact_nc(x: int, y: int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 10}, {y}) -- ({x+20}, {y-5});\n' +
            f'\\draw ({x+19},{y-5}) -- ({x+19},{y}) -- ({x+30}, {y});\n' +
            f'\draw ({x+15}, {y}) node [above, align=center] {{${name}$}};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{${x_name}$}};\n' +
            f'\draw ({x + 30}, {y}) node [below, align=center] {{${y_name}$}};\n')

def relay(x: int, y: int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 5}, {y});\n \\draw ({x+10}, {y}) -- ({x+15}, {y});\n' +
            f'\\draw ({x+5},{y-5}) -- ({x+5}, {y+5}) -- ({x+10}, {y+5}) -- ({x+10}, {y-5}) -- cycle;\n' +
            f'\draw ({x+7}, {y+7}) node [above, align=center] {{${name}$}};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{${x_name}$}};\n' +
            f'\draw ({x + 15}, {y}) node [below, align=center] {{${y_name}$}};\n')

