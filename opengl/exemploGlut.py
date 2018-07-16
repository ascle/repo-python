from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

glutColor = 0
glutPrimitiva = 0

# Função callback de redesenho da janela de visualização
def Desenha():
	print("")
	print("")
	print("Calback de redesenho de tela")

	

	# Define a cor de fundo de tela
	# vermelho
	if(glutColor == 0):
		glClearColor(1.0, 0.0, 0.0, 1.0)
	# verde	
	elif(glutColor == 1):
		glClearColor(0.0, 1.0, 0.0, 1.0)
	# azul	
	else:
		glClearColor(0.0, 0.0, 1.0, 1.0)

	glClear(GL_COLOR_BUFFER_BIT)

	# Define a primitiva
	# quadrado
	if(glutPrimitiva == 0):
		glutWireCube(1.0)
	# triangulo
	elif(glutPrimitiva == 1):
		glutWireSphere(1.0, 25, 25)
		print("t")
	# losango
	else:
		glutSolidCone(0.3, 1.1, 20, 20)
		print("l")
		
	
	glutSwapBuffers()

#def Altera_tamanho_janela(GLsizei w, GLsizei h):
def AlteraTamanhoJanela(w, h):
	print("*** Callback de redimensionamento da tela\n")
	print(">>> Novo tamanho da janela: {} x {}".format( w, h))

def Teclado(tecla, x, y):
	modificadores = 0
	print("*** Tratamento de teclas comuns")
	print(">>> Tecla: {}".format(tecla))

	if (ord(tecla) == 27):
		exit(0)

	# muda para tela cheia - a
	if (ord(tecla) == 97):
		glutFullScreen()
	# muda posição da janela - A
	if (ord(tecla) == 65):
		glutReshapeWindow(500,400) 
		glutPositionWindow(100,100)
	
	# Trata SHIFT, CTRL e ALT
	modificadores = glutGetModifiers()
	if (modificadores & GLUT_ACTIVE_SHIFT):
		print("(SHIFT pressionado)")
	if (modificadores & GLUT_ACTIVE_CTRL):
		print("(CTRL pressionado)")
	if (modificadores & GLUT_ACTIVE_ALT):
		print("(ALT pressionado)")

# Função callback chamada para gerenciar eventos de teclas especiais(F1,PgDn,...)
def TeclasEspeciais (tecla, x, y):
	print("*** Tratamento de teclas especiais")
	if(tecla == GLUT_KEY_F1):
		print(">>> Tecla F1 pressionada")
	elif(tecla == GLUT_KEY_F2):
		print(">>> Tecla F2 pressionada")
	elif(tecla == GLUT_KEY_F3):
		print(">>> Tecla F3 pressionada")

# Função que trata a opção selecionada do menu principal
def MenuPrincipal(op):
	print("*** Menu principal!")

# Função callback chamada quando são notificados os eventos do mouse
def GerenciaMouse (button, state, x, y):
	print("*** Tratamento de Cliques de mouse")
	if (state == GLUT_DOWN):
		print(">>> Botao {} pressionado".format(button))
	if (state == GLUT_UP):
		print(">>> Botao {} liberado".format(button))


# Função que trata a opção selecionada do menu "Primitiva"
def MenuPrimitiva(op):
	op = int(op)
	print("*** Menu PRIMITIVA: ")	
	if(op == 0):
		print("Opcao QUADRADO")
	elif(op == 1):
		print("Opcao TRIANGULO")
	elif(op == 2):
		print("Opcao LOSANGO")

	global glutPrimitiva
	glutPrimitiva = op
	glutPostRedisplay()
	return 0

# Função que trata a opção selecionada do menu "Cor"
def MenuCor(op):
	op = int(op)
	print("*** Menu COR: ")
	if(op == 0):
		print("Opcao VERMELHO")
	elif(op == 1):
		print("Opcao VERDE")
	elif(op == 2):
		print("Opcao AZUL")
	
	global glutColor
	glutColor = op
	glutPostRedisplay()
	return 0
	
# Função responsável por criar os menus
def CriaMenu():
	menu = 0
	submenu1 = 0
	submenu2 = 0

	# Cria submenu para seleção de cor
	submenu1 = glutCreateMenu(MenuCor)
	glutAddMenuEntry("Vermelho",0)
	glutAddMenuEntry("Verde",1)
	glutAddMenuEntry("Azul",2)

	# Cria submenu para seleção de primitiva
	submenu2 = glutCreateMenu(MenuPrimitiva)
	glutAddMenuEntry("Quadrado",0)
	glutAddMenuEntry("Triângulo",1)
	glutAddMenuEntry("Losango",2)

	# Cria menu principal...
	menu = glutCreateMenu(MenuPrincipal)
	# ... e adiciona ambos submenus a ele
	glutAddSubMenu("Cor",submenu1)
	glutAddSubMenu("Primitivas",submenu2)

	# Associa o menu ao botão direito do mouse
	glutAttachMenu(GLUT_RIGHT_BUTTON)
	return 0

# Programa Principal
def main():
	# Define do modo de operação da GLUT
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB )

	# Especifica a posição inicial da janela GLUT
	glutInitWindowPosition(0,0)

	# Especifica o tamanho inicial em pixels da janela GLUT
	glutInitWindowSize(500,400)

	# Cria a janela passando como argumento o título da mesma
	glutInit(sys.argv)
	glutCreateWindow("Programa de Teste da GLUT")

	# Registra a função callback de redesenho da janela de visualização
	glutDisplayFunc (Desenha)

	# Registra a função callback de redimensionamento da janela de visualização
	glutReshapeFunc (AlteraTamanhoJanela)

	# Registra a função callback para tratamento das teclas ASCII
	glutKeyboardFunc (Teclado)

	# Registra a função callback que gerencia os eventos do mouse   
	glutMouseFunc (GerenciaMouse)

	# Registra a função callback para tratamento das teclas especiais
	glutSpecialFunc (TeclasEspeciais)

	# Chama função para criar o menu
	CriaMenu()

	# Inicia o processamento e aguarda interações do usuário
	glutMainLoop()


if __name__ == '__main__':
	main()

