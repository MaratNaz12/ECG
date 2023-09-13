import matplotlib.pyplot as plt

def visual_res(history, epochs_num ):
    plt.title('Динамика обучения')
    plt.xlabel('Эпоха')
    plt.ylabel('Метрика')


   
    plt.plot(list(range(epochs_num)), [x['model_F1score'] for x in history],label = 'F1')
    plt.plot(list(range(epochs_num)), [x['model_Recall'] for x in history],label = 'Recall')
    plt.plot(list(range(epochs_num)), [x['model_Specificity'] for x in history], label = 'Specificity')
    plt.plot(list(range(epochs_num)), [x['model_ROCAUC'] for x in history], label = 'AUC')
    plt.plot(list(range(epochs_num)), [x['model_acc'] for x in history], label = 'Acc')
 
    plt.grid(True)
    plt.legend()