import numpy as np
import wfdb
import ast
from unpack import unpack
import pandas as pd
from tqdm import tqdm
import os

'''
Построчно проходим по файлу ptbxl_database.csv, создаем вектор бинарных таргетов по патологиям [12x1] и, 
используя имена файлов из таблицы, обращаемся к ним и с помощью wfdb.rdsamp получаем матрицу данных [12x5000]. 
Далее создаем словарик из data/targets и записываем его в файл.npy 
файл scp_statements.csv нужен, чтобы получить список всех патологий
(возможно, стоит использвать альернативу словарику, так как файлы получаются тяжелыми.)
'''



def aggregate_diagnostic(y_dic, target_list):
      tmp = np.zeros((len(target_list),1))
      for i in range (len(target_list)):
          if target_list[i] in y_dic:
              tmp[i] = 1
      return tmp

        
def load_raw_data(df,path,target_list,dir_name  ):
    print('processing stareted')
    count = 1
    to_save = 'files_processed/'
    if not os.path.exists(to_save):
        os.mkdir(to_save)

    for index, row in tqdm(df.iterrows()):

        trn,_ = wfdb.rdsamp(path+row[dir_name])
        trn = np.array(trn).T

        trgt = ast.literal_eval(row['scp_codes']) 
        trgt =aggregate_diagnostic(trgt, target_list)
        
        
        tmp_dict = {'data': trn, 'target': trgt}
        np.save(to_save+str(count)+'.npy', tmp_dict)
        count+=1
    print('processing finished')


def start_processing():
    #possible to implement choice of sampl.rate 100/500 as input
    sampling_rate = 500
    dir_name = 'filename_hr'
    path = unpack()

    agg_df = pd.read_csv(path+ 'scp_statements.csv', index_col = 0)
    
    target_list  = list(agg_df[agg_df.rhythm == 1].index)

    Y = pd.read_csv(path+'ptbxl_database.csv', index_col = 'ecg_id')
    data = load_raw_data(Y, path, target_list, dir_name ) 