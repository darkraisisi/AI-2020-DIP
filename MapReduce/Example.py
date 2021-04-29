# Voorbeeld-code om te demonstreren hoe in Python gebruik gemaakt kan worden van
# Map/Filter/Reduce-functionaliteit.
# 
# Dezelfde functionaliteit wordt steeds gedemonstreerd dmv. een for-loop,
# een Map/Reduce/Filter-implementatie met een gedefinieeerde functie, en
# een Map/Reduce/Filter-implementatie die gebruik maakt van lambda's. 

from functools import reduce

LIST_OF_NUMBERS = [0, 1, 2, 3]

# Mapper: neemt een lijst met X elementen, en geeft een lijst met X elementen.
def multiply_with_for_loop(input_numbers):
    output_numbers = []
    for i in input_numbers:
        output_numbers.append(input_numbers[i] * 10)
    return output_numbers

def mymultiplier(x):
    return x * 10

def multiply_with_map(input_numbers):
    mapped = map(mymultiplier, input_numbers)
    return mapped

def multiply_with_map_lambda(input_numbers):
    mapped = map(lambda x: x * 10, input_numbers)
    return mapped

result = multiply_with_for_loop(LIST_OF_NUMBERS)
print("Resultaten van for/mapper:")
print("For-loop:        ", end='')
print(list(result))

result = multiply_with_map(LIST_OF_NUMBERS)
print("Mapper:          ", end='')
print(list(result))

result = multiply_with_map_lambda(LIST_OF_NUMBERS)
print("Mapper (lambda): ", end='')
print(list(result),'\n')


# Voorbeeld-code voor een FILTER-functie.
# Filter: neemt een lijst met X elementen, en geeft een lijst met 0..X elementen. 

def odd_with_for_loop(input_numbers):
    output_numbers = []
    for i in input_numbers:
        if i % 2 != 0:
            output_numbers.append(input_numbers[i])
    return output_numbers

def myfilter(x):
    return x % 2 != 0

def odd_with_filter(input_numbers):
    filtered = filter(myfilter, input_numbers)
    return filtered

def odd_with_filter_lambda(input_numbers):
    filtered = filter(lambda x: x % 2 != 0, input_numbers)
    return filtered

result = odd_with_for_loop(LIST_OF_NUMBERS)
print("Resultaten van for/filter:")
print("For-loop:        ", end='')
print(list(result))

result = odd_with_filter(LIST_OF_NUMBERS)
print("Filter:          ", end='')
print(list(result))

result = odd_with_filter_lambda(LIST_OF_NUMBERS)
print("Filter (lambda): ", end='')
print(list(result),'\n')

# Voorbeeld-code voor een REDUCER-functie.
# Reduce: neemt een lijst met X elementen, en geeft een enkele waarde terug 

def sum_with_for_loop(input_numbers):
    output_number = 0
    for i in input_numbers:
        output_number = output_number + input_numbers[i];
    return output_number

def mysum(x, y):
    return x + y

def sum_with_reduce(input_numbers):
    summed = reduce(mysum, input_numbers, 0)
    return summed

def sum_with_reduce_lambda(input_numbers):
    summed = reduce(lambda x, y: x + y, input_numbers, 0)
    return summed

result = sum_with_for_loop(LIST_OF_NUMBERS)
print("Resultaten van for/reduce:")
print("For-loop:        ", end='')
print(result)

result = sum_with_reduce(LIST_OF_NUMBERS)
print("Filter:          ", end='')
print(result)

result = sum_with_reduce_lambda(LIST_OF_NUMBERS)
print("Filter (lambda): ", end='')
print(result)

print("Eerst een mapper, dan een filter, dan een reducer:")
print(
    reduce(lambda x, y: x * y,
           filter(lambda x: x % 2 != 0, 
                  map(lambda x: x * 5, LIST_OF_NUMBERS)
           )
    )
)