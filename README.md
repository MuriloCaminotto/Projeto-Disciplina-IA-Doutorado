# Projeto-Disciplina-IA-Doutorado
Códigos e modelos criados para o projeto final da disciplina de IA

Este projeto é compostos pelos seguintes arquivos:  

  1) criaCSV  
    Este arquivo contem o código necessário para criar um arquivo .csv com os descritorres HOGs de acordo com o formato desejado.  
    Este processo é feito de acordo com os seguintes parâmetros:  
      'filenameout' -> Nome do arquivo .csv que sera gerado  
      'pathPos' -> Caminho para a pasta com as imagens da classe positiva  
      'extPos' -> Tipo de extensao das imagens positivas (.png, .jpg...)  
      'pathNeg' -> Caminho para a pasta com as imagens da classe negativa  
      'extNeg' -> Tipo de extensao das imagens negativas (.png, .jpg...)  
      'ori' -> Numero de orientacoes do HOG  
      'cell' -> Numero de pixeis por celula do HOG  
      'block' -> Numero de celulas por bloco do HOG  
      'method' -> Tipo do metodo aplicado a imagem, por padrao vazio  
        Caso "full" Aplica transformacao de contrate com variaveis globais de std e media  
        Caso "bin" aplica binarizacao nas imagens  
        Caso "equ" aplica equailizacao nas imagens  
        Qualquer combinacao dos 3 parametros pode ser feita atraves da separacao por "-" (full-equ-bin)  
        
  2)  treinaModelo  
    Este arquivo contem o código para treinar um modelo baseado em um arquivo csv de descritores HOG
    Este processo é feito de acordo com os seguintes parâmetros:
      'db' -> Caminho para o arquivo csv  
      'modelName' -> Nome do modelo que será gerado (sem extensão)  
      'model' -> Tipo do modelo a ser utilizado. Por padrão = 'svm'  
        Caso 'svm' treina com uma SVM de kernel RBF  
        Caso 'sigmoid' treina com uma SVM de kernel sigmoid  
        Caso 'rf' treina com uma Random Forest  
      
  3)    ProcessamentoImagem  
    Este arquivo contem o código para aplicar um modelo já treinado em uma imagem qualquer em busca de padrões de folhas de soja  
    Este processo é feito de acordo com os seguintes parâmetros  
      'path2img' -> Caminho para a imagem a ser analisada  
      'path2clf' -> Caminho para o modelo já treinado  
      'path2result' -> Caminho onde será escrita a imagem  
      'ori' -> Numero de orientacoes do HOG  
      'cell' -> Numero de pixeis por celula do HOG  
      'block' -> Numero de celulas por bloco do HOG  
      'method' -> Tipo do metodo aplicado a imagem, por padrao vazio  
        Caso "full" Aplica transformacao de contrate com variaveis globais de std e media  
        Caso "bin" aplica binarizacao nas imagens  
        Caso "equ" aplica equailizacao nas imagens  
        Qualquer combinacao dos 3 parametros pode ser feita atraves da separacao por "-" (full-equ-bin)  
      OBS: Os parâmetros ori,cell,block e method devem estar de acordo com os utilizados para o treinamendo do modelo carregado  
      'tamanhos' -> Tamanhos dos recortes que serão utilizados para encontrar regiões de folha na image,. Por padrão = [32,64,128,384]  

Além dos arquivo de código, também estão disponíveis todos os modelos treinados no arquivo .zip

Devido ao tamanho dos arquivos .csv, eles estarão disponíveis através do link https://drive.google.com/drive/folders/1b890HxVXUXS_WZ1zRq3aHx8vwwcVqQyw?usp=sharing 
