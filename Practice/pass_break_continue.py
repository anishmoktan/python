### PASS ###
#The pass keyword is mostly used as a placeholder in a loop. Nothing gets executed when pass is placed under a condition.



names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
   if 'j' in name.lower():
       pass
   else:
       print(name)


print("\n--------BREAK-------\n")
### BREAK ###

#The break keyword terminates a loop. break statements are typically found within conditional statements. If a certain condition is met, the loop stops iterating and breaks at that point.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'h' in name.lower():
      break
  else:
      print(name)


print("\n--------CONTINUE-------\n")
### CONTINUE ###

#The continue keyword skips over an iteration if the condition is met and goes onto the next iteration. The difference between the continue keyword and pass is that continue goes onto the next iteration while pass simply does not do anything.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'm' in name.lower():
      continue
  else:
      print(name)