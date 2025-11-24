
from zipfile import * 

with ZipFile('imgage.zip', 'r') as f:
    f.extractall()
    
    