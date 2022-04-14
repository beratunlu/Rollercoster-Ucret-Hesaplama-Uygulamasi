boyu = int(input("Lutfen boyunuzu cm cinsinden giriniz: "))

yetiskin_bilet= 12
genc_bilet = 7
cocuk_bilet = 5
fotograf_ucreti = 3




if boyu >= 120: 
  print("Rollercoster'a binebilirsiniz.")
  yas = int(input("Lutfen yaşınızı giriniz: "))
  print("""
 1-) Erişkin Bilet ücreti:${}
 2-) Genç Bilet ücreti:   ${}
 3-) Çocuk Bilet Ücreti:  ${} 
  """.format(yetiskin_bilet,genc_bilet,cocuk_bilet))
  foto_isteme_asamasi = input(" Rollercoster ile Giderken Fotoğraf Çekilmek istiyor musunuz ' Bilet Ücreti: 3$ ' Evet ise Y'e Basın.  'Hayırsa' herhangi bir tuşa Basın: ")
  if foto_isteme_asamasi == "Y" or "y":
    if yas < 12:
      print(f"Toplam Tutar:$ {cocuk_bilet+fotograf_ucreti}")
    elif yas < 18:  
      print(f"Toplam Tutar:$ {genc_bilet+fotograf_ucreti}")
    else:
      print(f"Toplam Tutar:$ {yetiskin_bilet+fotograf_ucreti}")  
  else:
    if yas < 12 :
      print(f"Bilet ucreti:$ {cocuk_bilet}")
    elif yas < 18:
      print(f"Bilet ucreti:$ {genc_bilet}")
    else:
      print(f"Bilet ucreti:$ {yetiskin_bilet}")  

else:
  print("Rollercoster'a binemezsiniz")  
