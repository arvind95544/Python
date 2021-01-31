def decorate(func1):
    def newdec():
        print("Bfore exicuting function ")
        func1()
        print("After exicuting function")
    return newdec()
@decorate
def forcheck():
    print("hello python is good")


# forcheck=decorate(forcheck)
forcheck()