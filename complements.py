# Python3 program to print 1's and 2's
# complement of a binary number
bin=input('Enter a Binary value:')
ones = ""
twos = ""
flag=0
for i in bin:
    if i=='0':
        ones+='1'
    else:
        ones+='0'
print("1's complement:",ones)
l=len(ones)
ones = list(ones.strip(""))
twos = list(ones)
#range(variable,endpoint,step)
for i in range(l - 1, -1, -1):
    if (ones[i] == '1'):
        twos[i] = '0'
    else:
        twos[i] = '1'
        flag=1
        break
if flag==0:
    i -= 1
    # If No break : all are 1 as in 111 or 11111
    # in such case, add extra 1 at beginning
    if (i == -1):
        twos.insert(0, '1')
print("2's compliment: ",*twos,sep='')
