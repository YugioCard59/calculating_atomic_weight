'''
From a given list of element symbols with corresponding atomic masses calculate the atomic weight
of a chemical formula that contains only the approved elements
'''
H = 1.00784
C = 12.0096
N = 14.00643
O = 15.99903
F = 18.998403163
P = 30.973761998
def main():
    #display menu of elements to choose from with directions
    printElementMenu()
    #getChmFormulaPerElement() gets the number of atoms per given element
    firstElementAtoms, storageElementAtoms, massTotal, storageWtTotal, firstElementType, storageElementTypes = getChmFormulaPerElement()
    #Add up all the atoms  
    s = 0
    for operand in storageElementAtoms:
        s += operand
    sumAtoms = firstElementAtoms + s
    m = 0
    for smallWt in storageWtTotal:
        m += smallWt
    sumWt = massTotal + m
    newElementList = [firstElementType]
    for elementType in storageElementTypes:
        newElementList.append(elementType)
    newAtomNumberList = [str(firstElementAtoms)]
    for atomNum in storageElementAtoms:
        newAtomNumberList.append(str(atomNum))

    #make Lists into string for chm formula
    chmFormula = makeChmFormula(newElementList, newAtomNumberList)
    

    #Print sum of atoms and weight
    #print(f'The sum of all your atoms in your formula is: {sumAtoms}')
    print(f'Your chemical formula is the following:  {chmFormula}')
    print(f'The total atomic weight of your formula is: {sumWt}')
    return sumAtoms, sumWt

def makeChmFormula(list1, list2):
    newList = []
    if list1[1] == 0 and list2[1] == '0':
    
         list1 = list1[0] + list2[0]
         newList.append(list1)
         completeList = ''.join(newList)
         return completeList
    else:
      
        for i in range(len(list1)):
            
            list1[i] = str(list1[i]) + list2[i]
            newList.append(list1[i])
            completeList = ''.join(newList)
        return(completeList)


def printElementMenu():
    print(f'Please choose from the elements in the Menu. Please\n',
          f'choose up to six different elements for your formula')
    print(f' MENU\n', f'H Hydrogen\n', f'C Carbon\n',
          f'N Nitrogen\n', f'O Oxygen\n', f'F Fluorine\n', f'P Phosphate\n')
    
def askIfNext():
    askUserNext = input("Do you have another element (Y= Yes, N=  No)? ").upper()
    if askUserNext == 'Y':
        return True
    else:
        return False
    
def isInvalid(elementAlpha):
    #if element given is not in the approved list per the menu
    if elementAlpha != 'C' and elementAlpha != 'H' and elementAlpha != 'N' and elementAlpha != 'O'\
        and elementAlpha != 'P' and elementAlpha != 'F':
        status = True     
    else:
        status = False
    return status

def calculateMass(atom, num):
    if atom == 'C':
        mass = C * num
    elif atom == 'H':
        mass = H * num
    elif atom == 'P':
        mass = P * num
    elif atom == 'F':
        mass = F * num
    elif atom == 'O':
        mass = O * num
    elif atom == 'N':
        mass = N * num
    return mass

def getChmFormulaPerElement():
    #Ask for each element in the chemical formula
    element1 = input("What is the first element symbol? ").upper()
    #validation loop to check if input is of approved elements
    while isInvalid(element1):
        print(f'\nPlease input correct element symbol (see Menu)')
        element1 = input("What is the first element symbol? ").upper()   
    numberAtomsE1 = int(input("How many atoms for this element? "))
    #calculate mass
    mass = calculateMass(element1, numberAtomsE1)
    #Ask if another element
    askNextElement = askIfNext()
    #create storage to keep all the number of atoms per elements
    storage = []
    storageWt = []
    storageElements = []
    while askNextElement == True:
        elementIndex = input("What is the next element symbol? ").upper()
        #Validation loop to check if input is in approved menu
        #Check that input is not the same as first element
        while elementIndex == element1:
            print("Please pick a different element")
            elementIndex = input("What is the next element symbol? ").upper()
        while isInvalid(elementIndex):
            print(f'\nPlease input correct element symbol (see Menu)')
            elementIndex = input("What is the next element symbol? ").upper()
            
        numberAtomsEIndex = int(input("How many atoms for this element? "))
        avgWt = calculateMass(elementIndex, numberAtomsEIndex)   
        newNumber = numberAtomsEIndex
        newElement = elementIndex
        storage.append(newNumber)
        storageWt.append(avgWt)
        storageElements.append(newElement)
        #for while loop ask if another element
        askNextElementAgain = askIfNext()
        askNextElement = askNextElementAgain
        if askNextElement == False:
            print(storageElements)
            #pass the first number of atoms and array that stores the number of other atoms
            return numberAtomsE1, storage, mass, storageWt, element1, storageElements

    else:
        #if formula consists of only one element
        storage = [0]
        storageWt = [0]
        storageElements = [0]
        return numberAtomsE1, storage, mass, storageWt, element1, storageElements

main()