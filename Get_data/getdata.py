import requests
from tqdm import tqdm
import os

url = 'https://physionet.org/static/published-projects/ptb-xl/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1.zip'
response = requests.get(url, stream=True)
print(response.headers)
zipfile_size  = int(response.headers.get('content-length', 0))
block_size = 1024 *1024
progress_bar = tqdm(total=zipfile_size, unit='iB', unit_scale=True)

with open('PTB_XL.zip', 'wb') as file:
    for data in response.iter_content(block_size):
        file.write(data)
        progress_bar.update(len(data))
progress_bar.close()
if zipfile_size != 0 and progress_bar.n != zipfile_size:
    print("ERROR, something went wrong")
else:
    print("DOWNLOAD WAS SUCCESSFUL")
    print("START DATA PROCESSING???",'\n', "type 'yes' if you want to start",'\n')
    s = input()
    if s == 'yes':
        from convert import start_processing
        print("started",'\n')
        start_processing()
        print("finished",'\n')

    else:
        print("then do it by yourself executing start_processing from convert.py calling from ECG")


# os.system("wget -r -N -c -np https://physionet.org/files/ptb-xl/1.0.1/")

# response = requests.get(url, stream=True)