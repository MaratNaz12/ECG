from torch.utils.data import Dataset
import numpy as np
import os
import torch
import ast
import pandas as pd
from torch.utils.data import DataLoader
from torch.utils.data import random_split


class DatasetPTBXL(Dataset):

    def __init__(self, cfg_dataset):

        self.path_for_data = cfg_dataset.path_for_sigs + '/'
        self.path_for_map =  cfg_dataset.path_for_datamap + '/'
    
        self.df = pd.read_csv(self.path_for_map+ 'ptbxl_database.csv', index_col = 'ecg_id')       

        self.target_name = cfg_dataset.pat_name

    def __len__(self):
        return  len(os.listdir(self.path_for_data ))


    def __getitem__(self, idx):
        data = np.load(self.path_for_data + str(idx+1) + '.npy')

        target  = int(self.target_name in ast.literal_eval(self.df.iloc[idx]['scp_codes'])) 

        return torch.from_numpy(data), torch.tensor(target, dtype=torch.float32)
        




def DatasetCreation(cfg_dataset):
  
    dataset = DatasetPTBXL(cfg_dataset)
    
    tmp_len = len(dataset)
    train_size = int (cfg_dataset.split[0] * tmp_len)
    valid_size = int (cfg_dataset.split[1] * tmp_len)
    test_size = tmp_len - train_size - valid_size

    train_dataset, valid_dataset,test_dataset = random_split(dataset, [train_size, valid_size, test_size])
    batch_size = cfg_dataset.batch_size
    train_dataset = DataLoader(train_dataset, batch_size, num_workers = cfg_dataset.num_workers, pin_memory = cfg_dataset.pin_memory )
    valid_dataset = DataLoader(valid_dataset, batch_size, num_workers = cfg_dataset.num_workers, pin_memory = cfg_dataset.pin_memory )
    test_dataset  = DataLoader(test_dataset , batch_size, num_workers = cfg_dataset.num_workers, pin_memory = cfg_dataset.pin_memory )
    
    return train_dataset,valid_dataset, test_dataset