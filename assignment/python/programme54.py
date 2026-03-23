"""54)Write a Python program to check multiple keys exists in a dictionary."""

d = {"Mon":3, "Tue":11,"Wed":6,"Thu":9}
check_keys={"Tue","Thu"}

# Use comaprision
if(check_keys.issubset(d.keys())):
   print("All keys are present")
else:
   print("All keys are not present")