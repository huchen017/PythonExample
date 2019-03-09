def add_method(x,y):
    try:
        return x+y
    except Exception as e:
        print(e)
        return None

# print(add_method(2,3))