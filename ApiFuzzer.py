import requests
import time
import re
import Design

def ValidateStatusCode(Status_code):
    for i in range(len(Status_code)):
        Status_code[i]=int(Status_code[i])
    return Status_code


def printline(keyword,response):
    lenngth = len(keyword)
    if response.status_code in result:
        print('  | Status:'+str(response.status_code))
        print('#Requesting :'+url,end='')
    else:
        for i in range(lenngth):
            print('\b', end='')



def Fuzz(file_name):
    try:
        file=open(file_name,'r')
    except:
        print('\nERROR OPENING FILE!!')
        exit(0)
    print('#Requesting :'+url, end='')
    for line in file:
        keyword=line.strip()
        print(keyword,end='')
        try:
            response=requests.get(url+keyword)
        except:
            print('\nERROR REACHING HOST!!')
            exit(0)
        printline(keyword,response)
    file.close()


Design.Pattern()
url=input('Enter the URL (with / at end):')
status_input=input('Enter status code you loooking for(separated by comma):')
file_name=input('Enter the filename with path:')
Status_Codes=re.split(',',status_input)
result=ValidateStatusCode(Status_Codes)
Fuzz(file_name)

print('\n')