import copy
import time 

time1 = time.time()

sBoxes = [ [ [],[],[],[] ] for i in range(8)]
sBoxes[0][0] = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
sBoxes[0][1] = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]
sBoxes[0][2] = [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0]
sBoxes[0][3] = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

sBoxes[1][0] = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10]
sBoxes[1][1] = [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5]
sBoxes[1][2] = [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15]
sBoxes[1][3] = [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

sBoxes[2][0] = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8]
sBoxes[2][1] = [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1]
sBoxes[2][2] = [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7]
sBoxes[2][3] = [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

sBoxes[3][0] = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15]
sBoxes[3][1] = [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9]
sBoxes[3][2] = [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4]
sBoxes[3][3] = [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

sBoxes[4][0] = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9]
sBoxes[4][1] = [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6]
sBoxes[4][2] = [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14]
sBoxes[4][3] = [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

sBoxes[5][0] = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11]
sBoxes[5][1] = [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8]
sBoxes[5][2] = [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6]
sBoxes[5][3] = [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

sBoxes[6][0] = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1]
sBoxes[6][1] = [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6]
sBoxes[6][2] = [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2]
sBoxes[6][3] = [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]

sBoxes[7][0] = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7]
sBoxes[7][1] = [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2]
sBoxes[7][2] = [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8]
sBoxes[7][3] = [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]




#16 elements, 48 bits long. 

#step 1 put first 16 in the end. Then, take firt 24, last 24. 
def GetKeys(bitString):
    keyArray = []

    newString = bitString[16:] + bitString[0:16] 
    
    for i in range(0, 16):
        key = newString[0:24] + newString[len(bitString)-24:]
        keyArray.append(key)
        newString = newString[16:] + newString[0:16]
    return(keyArray)

def ConvertToBinary(charstring):
    #print("INSIDE CONVERT TO BINARY FUNCTION")
    newString = ""
    for char in charstring:
        #print("char is", char)
        charNumber = ord(char)
        charBin = bin(charNumber)
        binString = str(charBin)
        binStringWithoutb = binString[(binString.index("b"))+1:]
        binStringPadded = (8-len(binStringWithoutb))*"0" + binStringWithoutb
        #if len(binStringPadded)!= 8:
            #print("HAVE A LOOK AT THIS!!!!!")
        newString = newString +  binStringPadded
    #print("UNPADDED LENGTH IS", len(newString))
    noOfPadString = 8-(int(((len(newString))%64)/8))
    #print("NO OF PAD STRING IS", noOfPadString)
    padString = bin(noOfPadString)[2:]
    #print("AND HENCE PAD STRING IS: ", padString)
    nBinPadded = "0"*(8- len(padString)) + padString
    
    newString += nBinPadded*noOfPadString
    return (newString)

def ConvertToBinaryNoPadding(charstring):
    newString = ""
    for char in charstring:
        #print("char is", char)
        charNumber = ord(char)
        charBin = bin(charNumber)
        binString = str(charBin)
        binStringWithoutb = binString[2:]
        binStringPadded = (8-len(binStringWithoutb))*"0" + binStringWithoutb
        if len(binStringPadded)!= 8:
            print("HAVE A LOOK AT THIS!!!!!")
        newString = newString +  binStringPadded
    return (newString)
    

def Expand(string):
    outputString = string[31] + string[0:5] + string[3:9] + string[7:13] + string[11:17] + string[15:21] + string[19:25] \
        + string[23:29]  + string[27:] + string[0]
    #print("expand output", outputString)
    return(outputString)

def Xor(a, b):
    #print("INSIDE XOR FUNCTION")
    #print("a is", a)
    #print("b is", b)
    outputString = ""
    length = len(a)
    for i in range(0, length):
        outputString += str(int(a[i]) ^ int(b[i]))   #^ xors the two operands. 
    #print("XOR FUNCTION RETURNS", outputString)
    return (outputString)

#Feistal Network:

