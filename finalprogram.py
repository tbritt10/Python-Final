# Tanner Britt
# Final Exam Program
import random
def initial():
        numbers = []
        i = 0
        while i <= 499:
                temp = random.randint(1,999)
                numbers.append(temp)
                i += 1
        return numbers
        
def sort(numbers):
    if len(numbers)>1:
        mid = len(numbers)//2
        lefthalf = numbers[:mid]
        righthalf = numbers[mid:]

        sort(lefthalf)
        sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numbers[k]=lefthalf[i]
                i=i+1
            else:
                numbers[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numbers[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numbers[k]=righthalf[j]
            j=j+1
            k=k+1

def printlist(numbers):
        print(numbers)
        mainmenu(numbers)
        
def find_max(numbers):
        greatest = numbers[0]
        for x in numbers:
                if x > greatest:
                        greatest = x
        print("The greatest: "+str(greatest))
        mainmenu(numbers)

def find_min(numbers):
        least = numbers[0]
        for x in numbers:
                if x < least:
                        least = x
        print("The least: " +str(least))
        mainmenu(numbers)

def median(numbers):
        sort(numbers)
        if len(numbers)%2 == 0:
                tempmid = numbers[249] + numbers[250]
                median = tempmid/2
                print("Te median of the list is: "+str(median))
        mainmenu(numbers)

def mean(numbers):
        accumulator = 0
        for element in numbers:
                accumulator += element
        print(accumulator)
        mean = accumulator/len(numbers)
        print("The mean of the list is: "+str(mean))
        mainmenu(numbers)

def mainmenu(numbers):
        print("***********MENU************")
        print("Sort List: 'sort'")
        print("Max of List: 'max'")
        print("Min of List: 'min'")
        print("Median of List: 'median'")
        print("Mean of List: 'mean'")
        ch = input("Please enter your menu option: ")
        ch = ch.lower()
        if ch == 'min':
              find_min(numbers)
        elif ch == 'max':
              find_max(numbers)
        elif ch == 'mean':
              mean(numbers)
        elif ch == 'median':
              median(numbers)
        elif ch == 'sort':
                sort(numbers)
                printlist(numbers)
        elif ch != 'min' or 'max' or 'mean' or 'median' or 'sort':
                print("ERROR! I don't want no scrubs...")
                mainmenu(numbers)

def main():
        numbers = initial()
        mainmenu(numbers)
main()
