import back_stream
if __name__ == '__main__':
    while True:
        sentence = input("search News, what you interested in(if you wanna quit press 0): ")
        if sentence == "0":
            break
        back_stream.predict(sentence)