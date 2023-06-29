def naive_bayes_classifier(text, word_freq , class_freq  ):
    """
    DESCRIPTION :
    ------------
        Implements a naive Bayes classifier to determine the probability of an email being spam.

    PARAMETERS:
    ----------
        - text (str): 
            The input email text to classify.
        
        - word_freq (dict): A dictionary containing word frequencies in the training corpus. 
            The keys are words, and the values are dictionaries containing frequencies for 'spam' and 'ham' classes.

        - class_freq (dict): A dictionary containing class frequencies in the training corpus. 
            The keys are class labels ('spam' and 'ham'), and the values are the respective frequencies.

    RETURNS:
    -------
        - float: The probability of the email being spam.

    """
    # lowering the email
    text = text.lower()
    words = set(text.split())

    # initialization with class frequencies
    cumulative_product_spam = class_freq["spam"]
    cumulative_product_ham = class_freq["ham"]
        
    # Iterate over the words in the email
    for word in words:
        # This implementation only include words that exist in the corpus in your calculations
        if word in word_freq.keys():
            cumulative_product_spam *= word_freq[word]["spam"]/class_freq["spam"]
            cumulative_product_ham *= word_freq[word]["ham"]/class_freq["ham"]
    
    # Calculate the posterior probability of the email being spam given that the words appear in the email (the probability of being a spam given the email content)
    prob_spam = cumulative_product_spam / (cumulative_product_spam + cumulative_product_ham)
        
    return prob_spam
