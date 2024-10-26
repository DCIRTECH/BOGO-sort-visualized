import random
numbers_to_be_sorter = []
solved = False
highest_consecutive_correct = 0
consecutive_correct = 0
length_of_list = 8

for i in range(length_of_list):
    numbers_to_be_sorter.append(i)

def randomized_sorter():
    for a in range(len(numbers_to_be_sorter)):
        b = random.randrange(length_of_list)
        numbers_to_be_sorter[a], numbers_to_be_sorter[b] = numbers_to_be_sorter[b], numbers_to_be_sorter[a]

def consecutive_correct_high_score(current_consecutive_correct, cchighest_consecutive_correct):
    if current_consecutive_correct > cchighest_consecutive_correct:
        cchighest_consecutive_correct = current_consecutive_correct
    return cchighest_consecutive_correct

randomized_sorter()

while solved == False:   
    randomized_sorter()
    
    for iterative in range(len(numbers_to_be_sorter) - 1):
        if consecutive_correct == length_of_list - 1:
            print(length_of_list)
            print(f"current consecutive correct {length_of_list}")
            highest_consecutive_correct = consecutive_correct_high_score(consecutive_correct, highest_consecutive_correct)
            print(f"The most consecutive correct {highest_consecutive_correct + 1}")
            solved = True
            break
        elif numbers_to_be_sorter[iterative] == consecutive_correct + 1:
            print(f"{numbers_to_be_sorter[iterative]}")
            consecutive_correct += 1
            print(f"current consecutive correct {consecutive_correct}.")
        else:
            for x in range(len(numbers_to_be_sorter)):
                print(f"{numbers_to_be_sorter[x]}")
                highest_consecutive_correct = consecutive_correct_high_score(consecutive_correct, highest_consecutive_correct)
                print(f"The most consecutive correct is {highest_consecutive_correct}")
                consecutive_correct = 0


