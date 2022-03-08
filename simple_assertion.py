def get_access_1(can_access):
    try:
        assert can_access
    except AssertionError:
        print("get_access_1 => No Access! 🔐")


def get_access_2(can_access):
    if not can_access:
        print("get_access_2 => No Access! 🔐")


def get_access_3(can_access):
    if can_access is False:
        print("get_access_3 => No Access! 🔐")


# if it's ran in optimized mode like 'python -O simple_assertion.py' the assertion is ignored
if __name__ == "__main__":
    can_access = False
    get_access_1(can_access)
    get_access_2(can_access)
    get_access_3(can_access)

    print("========")

    can_access = "false"
    get_access_1(can_access)
    get_access_2(can_access)
    get_access_3(can_access)



