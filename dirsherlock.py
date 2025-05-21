#디렉토리 사전대입 공격 도구/Directory Brute force attack(dictionary based)
import getArgs,requests

#check url end with '/' or not
url = getArgs.url.strip()[-1]
if url != '/':
    getArgs.url=getArgs.url+'/'
else:
    pass

f = open(getArgs.wordlist,'r',)
wordlist = []
res_200 = []
res_hidden = []
#make wordlist filetype:list
while True:
    word = f.readline()
    rm_ent = word.replace("\n","")
    wordlist.append(rm_ent)
    if not word:
        wordlist.pop()
        break

#brute force with wowrdlist
for i in wordlist:
    word = getArgs.url+i
    send_req = requests.get(word)
    status = str(send_req)
    print(i+status)
    if status == "<Response [200]>":
        res_200.append(i)
    elif status in("<Response [401]>","<Response [403]>"):
        res_hidden.append(i)

#result dir
print("exist directory",res_200)
print("pemission denied or have to check directory",res_hidden)
