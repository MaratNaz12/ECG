import numpy as np
import wfdb
import pandas as pd
from tqdm import tqdm
import os
from shutil import copyfile

'''
Построчно проходим по файлу ptbxl_database.csv, создаем вектор бинарных таргетов по патологиям [12x1] и, 
используя имена файлов из таблицы, обращаемся к ним и с помощью wfdb.rdsamp получаем матрицу данных [12x5000]. 
Далее создаем словарик из data/targets и записываем его в файл.npy 
файл scp_statements.csv нужен, чтобы получить список всех патологий
(возможно, стоит использвать альернативу словарику, так как файлы получаются тяжелыми.)
'''


        
#convert .dat .hea files into numpy arrays
def load_raw_data(df,path_src, path_for_dir,path,dir_name ):


    to_save = 'files_processed/'
    if not os.path.exists(path_for_dir+ to_save):
        os.mkdir(path_for_dir+ to_save)

    for index, row in tqdm(df.iterrows(), total=21837, desc = "Data processing status"):

        # .dat .hea -> numpy
        trn,_ = wfdb.rdsamp(path_src+path+row[dir_name])
        trn = np.array(trn, dtype = np.float32).T
    

        np.save(path_for_dir+ to_save+str(index)+'.npy', trn)



def start_processing(path_src, path_for_dir, path):
    if not os.path.exists(path_for_dir + 'data'):
        os.mkdir(path_for_dir+ 'data/')

    copyfile(path_src + 'ptbxl_database.csv', path_for_dir +'data/' + 'ptbxl_database.csv')

    dir_name = 'filename_hr' #sr = 500
    
    file_database= pd.read_csv(path_src + path+'ptbxl_database.csv', index_col = 'ecg_id')
    load_raw_data(file_database,path_src, path_for_dir + 'data/', path,  dir_name ) 

