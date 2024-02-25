import pandas as pd
df = pd.read_csv('../Fraud/dataset/teste.csv',sep=',',header=0)
i = 0
#df.loc[2, 'ip_address'] = 'SHIV CHANDRA'
for d in df['ip_address']:
    d = (d.split(".",1))
    #print(d[0])
    df.loc[i, 'ip_address'] = d[0]
    i = i+1
j=0
for d in df['email_address']:
    d = (d.split("@",1))
    #print(d[1])
    if(d[1] == "example.net"):
        df.loc[j, 'email_address'] = 0
    elif(d[1] == "example.org"):
        df.loc[j, 'email_address'] = 1
    elif(d[1] == "example.com"):
        df.loc[j, 'email_address'] = 2
    j = j + 1
z=0
for d in df['billing_address']:
    d = (d.split(" ",1))
    #print(d[0])
    df.loc[z, 'billing_address'] = d[0]
    z = z + 1
df = df.drop('billing_state', axis=1)
df = df.drop('user_agent', axis=1)
df = df.drop('phone_number', axis=1)
df = df.drop('EVENT_TIMESTAMP', axis=1)
print(df)