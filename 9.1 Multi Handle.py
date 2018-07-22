try:
   variable = 10
   print(str(variable) + "hello")
   print(str(variable / 2))
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")