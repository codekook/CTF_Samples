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
            num = number(given)
            fib = fib_func()
            count = 0
            while True:
                i = next(fib)
                #print(i)
                if num == i:
                    data = count + 1
                    break
                else:
                    count += 1
                    if count > 300:
                        break
                #print("count: ", count)

            client.send_data(str(data))
            print(f"Data: {data}")

#generator function to build a fibonacci sequence
def fib_func():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

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
    my_number = int(save_list[-1])
    #print("num: ", my_number)
    return my_number

if __name__ == "__main__":
    main()
