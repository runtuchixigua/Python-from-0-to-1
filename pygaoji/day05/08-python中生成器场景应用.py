import math
def data_loader(batch_size):
    with open('jaychou_lyrics.txt','r',encoding='utf-8') as f:
        lines = f.readlines()

    data_len = len(lines)

    batch_num = math.ceil(data_len/batch_size)

    for idx in range(batch_num):
        yield lines[idx*batch_size:(idx+1)*batch_size]

if __name__ == '__main__':
    loader = data_loader(4)
    for data in loader:
        print(data)

