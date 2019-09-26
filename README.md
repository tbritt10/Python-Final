# CS230 Final Exam Project

#### This project was the final assignment for my Introduction to Computer Programming course. 
##### Assignment instructions were to create a program to interact with a randomly generated list of numbers.

-----

## Functions

* `initial():`
### Declares a list `numbers = []` and fills it with 500 random integers generated using `random.randint()`. 
#### Return value list of intergers `numbers`.

* `sort(numbers):`
### Accepts a list of any size and sorts using the merge sort method.

* `find_max(numbers)`
### Accepts a list of any size and finds the greatest value.
#### This method declares the number in `numbers[0]` as the greatest and then iterates the entire list comparing each number. This is an inefficient method, but the assignment did not specify requirements to use more efficient methods.

* `find_min(numbers)`
### Accepts a list of any size and finds the lowest value.
#### This method declares the number in `numbers[0]` as the lowest and then iterates the entire list comparing each number. This is an inefficient method, but the assignment did not specify requirements to use more efficient methods.

* `median(numbers)`
### Accepts a list of 500 numbers and finds the median value.
#### This method checks to ensure the list is an even size, then adds the two middle numbers `numbers[249] + numbers[250]` to get the median value.

* `mean(numbers)
### Accepts a list of any size and finds the average of all the numbers in the list.
#### This method declares an accumulator and then iterates through each element in the list adding the value to the accumulator. After exiting the loop accumulator is divided by `len(numbers)` to get the average.

-----
