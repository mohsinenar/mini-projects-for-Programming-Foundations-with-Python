import os

def rename_files():
    # get the list of names
    file_list = os.listdir(r"E:\python\rename")
    #rename files
    os.chdir(r"E:\python\rename")
    for file_name in file_list :
        # here i get some issue because i work on python 3.6.2 and the function tranlate have been chnged  
        #uncomment this line to rename files  in "rename folder" 
        # os.rename(file_name,file_name.strip("0123456789"))
        
        os.rename(file_name,"name")
        print("old name is :" + file_name + ", new name is :" + file_name.strip("0123456789") )
        
rename_files()


