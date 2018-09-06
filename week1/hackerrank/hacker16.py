#find a string from hackerrank EASY

def count_substring(string, sub_string):
    count=0
    for n in range(0, len(string)-len(sub_string)+1):
        if string[n:n+len(sub_string)]==sub_string:
            count+=1
    return count