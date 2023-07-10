import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import os
import re
import base64
os.chdir(os.path.dirname(__file__))

st.set_page_config("生日快乐",page_icon="🍻")

with open("background.jpg", "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()

# 生成HTML代码，设置.stApp元素的background-image和background-size属性
html_code = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{b64}");
    background-size: 100%;
    background-attachment: fixed;
}}
</style>
"""

# 使用st.markdown显示HTML代码，设置unsafe_allow_html为True
st.markdown(html_code, unsafe_allow_html=True)

def display_img(file_name, caption):
    image = Image.open(file_name)
    st.image(image, caption=caption)

def play_music(file_name, start_sec = 0): # only .ogg format
    st.session_state.music = file_name
    with open(file_name, "rb") as file:
        data = file.read()
        b64 = base64.b64encode(data).decode()

        # 生成HTML代码，设置autoplay属性为true，controls属性为false
        html_code = f"""
        <script>
            var audio = document.getElementById("myAudio");
            audio.pause();
        </script>
        <audio id="myAudio" loop="true" controls>
            <source src="data:audio/{file_name.split('.')[-1]};base64,{b64}" type="audio/{file_name.split('.')[-1]}">
        </audio>
        <script>
        document.addEventListener('touchstart', function() {{
            document.getElementById('myAudio').play()
        }});
        document.addEventListener('DOMContentLoaded', function () {{
                function audioAutoPlay() {{
                    var audio = document.getElementById('myAudio');
                    audio.play();
                    document.addEventListener("WeixinJSBridgeReady", function () {{
                        audio.play();
                }}, false);
                }}
            audioAutoPlay();
        }});
        </script>
        """

        if start_sec is not None:
            html_code += f'''<script>
            var audio = document.getElementById("myAudio");
            audio.currentTime = {start_sec};
            </script>'''

        # 用html函数调用HTML与JS代码
        html(html_code, height=100)

st.title(':orange[Happy Birthday!🎂]')
answer = st.chat_input("想去到哪一年的生日：（如 2020）", )
st.markdown('''<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.element-container.css-1etyx85.esravye2 > div {
    background-color:transparent;
}
</style>''', unsafe_allow_html=True)

def display_history(startYear, endYear, text, music, pic, picText):
    if startYear <= int(year) <= endYear:
        with st.chat_message("user"):
            st.markdown(text,unsafe_allow_html=True)
            display_img(pic,picText)
            if st.session_state.music != music:
                play_music(music)

if answer is not None:
    year = re.findall("\d+\.?\d*",answer)[0]
    st.session_state.music = ""
    if year == '1998':
        with st.chat_message("user"):
            st.markdown(f'''**1998年，你出生了，我也出生了 👯‍♀️<br>这是我们能够产生缘分的开始。两只老虎、巨蟹和狮子的故事也将开展。
                        <br>祝刚出生的你生日快乐，这时的你充满希望，一切都将刚刚开始。
                        <br>而还需要等一个月，我才能降临世间。🐯🐯**''',unsafe_allow_html=True)
            play_music('儿歌多多 - 两只老虎.mp3',3)
    
    if 1999 <= int(year) <= 2008:
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到你的婴幼儿时期 👶<br>这是你的1-10岁，等你长大哦。
                        <br>祝这个阶段的你生日快乐，这时的你是初升的太阳，一颗冉冉升起的新星。🌞⭐**''',unsafe_allow_html=True)
            if st.session_state.music != '刘廷禹 - 初升的太阳.mp3':
                play_music('刘廷禹-初升的太阳.mp3',3)

    if 2009 <= int(year) <= 2012:
        with st.chat_message("user"):
            st.markdown(f'''**想回到厚外哇 🙋‍♀️<br>说起来，相比起初中，现在的你收获了很多，又失去了很多。
                        <br>但最终这些得失都将成为指引你成长的路灯，跟随你一直到老。
                        <br>Anyway，祝初中的你生日快乐，并且祝现在的你保持初中时的青春、纯粹与活力。🥳**''',unsafe_allow_html=True)
            if st.session_state.music != '徐良、小凌 - 坏女孩.mp3':
                display_img('middle school.jpg','致初中稚嫩而非主流的你')
                play_music('徐良、小凌 - 坏女孩.mp3')

    if 2013 <= int(year) <= 2015:
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到高中时期 👩‍🎓<br>高中的你比我更加成熟，欢迎回到那个成熟的年代！**''',unsafe_allow_html=True)
            if st.session_state.music != '胡夏 - 那些年.mp3':
                display_img('high school.jpg','假装是高中时期')
                play_music('胡夏-那些年.mp3')
    
    if year == '2016':
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到2016年 🐵<br>这一年是猴年，也是我们高考的那年。<br>
                        但是那时候我们真的不熟，那就祝你猴年大吉吧！**''',unsafe_allow_html=True)
            display_img('2016.jpg','假装是高考结束')
            play_music('安来宁 _ 房东的猫 - 下一站，茶山刘.mp3')

    if year == '2017':
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到2017年 🐔<br>这一年是鸡年，真的跟你不熟，就祝你鸡年大吉吧！<br>**''',unsafe_allow_html=True)
            display_img('2017.jpg','假装拿的是蛋糕')
            play_music('SWIN-S - 只因你太美.mp3')
    
    if year == '2018':
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到2018年 🤨🐶<br>这一年是狗年，我们都在各自的生活泥泞中无法自拔，为数不多的交集可能就是放假回家和大家伙一块出去玩。<br>
                            那时候的我是真的跟你不熟啦，但是一直知道你也是个非主流的人类，仅此而已。<br>
                            但是现在知道啦，那时候你迷恋着朱星杰，所以就用他非主流的歌带你回去那个非主流的2018年。🤡**''',unsafe_allow_html=True)
            display_img('2018.jpg', '致记忆中模糊的你')
            play_music('朱星杰-仲夏夜.mp3')

    if year == '2019':
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到2019年 😲🐽<br>这一年我们还没那么熟络，你也还在为一些虚无缥缈的事情感到困惑。<br>
                            “很多关系我舍不得断掉，解决也无能为力，只能你我都避而不谈，等它哪天自己不堪负重折了，我也算尽了全力。”<br>
                            那年的你和我还在两条平行线上，那时候的我们还在准备考研，谁也想不到在几个月之后两条平行线竟然找到了交点。<br>
                            那么姑且认为你在恋爱告急吧。😈**''',unsafe_allow_html=True)
            display_img('2019.jpg', '致年少忧郁且非主流的你')
            play_music('鞠婧祎-恋爱告急.mp3')
    
    if year == '2020':
        with st.chat_message("user"):
            st.markdown(f'''**欢迎回到2020年 🎶🐭<br>这是我们爱情开始的一年，也是鼠年<br>夏日也是2020年的产物，那时的朱星杰还是我们的热爱<br>
                            在这一年，我们因为疫情在赣州重逢，因为对未来的迷茫聊得愈加投机<br>
                            我们一起度过了考研的失败、愉快的广州之旅以及各自奔向新生活的开始<br>
                            那就随着这首夏日回到3年前的那个夏天吧~🎊**''',unsafe_allow_html=True)
            display_img('2020.jpg', '珠江边的港风照')
            play_music('朱星杰-夏日.mp3')
    
    if year == '2021':
        with st.chat_message("user"):
            st.markdown(f'''**2021年的生日绝对是一个不平凡的日子 🚗🐮<br>
                            这一年我们第一次自驾游去了千岛湖，收获了许多快乐与 “心酸”……<br>
                            这一年我们一起看了爆裂舞台上的单依纯，所以就让这首RnB All Night带你回到那个2021吧。🥰**''',unsafe_allow_html=True)
            display_img('2021.jpg', '让我们在漂流中荡起双桨')
            play_music('单依纯 - RB All Night (Live).mp3', 2)
    
    if year == '2022':
        with st.chat_message("user"):
            st.markdown(f'''**2022年的生日或许略显平凡 👩‍💻🐯<br>
                            在本命年的那一年碰上了疫情，我们甚至没有见面……😥<br>
                            但我收到了一份珍贵的礼物——2 anniversary专辑！💽
                            精美的设计，精心挑选的歌曲，承载着我们的经历与闪闪发光的记忆点。
                            多么希望这张专辑能够常听常新，永远不会江郎才尽，让音乐成为我们感情的记录者。**''',unsafe_allow_html=True)
            display_img('2022.jpg', '2周年快乐呀')
            play_music('李健-一往情深的恋人-_Live_.mp3',3)

    if year == '2023':
        with st.chat_message("user"):
            st.markdown(f'''**wow 这里是2023年，It's now！👻🐰<br>
                        其实每年生日都是最好的一年，所以欢迎你来到2023年，也是兔年！<br>
                        今年是不平凡的一年，我们终于结束了三年的异地，我来到了你的城市，好久不见。<br>
                        在你生日的这天，我正好已经工作了一周，相信未来的日子我们会越来越好，并且步入人生的正轨。<br>
                        虽然现在我们还有一小时的异地，但我会在莘庄等着你。❤️<br>
                        未来的每一个生日，都由我来陪你度过吧！**''',unsafe_allow_html=True)
            display_img('2023.jpg', '难得的化妆美美哒')
            play_music('陈奕迅 - 好久不见.mp3', 14)

    if 8 < int(year) < 1998:
        with st.chat_message("user"):
            st.markdown(f'''**我知道你并不想回到你出生以后，但是只有活着，才能感受到人生的酸甜苦辣、阴晴圆缺，<br>
                     何况还有fisher陪伴着你度过慢慢余生。<br>所以，请输入1998-2023的年份吧！😊**''',unsafe_allow_html=True)
            display_img('before 1998.jpg','让我们相约1998')
            play_music("那英-_-王菲-相约一九九八.mp3", 18)
            
    if int(year) > 2023:
        with st.chat_message("user"):
            st.markdown(f'''**前方岁月待解锁 with fisher💏👪👨‍👩‍👧‍👦**''',unsafe_allow_html=True)
            display_img('future.png','future is better')
            play_music('林俊杰-将故事写成我们.mp3')

    display_history(0,8,
                    f'''**我看你是想穿越，那就带着前世的记忆，来到这熟悉又陌生的西汉吧。<br>
                        这里有你的刘氏王朝，刘邦即将开大来到你身边，并且给你套上盾跟你说一句：<br>
                        生日快乐！🎂**''',
                        '林俊杰-穿越.mp3', '西汉.jpg', '楚汉之争的不太平时代')
    
    