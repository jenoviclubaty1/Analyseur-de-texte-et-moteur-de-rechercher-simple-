def read_text_file(file_path):
' cette fonction ouvre un fichier texte et lit son contenu
  with open(file_path, 'r', encoding='utf-8')as f:
' ouve le fichier en mode lecture avec encodage utd-8
'ouvre et lit le fichier texte donné par son chemi
    return f.read()
'retourne le contenu du fichier 
def clean_text(text):
' une fonction qui nettoie le texte
'transforme le texte en minuscules et enleve la ponctuation
  texte=texte.lower()
' converti le texte en monuscules
  text=re.sub(r'[^\w\s]','',text) 
' enleve tout sauf les lettres et les espaces
  return text
'retourne le texte nettoyé
def tokenize(text):
'decoupe le texte en mots appelé tokenisation
    return clean_text(text).split()
' nettoie le texte et le decoupe en mot
