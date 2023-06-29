import pandas as pd

def split_datas ( dataframe , frac = (.7 , .3 ) ) :
    """
    DESCRIPTION :
    -----------
        Take a DateFrame and split into to differents dataframes for training and testing

    PARAMETERS :
    -----------
        - dataframe (DataFrame): initial DataFrame to be split in two parts
        - frac ( tuple) : a tuple that contain the proportion of train and test data to perform
            The first element correspond to the proportion of training set and the second to the test

    RETURN :
    ------
        - DataFrame , DataFrame : a tuple of DataFrame. The first element is the training and the second the test
    """

    # shuffel the datas
    dataframe = dataframe.sample(frac = 1)

    # Define a 70/30 training/testing split
    train_len = int(dataframe.shape[0]*frac[0])

    # Do the split
    train_data = dataframe[:train_len].reset_index(drop=True)
    test_data = dataframe[train_len:].reset_index(drop=True)

    return train_data, test_data

def load_dataset( datapath ):
    """
    DESCRIPTION :
    ------------
        load .csv Data from a given path and process it

    PARAMETERS :
    -----------
        - datapath ( str ) : the path to the data to load

    RETURNS: 
    -------
        - DataFrame : Load and process DataFrame
    """ 

    # Load the dataset
    emails = pd.read_csv(datapath )

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
