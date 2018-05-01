import requests
import shutil
def callme():
    url = "https://trades.nationalgrid.co.uk/download-csv"
    r = requests.get(url, verify=False,stream=True)
    if r.status_code!=200:
        print ("Failure!!")
        exit()
    else:
        r.raw.decode_content = True
        with open("file1.csv", 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print ("Success")

if __name__ == '__main__':
    callme()