#mutations from hackerrank EASY

def mutate_string(string, position, character):
    return string[:int(position)] + character + string[int(position) + 1:]
