import matplotlib.pyplot as plt

def visual_res(history, epochs_num ):
    plt.title('res')
    plt.xlabel('epoch')
    plt.ylabel('metric')


   
    plt.plot(list(range(epochs_num)), [x['model_F1score'] for x in history],label = 'F1')
    plt.plot(list(range(epochs_num)), [x['model_Recall'] for x in history],label = 'Recall')
    plt.plot(list(range(epochs_num)), [x['model_Specificity'] for x in history], label = 'Specificity')
    plt.plot(list(range(epochs_num)), [x['model_ROCAUC'] for x in history], label = 'AUC')
    plt.plot(list(range(epochs_num)), [x['model_acc'] for x in history], label = 'Acc')
    plt.plot(list(range(epochs_num)), [x['mean_train_loss'] for x in history], label = 'train_loss')
    plt.plot(list(range(epochs_num)), [x['model_mean_valid_loss'] for x in history], label = 'valid_loss')
    plt.grid(True)
    plt.legend()