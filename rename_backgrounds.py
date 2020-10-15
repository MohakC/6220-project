import os

PATH_TO_LIGHT_BACKGROUNDS = 'light_backgrounds/'
PATH_TO_DARK_BACKGROUNDS = 'dark_backgrounds/'


for count, filename in enumerate(os.listdir(PATH_TO_LIGHT_BACKGROUNDS)): 
    dst ="lightBackground" + str(count) + ".jpeg"
    src =PATH_TO_LIGHT_BACKGROUNDS + filename 
    dst =PATH_TO_LIGHT_BACKGROUNDS + dst 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst)

for count, filename in enumerate(os.listdir(PATH_TO_DARK_BACKGROUNDS)): 
    dst ="darkBackground" + str(count) + ".jpeg"
    src =PATH_TO_DARK_BACKGROUNDS + filename 
    dst =PATH_TO_DARK_BACKGROUNDS + dst 
          
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 