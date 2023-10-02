import os 
import shutil
from Get_data.convert import start_processing
from Get_data.getdata import data_load
from Get_data.unpack import unpack
import argparse



parser = argparse.ArgumentParser(description='Dataloading configuration')

parser.add_argument( '-ps', '--path_src', type=str, default='', help='dir with data'  )
parser.add_argument( '-pd', '--path_dst', type=str, default='', help='dir for dataset')
parser.add_argument( '-k', '--keep', action = "store_true", help='flag to keep raw data' )


args = parser.parse_args() 


# if not (args.path_dst == ''): 
#     args.path_dst += '/'

if args.path_src == '':
    arxiv_path = os.path.join(args.path_dst, 'PTB_XL.zip')
    processed_dir = os.path.join(args.path_dst, 'files_processed')
    if not arxiv_path and not processed_dir:
        print("Downloading started") 
        flag = data_load(args.path_dst)
        if flag == False:
            print("ERROR. Delete downloaded file and start again")  
        else:
            print("Downoading completed") 
    
    else:
        print('Delete old files first')

    args.path_src = args.path_dst
    path = unpack(args.path_dst) 
else:
    args.path_src += '/'  
    path = ''


       
start_processing(args.path_src, args.path_dst,  path)


if not (args.keep):
    shutil.rmtree(args.path_src)


        
    
