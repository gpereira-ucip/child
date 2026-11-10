import re,html
md=open('PROYECTO.md',encoding='utf8').read().split('\n')
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'`(.+?)`',r'<code>\1</code>',t)
    return t
out=[];ul=None;ol=False
def close():
    global ul
    if ul:out.append('</ul>');ul=None
for l in md:
    if l.startswith('# '):close();out.append('<h1>%s</h1>'%inline(l[2:]))
    elif l.startswith('## '):close();out.append('<h2>%s</h2>'%inline(l[3:]))
    elif l.startswith('> '):close();out.append('<blockquote>%s</blockquote>'%inline(l[2:]))
    elif re.match(r'^(- |\d+\. )',l):
        if not ul:out.append('<ul>');ul=True
        out.append('<li>%s</li>'%inline(re.sub(r'^(- |\d+\. )','',l)))
    elif l.strip()=='' :close()
    else:close();out.append('<p>%s</p>'%inline(l))
close()
body='\n'.join(out)
page='''<title>Child, proyecto maestro</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{--bg:#FFFFFF;--fg:#16140F;--mut:#6F6B5F;--line:#ECEAE3;--y:#F0AB0C;--soft:#F8F7F3;--blue:#2E86C9;--red:#D8373B;--violet:#8E4BB8;--green:#4E9E3C;--orange:#EF8A1E;color-scheme:light}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px;margin:0}
.bar{height:4px;background:linear-gradient(90deg,var(--blue) 0 20%,var(--red) 20% 40%,var(--violet) 40% 60%,var(--green) 60% 80%,var(--orange) 80%);margin:0 calc(-1 * max(16px,env(safe-area-inset-left,0px)))}
main{max-width:720px;margin:0 auto;padding-top:28px}
h1{font-size:30px;line-height:1.15;letter-spacing:-.02em;margin:0 0 6px;text-wrap:balance}
h2{font-size:21px;line-height:1.2;letter-spacing:-.01em;margin:34px 0 10px;padding-top:18px;border-top:1px solid var(--line);text-wrap:balance}
p{margin:0 0 12px}
ul{padding-left:22px;margin:0 0 14px}li{margin:6px 0}
blockquote{margin:14px 0;padding:12px 16px;background:#FFF3CF;border-radius:14px;font-weight:600}
code{background:var(--soft);border-radius:6px;padding:1px 6px;font-size:.9em;overflow-wrap:anywhere}
strong{font-weight:700}
</style>
<div class="bar"></div>
<main>
@@BODY@@
</main>
'''.replace('@@BODY@@',body)
open('proyecto.html','w',encoding='utf8').write(page)
print(len(page))
