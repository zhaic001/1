path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add password gate CSS
pw_css = '''
#pwgate { position:fixed; inset:0; z-index:99999; background:#0a0a0a; display:flex; flex-direction:column; align-items:center; justify-content:center; }
#pwgate input { background:#1a1a1a; border:1px solid #b8860b; color:#fff; padding:12px 20px; font-size:18px; border-radius:8px; width:220px; text-align:center; outline:none; letter-spacing:4px; }
#pwgate button { margin-top:12px; background:linear-gradient(135deg,#e8c376,#d4a017); border:none; padding:12px 40px; font-size:16px; border-radius:8px; cursor:pointer; color:#1a1a1a; font-weight:700; }
#pwgate .err { color:#e74c3c; margin-top:10px; font-size:13px; }
#pwgate h2 { color:#b8860b; font-family:'Noto Serif SC',serif; margin-bottom:24px; letter-spacing:2px; }
'''
html = html.replace('</style>', pw_css + '</style>', 1)

# Add password gate HTML right after <body>
pw_html = '''
<div id="pwgate">
  <h2>资海春 · 作品集</h2>
  <input type="password" id="pwinput" placeholder="请输入密码" />
  <button onclick="checkPw()">进 入</button>
  <div class="err" id="pwerr"></div>
</div>
'''
# Insert after <body>
html = html.replace('<body>', '<body>\n' + pw_html, 1)

# Add password check JS before </body>
pw_js = '''<script>
function checkPw(){
  var v = document.getElementById('pwinput').value;
  if(v === '2004'){
    document.getElementById('pwgate').style.display='none';
    sessionStorage.setItem('pwok','1');
  } else {
    document.getElementById('pwerr').textContent = '密码错误，请重试';
  }
}
document.getElementById('pwinput').addEventListener('keydown', function(e){ if(e.key==='Enter') checkPw(); });
if(sessionStorage.getItem('pwok')==='1'){ document.getElementById('pwgate').style.display='none'; }
</script>'''
html = html.replace('</body>', pw_js + '\n</body>', 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Password gate added: 2004")
