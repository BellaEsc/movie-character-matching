import re
import os
import pandas as pd


def read_script(filename):
    ''' takes the script's filename
    and outputs it as a string '''
    path = os.path.join(os.path.abspath(''), 'moviescripts', filename)

    with open(path) as file:
        script = file.read()

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
            d[name].append(txt.strip().replace('\n', ' '))
        else:
            d[name] = [txt.strip().replace('\n', ' ')]
    
    return d


def movie_dict_to_df(movie_dict, movie_name):
    ''' Takes the movie dictionary and the name of the movie
    and turns it into a properly formatted dataframe. Only 
    contains speakers with >100 lines.'''
    df = pd.DataFrame.from_dict(movie_dict, orient='index').stack().reset_index()
    df.columns = ['character_name', 'line_num', 'line']

    df2 = df[(df['character_name'].str.len() > 1)].copy(deep=True)
    df2['line'] = df2['line'].str.lower()
    df2['character_name'] = df2['character_name'].str.title()

    movie_name_format = movie_name.replace('_', ' ').title()

    counts = df2['character_name'].value_counts()
    filtered_df = df2[df2['character_name'].isin(counts[counts > 100].index)]
    filtered_df.insert(0, 'movie', movie_name_format)

    return filtered_df


def file_to_df(filename):
    ''' Takes the .txt file name of the movie script
    and turns it into a properly formatted dataframe.'''
    movie_script = read_script(filename)
    movie_dict = script_to_dict(movie_script)
    movie_df = movie_dict_to_df(movie_dict, filename[:-4])

    return movie_df


def movies_to_df(movie_folder):
    '''Takes the name of the movie folder as a string
    and outputs a dataframe with all of the movies' top 7
    speakers, their lines, and the movie they came from.'''
    all_movies = os.listdir(movie_folder)
    movies = []

    for movie in all_movies:
        movie_df = file_to_df(movie)
        movies.append(movie_df)
    
    movies_df = pd.concat(movies)

    return movies_df