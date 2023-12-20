def hash_quadratic(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Uses quadratic probing (see question for details) to resolve 
    collisions.
    """

    h = HashTable(31)

    for key in d:
        hash_val = (2*key + 11) % 31
        i = 0
        while h.lookup(hash_val) != "-":
            i = i + 1
            hash_val = (2*key + 11 + i*i) % 31
        h.add(hash_val, key)

    return h

def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Uses secondary hashing (see question for details) to resolve
    collisions.
    """

    h = HashTable(31)

    for key in d:
        hash_val = (2*key + 11) % 31
        i = 0
        while h.lookup(hash_val) != "-":
            i = i + 1
            hash_val = 19 - (key % 19)
        h.add(hash_val, key)

    return h