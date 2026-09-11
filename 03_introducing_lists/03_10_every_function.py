names = ['Freddy', 'Bonnie', 'Chica', 'Foxy', 'Golden Freddy']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

names = ['Freddy', 'Bonnie', 'Chica', 'Foxy', 'Golden Freddy']
print(names)
messages = [f"Hello {name}, I hope to see you again in the future!" for name in names]
print(messages[4])

pmsg = f"Freddy, I hope to see you again in the future."
print(pmsg)
pmsg = f"Bonnie, I hope to see you again in the future."
print(pmsg)
pmsg = f"Chica, I hope to see you again in the future."
print(pmsg)
pmsg = f"Foxy, I hope to see you again in the future."
print(pmsg)
pmsg = f"Golden Freddy, I hope to see you again in the future."
print(pmsg)

pizza_toppings = ['Pepperoni', 'Mushrooms', 'Onions', 'Bell Peppers', 'Olives']
print(pizza_toppings)

guest_list = ['Freddy','Bonnie','Chica','Foxy','Golden Freddy','Springtrap']

print(guest_list[0])
print(guest_list[1])
print(guest_list[2])
print(guest_list[3])
print(guest_list[4])
print(guest_list[5])


print("Here is the original list:")
guest_list = ['Freddy','Bonnie','Chica','Foxy','Golden Freddy','Springtrap']


print(guest_list[0])
print(guest_list[1])
print(guest_list[2])
print(guest_list[3])
print(guest_list[4])
print(guest_list[5])

print("Here is the new list:")
guest_list = ['Freddy','Bonnie','Chica','Foxy','Golden Freddy','Circus Baby']

print(guest_list[0])
print(guest_list[1])
print(guest_list[2])
print(guest_list[3])
print(guest_list[4])
print(guest_list[5])

pmsg = f"Hello {'Freddy'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Bonnie'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Chica'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Foxy'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Golden Freddy'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Circus Baby'}, I would like to invite you to my party."
print(pmsg)

print("Springtrap is not able to make it to the party. I will invite someone else instead.")



print("Here is the new list:") 
guest_list = ['Freddy','Bonnie','Chica','Foxy','Golden Freddy','Circus Baby']

guest_list=[0]
guest_list=[1]
guest_list=[2]
guest_list=[3]
guest_list=[4]
guest_list=[5]

print(guest_list.insert(0, 'Marionette'))

print(guest_list.insert(2, 'Ballora'))

print(guest_list.append('Lefty'))

print("Here is the new list:")
guest_list = ['Marionette','Freddy','Ballora',
              'Bonnie','Chica','Foxy',
              'Golden Freddy','Circus Baby','Lefty']



'''
guest_list=[0]
guest_list=[1]
guest_list=[2]
guest_list=[3]
guest_list=[4]
guest_list=[5]
guest_list=[6]
guest_list=[7]
guest_list=[8]
'''

pmsg = f"Hello {'Marionette'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Ballora'}, I would like to invite you to my party."
print(pmsg)
pmsg = f"Hello {'Lefty'}, I would like to invite you to my party."
print(pmsg)

print(guest_list)


print("Message: I can only invite two people to my party. I will have to remove some people from my guest list.")
print("Here is the new list:") 
guest_list = ['Marionette','Freddy','Ballora','Bonnie','Chica','Foxy','Golden Freddy','Circus Baby','Lefty']

popped_guest = guest_list.pop(guest_list.index('Circus Baby'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Lefty'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Ballora'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Golden Freddy'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Chica'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Bonnie'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")
popped_guest = guest_list.pop(guest_list.index('Marionette'))
print(f"Sorry {popped_guest}, but I can't invite you to my party.")

print("Here is the new list:") 
guest_list = ['Freddy','Foxy']

print(f"Hello {'Freddy'}, You are still invited to my party.")
print(f"Hello {'Foxy'}, You are still invited to my party.")

print("Hello neighbour house"), ("Joey Drew studios") , ("The upside down"), ("Baldis school house"), ("The Backrooms") 

print(sorted(['Baldis school house', 'Hello neighbour house', 'Joey Drew studios', 'The backrooms', 'The upside down']))
print(sorted(['The upside down', 'The backrooms', 'Joey Drew studios', 'Hello neighbour house', 'Baldis school house'], reverse=True))
print(list(reversed(['The upside down', 'The backrooms', 'Joey Drew studios', 'Hello neighbour house', 'Baldis school house'])))
print(list(reversed(['Baldis school house', 'Hello neighbour house', 'Joey Drew studios', 'The backrooms', 'The upside down'])))
print(sorted(['Baldis school house', 'Hello neighbour house', 'Joey Drew studios', 'The backrooms', 'The upside down']))
print(sorted(['The upside down', 'The backrooms', 'Joey Drew studios', 'Hello neighbour house', 'Baldis school house'], reverse=True))

guest_list = ['Freddy','Bonnie','Chica','Foxy','Golden Freddy','Circus Baby']

length = len(guest_list)
print(f"Number of guests invited to dinner: {length}")

print(guest_list[0])
print(guest_list[1])
print(guest_list[2])
print(guest_list[3])
print(guest_list[4])
print(guest_list[5])