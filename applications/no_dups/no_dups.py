def no_dups(s):
    # Implement me.
    words = s.split()
    word_dic = {}
    for word in words:
        word_dic[word] = 1
    
    string = ""

    for key in word_dic:
        string = string + " " + key
    
    return string.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))