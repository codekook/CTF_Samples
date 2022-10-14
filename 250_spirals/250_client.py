import sys, re
from ctf_client import CTFClient, CTFException

def main():

    #Initialize the connection
    try:
        client = CTFClient("localhost", 9000)
    except CTFException:
        sys.exit("Failed to connect -- is the server running?")

    while True:
        # Get fibonacci number from the server
        given = client.get_data()
        print(f"*** Received Below from Server ***\n\n{given}")

        # Check for a flag
        if "flag" in given:
            # Snag just the flag in the form "flag{...}"
            start = given.find("flag{")
            end = given.find("}", start)

            # We're done!
            print(f"---> Found the flag: {given[start:end + 1]}")
            sys.exit(0)
        #call fibonacci function to provide index position and return to server
        else:
            data = fib_func(number2(given))
            client.send_data(data)
            print(f"Data: {data}")

#returns the index position of the fibonacci number
def fib_func(number):
    #create a fibonacci sequence until matching the number provided by the server
    list = [0]
    fib_num = 1
    n = 0
    while n < number and fib_num < number:
        fib_num = fib_num + n
        list.append(fib_num)
        n = n + fib_num
        list.append(n)
        #print("n: ", n, "fib_num: ", fib_num)
    #print(list)
    final = len(list) - 1
    return str(final)

#returns the integer type number from the server
def number(given):
    tmp_list = given.split(" ")
    #print(tmp_list)
    save_list = []
    for i in tmp_list:
        if i.isnumeric():
            #append any numbers to the list
            save_list.append(i)
    #print(save_list)
    #covert the last number to an integer
    number = int(save_list[-1])
    return number

#returns the integer type number from the server using re 
def number2(given):
    number = re.search("\d+\d", given)
    return int(number.group())

if __name__ == "__main__":
    main()
