
# Setup
actor = {"name": "John", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    try:
        last_name = actor["name"].split(" ")[1]
        return last_name
    except IndexError:
        return actor["name"]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())