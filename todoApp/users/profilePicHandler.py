import os
import base64
from flask import url_for 

#Profile Picture Handler
def addProfilePic(picUpload=None):
    if picUpload:
        filedata = picUpload.read()
    else:
        return 'None'

    filedata = base64.b64encode(filedata)
    filedata = filedata.decode("UTF-8")
    return filedata
