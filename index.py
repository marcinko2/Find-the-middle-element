def gimme(input_array):
    # Find the middle element by comparing each number with the other two
    if input_array[0] < input_array[1] < input_array[2] or input_array[2] < input_array[1] < input_array[0]:
        return 1
    elif input_array[1] < input_array[0] < input_array[2] or input_array[2] < input_array[0] < input_array[1]:
        return 0
    else:
        return 2
