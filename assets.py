import random as rd
import emoji

def WinImages():
    dict_win = [
        "https://pbs.twimg.com/media/CLytB7WWgAALf8B.jpg",
        "https://i.kym-cdn.com/photos/images/original/000/574/640/ddf.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_fe-QxC1KN01OSWJmUtODDMLhuZiHq0i6Xg&usqp=CAU"
    ]
    return rd.choice(dict_win)

def LoseImages():
    dict_lose = [
        "https://i.kym-cdn.com/photos/images/original/001/166/089/485.jpg",
        "https://media.makeameme.org/created/sorry-you-lose.jpg",
        "https://static.vecteezy.com/system/resources/thumbnails/018/885/244/small/black-star-badge-you-lose-game-award-icon-for-2d-png.png"
    ]
    return rd.choice(dict_lose)

def DrawImages():
    dict_draw = [
        "https://i.redd.it/wjk9tukitag41.jpg",
        "https://preview.redd.it/bekphnqftcb41.jpg?auto=webp&s=26c9684c7326870bfa6680be462341be38bb0635",
        "https://images.inc.com/uploaded_files/image/1920x1080/getty_487252293_112166.jpg",
    ]
    return rd.choice(dict_draw)

emoji_list = {
    'libra': emoji.emojize(":libra:"),
    'information': emoji.emojize(":round_pushpin:"),
    'person': emoji.emojize(":bust_in_silhouette:"),
    'game': emoji.emojize(":video_game:"),
    'rock': emoji.emojize(":raised_fist:"),
    'paper': emoji.emojize(":hand_with_fingers_splayed:"),
    'scissors': emoji.emojize(":victory_hand:"),
}