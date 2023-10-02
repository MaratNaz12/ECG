import torch
import evaluation as evl
from tqdm import tqdm

def fit(epochs_num, model, optimizer, device, train_dataset, valid_dataset):

    history = []


    for epoch in range(epochs_num):
        torch.cuda.empty_cache()
        model.train()
        train_loss = 0
        samples_num = 0

        for batch in tqdm(train_dataset, desc = f"epoch{epoch}"):

            data, target = batch
            data   = data.to(device)
            target = target.to(device)
            
            
            loss = model.training_step((data,target))
            loss.backward()
            optimizer.step()

            train_loss  += loss.item()
            samples_num += len(data)

        result = evl.evaluate(model, valid_dataset, device)
        result['mean_train_loss'] = train_loss / samples_num
        result['total_train_loss'] = train_loss 
        history.append(result)

    return model,history


def train_model(model, optim, device,  train_dataset, valid_dataset, epochs_num):
    
    model = model.to(device)
    optimizer = optim (params = model.parameters() )
    model,history = fit(epochs_num, model, optimizer, device, train_dataset, valid_dataset)
    return model, history