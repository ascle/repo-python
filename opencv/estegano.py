import ascleCV as ascle

img = ascle.abr_img_cinza('satanas.png')

print(img.shape)
print("Qtd de pixeis: {}".format(ascle.get_qtd_pixel(img)))

print("decimal: {} Binário: {}".format(img.item(0,0), bin(img.item(0,0))))
print("decimal: {} Binário: {}".format(img.item(0,0), img.item(0,0)))
img.itemset((0,0), 255)
print("decimal: {} Binário: {}".format(img.item(0,0), bin(img.item(0,0))))

#img.itemset((1,1), 255)
#img.itemset((2,2), 255)
ascle.ver_img(img)