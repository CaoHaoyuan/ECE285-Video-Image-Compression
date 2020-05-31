#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Helper functions
def decimalToBinary(n):  
    if(n==0):
        return [0]
    res = []
    while(n>0):
        res.append(n%2)
        n = n//2
    return res[::-1]
def binaryToDecimal(n):
    res = 0
    mul = 1
    for element in n[::-1]:
        res += element*mul
        mul *= 2
    return res


# ## Unary encoder and decoder

# In[2]:


def unary_encode(Input):
    res = []
    for element in Input:
        for i in range(element):
            res.append(1)
        res.append(0)
    return res

def unary_decode(Input):
    res = []
    counter = 0
    for element in Input:
        if(element == 1):
            counter += 1
        else:
            res.append(counter)
            counter = 0
    return res


# ## Arithmetic encoder and decoder

# In[8]:


p0,p1 = 3/16,13/16
print("Digit 0 probability is ",p0,". Digit 1 probability is ",p1)


# In[9]:


class binaryAriCoder:
    def __init__(self,bitsConstraint,p0,p1):
        self.L = 0
        self.Whole = 2**bitsConstraint
        self.Half = int(2**bitsConstraint/2)
        self.Quater = int(self.Half/2)
        self.bitsConstraint = bitsConstraint
        
        self.p0 = p0
        self.p1 = p1
    
    # Encoder
    def ari_encode(self,Input):
        res = []
        L,R = 0,self.Whole
        s = 0
        for digit in Input:
            # update the lower bound and range
            if(digit==0):
                L = L
                R = round(R*self.p0)
            else:
                L = L+round(R*self.p0)
                R = round(R*p1)
                
            # renormalization
            while(L+R<self.Half or L>self.Half):
                if(L+R<self.Half):
                    res.extend([0])
                    res.extend([1]*s)
                    s = 0
                    L = 2*L
                    R = 2*R
                else:
                    res.extend([1])
                    res.extend([0]*s)
                    s = 0
                    L = 2*(L-self.Half)
                    R = 2*R
            while(L>self.Quater and L+R<3*self.Quater):
                s += 1
                L = 2*(L-self.Quater)
                R = 2*R
        s += 1
        
        # last step before getting res
        if(L==0):
            res.append(0)
        elif(L+R==self.Whole):
            res.append(1)
        elif(L<=self.Quater):
            res.extend([0])
            res.extend([1]*s)
        else:  
            res.extend([1])
            res.extend([0]*s)
        return res
     
                    

    # Decoder
    def ari_decode(self,Input,originalBitsLength):
        res = []
        L,R = 0,16
        z,i = 0,0
        while(i<self.bitsConstraint and i<len(Input)):
            if(Input[i]==1):
                z = z+2**(self.bitsConstraint-1-i)
            i += 1
        while(1):
            if(len(res)==originalBitsLength): return res
            if(z>=L+round(R*self.p0)):
                res.append(1)
                L = L+round(R*self.p0)
                R = round(R*p1)
            else:
                res.append(0)
                L = L
                R = round(R*p0)
                
            # handle the rescaling part. Rescaling happens at exact time and condition as in encoder
            while(L>self.Half or L+R<self.Half):
                if(L+R<self.Half):
                    L = 2*L
                    R = 2*R
                    z = 2*z
                else:
                    L = 2*(L-self.Half)
                    R = 2*R
                    z = 2*(z-self.Half)
                if(i<len(Input) and Input[i]==1):
                    z += 1
                i += 1
            while(L>self.Quater and L+R<3*self.Quater):
                L = 2*(L-self.Quater)
                R = 2*R
                z = 2*(z-self.Quater)
                if(i<len(Input)and Input[i]==1):
                    z += 1
                i += 1


# In[10]:


# create a binary arithmetic encoder with bits constraint 4
myBAC = binaryAriCoder(4,p0,p1)


# In[11]:


# Test
Raw = [2,2,2,5,7,7,7,7,2,2,2,2,2,7]
Input = unary_encode(Raw)
print("Original message is \n",Raw)
print("Unary encoded sequence is \n",Input)
Coded = myBAC.ari_encode(Input)
print("Arithmeic encoded is \n",Coded)
Recovered = myBAC.ari_decode(Coded,len(Input))
print("Recovered unary encoded sequence is \n ",Recovered)
FinalRes = unary_decode(Recovered)
print("Reconstructed Raw message is \n",FinalRes)

if(FinalRes == Raw):
    print("\n\n **************** We got it! Recovered message is lossless! ************\n")
else:
    print("\n\n **************** So sad. Something is wrong.... ************\n")


# In[ ]:




