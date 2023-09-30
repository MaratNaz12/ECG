from torch import no_grad
from torchmetrics.classification import BinaryF1Score
from torchmetrics.classification import BinaryRecall
from torchmetrics.classification import BinarySpecificity
from torchmetrics.classification import BinaryAUROC
from torchmetrics.classification import BinaryAccuracy
import torch.nn as nn

def evaluate(model, valid_dataset,device):
    model.eval()

    metric_F1 = BinaryF1Score().to(device)
    metric_Rec = BinaryRecall().to(device)
    metric_Spec = BinarySpecificity().to(device)
    metric_AUC = BinaryAUROC(thresholds=None).to(device)
    metric_Acc = BinaryAccuracy().to(device)

    with no_grad():
        valid_loss = 0
        samples_num = 0
        for batch in valid_dataset:
            data, targets = batch
            data   = data.to(device)
            target = target.to(device)
            preds = model.validation_step((data,targets))

            loss = nn.BCELoss(reduction='sum')
            vaild_loss += loss(preds, targets)
            samples_num += len(data)

            metric_F1  (preds, targets)
            metric_Rec (preds, targets)
            metric_Spec(preds, targets)
            metric_AUC (preds, targets)
            metric_Acc (preds, targets)
           



    return {'model_acc':               metric_Acc.compute().item(),
            'model_F1score':           metric_F1.compute().item(),
            'model_Recall':            metric_Rec.compute().item(),
            'model_Specificity':       metric_Spec.compute().item(),
            'model_ROCAUC':            metric_AUC.compute().item(),
            'model_total_loss':  valid_loss, 
            'model_mean_loss':   valid_loss / samples_num}
