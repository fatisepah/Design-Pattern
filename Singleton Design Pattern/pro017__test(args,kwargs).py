def test_argument(first_arg, *args):
    print(" first_arg:", first_arg)
    for arg in args:
        print(" argument dar args:", arg)


test_argument('first', 'second', 'third')