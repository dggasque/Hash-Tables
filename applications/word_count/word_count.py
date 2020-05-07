import re
def word_count(s):
    # Implement me.
    s = s.lower()
    s = re.sub('[^a-z\ \']+', " ", s)
    words = s.split()
    word_count = {}
    word_set = set(words)
    for word in word_set:
        word_count[word] = words.count(word)
    return word_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))