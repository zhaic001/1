# -*- coding: utf-8 -*-
import io, re

src = r'D:\资海春\resume-website\index.html'
s = io.open(src, encoding='utf-8').read()

repls = [
    ('../Zhaic/母亲的枷锁.jpg', 'assets/deploy_assets/mama.jpg'),
    ('../Zhaic/清北梦.jpg', 'assets/deploy_assets/qingbei.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/张不为.png', 'assets/deploy_assets/renwu/xiuzhang/zhangbuwei.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/张不为战损.png', 'assets/deploy_assets/renwu/xiuzhang/zhangbuwei_dmg.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/胡瑶瑶.png', 'assets/deploy_assets/renwu/xiuzhang/huyaoyao.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/胡瑶瑶（本体）.png', 'assets/deploy_assets/renwu/xiuzhang/huyaoyao_orig.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/苏也清（日常）.png', 'assets/deploy_assets/renwu/xiuzhang/suyeqing.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/苏也清（日常）1.png', 'assets/deploy_assets/renwu/xiuzhang/suyeqing_b.jpg'),
    ('../Zhaic/人物资产/修仙（男女主）/苏也清（日常）2.jpg', 'assets/deploy_assets/renwu/xiuzhang/suyeqing_c.jpg'),
    ('../Zhaic/人物资产/古装（男女主）/沈延.png', 'assets/deploy_assets/renwu/guzhuang/shenyan.jpg'),
    ('../Zhaic/人物资产/古装（男女主）/苏锦宁（便服）.png', 'assets/deploy_assets/renwu/guzhuang/sujinning.jpg'),
    ('../Zhaic/人物资产/废土科技风（男女主）/林小满.jpg', 'assets/deploy_assets/renwu/feitu/linxiaoman.jpg'),
    ('../Zhaic/人物资产/废土科技风（男女主）/裴川.jpg', 'assets/deploy_assets/renwu/feitu/peichuan.jpg'),
    ('../Zhaic/人物资产/废土科技风（男女主）/3DQ版林小满.png', 'assets/deploy_assets/renwu/feitu/linxiaoman_chibi.jpg'),
    ('../Zhaic/人物资产/废土科技风（男女主）/3DQ版裴川.png', 'assets/deploy_assets/renwu/feitu/peichuan_chibi.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/苏凡正装.png', 'assets/deploy_assets/renwu/dushi/sufan_suit.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/苏凡.png', 'assets/deploy_assets/renwu/dushi/sufan.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/苏凡（日常）.png', 'assets/deploy_assets/renwu/dushi/sufan_casual.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/苏凡（睡衣）.png', 'assets/deploy_assets/renwu/dushi/sufan_pajama.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/秦璐.png', 'assets/deploy_assets/renwu/dushi/qinlu.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/秦璐（日常）.png', 'assets/deploy_assets/renwu/dushi/qinlu_casual.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/秦璐（日常2）.png', 'assets/deploy_assets/renwu/dushi/qinlu_casual2.jpg'),
    ('../Zhaic/人物资产/都市风（男女主）/秦璐（居家）.png', 'assets/deploy_assets/renwu/dushi/qinlu_home.jpg'),
    ('../Zhaic/场景资产/修仙/凡俗小镇铁匠铺.png', 'assets/deploy_assets/scenes/xiuzhen_smithy.jpg'),
    ('../Zhaic/场景资产/修仙/秘境地下兵器库青铜阶梯通道.png', 'assets/deploy_assets/scenes/xiuzhen_armory.jpg'),
    ('../Zhaic/场景资产/修仙/青云宗演武场.png', 'assets/deploy_assets/scenes/xiuzhen_ground.jpg'),
    ('../Zhaic/场景资产/废土风/垃圾交易点.png', 'assets/deploy_assets/scenes/feitu_market.jpg'),
    ('../Zhaic/场景资产/废土风/离舰出口 舷窗.jpg', 'assets/deploy_assets/scenes/feitu_hatch.jpg'),
    ('../Zhaic/场景资产/废土风/舰队通讯舱.jpg', 'assets/deploy_assets/scenes/feitu_comms.jpg'),
    ('../Zhaic/场景资产/都市爽剧/公司楼下街道.png', 'assets/deploy_assets/scenes/dushi_street.jpg'),
    ('../Zhaic/场景资产/都市爽剧/华腾集团一楼大办公厅.png', 'assets/deploy_assets/scenes/dushi_office.jpg'),
    ('../Zhaic/场景资产/都市爽剧/苏凡出租屋.png', 'assets/deploy_assets/scenes/dushi_rental.jpg'),
    ('../Zhaic/婚庆拍摄/婚礼封面.jpg', 'assets/deploy_assets/wedding_cover.jpg'),
    ('../Zhaic/婚庆拍摄/婚礼.mp4', 'assets/deploy_assets/wedding.mp4'),
    ('../Zhaic/音频资产/男主.mp3', 'assets/deploy_assets/audio/male_lead'),
    ('../Zhaic/音频资产/女-睿智女主.mp3', 'assets/deploy_assets/audio/female_wise'),
    ('../Zhaic/音频资产/男-霸气.mp3', 'assets/deploy_assets/audio/male_boss'),
    ('../Zhaic/音频资产/胡瑶瑶.mp3', 'assets/deploy_assets/audio/huyaoyao'),
]

for old, new in repls:
    s = s.replace(old, new)
s = s.replace('download="资海春-简历.pdf"', 'download="zihai-chun-resume.pdf"')

io.open(r'D:\资海春\resume-website\deploy.html', 'w', encoding='utf-8').write(s)
rem = re.findall(r'src="\.\./Zhaic/[^"]*"', s)
print('deploy.html done, remaining:', len(rem))
