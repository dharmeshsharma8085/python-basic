try:
    f=open("txt.file","w")
    f.write("Write a txt file")
except TypeError:
    print("THEre was an type error")
except OSError:
    print("There was an OS error")
finally:
    print("I always run")
    
# there is no error in above block of code let create error
# by switch "w" to "r"
try:
    f=open("txt.file","r")
    f.write("Write a txt file")
except TypeError:
    print("THEre was an type error")
except OSError:
    print("There was an OS error")
finally:
    print("I always run")