def word_freq_per_class( dataframe ):
    """
    PARAMETERS :
    -----------
        Calculates the frequency of words in each class (spam and ham) based on a given dataframe.

    PARAMETERS :
    -----------
        - dataframe (pandas.DataFrame): The input dataframe containing email data, 
        with a column named 'words' representing the words in each email.

    Returns:
        - dict: A dictionary containing the frequency of words in each class. 
            The keys of the dictionary are words, and the values are nested dictionaries with keys 
            'spam' and 'ham' representing the frequency of the word in spam and ham emails, respectively.
    """
    
    word_freq_dict = {}
        
    # This method yields an index and the data in the row so you can ignore the first returned value. 
    for _, sub_df in dataframe.iterrows():
        # Iterate over the words in each email
        for word in sub_df["words"]:
            # Check if word doesn't exist within the dictionary
            if word not in word_freq_dict.keys():
                # If word doesn't exist, initialize the count at 0
                word_freq_dict[word] = {"spam": 0, "ham": 0}
            
            # Check if the email was spam
            match sub_df["spam"]:
                case 0: 
                    # If ham then add 1 to the count of ham
                    word_freq_dict[word]["ham"] += 1
                case 1: 
                    # If spam then add 1 to the count of spam
                    word_freq_dict[word]["spam"] += 1  

    return word_freq_dict

def class_frequencies(dataframe):
    """
    DESCRIPTION :
    ------------
        Calculate the frequencies of classes in a DataFrame.

    PARAMETERS:
    ----------
        - dataframe (DataFrame): The input DataFrame containing a column 'spam' indicating class labels.

    RETURNS :
        - dict: A dictionary containing the frequencies of the classes.
            The keys are 'spam' and 'ham', representing the class labels.
            The values are the corresponding frequencies in the DataFrame.
    """
        
    class_freq_dict = { 
        "spam": ( dataframe.spam == 1 ).sum() ,
        "ham" : ( dataframe.spam == 0 ).sum()
    } 
        
    return class_freq_dict