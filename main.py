''''''
import streamlit as st
import pandas as pd
from PIL import Image
import json
import random
import time


def Home():
    '''首页'''
    st.write('# 首页')
    st.write('')
    st.write('在左侧边栏选择功能，开始使用吧~')
    st.write('')
    st.write('')
    st.write('*v0.3.5*')
    st.write('----------------')
    st.write('今日人品')
    col1, col2 = st.columns([1, 5])
    with col1:
        if_luck = st.button('点击查看')
    with col2:
        if if_luck:
            if check_date() == 'AFD':
                luck = random.randint(-100, 0)
                st.write(f'今日人品：{str(luck)}。愚人节快乐！')
            if check_date() == 'ND':
                luck = random.randint(81, 100)
                st.write(f'今日人品：{str(luck)}。国庆节快乐！')
            else:
                luck = random.randint(0, 100)
                if luck == 0:
                    st.write(f'今日人品：{str(luck)}。从某种意义上来说还是很欧的。')
                elif luck == 100:
                    st.write(f'今日人品：{str(luck)}。今天运气爆棚！')
                elif luck <= 40:
                    st.write(f'今日人品：{str(luck)}。今天运气有点差哦。')
                elif luck <= 80:
                    st.write(f'今日人品：{str(luck)}。今天运气还好哦。')
                else:
                    st.write(f'今日人品：{str(luck)}。今天运气不错哦。')

def Hobbies():
    '''我的兴趣推荐'''
    st.write('# 我的兴趣推荐')
    st.write('')
    st.write('')
    st.write('我的兴趣：')
    st.write('')
    col3, col4, col5 = st.columns([1, 1, 1])
    with col3:
        st.write('打篮球')
    with col4:
        st.write('编程')
    with col5:
        st.write('玩魔方')
    st.write('----------------')
    ws_coding = 'https://shequ.codemao.cn/'
    ws_cubes = 'http://www.rubik.com.cn/'
    st.write('兴趣网站推荐：')
    st.write('')
    col6, col7 = st.columns([1, 1])
    with col6:
        st.write('编程猫社区'+ws_coding)
    with col7:
        st.write('魔方小站'+ws_cubes)
    st.write('----------------')
    st.write('其他：')
    st.write('')
    col1, col2 = st.columns([1, 1])
    turtle2_img = Image.open('turtle2.jpg')
    turtle2_img = turtle2_img.resize((250, 250))
    with col1:
        st.write('我们的编程软件：海龟编辑器2.0')
        st.image(turtle2_img)
    cubes_img = Image.open('cubes.jpg')
    cubes_img = cubes_img.resize((250, 250))
    with col2:
        st.write('我的魔方')
        st.image(cubes_img)

def Calculator():
    '''计算器'''
    st.write('# 计算器')
    # 创建算式输入框
    content = st.text_input('请输入算式  --注意：加号+，减号-，乘号*，除号/，乘方**，开方请转换为乘方（转换方法：n次根号a = a**(1/n)），括号一律用()')
    if content:
        try:
            # 计算
            result = eval(content)
            st.write(content + ' = ' + str(result))
        except:
            # 错误输出
            result = '输入错误或除数为零，请检查输入格式与内容'
            st.write(result)

