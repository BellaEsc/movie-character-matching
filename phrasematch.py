import spacy
import pandas as pd

nlp = spacy.load('en_core_web_lg')
data = pd.read_csv('data/moviedata2.csv')

def get_best_match(phrase, character, moviedata):
    '''Matches the phrase to the most similar line spoken
    by a given character'''

    phrase_doc = nlp(phrase)
    char_lines = moviedata[moviedata['character_name'] == character]['line'].apply(nlp).reset_index(drop=True)

    for i in range(len(char_lines)):

        if i==0:
            best_match = char_lines[i]
            max_similarity = 0
            next

        similarity = phrase_doc.similarity(char_lines[i])

        if similarity > max_similarity:
            best_match = char_lines[i]
            max_similarity = similarity
    
    return best_match, max_similarity

best_match, max_similarity = get_best_match("I can't believe you destroyed the sacred bond.", "Harry Potter", data)

print(f'Best Match: {best_match} \nSimilarity: {max_similarity:.2f}')


def phrase_match(user_input_list, matched_character, moviedata):
    '''Finds best phrase match between all of the user's inputs
    and their matched character.'''
    
    for i in range(len(user_input_list)):
        match, similarity = get_best_match(user_input_list[i], matched_character, moviedata)
        if i == 0:
            input_match = user_input_list[i]
            best_match = match
            max_similarity = similarity
            next
        
        if similarity > max_similarity:
            input_match = user_input_list[i]
            best_match = match
            max_similarity = similarity
    
    return input_match, best_match, max_similarity

my_phrases = ["It's a mighty fine day today.", "This is absurd! I demand to see who is in charge here.", "If only I was a frog hopping around in a murky bog."]

input_phrase, match, similarity = phrase_match(my_phrases, 'Jack Sparrow', data)
print(f'Best Match: {match} \nInput: {input_phrase} \nSimilarity: {similarity:.2f}')