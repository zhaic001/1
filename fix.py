import base64

path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add protection CSS
protect_css = "\n/* Anti-download */\nimg,video{-webkit-user-drag:none!important;user-select:none!important;-webkit-touch-callout:none!important}\n"
content = content.replace('</style>', protect_css + '</style>', 1)

# Add protection JS
protect_js = '\n<script>document.addEventListener("contextmenu",function(e){if(!e.target.closest(\'a[href$=".pdf"],button,input\'))e.preventDefault()});document.addEventListener("dragstart",function(e){if(e.target.tagName==="IMG"||e.target.tagName==="VIDEO")e.preventDefault()});document.addEventListener("touchstart",function(e){if(e.target.tagName==="IMG"||e.target.tagName==="VIDEO")e.preventDefault()},{passive:false});</script>\n'
content = content.replace('</body>', protect_js + '</body>', 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Protection added. Size: {len(content)} chars")
