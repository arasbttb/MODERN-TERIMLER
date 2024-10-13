meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "LMAO":"Birine saçma sapan birşekilde ve ya anlamadığınız birşeye okomik demek.",
            "CREEPY":"- korkunç"
            }
#fazla
#for i in range(4)

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
   print(meme_dict[word]) 
else:
