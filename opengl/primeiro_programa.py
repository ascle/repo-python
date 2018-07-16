from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def desenha():
	# limpa a janela de visualização com a cor branca
	glClearColor(1,1,1,0)
	glClear(GL_COLOR_BUFFER_BIT)

	# define a cor de desenho vermelho
	glColor3f(1,0,0)

	# desenha um triangulo no centro da janela
	glBegin(GL_TRIANGLES)
	glVertex3f(-0.5,-0.5,0)
	glVertex3f(0,0.5,0)
	glVertex3f(0.5,-0.5,0)
	glEnd()
	# executa  os comandos opengl
	glFlush()

# NAO TA FUNCIONANDO
def teclado(key, x, y):
	if(key==27):
		exit(0)

# FUNÇÃO RESPONSÁVEL POR INICIALIZAR PARAMETROS E VARIAVEIS
def inicializa():
	# Define a janela de visualização 2D
	glMatrixMode(GL_PROJECTION)
	# exibição bidimensional
	gluOrtho2D(-1.0,1.0,-1.0,1.0)
	glMatrixMode(GL_MODELVIEW)

if __name__ == '__main__':
	glutInit()
	# GLUT_SINGLE - apenas um buffer de cor -> glFlush
	# GLUT_DEPTH - imagens em tres dimensoes
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(640,480)
	glutCreateWindow("Poligono")    
	glutDisplayFunc(desenha)
	glutKeyboardFunc(teclado)
	inicializa()
	glutMainLoop()