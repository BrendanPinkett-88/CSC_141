print("Message: I can only invite two people to my party. I will have to remove some people from my guest list.")
print("Here is the new list:") 
guest_list = ['Chris Evans','Tom holland','Ryan Reynolds','Mark Ruffalo','Chris Pratt','Oscar Isaac','Chris Hemsworth','Robert Downey Jr','Pedro Pascal']

popped_guest = guest_list.pop(guest_list.index('Ryan Reynolds'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Pedro Pascal'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Chris Pratt'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Chris Evans'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Mark Ruffalo'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Tom holland'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Chris Hemsworth'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")

print("Here is the new list:") 
guest_list = ['Robert Downey Jr','Oscar Isaac']

print(f"Hello {'Robert Downey Jr.'}, You are still invited to my party.")
print(f"Hello {'Oscar Isaac'}, You are still invited to my party.")