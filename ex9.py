# The variable varFirst store a string
varFirst = "This normal string"

# The variable varSecond store a string and next line characters (\n)
varSecond = "\nThis\nis\nPrint\nLines\n"

# The variable varThird store a string
varThird = "___________________________"

# Print the varFirst
print(varFirst)

# Print the varSecond
print(varSecond)

# Print the triple double-quotes (Long comment) and some format-string of the variable varThird 
print("""   
{}

Multiple line string
i can do more than 1 line
as we need  

{}    
""".format(varThird, varThird))
