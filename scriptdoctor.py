import re
import os


def del_non_ascii(filename):
    '''Run this function to rid script file
    of non-ascii characters!'''
    folder_name = 'broken_moviescripts'
    folder_path = os.path.abspath(folder_name)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        script = f.read()
    
    script = re.sub(r'[^\x00-\x7F]+', '', script)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(script)


def read_broken_script(filename):
    ''' takes the broken script's filename
    and outputs the script as a string '''
    folder_name = 'broken_moviescripts'
    folder_path = os.path.abspath(folder_name)
    file_path = os.path.join(folder_path, filename)

    with open(file_path) as file:
        script = file.read()

    return script


def del_parenthesis(script):
    return re.sub(r'\([^)]*\)', '', script)


def del_spacing(script):
    pattern = re.compile(r'([A-Z]+\s.*)(?:\n{2,})')
    new_script = pattern.sub(r'\1\n', script)
    
    return new_script



def update_script(filename, newscript):
    '''Takes the updated script and adds it to
    the moviescripts folder. Old script will remain in
    broken_moviescripts folder.'''
    path = os.path.join(os.path.abspath(''), 'moviescripts', filename)

    with open(path, 'w') as file:
        file.write(newscript)

    return



