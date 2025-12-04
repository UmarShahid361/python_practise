# File: utils.py

def get_favorite_color():
    return "Blue"


print("--- 'utils.py' is being read by Python ---")

if __name__ == "__main__":
    print(">> You are running utils.py DIRECTLY.")
    print(">> Testing the function:", get_favorite_color())
else:
    print(">> utils.py has been IMPORTED by another file.")
