import requests
import io

# Récupérer le contenu du fichier contenant la fonction via son URL
url1 = 'https://raw.githubusercontent.com/bablebab/M1-Programming-JANATI-LOUALI-UNLUBAYIR/main/joueur.py'
response1 = requests.get(url1)
content1 = response1.content

# Créer un flux de lecture pour le contenu récupéré
stream1 = io.StringIO(content1.decode('utf-8'))

# Exécuter le code dans le flux de lecture
exec(stream1.read())

# Appeler la fonction du fichier importé
joueur()

# Récupérer le contenu du fichier contenant la fonction via son URL
url2 = 'https://raw.githubusercontent.com/bablebab/M1-Programming-JANATI-LOUALI-UNLUBAYIR/main/poste.py'
response2 = requests.get(url2)
content2 = response2.content

# Créer un flux de lecture pour le contenu récupéré
stream2 = io.StringIO(content2.decode('utf-8'))

# Exécuter le code dans le flux de lecture
exec(stream2.read())

# Appeler la fonction du fichier importé
poste()