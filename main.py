from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json


FOLDER_ID = "1Vtpe-8Hl-7l-btPf2h52ASAWymOWbPyO"


gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("credentials.txt")


drive = GoogleDrive(gauth)


def getChildrenForFolder(folderId):
    out = {}
    fileList = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folderId)}).GetList()
    for file in fileList:
        if file["mimeType"] == "application/vnd.google-apps.folder":
            out[file["title"]] = getChildrenForFolder(file["id"])
        else:
            print(json.dumps(file, sort_keys=True, indent=4))
            print("\n\n\n\n\n\n")
            out[file["title"]] = file["id"]
    return out

with open('notes.json', 'w') as out:
    data = getChildrenForFolder(FOLDER_ID)
    json.dump(data, out)
    print(json.dumps(data, sort_keys=True, indent=4))
    print("data written to notes.json")
