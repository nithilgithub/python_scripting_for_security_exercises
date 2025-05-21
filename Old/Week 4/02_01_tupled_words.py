# create a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


def create_tuple_list(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Create a list of tuples for each word
    result_list = [tuple(word) for word in words]
    
    return result_list

# Example usage
input_string = "hello world"
result_list = create_tuple_list(input_string)
print(result_list)
