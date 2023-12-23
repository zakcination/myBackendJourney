from collections import ChainMap

toys = {'Car': 30, 'Robot': 20}
laptops = {'Macbook': 1400, 'Chromebook': 800, 'Lenovo': 1200}
accessories = {'Case': 15, 'Screen Protector': 20}


inventory = ChainMap(toys, laptops, accessories)


# print the whole chainmap
print(inventory)


# print price of Robot from an inventory
print(inventory['Robot'])


# update any dictionary and see a reflection on inventory
print(inventory['Macbook'])
laptops['Macbook'] = 1600
print(inventory['Macbook'])


print(inventory.maps)
print(inventory.parents) # prints the same as inventory.maps[1:]


v = inventory.new_child() # create a new child
print(v.parents) # prints the same as inventory.maps[1:]


#get an non existing k-v pair from an inventory
print(inventory['Bike'])  # KeyError: 'Bike'


# Actually dictinaries could come from totally different modules or packages. 
# This is because ChainMap stores the underlying dictionaries by reference.