def sBox(string_48, sBoxes = sBoxes):
    #print("INSIDE SBOX", string_48)
    chunks, chunk_size = len(string_48), 6
    string_6 = [ string_48[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    #print(string_48)
    #print(string_6)
    output = ""
    for i in range(0, len(string_6)):
        element = string_6[i]
        af = element[0]+element[-1]
        bcde = element[1:5]
        afDecimal = int(af, 2)
        bcdeDecimal = int(bcde, 2)
        n = sBoxes[i][afDecimal][bcdeDecimal]
        nBin = bin(n)[2:]
        nBinPadded = "0"*(4- len(nBin)) + nBin
        output += nBinPadded
    #print("SBOX RETURNS", output)
    return output


def pBox(b):
    #print("INSIDE PBOX", b )
    pBoxList =  [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]
    outputList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0, len(b)):
        outputList[i] = b[pBoxList[i]]
    #print(outputList)
    output = "".join(outputList)
    #print("PBOX RETURNS", output)
    return output

#this function xors the vector and the block.
def FeistalFunction(plainTextBinary, vectorBinary, key, flag = False):
    #print("INSIDE FEISTAL FUNCTION")
    keys_16 = GetKeys(key)
    #print("KEYS ARE", keys_16)
    chunks, chunk_size = len(plainTextBinary), 64
    plainTextBinary64 = [ plainTextBinary[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    #print("PLAIN TEXT IN 64 BIT CHUNKS ARE",plainTextBinary64 )
    crypticText = []

    if flag == True:
        keys_16= copy.deepcopy(keys_16[::-1])        

    
    for text in plainTextBinary64:
        #print("INSIDE FOR TEXT LOOP", count, "th time")
        #print("YO TEXT IS", text)
        #print("text is", text)
        #print("binary of vector is :", vectorBinary)
        
        if flag == False:
            xorText = Xor(text, vectorBinary)
        else:
            xorText = text
        #print("xor text is:", xorText)
        zLeft = xorText[:32]
        zRight = xorText[32:]
        
        for i in range(0, 16):
            #print("RIGHT IS", zRight, ",", len(zRight))
            zRightDash = Expand(zRight)
            #print("EXPANDED RIGHT IS:", zRightDash, ",", len(zRightDash))
            a = Xor(keys_16[i], zRightDash)
            #print("AFTER XOR OF ROUND KEY AND EXPANDED RIGHT", a, ",", len(a))
            b = sBox(a)
            #print("after s box", b, ",", len(b))
            c = pBox(b)
            #print("after p box",c, ",", len(c))
            #print("AFTER XOR, SBOX AND PBOX, a,b,c:", a,b,c)

            temp = copy.deepcopy(zRight)
            zRight = copy.deepcopy(Xor(zLeft, c))
            zLeft = copy.deepcopy(temp)
            #print("AT THE END OF THE FOR ITERATION, ZRIGHT AND Z LEFT:", zRight, zLeft)
        #print("EXIT FOR LOOP IN FEISTAL")
        
        rightPlusLeft = zRight+ zLeft
        #if flag == True:
            #print("Right plus left for decryption is", rightPlusLeft)
            #inpt = input("waiting for input")
        #originalRightPlusLeft = copy.deepcopy(rightPlusLeft)
        
        #print("originalRightPlusLeft is :", originalRightPlusLeft)
        

        if flag == True:
            rightPlusLeft = Xor(rightPlusLeft, vectorBinary)
            vectorBinary = copy.deepcopy(text)
        else:
            vectorBinary = rightPlusLeft

        crypticText += [rightPlusLeft]
        
        #print("new vector is", vectorBinary)

        #print("UPDATED CRYPTIC TEXT AND IT IS NOW:", crypticText )
        #l = input("pausing for input")
    #print(crypticText)
    return crypticText


plainText = "romeoandjulietweregreatlovers"
plainTextBinary = ConvertToBinary(plainText)
#print("PLAIN TEXT BINARY IS", plainTextBinary)
#print("AND LENGTH OF IT IS", len(plainTextBinary))
vector = "abcdefgh"
vectorBinary = ConvertToBinaryNoPadding(vector)
key = "Z8tb;a="
#key = "01010001100101011100011001100111110101011100001011100011"
keyBinary = ConvertToBinaryNoPadding(key)
#print("BINARY OF KEY", keyBinary)
#print()

#print(vectorBinary)
encrypted = FeistalFunction(plainTextBinary, vectorBinary, keyBinary)
print(encrypted)

allEncrypted = ""
for i in encrypted:
    allEncrypted += i
#print(allEncrypted)
vector = "abcdefgh"
vectorBinary = ConvertToBinaryNoPadding(vector)
key = "Z8tb;a="
keyBinary = ConvertToBinaryNoPadding(key)


decrypted = FeistalFunction(allEncrypted, vectorBinary, keyBinary, flag = True)
print("DECRYPTED TEXT IS", decrypted)

allDecrypted = ""
for i in decrypted:
    allDecrypted += i

print(allDecrypted)


chunks, chunk_size = len(allDecrypted), 8
decryptedBinaryString = [allDecrypted[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

outputString = ""

for element in decryptedBinaryString:
    asciiNumber = int(element, 2)
    if asciiNumber >= 9:
        newChar = chr(asciiNumber)
        outputString += newChar
    else:
        pass
print(decryptedBinaryString, len(decryptedBinaryString))
print(outputString)

time2 = time.time()

print("TOTAL TIME TAKEN WAS", (time2- time1))