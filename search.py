from aip import AipOcr
from PIL import ImageGrab
import re
import time
APP_ID = '15679213'
API_KEY = 'ITOQAuZHCipDKPlXpbM2KyW7'
SECRET_KEY = 'ewuoybwn1YfQE6vtvH8UFkaFYf3Soppk'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def number():
    pic = ImageGrab.grab(bbox=(437,138,488,157))
    pic.save("4.jpg")
    image = get_file_content('4.jpg')
    text = client.basicGeneral(image)
    try:
        alltext  =''
        for word in text['words_result']:
            alltext =alltext + word.get('words','')
        alltext= re.findall("\d+",alltext)
        num= int(alltext[0])
        return num
    except:
        num =1000000000000
        return num
# if __name__ == "__main__":
#     time.sleep(2)
#     print(number())
