import os

# Get the value of a specific environment variable
variable_name = "PATH"
value = os.getenv(variable_name)

if value is not None:
    print(f"The value of {variable_name} is: {value}")
else:
    print(f"The environment variable {variable_name} is not set.")