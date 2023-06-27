def test(b):
    if b:
        print("t")
    if b:
        print("t")
    if not b:
        print("t")
    if b:
        print("t")


test(True)