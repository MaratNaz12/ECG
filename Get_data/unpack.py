import zipfile

'''
Gets path to dataset zip as an argument, unzips it, returns path to data itself
'''

def unpack(path_for_dir ):
    with zipfile.ZipFile(path_for_dir + 'PTB_XL.zip', 'r') as zip_ref:
        zip_ref.extractall(path_for_dir + 'PTB_XL')
        return 'PTB_XL/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'
    