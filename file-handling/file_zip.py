
from zipfile import * 

with ZipFile('imgage.zip', 'w', ZIP_DEFLATED) as f:
    f.write('img1.png')
    f.write('img2.jpg')
    
    