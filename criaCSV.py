import cv2 
import glob 
from skimage import exposure
from skimage import feature
import numpy as np

#Caclulados a partir das 65 mil imagens positivas
MEDIAGLOBAL = 73.8515
STDGLOBAL   = 33.5265


def aplyFullTransform(img):
    equ = cv2.equalizeHist(img)
    
    #cria tabela vazia
    lookUpTable = np.empty((1,256), np.uint8)

    #Calculo dos fatores de padronizacao
    mi   = np.mean(equ)
    stdi = np.std(equ)

    A = stdi/STDGLOBAL
    B = mi - A*MEDIAGLOBAL
    
    #calcula os valores para a tabela de lookup
    for i in range(256):
        lookUpTable[0,i] = np.clip(A*i+B, 0, 255)

    #aplica a transformacao
    res = cv2.LUT(img,lookUpTable)

    return res


def parametros():
    print('filenameout -> Nome do arquivo .csv que sera gerado')
    print('pathPos -> Caminho para a pasta com as imagens da classe positiva')
    print('extPos -> Tipo de extensao das imagens positivas (.png, .jpg...)')
    print('pathNeg -> Caminho para a pasta com as imagens da classe negativa')
    print('extNeg > Tipo de extensao das imagens negativas (.png, .jpg...)')
    print('ori -> Numero de orientacoes do HOG')
    print('cell -> Numero de pixeis por celula do HOG')
    print('block -> Numero de celulas por bloco do HOG')
    print('method -> Tipo do metodo aplicado a imagem, por padrao vazio.')
    print('Caso "full" Aplica transformacao de contrate com variaveis globais de std e media')
    print('Caso "bin" aplica binarizacao nas imagens')
    print('Caso "equ" aplica equailizacao nas imagens')
    print('Qualquer combinacao dos 3 parametros pode ser feita atraves da separacao por "-" (full-equ-bin)')

def criaCSV(filenameout,pathPos,extPos,pathNeg,extNeg,ori,cell,block,method=''):
     
    files = glob.glob(pathPos+'*'+extPos)

    img = cv2.imread(files[0], cv2.IMREAD_GRAYSCALE)

    fd = feature.hog(img, orientations=ori, pixels_per_cell=(cell, cell),
        cells_per_block=(block, block), transform_sqrt=True, block_norm="L1",
        visualize=False)

    filename = filenameout 
    counter = 0
    with open(filename,'w') as f:
        #constroi cabecalho
        for i in range(len(fd)):
            f.write('hog-'+str(i)+',')
        f.write('target\n')

        path = pathPos
        files = glob.glob(pathPos+'*'+extPos)
        #cria classe positiva
        for file in files:
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            for m in method.split('-'):
                if m == 'full':
                    img = aplyFullTransform(img)
                elif m == 'bin':
                    img,_ = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                elif m == 'equ':
                    img = cv2.equalizeHist(img)

            fd = feature.hog(img, orientations=ori, pixels_per_cell=(cell,cell),
                cells_per_block=(block,block), transform_sqrt=True, block_norm="L1",
                visualize=False)
            descritores = ','.join([str(x) for x in fd])+',1\n'
            f.write(descritores)
            print('Total de imagens processadas -> ',counter)
            counter+=1
        #Carrega classe negativa
        path = pathNeg
        files = glob.glob(pathNeg+'*'+extNeg)
        #cria classe negativa
        for file in files:
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            for m in method.split('-'):
                if m == 'full':
                    img = aplyFullTransform(img)
                elif m == 'bin':
                    img,_ = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                elif m == 'equ':
                    img = cv2.equalizeHist(img)

            fd = feature.hog(img, orientations=ori, pixels_per_cell=(cell,cell),
                cells_per_block=(block, block), transform_sqrt=True, block_norm="L1",
                visualize=False)
            descritores = ','.join([str(x) for x in fd])+',0\n'
            f.write(descritores)
            print('Total de imagens processadas -> ',counter)
            counter+=1



        