#!/usr/bin/env python
# coding: utf-8

# In[5]:


from math import sqrt
print ("Giải phương trình bậc 1: ax+b=0")

a= float(input ("Nhập a="))
b= float(input ("Nhập b="))
if a>0 or a<0:
    x=-b/a
    print("Phương trình có nghiệm là: ",x)
else:
    if b==0: print("Phương trình có vô số nghiệm")
    else :print ("Phương trình vô nghiệm")


# In[7]:


from math import sqrt
print("Tính tổng s= 0+1+2+...+n")

n= int(input("Nhập số nguyên n="))
i=0
s=0
while i<=n:
    s=s+i
    i=i+1
print ("Tổng là:",s)
    


# In[46]:


from math import sqrt
print ("Tính tiền điện:")
n= int(input("Nhập số kWh:"))
tongtien=0
if n <=100: 
    tongtien=n*2000
else :
    tongtien=tongtien+n*2000
    for a in range(n-100+1):
        tongtien=tongtien+a*100
    
    
print("Tổng tiền điện là:",tongtien)
    


# In[5]:


def isPrime(n):
    if(n<0):
        return False
    elif (n==0):
        return False
    elif (n==1):
        return False
    elif (n==2):
        return True
    else:
        for i in range (2,n):
            if(n%i==0):
                return False
            return True
    


# In[40]:


'''Hãy nhập từ bàn phím số tự nhiên n và xuất ra màn hình:
1. Các số nguyên tố nhỏ hơn n
2. Xuất ra tổng các số nguyên tố nhỏ hơn n'''
print("Kiểm tra số nguyên tố:")
isPrime(n)
n=int(input("Nhập số tự nhiên:"))
if(isPrime(n)== True):
    print("n là số nguyên tố")
else:
    print("n không phải là số nguyên tố")
    print("cac số nguyên tố bé hơn số cần kiểm tra là :")
    tongsnt=0
for i in range(n+1):
  if isPrime(i)==1:
    print(i,end="\t")
    
print("\n")
for i in range(n+1):
  if isPrime(i)==1:
    tongsnt+=i
print("tong cac so nguyen to la : ",tongsnt)


# In[43]:


'''Hãy viết chương trình đọc file in.txt và hiển thị ra màn hình nội dung từng dòng trong file 
đó'''
fr= open('in.txt')
flines = fr.readlines()
for line in flines:
    print (line)
fr.close()


# In[3]:


'''Hãy viết chương trình xuất ra file out.txt các số chẵn nhỏ số n được nhập từ bàn phím. 
Biết rằng mỗi dòng thì lưu 1 số'''
n=int(input('Nhập số n:'))
fw = open('out.txt','w')
for i in range(n):
    if(i%2==0):
        fw.write(str(i)+'\r\n')
fw.close()


# In[4]:


fr= open('out.txt')
flines = fr.readlines()
for line in flines:
    print (line)
fr.close()


# In[63]:


fr =open('num_input.csv')
flines = fr.readlines()
for line in flines:
    print (line)
fr.close()


# In[65]:


''' Đọc file dữ liệu num_input.csv. Hãy lưu trữ các số trong file vào chương trình. Sau đó,
xuất ra màn hình tổng của các số trong file
'''
fr =open('num_input.csv')
ds_num=[]
flines = fr.readlines()
for line in flines:
    ds_num = ds_num + line.strip().split(',')    
print(ds_num)
ds_num=[int(i) for i in ds_num]
s=0
for val in ds_num:
    s=s+val
print("tong la :",s)
fr.close()


# In[ ]:


'''Viết chương trình xuất ra file prime.data lưu các số nguyên tố trong file num_input.csv. 
Biết rằng mỗi dòng sẽ chứa tối đa 5 số nguyên tố và các số nguyên tố cách nhau bởi dấu ‘;'''

