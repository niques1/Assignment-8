import os 

# ask the user for directory

directory = input('Enter the directory to save file:')

#if the user hits the enter key, default directory to current directory 
if directory == '':
    directory = os.path.dirname(os.path.realpath(__file__))

# ask user for the filename
file_name = input('Enter file name: ')

#ask the user for the relevant details

name = input('Enter name: ')
address = input('Enter address: ')
phone_num = input('Enter phone number: ')

#create a new file to write to particular file in the directory

with open('{}/{}.csv'.format(directory, file_name), 'w') as file:
    file.write(','.join([name, address, phone_num]) + '\n')

#create a new file to read to particular file in the directory

with open('{}/{}.csv'.format(directory, file_name), 'r') as file:

    print('{}\{}.csv contents'.format(directory, file_name))
  
  #loop through each file and print.   

    for line in file:
        print(line)



