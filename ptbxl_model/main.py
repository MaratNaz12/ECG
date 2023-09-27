import torch.optim
import data_preparation as dp
import model as mdl
import training as tr
import argparse

'''
batch_size = 500
t_s = 0.8
v_s = 0.1
num_workers = 1
pin_memory = True
batch_size = 500
path = 'files_processed/'
'''

parser = argparse.ArgumentParser(description='Dataloading configuration')

parser.add_argument('-p', '--path', type=str, default='', help='dir with data'  )

args = parser.parse_args() 

ptlg_name = 'SR'

train_dataset,valid_dataset,test_dataset = dp.DatasetCreation(args.path, ptlg_name)




model = mdl.RhythmECGClassification(12,1)
lr = 0.000
epochs_num = 10
optim = torch.optim.Adam
weight_decay = True
grad_clipping = True
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


model = tr.train_model(model, device, train_dataset, valid_dataset, epochs_num, lr)