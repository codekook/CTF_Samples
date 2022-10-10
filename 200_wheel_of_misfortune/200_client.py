import socket, sys, re
from ctf_client import CTFClient, CTFException

def main():
    # Initialize our connection
    try:
        client = CTFClient("localhost", 9000)
    except CTFException:
        sys.exit("Failed to connect -- is the server running?")

    while True:
        # Get some stuff from the server
        given = client.get_data()
        print(f"*** Received Below from Server ***\n\n{given}")

        # Does it have a flag?
        if "flag" in given:
            # Snag just the flag in the form "flag{...}"
            start = given.find("flag{")
            end = given.find("}", start)

            # We're done!
            print(f"---> Found the flag: {given[start:end + 1]}")
            sys.exit(0)
        else:
            #print(given)
            data = wheel(given)
            client.send_data(data)
            print(f"Data: {data}")

#takes the server output, splits on the arrow and then on the newline and calls vowels()
def wheel(words):
    word_list = words.split("->")
    #print("word_list: ", word_list)
    word = word_list[0]
    #print("word: ", word)
    word_list_2 = word.split("\n")
    #print("word_2: ", word_list_2)
    word_3 = word_list_2[-1]
    #print("word_3: ", word_3)
    word_3 = word_3.strip()
    v = vowels(word_3)
    return v

#return a string of vowels from the word
def vowels(word):
    lst = ["a", "e", "i", "o", "u"]
    vwls = []
    for letter in word:
        for vowel in lst:
            if letter == vowel:
                vwls.append(letter)
    final = ''.join(vwls)
    return final

if __name__ == "__main__":
    main()
