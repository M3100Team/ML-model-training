import os
from PIL import Image
import numpy as np
from random import randint, choice
FALSE_IMAGES_COUNT = 5000
TRUE_IMAGES_COUNT = 500


def paste_symb(x, y, x1, y1, paper, im, rm=170, gm=170, bm=170):
    delta = randint(-5, 5)
    im = im.resize((x1 - x + delta, y1 - y + delta))
    px = im.load()
    for i in range(x1 - x + delta):
        for j in range(y1 - y + delta):
            if px[i, j][0] < rm and px[i, j][1] < gm and px[i, j][2] < bm:
                paper[x + i, y + j] = px[i, j]


def generate_symb(x, y, paper):
    if randint(0, 2) == 0:
        os.chdir('-')
        im = Image.open(choice(os.listdir()))
        im = im.convert('RGB')
        paste_symb(x, y, x + 15, y + 15, paper, im)
        x += 10
        os.chdir('..')
    digit = randint(0, 9)
    os.chdir(str(digit))
    im = Image.open(choice(os.listdir()))
    im = im.convert('RGB')
    paste_symb(x, y, x + 40, y + 40, paper, im)
    os.chdir('..')


def paste_matrix(rows, columns, x, y, paper):
    # print(os.getcwd())
    os.chdir('(')
    im = Image.open(choice(os.listdir()))
    im = im.convert('RGB')
    delt_x = im.size[0] * (rows * 45 // im.size[1])
    paste_symb(x, y, x + delt_x, y + rows * 40, paper, im)
    x += 80
    os.chdir('..')
    for i in range(rows):
        for j in range(columns):
            generate_symb(x + j * 45, y + i * 45, paper)
    x += 20
    os.chdir(')')
    im = Image.open(choice(os.listdir()))
    im = im.convert('RGB')
    paste_symb(x + 45 * (columns - 1), y, x + 45 * (columns - 1) + delt_x,
               y + rows * 45, paper, im)
    os.chdir('..')


def false_data_generation():
    if not os.path.isdir('dataset_false'):
        os.mkdir('dataset_false')
    os.chdir('raw_data')
    os.chdir('natural_images')
    ways = np.array([])
    for i in os.listdir():
        os.chdir(i)
        for j in os.listdir():
            ways = np.append(ways, i + '\\' + j)
        os.chdir('..')
    np.random.shuffle(ways)
    os.chdir('..')
    os.chdir('..')
    for i in range(min(FALSE_IMAGES_COUNT, len(ways))):
        im = Image.open('raw_data\\natural_images\\' + ways[i])
        out = im.resize((500, 500))
        out.save('dataset_false\\im' + str(i) + '.png')


def true_data_generation():
    if not os.path.isdir('dataset_true'):
        os.mkdir('dataset_true')
    for i in range(TRUE_IMAGES_COUNT):
        os.chdir('raw_data')
        os.chdir('paper')
        paper = Image.open(choice(os.listdir()))
        paper = paper.convert('RGB')
        paper_copy = paper
        paper_copy = paper_copy.resize((1000, 1000))
        px = paper_copy.load()
        os.chdir('..')
        rows = randint(1, 6)
        columns = randint(1, 6)
        written = False
        for j in range(100, paper_copy.size[1] - 200, rows * 50 + 35):
            for g in range(100, paper_copy.size[0] - 200, columns * 70 + 35):
                try:
                    paste_matrix(rows, columns, g, j, px)
                except IndexError:
                    os.chdir('..')
                except:
                    os.chdir('C:\\Users\\eugen\\Downloads\\ML_model_training\\raw_data')
                else:
                    written = True
        if written:
            os.chdir('..')
            os.chdir('dataset_true')
            paper_copy = paper_copy.resize((500, 500))
            paper_copy.save(str(i) + '.png')
            os.chdir('..')


false_data_generation()
true_data_generation()

