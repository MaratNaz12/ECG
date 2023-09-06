import zipfile
def unpack():
    with zipfile.ZipFile('PTB_XL.zip', 'r') as zip_ref:
        zip_ref.extractall('PTB_XL')
        return 'PTB_XL/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'
    