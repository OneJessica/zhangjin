import streamlit as st
import time
import pandas as pd
import streamlit.components.v1 as components
st.set_page_config(
    page_title='jessica',
    page_icon=':shark',
layout = 'wide'
)
st.sidebar.title('Home')

st.title("Jessica's Home")
placeholder = st.sidebar.empty()
placeholder.text('hello')

if st.sidebar.button('Email to me'):
    placeholder.text('janezhangbest@outlook.com')
    
from glob import glob


path = '/Users/jessicazhang/Desktop/Video/'
col1,col2 = st.columns(2)
with col1:
    st.image('images/bys.png')
with col2:
    text = st.text_input('你的名字是 ')
    st.text(f'你好👋{text}')
    choice = st.radio('你的状态是',('happy','sad','not moody'),horizontal = True)
    if choice == 'happy':
        st.write('继续保持!')
    if choice == 'sad':
        st.write('做人就是需要开心嘛😄想开点～')
    if choice == 'not moody':
        st.write('道可道，非常道')


#     with st.expander('See data'):
#         @st.experimental_memo
#         def get_data():
#             df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
#             return df
#         df = get_data()
#         st.dataframe(df,height = 400,width = 1000,)
#         # st.experimental_show(df)
#         choice = st.radio('列分布',df.columns,horizontal = True)
#         st.bar_chart(df[choice])
#         # if choice == 'happy':
#         #     st.write('a great day!')
#     with st.expander('看电影'):
#         filepaths = glob(f'{path}/*')
#         filepath = st.selectbox('请选一个类别',[i.split('/')[-1]for i in filepaths])
#         if filepath:
#             filenames = glob(f'{path}/{filepath}/*')
#             filename = st.selectbox('请选一个视频',[i.split('/')[-1]for i in filenames])
#             if filename:
#                 video_file = open(f'{path}/{filepath}/{filename}','rb')
#                 video_byte = video_file.read()
#                 st.video(video_byte)

    # def form_callback():
    #     st.write(st.session_state.my_slider)
    #     st.write(st.session_state.my_checkbox)

    # with st.form(key='form'):
    #     slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    #     checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    #     submit_button = st.form_submit_button(label='Submit', on_click=form_callback)


    with st.expander('照照片'):


        picture = st.camera_input("Take a picture")

        if picture:
            st.image(picture)
            st.download_button('下载图片',data = picture,file_name = '我的自拍.jpg',)
    with st.expander('搜索一下'):
       components.iframe('https://www.fwfly.com/',height = 1000,scrolling = True) 
    with st.expander('搜电影'):
        components.iframe('https://yyets.dmesg.app',height = 1000,scrolling = True)
    with st.expander('阿里云盘'):
        components.iframe('https://www.aliyundrive.com/drive/folder/635dfdf85f0e6a6dc4ff48919db2be99d960dd98',
        height = 1000,scrolling = True)
st.sidebar.snow()
