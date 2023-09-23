from torch.utils.data import Dataset
import numpy as np
import os
import torch
import ast
import pandas as pd
from torch.utils.data import DataLoader
from torch.utils.data import random_split


class DatasetPTBXL(Dataset):

    def __init__(self, path,p_name):

        self.path = path +'data/'

        self.df = pd.read_csv(self.path + 'ptbxl_database.csv', index_col = 'ecg_id')       

        self.target_name = p_name

    def __len__(self):
        return  len(os.listdir(self.path + 'files_processed/' ))


    def __getitem__(self, idx):
        data = np.load(self.path + 'files_processed/' + str(idx+1) + '.npy')

        target  = int(self.target_name in ast.literal_eval(self.df.iloc[idx]['scp_codes'])) 

        return torch.from_numpy(data), torch.tensor(target, dtype=torch.float32)
        




def DatasetCreation(path, ptlg_name, t_size = 0.8, v_size = 0.1, batch_size = 500, num_workers = 1, pin_memory = True):
  
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