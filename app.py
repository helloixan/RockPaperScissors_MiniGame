import streamlit as st
import random as rd
import time
from prediction import predict_image, conver_to_img
from assets import WinImages, LoseImages, DrawImages, emoji_list


score = 0

def about_us() :
    st.title("Tentang Kami")
    st.image("./images/about_us.png")
    # developer = {'dev1': ["Iksan Oktav Risandy", "1302223042", "https://media.licdn.com/dms/image/D5603AQF2GdU6S_us0Q/profile-displayphoto-shrink_800_800/0/1676416271725?e=1709769600&v=beta&t=id_JEpdyXcIFWhjf_pfar7VX89aJZ2sm5YkEWIghY-U"],
    #              'dev2': ["Zaky Al Fatih Nata Imam", "1301223172", "https://media.licdn.com/dms/image/D5603AQFnW7GD8n_niw/profile-displayphoto-shrink_800_800/0/1669208004343?e=1709769600&v=beta&t=lsIoX-ScJV0xAtNJ1w0ub0075dZJVWcDjB-j4D_OwlQ"],
    #              'dev3': ["Muhammad Ghozy Abdurrahman", "103012330264", "https://media.licdn.com/dms/image/D5603AQHQByjIOZzp_w/profile-displayphoto-shrink_800_800/0/1676005912660?e=1709769600&v=beta&t=f77K9mlIeEJnB1rxZe93peDHl-9vwI6X9SMKafcsPOg"],
    #              }
    # for dev in developer:
    #     st.image(developer[dev][2],caption=f"Nama: {developer[dev][0]},\tNIM: {developer[dev][1]}", width=500)

def convert_choice(choice) :
    if choice == "paper" :
        return emoji_list["paper"]
    elif choice == "rock" :
        return emoji_list["rock"]
    else :
        return emoji_list["scissors"]

def informasi() :
    st.title("Rock Paper Scissors Game")
    st.header(" Tentang Permainan")
    st.write("Rock, Paper, Scissors merupakan permainan sederhana diantara 2 player yang hanya membutuhkan tangan pemain, game ini biasanya bertujuan untuk menentukan pilihan")
    # st.image("https://www.science.org/do/10.1126/science.aac4663/abs/sn-rockpaper.jpg", caption="Rock Paper Scissor")
    st.image("https://cdn.dribbble.com/users/976907/screenshots/4879640/dribbble_13.gif", caption="Rock Paper Scissor")
    st.text("Permainan Rock Paper Scissors pada web ini memiliki prosedur sebagai berikut: \n1. Libra (Komputer) akan memutuskan pilihan terlebih dahulu \n2. Pemain menentukan pilihannya berdasarkan input kamera yang akan ditampilkan \n3. Pemain akan mendapatkan hasil sesuai peraturan permainan beserta skornya")
    st.text("Peraturan permainan : \n1. Rock (Batu) akan kalah terhadap Paper (kertas) \n2. Paper (Kertas) akan kalah terhadap Scissors (gunting) \n3. Scissors (gunting) akan kalah terhadap rock (batu) \n4. Pemain akan mendapatkan hasil SERI jika pilihan kedua pihak sama \nUntuk lebih jelas perhatikan ilustrasi berikut: ")
    st.image("https://andygrunwald.com/images/posts/playing-rock-paper-scissors-with-500-people/rock-paper-scissors-game-rules.png", caption="Peraturan Permainan")
    if st.button("Selengkapnya") :
        st.write("Permainan Rock Paper Scissors dibuat menggunakan algoritma AI dengan bahasa pemrograman python, framework yang digunakan yaitu YOLOv8 untuk pembuatan model klasifikasinya dan Streamlit untuk interface dari permainan ini.")
        st.write("Berikut statistik dari model yang dibuat: ")
        st.image("./runs/classify/train/results.png")

def rules_game(p1, p2, score):
    if (p1 == p2) :
        st.image(DrawImages(), width=500)
        st.write("SERI!")
    elif ((p1 == "paper" and p2 == "rock") or (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper")) :
        st.image(WinImages(), width=500)
        st.write("Kamu Menang!")
        score += 1
    else :
        st.image(LoseImages(), width=500)
        st.write("Kamu Kalah!")
        if score > 0 :
            score -= 1
    return score

def start_game():
    global score
    st.title("Rock Paper Scissors Game")
    nama = st.text_input(label="Nama Pemain", key="input1")
    if nama :
        st.write(f"{emoji_list['libra']}: Hai {nama}! Perkenalkan aku Libra yang akan menjadi lawanmu pada permainan ini!")
        time.sleep(3)
        libra_choice = rd.choice(["rock", "paper", "scissors"])
        # st.write(f"<dev hint> Libra memilih {libra_choice} </>")
        st.write(f"{emoji_list['libra']}: Ok, aku sudah menentukan pilihanku, sekarang giliranmu!")
        time.sleep(3)
        image_player = st.camera_input(label="Tentukan pilihanmu dengan gesture tangan kamu!")
        if image_player :
            img = conver_to_img(image_player)
            player_choice = predict_image(img)
            # st.write(player_choice)
            st.write(f"{emoji_list['libra']}: {convert_choice(libra_choice)}")
            st.text(f"{nama}: {convert_choice(player_choice)}\nHasil:")
            score = rules_game(player_choice, libra_choice, score)
            st.write(f"Score kamu: {score}")
                
            
def sidebar():
    st.sidebar.image("./images/logo_sidebar.png", width=100)
    st.sidebar.title('Menu')
    choice = st.sidebar.radio(label="Pilihan", options=[f"{emoji_list['information']}Informasi", f"{emoji_list['game']}Mulai Permainan", f"{emoji_list['person']}Tentang Kami"])
    if choice == f"{emoji_list['information']}Informasi":
        informasi()
    elif choice == f"{emoji_list['game']}Mulai Permainan" :
        start_game()
    elif choice == f"{emoji_list['person']}Tentang Kami" :
        about_us()

sidebar()