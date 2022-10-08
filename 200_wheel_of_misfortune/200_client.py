import socket, sys, re

def main():
    #create a connection to the server app
    tcp_socket = socket.create_connection(("localhost", 9000))
    print("tcp_socket: ", tcp_socket)

    while True:
        words = tcp_socket.recv(1024).decode()
        print("words: ", words)
        data = wheel(words).encode()
        tcp_socket.sendall(data)
        print(f"Data: {data}")

    print("Closing socket")
    tcp_socket.close()

#takes the server output, splits the list and uses the vowels()
def wheel(words):
    word_list = words.split(" ")
    print("word_list: ", word_list)
    print(len(word_list))
    if len(word_list) > 3:
        word = word_list[3].split("\n")
    else:
        word = word_list[0]
    print("word: ", word)
    v = vowels(word[1])
    return v

#return a string of vowels from the word
def vowels(word):
    lst = ["a", "e", "i", "o", "u"]
    vwls = []
    for letter in word:
        print(letter)
        for vowel in lst:
            print(vowel)
            if letter == vowel:
                vwls.append(letter)
    final = ''.join(vwls)
    return final


if __name__ == "__main__":
    main()
