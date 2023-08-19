import os

# Specify the directory path you want to list files from
directory_path = '//lubeai_storage/mf_sds_st_source_files/cbccadoil/st'

# List all files and directories in the specified directory
files_and_directories = os.listdir(directory_path)

# Print the list
for item in files_and_directories:
    print(item)