from stegano import lsb
secret = lsb.hide('aguia.jpg', 'hawksec')

secret.save('secret.png')

