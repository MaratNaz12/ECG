import zipfile
import os

'''
Gets path to dataset zip as an argument, unzips it, returns path to data itself
'''

def unpack(path_dst ):
    print("Unpacking started")
    with zipfile.ZipFile(path_dst + 'PTB_XL.zip', 'r') as zip_ref:
        zip_ref.extractall(path_dst + 'PTB_XL')
    print("Unpacking completed")

    os.remove(path_dst + 'PTB_XL.zip')

    return 'PTB_XL/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'