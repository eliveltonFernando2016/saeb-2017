import zipfile
import requests
import sys
import os

if not os.path.isdir("saeb-2017"):

    link = "http://download.inep.gov.br/microdados/microdados_saeb_2017.zip"
    file_name = "saeb2017.zip"

    with open(file_name, "wb") as f:
            print("Downloading {}".format(file_name))
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
    print("\n")

    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall("saeb-2017")
    zip_ref.close()

    os.remove("saeb2017.zip")