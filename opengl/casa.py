from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Função callback de redesenho da janela de visualização
def Desenha():
	# Limpa a janela de visualização com a cor  
	# de fundo definida previamente
	glClear(GL_COLOR_BUFFER_BIT)

	# Desenha uma casinha composta de um quadrado e um triângulo

	# Altera a cor do desenho para azul
	glColor3f(0.0, 0.0, 1.0)     
	# Desenha a casa
	glBegin(GL_QUADS)
	glVertex2f(-15.0,-15.0)
	glVertex2f(-15.0,  5.0)       
	glVertex2f( 15.0,  5.0)       
	glVertex2f( 15.0,-15.0)
	glEnd()

	# Altera a cor do desenho para branco
	glColor3f(1.0, 1.0, 1.0)  
	# Desenha a porta e a janela  
	glBegin(GL_QUADS)
	glVertex2f(-4.0,-14.5)
	glVertex2f(-4.0,  0.0)       
	glVertex2f( 4.0,  0.0)       
	glVertex2f( 4.0,-14.5)       
	glVertex2f( 7.0,-5.0)
	glVertex2f( 7.0,-1.0)       
	glVertex2f(13.0,-1.0)       
	glVertex2f(13.0,-5.0)             
	glEnd()

	# Altera a cor do desenho para azul
	glColor3f(0.0, 0.0, 1.0)     
	# Desenha as "linhas" da janela  
	glBegin(GL_LINES)      
	glVertex2f( 7.0,-3.0)      
	glVertex2f(13.0,-3.0)       
	glVertex2f(10.0,-1.0)    
	glVertex2f(10.0,-5.0)             
	glEnd()    

	# Altera a cor do desenho para vermelho
	glColor3f(1.0, 0.0, 0.0) 
	# Desenha o telhado
	glBegin(GL_TRIANGLES)
	glVertex2f(-15.0, 5.0)   
	glVertex2f(  0.0,17.0)    
	glVertex2f( 15.0, 5.0)       
	glEnd()
 
	# Executa os comandos OpenGL 
	glFlush()

# Função callback chamada quando o tamanho da janela é alterado 
def AlteraTamanhoJanela(w, h):
	largura = 0
	altura = 0

	# Evita a divisao por zero
	if(h == 0):
		h = 1

	# Atualiza as variáveis
	largura = w
	altura = h

	# Especifica as dimensões da Viewport
	glViewport(0, 0, largura, altura)

	# Inicializa o sistema de coordenadas
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	# Estabelece a janela de seleção (esquerda, direita, inferior, 
	# superior) mantendo a proporção com a janela de visualização
	if (largura <= altura):
		gluOrtho2D (-40.0, 40.0, -40.0*altura/largura, 40.0*altura/largura)
	else:
		gluOrtho2D (-40.0*largura/altura, 40.0*largura/altura, -40.0, 40.0)

# Função callback chamada para gerenciar eventos de teclas
def Teclado (key, x, y):
	if (ord(key) == 27):
		exit(0)

# Função responsável por inicializar parâmetros e variáveis
def Inicializa ():
	# Define a cor de fundo da janela de visualização como branca
	glClearColor(1.0, 1.0, 1.0, 1.0)

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
	glutCreateWindow("Desenho de uma casa")

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
