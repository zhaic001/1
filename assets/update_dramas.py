# -*- coding: utf-8 -*-
import io, re

p = r'D:\资海春\resume-website\deploy.html'
s = io.open(p, encoding='utf-8').read()

# Replace DRAMAS with online paths
old_dramas = re.search(r'const DRAMAS = \{.*?\};', s, re.DOTALL).group()

new_dramas = """const DRAMAS = {
  'eps-guzhuang': {
    dir: 'assets/deploy_assets/reels/',
    eps: [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55].map(n => ({
      file: `ep_guzhuang_${n}.mp4`, label: `EP${n}`
    }))
  },
  'eps-xiandai': {
    dir: 'assets/deploy_assets/reels/',
    eps: [
      ['ep_xiandai_35.mp4','EP35'],['ep_xiandai_36.mp4','EP36'],['ep_xiandai_37.mp4','EP37'],
      ['ep_xiandai_38.mp4','EP38'],['ep_xiandai_39.mp4','EP39'],['ep_xiandai_40.mp4','EP40'],
      ['ep_xiandai_41.mp4','EP41']
    ].map(([f,l]) => ({file:f, label:l}))
  },
  'eps-dou': {
    dir: 'assets/deploy_assets/reels/',
    eps: [
      ['ep_dou_15.mp4','EP15'],['ep_dou_16.mp4','EP16'],['ep_dou_17.mp4','EP17'],
      ['ep_dou_18.mp4','EP18'],['ep_dou_19.mp4','EP19'],['ep_dou_20.mp4','EP20'],
      ['ep_dou_21.mp4','EP21'],['ep_dou_32.mp4','EP32'],['ep_dou_33.mp4','EP33'],
      ['ep_dou_34.mp4','EP34']
    ].map(([f,l]) => ({file:f, label:l}))
  },
  'eps-feitu': {
    dir: 'assets/deploy_assets/reels/',
    eps: [
      ['ep_feitu_08.mp4','EP8'],['ep_feitu_09.mp4','EP9'],['ep_feitu_10.mp4','EP10'],
      ['ep_feitu_14.mp4','EP14'],['ep_feitu_15.mp4','EP15'],['ep_feitu_23.mp4','EP23'],
      ['ep_feitu_24.mp4','EP24']
    ].map(([f,l]) => ({file:f, label:l}))
  }
};"""

s = s.replace(old_dramas, new_dramas)

# Also remove the ../Zhaic guard in openVideo since episodes now use online paths
old_guard = """function openVideo(src){
  if(src && src.indexOf('../Zhaic/') === 0) return;
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""
new_guard = """function openVideo(src){
  const m = document.getElementById('vmodal');
  const v = m.querySelector('video');
  v.src = src; m.classList.add('on'); v.play();
}"""
s = s.replace(old_guard, new_guard)

io.open(p, 'w', encoding='utf-8').write(s)
print('DRAMAS updated to online paths, guard removed')
