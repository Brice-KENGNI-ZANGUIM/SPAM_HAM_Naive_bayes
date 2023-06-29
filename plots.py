import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np

def print_confusion_matrix(label_true , label_predict, class_names, figsize = (8,7), cmap = plt.cm.Blues): 
    import itertools
    
    """
    Affiche la transposée de la  matrice de confusion tel que fournie par 
    la fonction sklearn.metrics.confusion_matrix, sous forme de heatmap
    
    Paramètres :
    ------------
        label_true , label_predict : Array_type
             labels exactes et label prédit par le modèle
        class_name : list or Array_type
            label à attribuer aux observations : 0 - 1 , oui - non , bon - mauvais , ok - pas ok
    
    Return : None
    --------
    
    """    

    confusion_matrix = metrics.confusion_matrix( label_true , label_predict)
    print( confusion_matrix)
    confusion_matrix = confusion_matrix.T
    with plt.style.context(('ggplot', 'seaborn')):
        fig = plt.figure(figsize=figsize, num=1)
        plt.imshow(confusion_matrix, interpolation='nearest',cmap= cmap )
        plt.xticks([0,1],class_names , )
        plt.yticks([0,1],class_names)
        plt.xlabel('Vraie étiquette' , size = 3*np.min(figsize) )
        plt.ylabel('Etiqeutte prédite' , size = 3*np.min(figsize))
        for i, j in itertools.product(range(confusion_matrix.shape[0]), range(confusion_matrix.shape[1])):
                    plt.text(j, i,confusion_matrix[i, j], horizontalalignment="center",color="red" , fontsize = 2.2*np.min(figsize))
        plt.grid(None)
        plt.title('Confusion Matrix' , fontsize = 4*np.min(figsize))
        plt.colorbar() 

def plot_gaussian_distributions(gaussian_0, gaussian_1, gaussian_2):
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.hist(gaussian_0, alpha=0.5, label="gaussian_0", bins=32)
    ax.hist(gaussian_1, alpha=0.5, label="gaussian_1", bins=32)
    ax.hist(gaussian_2, alpha=0.5, label="gaussian_2", bins=32)
    ax.set_title("Histograms of Gaussian distributions")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequencies")
    ax.legend()
    plt.show()
    
    
def plot_binomial_distributions(binomial_0, binomial_1, binomial_2):
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.hist(binomial_0, alpha=0.5, label="binomial_0")
    ax.hist(binomial_1, alpha=0.5, label="binomial_1")
    ax.hist(binomial_2, alpha=0.5, label="binomial_2")
    ax.set_title("Histograms of Binomial distributions")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequencies")
    ax.legend()
    plt.show()

