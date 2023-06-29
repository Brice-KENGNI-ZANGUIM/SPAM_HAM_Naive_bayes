import pandas as pd

def split_datas ( dataframe , frac = (.7 , .3 ) ) :
    # shuffel the datas
    dataframe = dataframe.sample(frac = 1)

    # Define a 70/30 training/testing split
    train_len = int(dataframe.shape[0]*frac[0])

    # Do the split
    train_data = dataframe[:train_len].reset_index(drop=True)
    test_data = dataframe[train_len:].reset_index(drop=True)

    return train_data, test_data



def load_dataset( ): 
    # Load the dataset
    emails = pd.read_csv('medias/csv/emails.csv')

    # Helper function that converts text to lowercase and splits words into a list
    def process_email(text):
        """
        Processes the given email text by converting it to lowercase, splitting it into words,
        and returning a list of unique words.

        Parameters:
        - text (str): The email text to be processed.

        Returns:
        - list: A list of unique words extracted from the email text.
        """

        text = text.lower()
        return list(set(text.split()))

    # Create an extra column with the text converted to a lower-cased list of words
    emails['words'] = emails['text'].apply(process_email)

    return emails
