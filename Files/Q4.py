def check_line():
    word="programming"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
         while data:
          data=f.readline()
          if(word in data):
              print(line_no)
              return
         line_no+=1
         
    return -1
print(check_line())