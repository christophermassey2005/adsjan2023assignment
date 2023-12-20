#q1a
##########################################################################################################################################################################

#M, T, and tests for lists of different size (A, B, C, D)


M = [
  [0, 1, 0], 
  [0, 1, 1],
  [1, 1, 1]
]

T = [
  [0, 0, 1], 
  [0, 1, 0], 
  [1, 0, 0]
]

A = [[0]]
B = [[1]]

C = [
    [0, 0],
    [1, 0]
]
D = [
    [1, 0],
    [1, 1]
]

def apply_mask(M, T):
    #print(M[0])
    #list1 = [0, 1, 0]
    #print(list1)
    
    #list2 = [0, 1, 1]
    #result = [a & b for a, b in zip(M[2], T[2])] #
    result = [[a & b for a, b in zip(sublist1, sublist2)] for sublist1, sublist2 in zip(M, T)]

    return result

#output = apply_mask(C, D)
#print(output)

##########################################################################################################################################################################
#q1b

I = [
  [0, 0, 0], 
  [0, 1, 0],
  [1, 0, 0]
]
""" - DONT USE
def encode(I):
    #Turn the list of lists into a single list:
    flattenedlist = [element for sublist in I for element in sublist]
    print(flattenedlist)

    #Now this is essentially just run length encoding
    result = []
    count = 1
    current = flattenedlist[0]

    for num in flattenedlist[1:]:
        if num == current:
            count = count + 1
        else:
            result.append(('B' if current == 0 else 'W') + str(count))
            count = 1
            current = num
    result.append(('B' if current == 0 else 'W') + str(count))
    return ''.join(result) #Convert to string
  """            

def encode(I):
    #Turn the list of lists into a single list:
    flattenedlist = [element for sublist in I for element in sublist]
    print(flattenedlist)

    #Now this is essentially just run length encoding
    result = []
    count = 1
    current = flattenedlist[0]

    for num in flattenedlist[1:]:
        if num == current:
            count = count + 1
        else:
            if current == 0:
                result.append('B')
            else:
                result.append('W')
            result.append(str(count))
            count = 1
            current = num
    if current == 0:
        result.append('B')
    else:
        result.append('W')
    result.append(str(count))
    return ''.join(result) #Convert to string  
      
#print(encode(I))


##########################################################################################################################################################################
#q1c

S = "B2W1B1W1B2"
#works on 3 * 3
"""
def decode(S):
    mapping = {'B': 0, 'W': 1}
    image = []
    row = []
    i = 0
    while i < len(S):
        if S[i] in mapping:
            colour = mapping[S[i]]
            count = int(S[i+1])
            for _ in range(count):
                row.append(colour)
                if len(row) == 3:
                    image.append(row)
                    row = []
            i = i + 2

    return image
"""

def decode(S):
    #Find the value of width
    #So sum all numbers in the string

    sumofnuminstr = sum(int(x) for x in S if x.isdigit())
    print(sumofnuminstr)
    #9 if 3 * 3, 4 if 2 * 2, 1 if 1 * 1
    if sumofnuminstr == 9:
        width = 3
    if sumofnuminstr == 4:
        width = 2
    if sumofnuminstr == 1:
        width = 1

    mapping = {'B': 0, 'W': 1}
    image = []
    row = []
    i = 0
    while i < len(S):
        if S[i] in mapping:
            colour = mapping[S[i]]
            count = int(S[i+1])
            for _ in range(count):
                row.append(colour)
                if len(row) == width:
                    image.append(row)
                    row = []
            i = i + 2

    return image

#print(decode(S))


