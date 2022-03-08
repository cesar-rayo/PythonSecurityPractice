class User:
    def __init__(self, trusted=False):
        self.trusted = trusted

    def can_login(self):
        return self.trusted


def insecure_login(user):
    # It returns the function itself
    if user.can_login:
        print("Show all secrets.. 🔐")
    else:
        print("Unauthorized")


def secure_login(user):
    if user.can_login():
        print("Show all secrets.. 🔐")
    else:
        print("Unauthorized")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hacker = User(trusted=False)
    user = User(trusted=True)

    insecure_login(hacker)
    insecure_login(user)
    print("=================")
    secure_login(hacker)
    secure_login(user)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
