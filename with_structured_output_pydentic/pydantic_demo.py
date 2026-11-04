from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# 1) Default value: we can also define the default values of each key

# 2) Optional value: We can give any key as optional in class that inherits BaseModal, but we have to provide default value,
#                so if that key is not define it will take that default value.

# 3) Built in validation: pydatic library also provides some built in validation, let say for email there is type EmailStr that 
#    will validate that given string follows email pattern

# 4) Coerce :  Pydantic will auto typecast the key value wherever it is possible, let say here we put age 45 but as string, so it converted to integer

# 5) Field Function: We can add default values, constraints, description, regex expression with help of this for any key value

# 6) The object created from Base Model class is pydentic object, but we can convert to type like python dictionary and JSON

class Student(BaseModel):
    name : str = "Abc"
    age : Optional[int] = None
    email: EmailStr
    gpa: float = Field(gt=0.0, lt=4.0, default=2.0, description="Digital value represnting the GPA of student")
    
# here the value of age will be None since we did not provide optional value
new_student1 = {"name" : "Priyank", "email":"priyank@gmail.com", "gpa":3.9}  
    # "email":"priyank@gmail" will give error since email does not follow pattern
    # "gpa": 5.8 will give error since it is greater than 4.0 
student1 = Student(**new_student1)
print("Student1",student1)
print("Student1 Name",student1.name)

# Here we can see the default value of name
new_student2 = {"age": 26, "email":"priyank@gmail.com"}
student2 = Student(**new_student2) 
print("Student2 Name",student2.name)
print("Student2",student2)

#  Pydantic will auto typecast the key value here, let say here we put age 45 but as string, so it converted to integer
new_student3 = {"name": "John", "age": "45",  "email":"priyank@gmail.com", "gpa":3.6}
student3 = Student(**new_student3)
print("Student3:",student3)
print("Student3 Type:",type(student3.age))

# convert pydentic to dict
student_3_dict = dict(student3)
# Now we can accessobject similar to as dictionary
print("Student3 name from dict:",student_3_dict['name'])

# convert to json
student_3_json = student3.model_dump_json()
