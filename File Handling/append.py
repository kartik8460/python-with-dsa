f4 = open('append.txt', 'a')
# If the file is not available the above code will create a new file
# Also it will not overwrite the file though it will append the data
f4.write('Data from OpenCLose.py\n')
f4.write('Data from OpenCLose.py Again\n')
f4.writelines('Hi ')
f4.close()
