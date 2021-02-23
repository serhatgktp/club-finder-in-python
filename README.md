# club-finder-in-python

A simple python application that gives suggestions about which clubs a person should attend based on their friends.

You may import a network of people and clubs by having a profiles.txt file in the same folder in the following format:
        
        LNAME, FNAME
        FRIEND_NAME (Same format - LNAME,FNAME)
        FRIEND_NAME
        CLUB_NAME
        CLUB_NAME
        FRIEND_NAME
        ...
        
The order of friends and clubs do not matter. It is important that club names do not have any commas (",") inside of them.

To use the program simply run club_finder.py, and instructions will be inside the shell.

There are also several internal functions like sorting etc. that are not accessible through the shell. These functions were written to be tested.

NOTE: There are a couple bugs that I will get around to fixing.

![Alt Text](https://github.com/serhatgktp/club-finder-in-python/blob/main/Example.jpg)
