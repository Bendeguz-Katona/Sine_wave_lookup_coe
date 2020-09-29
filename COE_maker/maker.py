import math
#29. Sept. 2020: Created
#Author: Bendeguz Katona


#DESCRIPTION:
#This script creates a sine-wave lookup table with user-set amounts of datapoints per period,
#number of periods and max-min values.
#The created .coe file can be used to initialise RAM in vivado for a sine-wave lookup table.
#The output datapoints are radix 10 integers.

#Python version used for the project:
#Python 3.8.3rc1

#SETTINGS------------------------------------------------------------------------------------------------------
#Number of datapoints for a whole period:
n = 128
#Peak values of sine wave:
min_peak = -10
max_peak = 10
#Number of periods:
n_per = 1                        
#Path to output .txt file:
filepath_out = "Sine.norm.coe"
#Path to chosen header - it will be copied to ouput first:
filepath_header = "Header.txt"


#SETUP---------------------------------------------------------------------------------------------------------
y = 0.0                                     #Start value for rad variable.
increment = 2* math.pi / n                  #Increment of rad variable - Calculated using user-set variable n; number of datapoints.



#WIRITNG HEADER FOR .COE FILE (CAN BE CHANGED TO TASTE - SEMICOLONS AT START OF LINE ARE MUST FOR COMMENTS)-----
with open(filepath_out, 'a') as f:
    for line in open(filepath_header):
        f.write(line)



#WRITING DATAPOINTS---------------------------------------------------------------------------------------------
f = open(filepath_out, "a+")                #Open file given using filepath variable. If it doesn't exist, it will be created on first run.
f.seek(0,2) #Jumps to the end

while (y <= n_per * 2 * math.pi):                     #Loop to calculate and write datapoints to file.
    x = math.sin(y) * ((max_peak - min_peak) / 2) + ((min_peak + max_peak) / 2) 
    if ((y+increment) <= (2*math.pi)):      #Write datapoints to output.
        f.writelines(f'{math.floor(x)},\n')
    else:                                   #After last datapoint put semicolon instead of comma, and use no newline-char.
        f.writelines(f'{math.floor(x)};')
    y = y+increment                         #Increment rad variable

#Close file
f.close()