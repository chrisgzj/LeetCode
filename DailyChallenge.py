
# Daily challenge 4 sep 2020
def combinar(fragm1, fragm2):
    #print("Entran: " + str(fragm1) + " y " + str(fragm2))
    if fragm1[1] < fragm2[0] or fragm2[1] < fragm1[0]:
        return [fragm1, fragm2]
    final = [[min(fragm1[0], fragm2[0]), max(fragm1[1], fragm2[1])]]
    #print ("Salen: " + str(final))
    return final

cadena = "eaaaabaaec"
dicc = {}
for letra in range(len(cadena)):
    if cadena[letra] not in dicc:
        dicc[cadena[letra]] = []
        dicc[cadena[letra]].append(letra)
    if len(dicc[cadena[letra]]) > 1:
        dicc[cadena[letra]][1] = letra
    else:
        dicc[cadena[letra]].append(letra)
print(dicc)
fragmentos = list(dicc.values())

se_combino = True
while(se_combino):
    se_combino = False
    #print("Reinicia")
    for elem1 in range(len(fragmentos)):
        for elem2 in range(len(fragmentos)):
            if elem1 != elem2 and not se_combino:
                #print ("Revisando: " + str(elem1) + " y " + str(elem2))
                result = combinar(fragmentos[elem1], fragmentos[elem2])
                if len(result) == 1:
                    #print("Entra")
                    se_combino = True
                    fragmentos.pop(elem1)
                    if elem2 > elem1: elem2 -=1
                    fragmentos.pop(elem2)
                    fragmentos.append(result[0])

fragmentos.sort()
print(fragmentos)
result = [fr[1] - fr[0] + 1 for fr in fragmentos]
print(result)

# Top interviews num. 1
nums = [0,0,1,1,1,2,2,3,3,4]
hist = []
for num in reversed(range(len(nums))):
    print(num)
    print(hist)
    if nums[num] not in hist:
        hist.append(nums[num])
    else:
        print("Remove: " + str(num))
        nums.remove(nums[num])
print(nums)

# Top interviews num. 2. Best time to buy and sell stock II
prices = [7,6,4,3,1]
tengo = False
precio_actual = 0
profit = 0
for ind_precio in range(len(prices)-1):
    if not tengo:
        if prices[ind_precio + 1] > prices[ind_precio]:
            tengo = True
            precio_actual = prices[ind_precio]
    else:
        if prices[ind_precio + 1] < prices[ind_precio]:
            tengo = False
            profit = profit + prices[ind_precio] - precio_actual
            precio_actual = 0
if tengo:
    profit = profit + prices[len(prices) - 1] - precio_actual
print(profit)


# Daily challenge 7 sep 2020

pattern = "abba"
stri = "dog dog dog dog"
patron = list(pattern)
cadena = stri.split()
dicc1 = {}
iguales = True
if len(patron) != len(cadena):
    iguales = False
else:
    for ind_letra in range(len(patron)):
        if patron[ind_letra] in dicc1:
            if dicc1[patron[ind_letra]] != cadena[ind_letra]:
                iguales = False
        else:
            dicc1[patron[ind_letra]] = cadena[ind_letra]
    if iguales:
        dicc1 = {}
        for ind_letra in range(len(patron)):
            if cadena[ind_letra] in dicc1:
                if dicc1[cadena[ind_letra]] != patron[ind_letra]:
                    iguales = False
            else:
                dicc1[cadena[ind_letra]] = patron[ind_letra]

print (iguales)

nums = [1,2,3,4,5,6,7]
k = 3
nvo =  [nums[(n - k) % len(nums)] for n in range(len(nums))]
print (nvo)


