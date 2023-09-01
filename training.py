import torch
import visualization as vs
import evaluation as evl

def fit(epochs_num, lr,model, device, train_dataset, valid_dataset, opt = torch.optim.Adam, wd = True, gc = True):

    
    optimizer = opt(model.parameters(), lr, weight_decay = wd)
    history = []


    for epoch in range(epochs_num):
        torch.cuda.empty_cache()
        model.train()
        train_loss = 0
        samples_num = 0

        for batch in train_dataset:
            data, target = batch
            data   = data.to(device)
            target = target.to(device)
            
            
            loss = model.training_step((data,target))
            loss.backward()
            #if gc == True:
            #   torch.nn.utils.clip_grad_norm_(model.parameters(), args.clip)
            optimizer.step()
            #optimizer.zero_grad()

            train_loss  += loss.detach()
            samples_num += len(data)

        result = evl.evaluate(model, valid_dataset, device)
        result['train_loss'] = train_loss / samples_num
        history.append(result)

        print('Epoch ', epoch,end = "")
        print(': train_loss = %.4f'%(train_loss/ samples_num))

    return history


def train_model(model, device,  train_dataset, valid_dataset, epochs_num, lr, opt = torch.optim.Adam, wd = True, gc = True):
    model = model.to(device)
    history = fit(epochs_num, lr,model, device, train_dataset, valid_dataset,opt,wd,gc)
    vs.isual_res(history,epochs_num)
    return model