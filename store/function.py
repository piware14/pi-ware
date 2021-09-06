
#Functions
def istherefile(file): # This Function check whether a file existes
    try:
        file_tst = open(file)
        file_tst.close()
    except FileNotFoundError:
        return False
    else:
        return True