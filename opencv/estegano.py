import ascleCV as ascle

img = ascle.abr_img_cinza('imagem-peq.png')

print("Qtd de pixeis: {}".format(ascle.get_qtd_pixel(img)))
print("Qtd de letras: {}".format(ascle.get_qtd_pixel(img)/8))

# print do pixeis originais
#print(img)

img2 = ascle.estegano_lsd(img, 'vamos lá')

# print dos pixeis alterados
#print(img2)

print(ascle.des_estegano_lsd(img2))

#ascle.ver_img(img)