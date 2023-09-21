import zipfile
import os

'''
Gets path to dataset zip as an argument, unzips it, returns path to data itself
'''

def unpack(path_src,path_dist, flag1,flag2  ):
    if not flag1:
        print("Unpacking started")
        with zipfile.ZipFile(path_src + 'PTB_XL.zip', 'r') as zip_ref:
            zip_ref.extractall(path_dist + 'PTB_XL')
        print("Unpacking completed")

    if not flag2:
            os.remove(path_src + 'PTB_XL.zip')

    return 'PTB_XL/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'