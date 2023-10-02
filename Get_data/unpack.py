import zipfile
import os

'''
Gets path to dataset zip as an argument, unzips it, returns path to data itself
'''

def unpack(path_dst ):
    print("Unpacking started")
    arxiv_path = os.path.join(path_dst, 'PTB_XL.zip')
    with zipfile.ZipFile(arxiv_path, 'r') as zip_ref:
        zip_ref.extractall(path_dst + 'PTB_XL')
    print("Unpacking completed")

    os.remove(arxiv_path)

    return 'PTB_XL/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'