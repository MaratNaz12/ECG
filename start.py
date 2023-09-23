import os 
import shutil
from Get_data.convert import start_processing
from Get_data.getdata import data_load
from Get_data.unpack import unpack
import argparse

'''
This file starts data loading and processsing
    1. Asks for a confirmation 
    2. Asks if there is a user's path to place dataset
        - THERE IS NO INPUT: path_for_dir = '' ;         data will be placed in the current directory
        - THERE IS INPUT:    path_for_dir =  input() ;   data will be placed in path_for_dir
             file 'userpath_to_dataset.txt' will be created in the current directory to store the path
    3. If PTB_XL.zip or files_processed are not already in the directory continue
    4. Calls for unpack() to unpack archieve, which returnes path to data into path
    5. Calls for start_processing() to convert dara to the required format (.npy)
    6. Delete intermediate data
'''

parser = argparse.ArgumentParser(description='Dataloading configuration')

parser.add_argument( '-ps', '--path_src', type=str, default='', help='dir with data'  )
parser.add_argument( '-pd', '--path_dst', type=str, default='', help='dir for dataset')
parser.add_argument( '-k', '--keep', action = "store_true", help='flag to keep raw data' )


args = parser.parse_args() 


if not (args.path_dst == ''): 
    args.path_dst += '/'

if args.path_src == '':
    if not os.path.exists(args.path_dst + 'PTB_XL.zip') and not os.path.exists(args.path_dst + 'files_processed'):
        print("Downloading started") 
        flag = data_load(args.path_dst)
        if flag == False:
            print("ERROR. Delete downloaded file and start again")  
        else:
            print("Downoading completed") 
    
    else:
        print('Delete old files first')

    args.path_src = args.path_dst
    path = unpack(args.path_dst) 
else:
    args.path_src += '/'  
    path = ''


       
start_processing(args.path_src, args.path_dst,  path)


if not (args.keep):
    shutil.rmtree(args.path_src + 'PTB_XL')


        
    
