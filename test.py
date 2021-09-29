z= "Cryptographypriortothemodernagewaseffectivelysynonymouswithencryption,convertinginformationfromareadablestatetounintelligiblenonsense.Thesenderofanencryptedmessagesharesthedecodingtechniqueonlywithintendedrecipientstoprecludeaccessfromadversaries.ThecryptographyliteratureoftenusesthenamesAliceforthesender,Bobfortheintendedrecipient,andEvefortheadversary."

text = z
text = text.replace(" ", "")
text = text.replace("!", "")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.upper()

print(text)