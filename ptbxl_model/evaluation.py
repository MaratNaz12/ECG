import torch
from torchmetrics.classification import BinaryF1Score
from torchmetrics.classification import BinaryRecall
from torchmetrics.classification import BinarySpecificity
from torchmetrics.classification import BinaryAUROC
from torchmetrics.classification import BinaryAccuracy


def evaluate(model, valid_dataset,device):
    model.eval()

    metric_F1 = BinaryF1Score().to(device)
    metric_Rec = BinaryRecall().to(device)
    metric_Spec = BinarySpecificity().to(device)
    metric_AUC = BinaryAUROC(thresholds=None).to(device)
    metric_Acc = BinaryAccuracy().to(device)

    with torch.no_grad():
        for batch in valid_dataset:
            data, target = batch
            data   = data.to(device)
            target = target.to(device)
            tmp = model.validation_step((data,target))

            metric_F1(tmp['batch_preds'], tmp['batch_targets'] )
            metric_Rec(tmp['batch_preds'], tmp['batch_targets'] )
            metric_Spec(tmp['batch_preds'], tmp['batch_targets'] )
            metric_AUC(tmp['batch_preds'], tmp['batch_targets'] )
            metric_Acc(tmp['batch_preds'], tmp['batch_targets'] )



    return {'model_acc': metric_Acc.compute().item(),
          'model_F1score': metric_F1.compute().item(),
          'model_Recall': metric_Rec.compute().item(),
          'model_Specificity': metric_Spec.compute().item(),
          'model_ROCAUC': metric_AUC.compute().item() }
