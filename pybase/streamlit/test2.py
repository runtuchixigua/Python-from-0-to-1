import streamlit as st

st.title('My first app')
st.write('Hello, *World!* ')
daca = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]

]
st.table(daca)
st.write('qifei')
'# ajdskkfjals'

data = {
    'name': ['张三', '李四', '王五'],
    'age': [18, 20, 22],
    'address': ['北京', '上海', '广州']
}
st.table(data)
st.dataframe(data)


with st.sidebar:
    st.header('用户注册')


st.number_input('mima:')
st.text_input('name:')
st.radio('性别:', ['男', '女'])
st.date_input('生日:')