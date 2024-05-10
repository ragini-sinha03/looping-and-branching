import pathlib
import time
#import stellar_analytics_utils

# function1
def create_folders_for_range(start_year,end_year):
    ''' to create folders for a range of years'''
    project_path=pathlib.Path.cwd()
    for years in range(start_year,end_year+1):
        year_path=project_path.joinpath(str(years))
        year_path.mkdir()


# function2
def create_folders_from_list(folder_list,to_lowercase=False, remove_spaces=False):
    ''' to create folders from a list of names'''
    project_path=pathlib.Path.cwd()
    for folder_name in folder_list:
        if to_lowercase:
            folder_name=folder_name.lower()
        if remove_spaces:
            folder_name=folder_name.replace('','')
        folder_path=project_path.joinpath(folder_name)
        folder_path.mkdir()


# function 3
def create_prefixed_folders(folderlist, prefix):
    ''' to create folders with prefix'''
    project_path=pathlib.Path.cwd()
    for folder_name in folderlist:
        folder_path=project_path.joinpath(prefix + folder_name)
        folder_path.mkdir()

# function 4
def create_folders_periodically(duration, time_limit):
    ''' to create folders periodically with a time limit'''
    project_path=pathlib.Path.cwd()
    start_time=time.time() # to record the start time
    while time.time() - start_time < time_limit:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        pathlib.Path(timestamp).mkdir(parents=True, exist_ok=True)
        time.sleep(duration)


def main():


    ''' main function will show the capacity of module'''

    # print byline from imported module


    # call function1
    create_folders_for_range(start_year=2020, end_year=2024)

    # call function2
    folder_names=['data-csv','data-excel','data-json']
    create_folders_from_list(folder_names)

    # call function3
    folder_names=['csv','excel','json']
    prefix='data1-'
    create_prefixed_folders(folder_names, prefix)

    #call function4
    
    create_folders_periodically(duration=5, time_limit=10)

    # call function to check below options

    regions=["Asia","Europe","Africa","North America","South America"]
    
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True )


#if __name__=='_ _main_ _':
main()

        


