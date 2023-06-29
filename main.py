import pandas as pd
from plots import print_confusion_matrix
from datas_loading import load_dataset, split_datas
from naive_bayes_categorical_classifier import naive_bayes_classifier
from frequencies import ( word_freq_per_class , 
                         class_frequencies 
                         )


if __name__ == "__main__" :
    # loading the datas ( emails )
    emails = load_dataset()

    # generate train and tests emails datas
    train_emails , test_emails = split_datas( emails , (.5 , .5))
    #print(emails.head())

    # get a dictionary of frequency of every word for each classes
    # This content all the posterior probability requiere to perform the bayes classification
    word_freq = word_freq_per_class(train_emails)

    # get the frequency of every class ( spam, ham )
    class_freq = class_frequencies(train_emails)

    #Evaluate the model :  confusion matrix ploting
    true_label    = test_emails["spam"]
    predict_label = test_emails["text"].apply(lambda x : int(naive_bayes_classifier( x , word_freq, class_freq) > 0.5))
    print_confusion_matrix(true_label , predict_label , class_names=("ham", "spam"), cmap = "hot_r")

    # Test your function
    msg = "Thank you for your application to our job proposition, we will like to invite you for an interview"
    print(f"- Email :'{msg}' \n- Probability to be a SPAM : {100*naive_bayes_classifier(msg , word_freq, class_freq):.3f}%\n")


