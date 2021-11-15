#------------------------------------------#
# Title: CDInventory.py
# Desc: Script to create a txt file with user entered data.
# Change log [Who, When, What]
# rtovar, 2021-Nov-13, created file
# rtovar, 2021-Nov-14, Changed lstRow to a dict
# rtovar, 2021-Nov-14, added code to 'x', 'a', 's'
# rtovar, 2021-Nov-14, add "press anything to finish"
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = {}  # diclist of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Have the file load on entry
objFile = open(strFileName, 'r')
for row in objFile:
    lstSvd = row.strip().split(',')
    lstRow = {'ID': lstSvd[0], 'CD Title': lstSvd[1], 'Artist': lstSvd[2]}
    lstTbl.append(lstRow)
objFile.close()

# Print what is in the file w/some formatting 

print('ID, CD Title, Artist\n')
for row in lstTbl:
    print(*row.values(), sep = ' |\t ', end=' |\n\n')


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstSvd = row.strip().split(',')
            lstRow = {'ID': lstSvd[0], 'CD Title': lstSvd[1], 'Artist': lstSvd[2]}
            lstTbl.append(lstRow)
        objFile.close()
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(lstRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist\n')
        for row in lstTbl:
            print(*row.values(), sep = ' |\t ', end=' |\n\n')
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        delID = int(input('Enter an ID to Delete: '))
        for row in lstTbl:
            if delID != row['ID']:                
                lstTbl.remove(row)
                print(row, 'deleted')
            else:
                delID == row['ID']
                print('nope')
        pass
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            print(row)
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Your information has been saved! \n')
        input('Press any key to continue: \n')
    else:
        print('\nPlease choose either l, a, i, d, s or x!\n')
