from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

fAspect = 0

# Função callback de redesenho da janela de visualização
def Desenha():
	# Limpa a janela de visualização com a cor  
	# de fundo definida previamente
	glClear(GL_COLOR_BUFFER_BIT)

	# Altera a cor do desenho para preto
	glColor3f(0.0, 0.0, 0.0)

	# Função da GLUT para fazer o desenho de um cubo 
	# com a cor corrente
	glutWireCube(50)

	# Executa os comandos OpenGL
	glFlush()


# Função usada para especificar o volume de visualização
def EspecificaParametrosVisualizacao():
	# Especifica sistema de coordenadas de projeção
	glMatrixMode(GL_PROJECTION)
	# Inicializa sistema de coordenadas de projeção
	glLoadIdentity()

	# Especifica a projeção perspectiva(angulo,aspecto,zMin,zMax)
	gluPerspective(60,fAspect,0.5,500)

	# Especifica sistema de coordenadas do modelo
	glMatrixMode(GL_MODELVIEW)
	# Inicializa sistema de coordenadas do modelo
	glLoadIdentity()

	# Especifica posição do observador e do alvo
	gluLookAt(40,60,100, 0,0,0, 0,1,0)


# Função callback chamada quando o tamanho da janela é alterado 
def AlteraTamanhoJanela(w, h):
	# Para previnir uma divisão por zero
	if ( h == 0 ):
		h = 1

	# Especifica as dimensões da viewport
	glViewport(0, 0, w, h)
 
	# Calcula a correção de aspecto
	global fAspect 
	fAspect = w/h

	EspecificaParametrosVisualizacao()


# Função callback chamada para gerenciar eventos de teclas
def Teclado (key, x, y):
	if (ord(key) == 27):
		exit(0)


# Função responsável por inicializar parâmetros e variáveis
def Inicializa ():
	# Define a cor de fundo da janela de visualização como branca
	glClearColor(1.0, 1.0, 1.0, 1.0)
	glLineWidth(2.0)


# Programa Principal 
def Main():
	# Define do modo de operação da GLUT
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 

	# Especifica a posição inicial da janela GLUT
	glutInitWindowPosition(5,5) 

	# Especifica o tamanho inicial em pixels da janela GLUT
	glutInitWindowSize(450,450) 
 
	# Cria a janela passando como argumento o título da mesma
	glutInit(sys.argv)
	glutCreateWindow("Desenho de um cubo")

	# Registra a função callback de redesenho da janela de visualização
	glutDisplayFunc(Desenha)

	# Registra a função callback de redimensionamento da janela de visualização
	glutReshapeFunc(AlteraTamanhoJanela)

	# Registra a função callback para tratamento das teclas ASCII
	glutKeyboardFunc (Teclado)

	# Chama a função responsável por fazer as inicializações 
	Inicializa()
 
	# Inicia o processamento e aguarda interações do usuário
	glutMainLoop()


if __name__ == '__main__':
	Main()