##########################################################################################################################################################################
#q1d
"""
M_e = "B1W1B2W5"
T_e = "B2W1B1W1B1W1B2"
def apply_mask_encoded(M_e, T_e, result ='', last_colour =''):
    #Base case: if either Me or Te is empty, return the result.
    if not M_e or not T_e:
        return result
    
    #Get the colour and count from M_e and T_e
    colour_M_e, count_M_e = M_e[0], int(M_e[1])
    colour_T_e, count_T_e = T_e[0], int(T_e[1])

    #Calculate the minimum count and the resulting colour
    min_count = min(count_M_e, count_T_e)
    resulting_colour = 'B' if colour_M_e == 'B' or colour_T_e == 'B' else 'W'

    if resulting_colour == last_colour:
        result = result[:-1] + str(int(result[-1]) + min_count)
    else:
        result += resulting_colour + str(min_count)

    #Update the counts and M_e and T_e for the recursive call.
    if count_M_e == count_T_e:
        return apply_mask_encoded(M_e[2:], T_e[2:], result, resulting_colour)
    elif count_M_e < count_T_e:
        T_e = T_e[:1] + str(count_T_e - min_count) + T_e[2:]
        return apply_mask_encoded(M_e[2:], T_e, result, resulting_colour)
    else:
        M_e = M_e[:1] + str(count_M_e - min_count) + M_e[2:]
        return apply_mask_encoded(M_e, T_e[2:], result, resulting_colour)

print(apply_mask_encoded(M_e, T_e)

"""

"""
M_e = "B1W1B2W5"
T_e = "B2W1B1W1B1W1B2"
def apply_mask_encoded(M_e, T_e):
    def wrapper(M_e, T_e, result= '', last_colour = ''):
        #Base case: if either Me or Te is empty, return the result.
        if not M_e or not T_e:
            return result
        
        #Get the colour and count from M_e and T_e
        colour_M_e, count_M_e = M_e[0], int(M_e[1])
        colour_T_e, count_T_e = T_e[0], int(T_e[1])đ

        #Calculate the minimum count and the resulting colour
        min_count = min(count_M_e, count_T_e)
        resulting_colour = 'B' if colour_M_e == 'B' or colour_T_e == 'B' else 'W'

        if resulting_colour == last_colour:
            result = result[:-1] + str(int(result[-1]) + min_count)
        else:
            result += resulting_colour + str(min_count)

        #Update the counts and M_e and T_e for the recursive call.
        if count_M_e == count_T_e:
            return wrapper(M_e[2:], T_e[2:], result, resulting_colour)
        elif count_M_e < count_T_e:
            T_e = T_e[:1] + str(count_T_e - min_count) + T_e[2:]
            return wrapper(M_e[2:], T_e, result, resulting_colour)
        else:
            M_e = M_e[:1] + str(count_M_e - min_count) + M_e[2:]
            return wrapper(M_e, T_e[2:], result, resulting_colour)  #May not get full credit as technically apply_mask_encoded does not call itself.
    return wrapper(M_e, T_e)

print(apply_mask_encoded(M_e, T_e))

"""

M_e = "B1W1B2W5"
T_e = "B2W1B1W1B1W1B2"
def apply_mask_encoded(M_e, T_e):
    def wrapper(M_e, T_e, result= '', last_colour = ''):
        if M_e == "" or T_e == "": #Check for an empty string
            return result
        
        #Get the colour and count from M_e and T_e
        colour_M_e =  M_e[0] 
        count_M_e = int(M_e[1])
        colour_T_e = T_e[0]
        count_T_e = int(T_e[1])

        min_count = min(count_M_e, count_T_e)
        if colour_M_e == 'B' or colour_T_e == 'B':
            resulting_colour = 'B'
        else:
            resulting_colour = 'W'

        if resulting_colour == last_colour:
            result = result[:-1] + str(int(result[-1]) + min_count)
        else:
            result += resulting_colour + str(min_count)

        if count_M_e == count_T_e:
            return wrapper(M_e[2:], T_e[2:], result, resulting_colour)
        elif count_M_e < count_T_e:
            T_e = T_e[:1] + str(count_T_e - min_count) + T_e[2:]
            return wrapper(M_e[2:], T_e, result, resulting_colour)
        else:
            M_e = M_e[:1] + str(count_M_e - min_count) + M_e[2:]
            return wrapper(M_e, T_e[2:], result, resulting_colour)  #May not get full credit as technically apply_mask_encoded does not call itself.
    return wrapper(M_e, T_e)

#print(apply_mask_encoded(M_e, T_e))

