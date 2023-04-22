# movie-character-matching

Our project uses natural language processing and machine learning tools in Python to match snippets of text to a movie character based on semantic similarity. After building a model to achieve this text, a user can then enter their own text (or someone else's) and see who they match with. The final app can be found [here](https://huggingface.co/spaces/christinaxxx/Movie_Character_Matching).

**Members**: Isabella Escamilla, Christina Nassar, Megan Wong

Our data source for this project comes primarily from imsdb.com, an online database of movie scripts. We have chosen scripts based off of popularity, character recognition, and availability (some movies are more difficult to get scripts online for). 

## Movie Dataframe
The movie dataframe used in our project has been created from the movie scripts using Python. The details of this transformation can be found in the jupyter notebook titled 
**1_script_to_df.ipynb** while the functions themselves can be found in **scriptfuncts.py**. The resulting reformatted data can be found in **moviedata.csv**.

### Codebook for moviedata.csv
There are 4 columns in the csv file:

`movie`: Gives (an abbreviated version of) the name of the movie that the character is from.

`character_name`: Gives the name of the movie character.

'line_num': Gives the line number of the line in a particular observation.

`line`: Gives the line spoken by the character as a string.

## Models
We tested with two different models: support vector machines (SVM) and multi-layer perceptrons (MLP). We also tested using unigrams only against a combination of unigrams and bigrams. After tuning and testing the models on testing data, the f1 scores were as follows:

|---|---|---|
| | Unigrams Only | Unigrams and Bigrams |
|---|---| --- |
|**SVM** | 0.524 | 0.532 |
|**MLP** | 0.538 | 0.554 |

We used the Unigrams and Bigrams MLP in our final app.

In the future, we also want to include sentence transformers in our models, but that is still being worked on.

## Packages
The packages used in this project include Pandas, Scikit-Learn, SpaCy, Joblib, and Gradio.

