from plots import print_confusion_matrix
from datas_loading import load_dataset, split_datas
from naive_bayes_categorical_classifier import naive_bayes_classifier, make_prediction
from frequencies import ( word_freq_per_class , 
                         class_frequencies 
                         )


if __name__ == "__main__" :

    # loading the datas ( emails )
    emails = load_dataset(datapath='medias/csv/emails.csv')

    # generate train and tests emails datas
    train_emails , test_emails = split_datas( emails , (.7 , .3))

    #print(train_emails.head())

    # get a dictionary of frequency of every word for each classes
    # This content all the posterior probability requiere to perform the bayes classification
    word_freq = word_freq_per_class(train_emails)
    # get the frequency of every class ( spam, ham )
    class_freq = class_frequencies(train_emails)

    #Evaluate the model :  confusion matrix ploting
    true_label    = test_emails["spam"]
    predict_label = make_prediction ( test_emails, word_freq, class_freq  ) 
    print_confusion_matrix(true_label , predict_label , class_names=("ham", "spam"), cmap = "hot_r")

    # Test your function
    msg = "hi hi"
    print(f"- Email :'{msg}' \n- Probability to be a SPAM : {100*naive_bayes_classifier(msg , word_freq, class_freq):.3f}%\n")


