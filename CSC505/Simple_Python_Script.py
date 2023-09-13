# Super Simple Python Script
# CSC 505

# Tell the user the situation that we are looking for Morgan
print("\nHello weary traveller, I am looking for someone named Morgan\n")

# Ask them if they are Morgan
name = input("\nYou wouldn't happen to be Morgan would you? What's your name?\n")

# If they are , *Insert story about why we need you*, the story will likely be supplied by ChatGPT

if name.lower() == 'morgan':
    print("\nAh! Ahoy, Captain Morgan! It's been a long and treacherous journey,\n"
        "but at last, Ive tracked you down. Our crew has been eagerly\n"
        "awaiting your return, and the time has finally come to set our sights\n"
        "on the goblins bank and execute our daring plan! Let's go!\n")

else:
    print("\nAh well, let me know if you find them!\n")