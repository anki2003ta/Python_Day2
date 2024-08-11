# Take limitation of tuple from user
limit = int(input("Enter the number of elements in the tuple: "))

# Take input for tuple from user
tuple1 = []
for i in range(limit):
    elem = input(f"Enter element {i+1} (or 'stop' to finish): ")
    if elem.lower() == 'stop':
        break
    elif elem.isdigit():
        tuple1.append(int(elem))
    elif elem.replace('.', '', 1).isdigit():
        tuple1.append(float(elem))
    elif elem.lower() == 'true':
        tuple1.append(True)
    elif elem.lower() == 'false':
        tuple1.append(False)
    elif elem.startswith('[') and elem.endswith(']'):
        # Handle list input
        elem = elem[1:-1]
        list_elem = [x.strip() for x in elem.split(',')]
        # Convert string to int if possible
        list_elem = [int(x) if x.isdigit() else x for x in list_elem]
        tuple1.append(list_elem)
    else:
        tuple1.append(elem)
print("Original tuple:", tuple(tuple1))
# Remove 2nd element and last element from the tuple
if len(tuple1) > 2:
    tuple1 = tuple1[:1] + tuple1[2:-1]
else:
    tuple1 = ()
print("Resultant tuple:", tuple(tuple1))


