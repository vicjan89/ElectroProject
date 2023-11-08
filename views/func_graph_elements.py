def diode_bridge(x, y, name):
    return (r'''\draw ''' + f'({x + 10}, {y}) to[diode] ({x}, {y - 10}) to[diode] ({x - 10}, {y});' + '''
    \draw ''' + f'({x + 10}, {y}) to[diode] ({x}, {y + 10}) to[diode] ({x - 10}, {y});' + '''
    \draw ''' + f'({x}, {y}) node {{${name}$}};\n' +
            f'\draw ({x-10}, {y}) node [below left] {{$+$}};\n' +
            f'\draw ({x+10}, {y}) node [below left] {{$-$}};\n' +
            f'\draw ({x}, {y+10}) node [above left] {{$~$}};\n' +
            f'\draw ({x}, {y - 10}) node [below left] {{$~$}};\n')


def contact_no(x: int, y:int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 3}, {y}) -- ({x+13}, {y+5});\n' +
            f'\\draw ({x+13},{y}) -- ({x+16}, {y});\n' +
            f'\draw ({x+8}, {y+5}) node [above, align=center] {{ \\text{{{name}}} }};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{ \\footnotesize {x_name} }};\n' +
            f'\draw ({x+16}, {y}) node [below, align=center] {{ \\footnotesize {y_name} }};\n')

def contact_nc(x: int, y: int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 3}, {y}) -- ({x+13}, {y-5});\n' +
            f'\\draw ({x+12},{y-5}) -- ({x+12},{y}) -- ({x+16}, {y});\n' +
            f'\draw ({x+8}, {y}) node [above, align=center] {{ {name} }};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{ \\footnotesize {x_name} }};\n' +
            f'\draw ({x + 16}, {y}) node [below, align=center] {{ \\footnotesize {y_name} }};\n')

def contact_noc(x: int, y:int, name1='', name4='', name2='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 3}, {y}) -- ({x+13}, {y-5});\n' +
            f'\\draw ({x+13},{y}) -- ({x+16}, {y});\n' +
            f'\\draw ({x+12},{y-4}) -- ({x+12}, {y-6});\n' +
            f'\draw ({x+8}, {y}) node [above, align=center] {{ {name} }};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{ \\footnotesize {name1} }};\n' +
            f'\draw ({x + 13}, {y-6}) node [below right] {{ \\footnotesize {name2} }};\n' +
            f'\draw ({x + 16}, {y}) node [below, align=center] {{ \\footnotesize {name4} }};\n')

def relay(x: int, y: int, x_name='', y_name='', name=''):
    return (f'\\draw ({x},{y}) -- ({x + 5}, {y});\n \\draw ({x+10}, {y}) -- ({x+15}, {y});\n' +
            f'\\draw ({x+5},{y-5}) -- ({x+5}, {y+5}) -- ({x+10}, {y+5}) -- ({x+10}, {y-5}) -- cycle;\n' +
            f'\draw ({x+7}, {y+7}) node [above, align=center] {{{name}}};\n' +
            f'\draw ({x}, {y}) node [below, align=center] {{ \\footnotesize {x_name}}};\n' +
            f'\draw ({x + 15}, {y}) node [below, align=center] {{ \\footnotesize {y_name}}};\n')

