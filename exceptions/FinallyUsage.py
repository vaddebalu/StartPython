def divide(a,b):
    result=0
    try:
        result=a/b
    except Exception as e:
        print(" Exception occured ")
        return result
    else:
        print("exception did not occur")
        return result
    finally:
        print("Runs even after return statement in function")

divide(10,1)