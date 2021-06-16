def prva(ime):
  return ("Pozdrav",{ime},"!")
print(prva("Boris"))

druga=lambda x: ("Dobrodosao" ,{x}, "!")
print(druga("Boris"))

def treca():
  return druga("Boris")
print(treca())

