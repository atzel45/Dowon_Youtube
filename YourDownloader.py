import pafy
e = raw_input("Ingresa la ID de el video: ")
v = pafy.new(e)
print("\nInformacion de el video: ")
print "_______________________________________________|"
print("Autor: " + v.author)
print "_______________________________________________|"
print("Categoria: " + v.category)
print "_______________________________________________|"
print("Numero De Likes: " + str(v.likes))
print "_______________________________________________|"
print("Numero De Dislikes: " + str(v.dislikes))
print "_______________________________________________|"
print("Duracion: " + str(v.duration))
print "_______________________________________________|"

desicion = raw_input("Desea descargarlo ya sea en audio o video(s/n): ")
while desicion != "s" and "n":
 if desicion == "n": break 
 else:
  desicion = raw_input("Desea descargarlo ya sea en audio o video(s/n): ")

if desicion == "s":
 formato = raw_input("Formato de descarga Video/Audio(v/a): ")
 if formato == "v":
  archivo = v.getbest()
  archivo.download()
 if formato == "a":
  archivo = v.getbestaudio()
  archivo.download()
else:
 pass
