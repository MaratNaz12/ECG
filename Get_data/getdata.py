import requests
from tqdm import tqdm

def data_load():

    url = 'https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1.zip'
    response = requests.get(url, stream=True)

    zipfile_size  = int(response.headers.get('content-length', 0))
    block_size = 1024 *1024
    progress_bar = tqdm(total=zipfile_size, unit='B', unit_scale=True)

    with open('PTB_XL.zip', 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            progress_bar.update(len(data))
    progress_bar.close()

    if zipfile_size != 0 and progress_bar.n != zipfile_size:
        return False
    else:
        return True
    