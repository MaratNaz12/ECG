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

parser.add_argument( '-ps', '--path_src', type=str, default='', help='dir with data')
parser.add_argument( '-pd', '--path_dst', type=str, default='', help='dir for dataset')

parser.add_argument( '-kd', '--keep_data', action = "store_true", help='flag to keep raw data' )

parser.add_argument( '-kz', '--keep_zip', action = "store_true", help='flag not to unzip zip' )

parser.add_argument( '-hz', '--have_zip', action = "store_true", help='flag to unzip then process' )

parser.add_argument( '-hd', '--have_raw_data', action = "store_true", help='flag to only process' )

args = parser.parse_args() 


if not (args.path_dst == ''): 
    args.path_dst += '/'

if not (args.path_src == ''): 
    args.path_src += '/'   


if not (args.have_zip):
    args.path_src = args.path_dst
    if not os.path.exists(args.path_dst + 'PTB_XL.zip') and not os.path.exists(args.path_dst + 'files_processed'):
        print("Downloading started") 
        flag = data_load(args.path_dst)
        if flag == False:
            print("ERROR. Delete downloaded file and start again")  
        else:
            print("Downoading completed") 
    
    else:
        print('Delete old files first')


path = unpack(args.path_src, args.path_dst, args.have_raw_data, args.keep_zip) 

args.path_dst = args.path_src
       
start_processing(args.path_src, args.path_dst,  path)


if args.have_raw_data:
    args.path_dst = args.path_src


if not (args.keep):
    shutil.rmtree(args.path_dst + 'PTB_XL')


        
    
