import os 
import shutil
from Get_data.convert import start_processing
from Get_data.getdata import data_load
from Get_data.unpack import unpack

st = input("Start loading data? (it will take 25 min)     y/n: ")
if st == 'y':
    st = input("Do you have special path to download data? (y/n) ")
    path_for_dir = ''
    if st == 'y':
        path_for_dir = input("insert the path: ")
    if not os.path.exists(path_for_dir + 'PTB_XL.zip'):
        flag = data_load(path_for_dir)
        if flag == False:
            print("ERROR. Delete downloaded file and start again")
        else:
            print("Downoading completed",'\n',"Unpacking started")
            path = unpack(path_for_dir) 
            print("Unpacking completed",'\n',"Data converting started")
            os.remove(path_for_dir + "PTB_XL.zip")
            start_processing(path_for_dir + path)
            shutil.rmtree(path_for_dir + 'PTB_XL')
            print("Coverting completed")
    else:
        print("ok, no problems")

