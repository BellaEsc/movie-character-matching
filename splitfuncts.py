import re
import os
import pandas as pd


def read_script(filename):
    ''' takes the script's filename
    and outputs it as a string'''
    path = os.path.join(os.path.abspath(''), 'moviescripts', filename)
    script_file = open(path)
    script = script_file.read()
    script_file.close()
    return script


def script_to_dict(script):
    ''' Takes in a script (string object) and outputs
    a dictionary with each character and their spoken lines '''

    pars = re.split(r'\n\n+', script, maxsplit=0)
    d = {}

    for p in pars:
        # Capture the name (anchored to the beginning of line and all capitals)
        # and the rest of the paragraph - (.*)
        regex = re.search(r'^([A-Z]+ [A-Z]+|[A-Z]+)(.*)', p, re.S + re.M)

        if not regex:  # Avoid calling group() on null results
            continue

        name, txt = regex.group(1, 2) 

        # Each sentence as a list item
        if name in d:
            d[name] += txt.strip().split('\n')
        else:
            d[name] = txt.strip().split('\n')
    
    for key in d:
        d[key] = ' '.join(d[key])
    
    return d


def movie_dict_to_df(movie_dict, movie_name):
    ''' Takes the movie dictionary and the name of the movie
    and turns it into a properly formatted dataframe.'''
    char_names = movie_dict.keys()
    movie_df = pd.DataFrame(movie_dict, index = [0])
    movie_df['movie_name'] = movie_name
    movie_df2 = movie_df.melt(id_vars = 'movie_name', 
                              value_vars = char_names,
                              var_name = 'character_name',
                              value_name = 'lines')
    movie_df2['lines_len'] = movie_df2['lines'].apply(len)

    movie_df3 = movie_df2.sort_values('lines_len', ascending = False).reset_index(drop=True)
    return movie_df3


def file_to_df(filename):
    movie_script = read_script(filename)
    movie_dict = script_to_dict(movie_script)
    movie_df = movie_dict_to_df(movie_dict, filename[:-4])
    return movie_df