def mutate_string(string, position, character):
    string1 = string[:position] + character + string[position+1:]
    return string1
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