def Image_processor():
    '''图片处理工具'''
    st.write('# 图片处理工具')
    uploaded_file = st.file_uploader('上传图片', type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
            ie = st.toggle('更改大小')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
            st.write('更改图片大小')

        if ie:
            size = st.text_input('请输入大小（不写默认不改动；格式为：宽,高  请用英文半角逗号）')
            try:
                width, height = [int(i) for i in size.split(',')]
                if width < 10:
                    width = 10
                if height < 10:
                    height = 10
            except:
                st.write('输入错误，将不更改大小')
                width, height = img.size
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            if ie:
                img = img_change_ie(img, width, height)
            st.write('右键"另存为"保存图片')
            st.image(img)


def Dictionary():
    '''智慧词典'''
    st.write('# 智慧词典')
    col5, col6 = st.columns([3, 2])
    with col5:
        # 从本地文件中将词典信息读取出来，并存储在列表中
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.readlines()
        words_list = [i.split('#') for i in words_list]
        # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [i[0], i[2]]
        # 从本地文件中将单词的查询次数读取出来，并存储在字典中，格式为“编号：次数”
        with open('check_out_times.json', 'r') as f:
            times_dict = json.load(f)
        # 创建输入框
        word = st.text_input('请输入要查询的单词')
        # 显示查询内容
        if word in words_dict:
            st.write(word)
            n, meaning = words_dict[word]
            st.write(meaning)
            # 查询次数更新
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            # 查询次数储存
            with open('check_out_times.json', 'w') as f:
                json.dump(times_dict, f)
            st.write('查询次数：', times_dict[n])       
            # 彩蛋
            if word == 'Python':
                st.code('''
                        # 恭喜你触发彩蛋，这是一行Python代码
                        print('hello world')
                        ''')
        elif word:
            col3, col4 = st.columns([3, 2])
            with col3:
                st.write(f'抱歉，暂时没有您想查询的单词{word}')
            with col4:
                st.link_button(f'去百度翻译查询{word}', f'https://fanyi.baidu.com/mtpe-individual/multimodal?query={word}&lang=en2zh')
            st.write('')
            request = st.text_input(f'想要反馈？请输入单词{word}的词性及意思，点击按钮提交反馈')
            col1, col2 = st.columns([1, 5])
            with col1:
                if_request = st.button('反馈')
            with col2:
                if if_request:
                    with open('dict_requests.txt', 'a', encoding='utf-8') as f:
                        request = word + '#' + request + '\n'
                        f.write(request)
                    st.write('感谢您的反馈！我们将尽快处理。')
    with col6:
        requests = '''用户反馈单词信息：
        '''
        with open('dict_requests.txt', 'r', encoding='utf-8') as f:
            requests += f.read()
        st.code(requests)

def Web_guide():
    '''网址导航'''
    st.write('# 网址导航')
    st.write('')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.link_button('百度一下', 'https://www.baidu.com/')
        st.write('')
        st.link_button('文件传输助手', 'https://filehelper.weixin.qq.com/')
        st.write('')
    with col2:
        st.link_button('百度图片', 'https://image.baidu.com/')
        st.write('')
        st.link_button('百度网盘', 'https://pan.baidu.com/')
        st.write('')
    with col3:
        st.link_button('Bilibili', 'https://www.bilibili.com/')
        st.write('')
        st.link_button('百度翻译', 'https://fanyi.baidu.com/')
        st.write('')
    with col4:
        st.link_button('编程猫社区', 'https://shequ.codemao.cn/')
        st.write('')
        st.link_button('搜狗搜索', 'https://www.sogou.com/')
        st.write('')

def RGB_designer():
    '''RGB调色板'''
    st.write('# RGB调色板')
    col1, _, col2 = st.columns([5, 1, 2])
    with col1:
        # 设置RGB的值
        r = new_slider('R', '.  ', 0, 255)
        g = new_slider('G', ' . ', 0, 255)
        b = new_slider('B', '  .', 0, 255)
        rgb = (r, g, b)
    with col2:
        # 显示对应颜色
        st.write('')
        st.write('')
        st.write('')
        st.write(' '+str(rgb)+' ')
        img = Image.new('RGBA', (100, 100), rgb)
        st.image(img)


def Message_box():
    '''留言区'''
    col3, col4 = st.columns([1, 1])
    with col4:
        messages_list = load_messages()
        name = st.text_input('我是……')
        new_message = st.text_input('想要说的话……')
        col1, col2 = st.columns([1, 3])
        with col1:
            if_leave_message = st.button('留言')
        with col2:
            if if_leave_message:
                message = [str(int(messages_list[-1][0])+1), name, new_message]
                messages_list.append(message)
                with open('leave_messages.json', 'w', encoding='utf-8') as f:
                    json.dump(messages_list, f)
                st.write('留言成功')
    with col3:
        st.write('# 留言区')
        messages_list = load_messages()
        for i in messages_list:
            display_message(i)

def load_messages():
    with open('leave_messages.json', 'r', encoding='utf-8') as f:
        messages_list = json.load(f)
    return messages_list

def display_message(i):
    if i[1] == 'Liu':
        with st.chat_message('🌞'):
            st.write('站长 : ' + i[2])
    else:
        with st.chat_message('🍥'):
            st.text(i[1] + ' : ' + i[2])

def img_change(img, rc=0, gc=0, bc=0):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            rgb = [r, g, b]
            m = rgb.index(max(rgb))
            if rgb[m] >= 200:
                rgb[m] = 255
            else:
                rgb[m] += 55
            r, g, b = rgb
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

def img_change_ie(img, width, height):
    img = img.resize((width, height))
    return img

def new_slider(label, _, min=0, max=100, origin=None):
    if origin == None:
        origin = min
    col1, col2 = st.columns([1, 9])
    with col1:
        st.write('')
        st.write('')
        st.write(label)
    with col2:
        slider = st.slider(_, min, max, origin)
    return slider

def check_date():
    time_dict = time.localtime(time.time())
    year, month, day = time.strftime('%Y#%m#%d', time_dict).split('#')
    if month == '10' and day == '01':
        return 'ND'
    if month == '04' and day == '01':
        return 'AFD'
    if month == '07' and day == '23':
        return f'WBD{str(int(year)-2024)}'
    else:
        return '-'.join([year, month, day])

def main():
    page = st.sidebar.radio('我的主页', ['首页', '我的兴趣推荐', '计算器', '图片处理工具', '智慧词典', '网址导航', 'RGB调色板', '留言区'])

    if page == '首页':
        Home()
    elif page == '我的兴趣推荐':
        Hobbies()
    elif page == '计算器':
        Calculator()
    elif page == '图片处理工具':
        Image_processor()
    elif page == '智慧词典':
        Dictionary()
    elif page == '网址导航':
        Web_guide()
    elif page == 'RGB调色板':
        RGB_designer()
    elif page == '留言区':
        Message_box()
        
    if check_date() == 'ND':
        st.write('----------------')
        nf = Image.open('China.jpg')
        nf = nf.resize((300, 200))
        st.image(nf)
    if 'WBD' in check_date():
        y = int(chech_date()[3:])
        st.write('----------------')
        st.write(f'祝贺建站{str(y)}周年！')

    st.write('----------------')
    with open('bgm.mp3', 'rb') as f:
        bgm = f.read()
    st.write('BGM:霞光')
    st.audio(bgm, format='audio/mp3', start_time=0)


main()
