# movie-character-matching

Group project for the UCSB Data Science Club. We are using NLTK in Python to match snippets of text to a movie character based on semantic similarity.

**Members**: Christina Nassar, Isabella Escamilla, Megan Wong, Nathan De Los Santos

Our data source for this project comes primarily from imsdb.com, an online database of movie scripts. We have chosen scripts based off of popularity, character recognition, and availability (some movies are more difficult to get scripts online for). 

## Movie Dataframe
The movie dataframe used in our project has been created from the movie scripts using Python. The details of this transformation can be found in the jupyter notebook titled 
**scriptsplitfunction.ipynb** while the functions themselves can be found in **splitfuncts.py**. The resulting reformatted data can be found in **moviedata.csv**.

### Codebook for moviedata.csv
There are 3 columns in the csv file:

`movie_name`: Gives (an abbreviated version of) the name of the movie that the character is from.

`character_name`: Gives the name of the movie character.

`lines`: Gives all of the lines spoken by the particular character as a single string.

