# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 7/8


def main():
    # intro message
    print("This program creates a Caesar cipher.")
    print("For a message entered it will shift the characters by a specified")
    print("number. A shift of [1] changes A->B B->C, [25] A->Z, B->A.")
    # enter word to encode
    message = str(input("Enter a message to encode: "))
    message = message.lower()
    # enter key
    key = int(input("Enter the number of characters to shift by [0 - 25]: "))
    # for loop creating encoded word
    encodedMessage = []
    lookup = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for word in message.split():
        encodedWord = ""
        for ch in word:
            encodedCh = ""
            encodedCh += lookup[lookup.find(ch) + key]
            encodedWord += encodedCh
        encodedMessage.append(encodedWord)

    # print result
    print(" ".join(encodedMessage))


main()
