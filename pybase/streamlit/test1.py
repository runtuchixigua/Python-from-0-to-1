import streamlit as st

st.title('跟狗哥玩猜拳')

st.image('D:\PyCharmproject\Python-from-0-to-1\pybase\文件操作\dog.png')

import random

def rock_paper_scissors():
    options = ["石头", "剪刀", "布"]
    user_choice = st.selectbox("请选择你的出拳：", options)
    computer_choice = random.choice(options)

    st.write(f"你选择了：{user_choice}")
    st.write(f"电脑选择了：{computer_choice}")

    if user_choice == computer_choice:
        st.write("平局！但是狗哥稳稳压你一头")
    elif (user_choice == "石头" and computer_choice == "剪刀") or (user_choice == "剪刀" and computer_choice == "布") or (user_choice == "布" and computer_choice == "石头"):
        st.write("你虽然赢了！但是狗哥并不服气")
    else:
        st.write("狗哥赢了你，并通便了你一顿！")



def generate_prediction():
    predictions = ["今天你会有好运", "可能会遇到小挑战，但能克服", "将有惊喜等着你", "需小心处理人际关系"]
    return random.choice(predictions)



import streamlit as st
import random

# 定义扑克牌的牌面和花色
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def draw_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return f"{rank}{suit}"


import random
import streamlit as st


def main1():
    st.title("猜数字游戏")
    number_to_guess = random.randint(1, 100)
    guess = st.number_input("请输入你的猜测 (1-100):", min_value=1, max_value=100)

    if st.button("提交"):
        if guess == number_to_guess:
            st.success(f"恭喜！你猜对了！数字是 {number_to_guess}")
        elif guess < number_to_guess:
            st.warning("你太小了！再试一次。")
        else:
            st.error("你太大了！再试一次。")


import streamlit as st

# 定义游戏地图
map_layout = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '.', '#', '#'],
    ['#', '.', 'B', '.', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

# 玩家初始位置
player_pos = (1, 1)

# 游戏逻辑函数
def move_player(direction):
    global player_pos
    new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
    # 处理移动逻辑

# Streamlit 界面
def main2():
    st.title("推箱子游戏")
    for row in map_layout:
        st.write(' '.join(row))
    # 添加用户输入组件，如按钮
    if st.button("上"):
        move_player((-1, 0))
    if st.button("下"):
        move_player((1, 0))
    if st.button("左"):
        move_player((0, -1))
    if st.button("右"):
        move_player((0, 1))


def main():

    rock_paper_scissors()

    st.title("狗哥会占卜")

    if st.button("狗哥亲吻了你，并给你占卜"):
        prediction = generate_prediction()
        st.write(prediction)

    st.title("狗狗抽扑克游戏")

    if st.button("抽一张牌"):
        card = draw_card()
        st.write(f"您抽到的牌是：{card} ，请给狗哥的主人转5￥")


    main1()
    main2()

if __name__ == "__main__":
    main()