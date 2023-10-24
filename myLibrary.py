#------------1-------------------#
# prints user input text with green clolor
def myInputPrint(text):  
  result = input(f"""{text} \033[32m""")
  print("\033[0m", end="")
  return result
#-------------2------------------#
#defins timestamp = datetime.now(Riga Time)
def rigaTS():
  import datetime
  import pytz
  rigaTZ = pytz.timezone("Europe/Riga")
  timestamp = datetime.datetime.now(rigaTZ)
  return timestamp
#--------------3-----------------#
#checkes if the sentence is palindrome
def isPalindrome(word):
  word = word.strip().lower()
  if len(word) <= 1:
    return True
  else:
    if word[0] == word[len(word)-1]:
      return isPalindrome(word[1:len(word)-1])
    else: 
      return False
#---------------4----------------#
#calculate factorial
def factorial(number):
  if number == 1:
    return 1
  else:
    return number * factorial(number - 1)
#---------------5----------------#
#create new folder
def createFolder(newFolder):
  import os
  files = os.listdir()
  if newFolder in files:
    return
  else:
    try:
      os.mkdir(newFolder)
    except:
      print("directory exists")
#---------------6----------------#
#create new file
def createFile(newFile):
  import os
  files = os.listdir()
  if newFile in files:
    return
  else:
    try:
      open(newFile, "w")
    except:
      print("file exists")
#---------------7----------------#
def addTxtFileToFolder(myfolder, myfile):
  import os
  songFilePath = os.path.join(myfolder, f"{myfile}.txt")
  if not os.path.exists(songFilePath):
      with open(songFilePath, "w"):
          pass  # Creates an empty file
  else:
      print(f"File for '{myfile}' already exists in '{myfolder}' folder.")

#---------------8----------------#
#add item to myList
def addNewItem(myList, item):
  #myList = [] should be initialized before this method
  myList.append(item)
  print(f"\n{item} has been added to your list.")
  return myList
#---------------9----------------#
#remove item from myList
def removeItem(myList, item):
  if item in myList:
    myList.remove(item)
    print(f"\n{item} has been removed from your inventory.")
  else:
    print(f"{item} is not in your inventory.")
#---------------10----------------#
#autoload
def autoload(file, myList):
  try:
    f = open(file , "r")
    myList = eval(f.read())
    f.close()
  except:
    print("the list is empty")
#---------------11----------------#
#autosave
def autosave(file, myList):
  try:
    f = open(file , "w")
    f.write(str(myList))
    f.close()
  except:
    print("cannot autosave")
#---------------12----------------#
#how many times the letter appears in the word
def howManyTimes (letter, myWord):
  count = 0
  if letter in myWord: 
    for index in range (len(myWord)):
      if letter == myWord[index]:
        count += 1
    return count  
  else:
    return 0
#---------------13----------------#
#prints in different colors the text
def myPrint(color, text): 
  if color.upper() == "RED":
    print("\033[0;31m",text,sep="", end="")
  elif color.upper() == "GREEN": 
    print("\033[0;32m",text,sep="", end="")
  elif color.upper() == "PURPLE":
    print("\033[0;35m",text,sep="", end="")
  elif color.upper() == "CYAN":
    print("\033[0;36m",text,sep="", end="")
  elif color.upper() == "BROWN":
    print("\033[0;33m",text,sep="", end="")
  elif color.upper() == "BLUE":
    print("\033[0;34m",text,sep="", end="")
  elif color.upper() == "LIGHT_GRAY":
    print("\033[0;37m",text,sep="", end="")
  elif color.upper() == "YELLOW":
    print("\033[1;33m",text,sep="", end="")
  elif color.upper() == "LIGHT_GREEN":
    print("\033[1;32m",text,sep="", end="")
  elif color.upper() == "LIGHT_BLUE":
    print("\033[1;34m",text,sep="", end="")
  else:
    print("\033[0m",text,sep="", end="")
  print("\033[0m",sep="", end="")
#---------------14----------------#