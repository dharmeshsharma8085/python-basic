marks=[23,4,56,786,34,6,544]

def fail(score):
    return score<50

result=filter(fail,marks)

print("failling scores:", list(result)) 