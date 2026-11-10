import base64
b=lambda p,m:"data:%s;base64,%s"%(m,base64.b64encode(open(p,'rb').read()).decode())
s=open('index.src.html',encoding='utf8').read()
for k,f,m in [('__LOGO__','logo.jpg','image/jpeg'),('__ICON180__','apple-touch-icon.png','image/png'),('__ICON192__','icon-192.png','image/png'),('__ICON512__','icon-512.png','image/png'),('__ICONM__','icon-maskable-512.png','image/png')]:
    s=s.replace(k,b(f,m))
open('index.html','w',encoding='utf8').write(s)
print(len(s))
