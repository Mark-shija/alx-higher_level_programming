#!/usr/bin/python3

def main():
    from add_0 import add
    """ main calls module func

    Args:
        no args

    Returns:
        The return add()
    """
    a = 1
    b = 2
    result = add(a,b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()
