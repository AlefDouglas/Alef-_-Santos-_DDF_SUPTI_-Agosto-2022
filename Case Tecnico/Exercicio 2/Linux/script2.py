#Necessario usar a biblioteca pandas
#pip3 install pandas


#importar as bibliotecas





# importing library
import pandas as pd
  
# Then loading csv file
df = pd.read_csv('usersg.csv')
  
# converting ;FRUIT_NAME' column into list
a = list(df["Nome"])
  
# converting list into string and then joining it with space
b = ' '.join(str(e) for e in a)
  
# printing result
print(b)
  
# converting 'PRICE' column into list
d = list(df['Email'])
  

  
# printing result
print(a)



