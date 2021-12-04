import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9jRtjB7drnQ56gURjtVG54tmFbyWDk5r34r1hUUZBlJ_qvXEMX1GiTBGSBPbm6lXLfgKEVYHIJA-KtfsNAl2ds-KWY7VrNDeO2qCC1OCrLknHmU-y6ECDNKsRADTC7CoSLr5AQQgi7l'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer -")
    file_to = input("Enter the full path to upload to dropbox -")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
if __name__ == '__main__':
    main()