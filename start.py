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

parser.add_argument( '-p', '--path_for_dir', type=str, default='', help='dir for dataset')

parser.add_argument( '-k', '--keep', action = "store_true", help='flag to (no) keep raw data' )

args = parser.parse_args() 

if not (args.path_for_dir == ''): 
    args.path_for_dir += '/'
    with open('userpath_to_dataset.txt', 'w') as file:
            file.write(args.path_for_dir )



if not os.path.exists(args.path_for_dir + 'PTB_XL.zip') and not os.path.exists(args.path_for_dir + 'files_processed'):
    flag = data_load(args.path_for_dir)

    if flag == False:
        print("ERROR. Delete downloaded file and start again")

    else:
        print("Downoading completed",'\n',"Unpacking started")
        path = unpack(args.path_for_dir) 
        print("Unpacking completed",'\n',"Data converting started")

        start_processing(args.path_for_dir, path)

        os.remove(args.path_for_dir + 'PTB_XL.zip')
        shutil.rmtree(args.path_for_dir + 'PTB_XL')

        print("Coverting completed")
else:
    print('files already exist, delete them')



