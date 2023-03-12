import seaborn as sns
import sys
import numpy as np 
import pandas as pd
from scipy.spatial.distance import euclidean
from tkinter import *
import matplotlib.pyplot as plt
from collections import Counter
import requests
import zipfile
import io

url = "https://storage.googleapis.com/kaggle-data-sets/1617785/2767201/compressed/players_22.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230312T165056Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9ea3cbff04eb5a9e57f29bcf14a79ec01e99febce2c595fc458933e7ecb73e83f8fe48f294a918a791b21469a97264a9dd77bbecf8e65506841c6c6ace944e989eb8cb2e2639603fba40e3493c33ccaf4da280fe30948aa7944a8282c75fa2cb238110fcb4d02995fab4470b8414bd6c0508dd645100573ff0021309d335ff66138b93815a6b71650e0bd03de3293df7651b5c63d0179a91e6a7363e868405d656f57018a794c0de0bf07f60260ba56e5df9f668f32a5309028edc4fd9ea73e64b33f33c9a32675e9e43e224bf500828aee04021534c0559372eebdae874c867ddfd86c72c8f30a74c4110f91ea8712c415c3819366cb1bc473ba18a7f99426b"
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
csv_file = zip_file.extract("players_22.csv")
df = pd.read_csv(csv_file, sep=',')
print(df.head())

# Importation des modules contenant les fonctions à appeler
from joueur import joueur
from poste import fposte

joueur()

poste()