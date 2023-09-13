from torch.utils.data import Dataset
import numpy as np
import os
import torch

from torch.utils.data import DataLoader
from torch.utils.data import random_split

class DatasetPTBXL(Dataset):

    def __init__(self, path,p_name):
        self.path = path
        self.len = len(os.listdir(self.path))
        self.ptlg_list = ['SR', 'AFIB', 'STACH', 'SARRH', 'SBRAD', 'PACE', 'SVARR', 'BIGU', 'AFLT', 'SVTAC', 'PSVT', 'TRIGU']
        self.target_name = p_name
    def __len__(self):
        return self.len


    def __getitem__(self, idx):
        file = np.load(self.path + str(idx+1) + '.npy', allow_pickle=True).item()
        return torch.from_numpy(file['data']).type('torch.FloatTensor'), torch.from_numpy(file['target'][self.ptlg_list.index(self.target_name)]).type('torch.FloatTensor')
        




def DatasetCreation(ptlg_name, t_size = 0.8, v_size = 0.1, batch_size = 500, path = 'files_processed/', num_workers = 1, pin_memory = True):
  
    dataset = DatasetPTBXL(path,ptlg_name)
    
    tmp_len = len(dataset)
    train_size = int (t_size * tmp_len)
    valid_size = int (v_size * tmp_len)
    test_size = tmp_len - train_size - valid_size

    train_dataset, valid_dataset,test_dataset = random_split(dataset, [train_size, valid_size, test_size])
    
    train_dataset = DataLoader(train_dataset, batch_size, num_workers = num_workers, pin_memory = pin_memory )
    valid_dataset = DataLoader(valid_dataset, batch_size, num_workers = num_workers, pin_memory = pin_memory )
    test_dataset  = DataLoader(test_dataset , batch_size, num_workers = num_workers, pin_memory = pin_memory )
    
    return train_dataset,valid_dataset, test_dataset