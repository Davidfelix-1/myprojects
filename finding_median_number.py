m_number=[5,10,10,20,20,20,25,30,35]
m=len(m_number)
m_number.sort()
print(m_number)
if m % 2==0:
    median1= m_number[m//2]
    median2=m_number[m//2 -1]
    median= (median1 +median2)/2
else:
    median =m_number[m//2]
    print('median is: '+str(median))