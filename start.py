import os 
from Get_data.convert import start_processing
from Get_data.getdata import data_load
from Get_data.unpack import unpack

if not os.path.exists('PTB_XL.zip'):
    print("Start loading data? (type 'yes' to agree)")
    st = input()
    if st == 'yes':
        flag = data_load()
        if flag == False:
            print("ERROR. Delete downloaded file and start again")
        else:
            print("Downoading completed",'\n',"Unpack zip? (type 'yes' to agree)")
            st = input()
            if st == 'yes':
                path = unpack() 
                print("Unpacking completed",'\n',"Start data converting? (type 'yes' to agree)")
                st = input()
                if st == 'yes':
                    start_processing(path)
                    print("Coverting completed")
        
        
