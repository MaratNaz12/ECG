import os 
import shutil
from Get_data.convert import start_processing
from Get_data.getdata import data_load
from Get_data.unpack import unpack

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

str_input = input("Start loading data? (it will take 25 min)     y/n: ")

if str_input == 'y':

    str_input = input("Do you have special path to download data?  (y/n) ")
    
    if str_input == 'y':
        path_for_dir = input("insert the path (ending with '/'): ")
        with open('userpath_to_dataset.txt', 'w') as file:
            file.write(path_for_dir)
    else:
        path_for_dir = ''

    

    if not os.path.exists(path_for_dir + 'PTB_XL.zip') and not os.path.exists(path_for_dir + 'files_processed'):
        flag = data_load(path_for_dir)

        if flag == False:
            print("ERROR. Delete downloaded file and start again")

        else:
            print("Downoading completed",'\n',"Unpacking started")
            path = unpack(path_for_dir) 
            print("Unpacking completed",'\n',"Data converting started")

            start_processing(path_for_dir, path)

            os.remove(path_for_dir + 'PTB_XL.zip')
            shutil.rmtree(path_for_dir + 'PTB_XL')

            print("Coverting completed")
    else:
        print('files already exist, delete them')

else:
    print("ok, no problems")



