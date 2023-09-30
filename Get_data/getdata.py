import requests
from tqdm import tqdm

'''
Function data_load collects PTB_XL dataset from the internet with py.requests
tdqm for progress bar
'''



def data_load(path_for_dir ):

    url = 'https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1.zip'
    
    # url = 'https://www.kaggle.com/datasets/khyeh0719/ptb-xl-dataset/download?datasetVersionNumber=1'
    response = requests.get(url, stream=True)

    zipfile_size  = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=zipfile_size, unit='KBi', desc = 'Data loading status', unit_scale=True)

    with open(path_for_dir + 'PTB_XL.zip', 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            progress_bar.update(len(data))
    progress_bar.close()

    if zipfile_size != 0 and progress_bar.n != zipfile_size:
        return False
    else:
        return True
    