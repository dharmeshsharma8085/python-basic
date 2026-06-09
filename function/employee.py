work_hour=[('Abby',100),('Billy',400),('Cassie',800)]
def employee_check(work_hour):
    current_max=0
    employee_of_month=''
    
    for employee,hours in work_hour:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass
    
    return (employee_of_month,current_max)



print("Employee of months goes to ",employee_check(work_hour))
result=employee_check(work_hour)
name,hours=employee_check(work_hour)# tupple unpacking 
print("Employee of the months goes to",name)
            