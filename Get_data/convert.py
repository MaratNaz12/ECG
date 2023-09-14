import numpy as np
import wfdb
import ast
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


# make binary target vector for each ecg
def aggregate_diagnostic(y_dic, target_list):
      tmp = np.zeros((len(target_list),1))
      for i in range (len(target_list)):
          if target_list[i] in y_dic:
              tmp[i] = 1
      return tmp

        
#convert .dat .hea files into numpy arrays
def load_raw_data(df,path_for_dir,path,target_list,dir_name ):
    #checks if directory exists
    #"count" to name new files
    count = 1
    to_save = 'files_processed/'
    if not os.path.exists(path_for_dir+ to_save):
        os.mkdir(path_for_dir+ to_save)

    for index, row in tqdm(df.iterrows()):

        #.dat .hea -> numpy
        trn,_ = wfdb.rdsamp(path_for_dir+path+row[dir_name])
        trn = np.array(trn).T

        #convert text from database to dicts of pathologies 
        trgt = ast.literal_eval(row['scp_codes']) 
        trgt =aggregate_diagnostic(trgt, target_list)
        
        #saving dicts for each ecg
        tmp_dict = {'data': trn, 'target': trgt}
        np.save(path_for_dir+ to_save+str(count)+'.npy', tmp_dict)
        count+=1




def start_processing(path_for_dir, path):
   
    dir_name = 'filename_hr' #sr = 500

    #creating list of rhytthm  pathologies from scp_statements.csv
    file_statements = pd.read_csv(path_for_dir+ path+ 'scp_statements.csv', index_col = 0)
    rhythm_pathologies  = list(file_statements[file_statements.rhythm == 1].index)

    
    file_database= pd.read_csv(path_for_dir + path+'ptbxl_database.csv', index_col = 'ecg_id')
    load_raw_data(file_database, path_for_dir, path, rhythm_pathologies, dir_name ) 