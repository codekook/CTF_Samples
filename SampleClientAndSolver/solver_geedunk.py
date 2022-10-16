#!/usr/bin/env python3
"""Example solver for the 100 Geedunk puzzle"""
import sys

from ctf_client import CTFClient, CTFException

if __name__ == "__main__":

    # Initialize our connection
    try:
        client = CTFClient("localhost", 9000)
    except CTFException:
        sys.exit("Failed to connect -- is the server running?")

    # Run forever
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
