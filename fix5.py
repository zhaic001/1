path = r'C:\Users\Administrator\resume-restore\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace video modal - remove native controls, add custom play button
old_modal = '''<div class="modal" id="vmodal">
  <button class="close" onclick="closeModal()">&times;</button>
  <div class="video-wrap"><video controlsList="nodownload noremoteplayback" disablePictureInPicture controls><div class="video-protect"></div></div></video>
</div>'''

new_modal = '''<div class="modal" id="vmodal">
  <button class="close" onclick="closeModal()">&times;</button>
  <video id="vplayer" playsinline webkit-playsinline controlsList="nodownload noremoteplayback" disablePictureInPicture style="max-width:92vw;max-height:85vh;border-radius:8px"></video>
  <div id="vplaybtn" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:70px;height:70px;border-radius:50%;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5">
    <svg width="28" height="28" fill="white" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
  </div>
</div>'''

html = html.replace(old_modal, new_modal)

# 2. Update openVideo/closeModal and add custom play toggle
old_js = '''function openVideo(src){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}
function closeModal(){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video'); v.pause(); v.src='';
  m.classList.remove('on');
}'''

new_js = '''var vp = document.getElementById('vplayer');
var vpb = document.getElementById('vplaybtn');
vpb.addEventListener('click', function(){ vp.play(); });
vp.addEventListener('click', function(){ if(vp.paused){vp.play();vpb.style.display='none';} else {vp.pause();vpb.style.display='flex';} });
vp.addEventListener('play', function(){ vpb.style.display='none'; });
vp.addEventListener('pause', function(){ vpb.style.display='flex'; });
vp.addEventListener('ended', function(){ vpb.style.display='flex'; });
function openVideo(src){
  const m = document.getElementById('vmodal');
  vp.src = src; m.classList.add('on'); vp.play();
}
function closeModal(){
  const m = document.getElementById('vmodal');
  vp.pause(); vp.src=''; vpb.style.display='flex';
  m.classList.remove('on');
}'''

html = html.replace(old_js, new_js)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Custom video player installed - no native controls, no download button")
