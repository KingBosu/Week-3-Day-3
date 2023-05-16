def linear_search(list_of_numbers,target):
    
    for index in range(len(list_of_numbers)):
        if list_of_numbers[index] == target:
            print(f'This is where your number is {index}')
            break
        
        print('Not found')
    index = 0
    while list_of_numbers[index]!= target:
        print('not found')
        index += 1
    print(f'This is where your number is {index}')
    
linear_search([1,32321,4242,30,4560,2013,100],30)


