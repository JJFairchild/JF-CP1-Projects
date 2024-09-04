#Jonas Fairchild Setting, Resetting, and Resetting

#Initial values
staff = 32
students = 100
guests = students*2

#Changes
students = 99
guests = students * 2 #This one is a duplicate to re-calculate guests
staff = 29
guests = guests-15
staff = 30

#Code
tables = (staff + students + guests)/12
print(f"We need {tables} tables.")