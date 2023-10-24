import myLibrary as ml
## 1 
print()
input = ml.myInputPrint("Enter the green input > ")
## 2
print()
timestamp = ml.rigaTS()
print(timestamp)
## 3
print()
print(ml.isPalindrome("kl jjlk"))
##4
print()
print(ml.factorial(5))
##5
print()
ml.createFolder("111")
##6
print()
ml.createFile("222")
##7
print()
ml.addTxtFileToFolder("111", "myFile")
##8##9
print()
myList = []
ml.addNewItem(myList, "Hello")
print("Add: ", myList)
ml.removeItem(myList, "Hello")
print("Remove ", myList)
##10##11
print()
myList = []
file = "myFile.txt"
ml.autoload(file, myList)
ml.autosave(file, myList)
##12
print()
print(ml.howManyTimes("a", "kal ambura"))
##13
print()
ml.myPrint("CYAN", "Hello All")
          
