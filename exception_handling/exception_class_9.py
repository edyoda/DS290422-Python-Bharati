class InvalidAgeError(Exception):
    def __str__(self):
        return "The age you mentioned is invalid for voting!"

    # def __init__(self):
    #     print("The age you mentioned is invalid for voting!")