'''
Carlos Peralta 201314556
'''
import os

class nodoCola():
	def __init__(self, valor):
		self.numero = valor
		self.siguiente = None

class cola():
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.tamano = 0
	
	def encolar(self, val):
		nuevo = nodoCola(val)
		if self.inicio == None:
			self.inicio = nuevo
		else:
			self.fin.siguiente = nuevo
		self.fin = nuevo
		self.tamano += 1
	
	def desencolar(self):
		num = self.inicio.numero		
		self.inicio = self.inicio.siguiente
		self.tamano -= 1		
		return num

	def tamanoCola(self):
		return self.tamano

	def toDot(self):
		with open("C:\Users\Carlos\Desktop\cola.dot", "w") as f:
			f.write("digraph ListaS{\n")
			f.write("label= \"Cola de numeros\"\n")
			f.write("\tnode [fontcolor=\"red\", height=0.5, color=\"black\"]\n")
			f.write("\tedge [color=\"black\", dir=fordware]\n")
			temp = self.inicio
			texto = ""
			texto2 = ""
			if temp != None:
				while temp != None:
					texto = "nodo" + str(id(temp)) + "[label=\"Numero: " + str(temp.numero) + "\"];\n";
					f.write(texto)
					if temp.siguiente != None:
						texto2 = "nodo" + str(id(temp)) + "->nodo" + str(id(temp.siguiente)) + ";\n";
						f.write(texto2)
					temp = temp.siguiente
			f.write("\n}")
		from subprocess import check_call
		check_call(['dot','-Tpng','C:\Users\Carlos\Desktop\cola.dot','-o','C:\Users\Carlos\Desktop\cola.png'])

class nodoPila():
	def __init__(self, val):
		self.numero = val
		self.siguiente = None

class pila():
	def __init__(self):
		self.top = None
		self.tamano = 0

	def push(self, numero):
		nuevo = nodoPila(numero)
		nuevo.siguiente = self.top
		self.top = nuevo
		self.tamano +=1

	def pop(self):
		aux = self.top.numero
		self.top = self.top.siguiente
		return aux

	def toDot(self):
		with open("C:\Users\Carlos\Desktop\pila.dot", "w") as f:
			f.write("digraph Pila{\n")
			f.write("label= \"Pila de numeros\"\n")
			f.write("\tnode [fontcolor=\"red\", height=0.5, color=\"black\"]\n")
			f.write("\tedge [color=\"black\", dir=fordware]\n")
			temp = self.top
			texto = ""
			texto2 = ""
			if temp != None:
				while temp != None:
					texto = "nodo" + str(id(temp)) + "[label=\"Numero: " + str(temp.numero) + "\"];\n";
					f.write(texto)
					if temp.siguiente != None:
						texto2 = "nodo" + str(id(temp)) + "->nodo" + str(id(temp.siguiente)) + ";\n";
						f.write(texto2)
					temp = temp.siguiente
			f.write("\n}")
		from subprocess import check_call
		check_call(['dot','-Tpng','C:\Users\Carlos\Desktop\pila.dot','-o','C:\Users\Carlos\Desktop\pila.png'])

class nodoSimple():
	def __init__(self, val):
		self.palabra = val
		self.siguiente = None	

class listaSimple():
	def __init__(self):
		self.inicio = None
		self.fin = None

	def insertarFinal(self, val):
		if self.inicio != None:
			self.fin.siguiente = nodoSimple(val)
			self.fin = self.fin.siguiente
		else:
			self.inicio = self.fin = nodoSimple(val)

	def eliminarNodo(self, val):
		if self.inicio != None:
			if self.inicio == self.fin and val == self.inicio.palabra:
				self.inicio = self.fin = None
			elif val == self.inicio.palabra:
				self.inicio = self.inicio.siguiente
			else:
				anterior = self.inicio
				temporal = self.inicio.siguiente
				while temporal != None and temporal.palabra != val:
					anterior = anterior.siguiente
					temporal = temporal.siguiente
				if temporal != None:
					anterior.siguiente = temporal.siguiente
					if temporal == self.fin:
						self.fin = anterior

	def toDot(self):
		with open("C:\Users\Carlos\Desktop\listasimple.dot", "w") as f:
			f.write("digraph listaSimple{\n")
			f.write("label= \"Lista de strings\"\n")
			f.write("\tnode [fontcolor=\"red\", height=0.5, color=\"black\"]\n")
			f.write("\tedge [color=\"black\", dir=fordware]\n")
			temp = self.inicio
			texto = ""
			texto2 = ""
			if temp != None:
				while temp != None:
					texto = "nodo" + str(id(temp)) + "[label=\"String: " + str(temp.palabra) + "\"];\n";
					f.write(texto)
					if temp.siguiente != None:
						texto2 = "nodo" + str(id(temp)) + "->nodo" + str(id(temp.siguiente)) + ";\n";
						f.write(texto2)
					temp = temp.siguiente
			f.write("\n}")
		from subprocess import check_call
		check_call(['dot','-Tpng','C:\Users\Carlos\Desktop\listasimple.dot','-o','C:\Users\Carlos\Desktop\listasimple.png'])

	def buscarNodo(self, val):
		temporal = self.inicio
		indice = 0
		while temporal != None and temporal.palabra != val:
			temporal = temporal.siguiente
			indice += 1
		if temporal != None:
			return "El dato se encuentra en el indice " + str(indice)
		else:
			return "No se encontro el dato"

class Nodo_Ortogonal():
	def __init__(self, x, y, stado, mail):
		self.x = x
		self.y = y
		self.mail = mail
		self.estado = stado
		self.arriba = None
		self.abajo = None
		self.izquierda = None
		self.derecha = None

class Lista_Vertical():
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def insertar(self, inserta):
		if self.vacia():
			self.primero = inserta
			self.ultimo = inserta
		else:
			if inserta.y < self.primero.y:
				self.insertaFrente(inserta)
			elif inserta.y > self.ultimo.y:
				self.insertaFinal(inserta)
			else:
				self.insertaMedio(inserta)

	def insertaFrente(self,inserta):
		self.primero.arriba = inserta
		inserta.abajo = self.primero
		self.primero = self.primero.arriba

	def insertaMedio(self, inserta):
		temporal1 = self.primero
		while temporal1.y < inserta.y:
			temporal1 = temporal1.abajo
		temporal2 = temporal1.arriba
		temporal2.abajo = inserta
		temporal1.arriba = inserta
		inserta.abajo = temporal1
		inserta.arriba = temporal2

	def insertaFinal(self, inserta):
		self.ultimo.abajo = inserta
		inserta.arriba = self.ultimo
		self.ultimo = self.ultimo.abajo

	def recorrer(self):
		if not self.vacia():
			temporal = self.primero
			while temporal !=None:
				temporal = temporal.abajo

class Lista_Horizontal():
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def insertar(self, inserta):
		if self.vacia():
			self.primero = inserta
			self.ultimo = inserta
		else:
			if inserta.x < self.primero.x:
				self.insertaFrente(inserta)
			elif inserta.x > self.ultimo.x:
				self.insertaFinal(inserta)
			else:
				self.insertaMedio(inserta)

	def insertaFrente(self,inserta):
		self.primero.izquierda = inserta
		inserta.derecha = self.primero
		self.primero = self.primero.izquierda

	def insertaMedio(self, inserta):
		temporal1 = self.primero
		while temporal1.x < inserta.x:
			temporal1 = temporal1.derecha
		temporal2 = temporal1.izquierda
		temporal2.derecha = inserta
		temporal1.izquierda = inserta
		inserta.derecha = temporal1
		inserta.izquierda = temporal2

	def insertaFinal(self, inserta):
		self.ultimo.derecha = inserta
		inserta.izquierda = self.ultimo
		self.ultimo = self.ultimo.derecha

	def recorrer(self):
		if not self.vacia():
			temporal = self.primero
			while temporal !=None:
				temporal = temporal.derecha

class Nodo_Cabecera():
	def __init__(self, x, mail):
		self.x = x
		self.proveedor = mail
		self.Columna = Lista_Vertical()
		self.siguiente = None
		self.anterior = None

class cabeceras():
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def insertar(self, inserta):
		if self.vacia():
			self.primero = inserta
			self.ultimo = inserta
		else:
			if inserta.x < self.primero.x:
				self.insertaFrente(inserta)
			elif inserta.x > self.ultimo.x:
				self.insertaFinal(inserta)
			else:
				self.insertaMedio(inserta)

	def insertaFrente(self,inserta):
		self.primero.anterior = inserta
		inserta.siguiente = self.primero
		self.primero = self.primero.anterior

	def insertaMedio(self, inserta):
		temporal1 = self.primero
		while temporal1.x < inserta.x:
			temporal1 = temporal1.siguiente
		temporal2 = temporal1.anterior
		temporal2.siguiente = inserta
		temporal1.anterior = inserta
		inserta.siguiente = temporal1
		inserta.anterior = temporal2

	def insertaFinal(self, inserta):
		self.ultimo.siguiente = inserta
		inserta.anterior = self.ultimo
		self.ultimo = self.ultimo.siguiente

	def recorrer(self):
		if not self.vacia():
			temporal = self.primero
			while temporal !=None:
				temporal = temporal.siguiente

	def existe(self, x):
		if self.vacia():
			return False
		else:
			temporal = self.primero
			while temporal != None:
				if temporal.x == x:
					return True
				elif temporal.siguiente == None:
					return False
				temporal = temporal.siguiente
		return False

	def busqueda(self, x):
		if self.existe(x):
			temporal = self.primero
			while temporal.x != x:
				temporal = temporal.siguiente
			return temporal
		else:
			return Nodo_Cabecera(-1, "")

	def existeSt(self, s):
		if self.vacia():
			return False
		else:
			temporal = self.primero
			while temporal != None:
				if temporal.proveedor == s:
					return True
				elif temporal.siguiente == None:
					return False
				temporal = temporal.siguiente
		return	False

	def busquedaSt(self, s):
		if self.existeSt(s):
			temporal = self.primero
			while temporal.proveedor != s:
				temporal = temporal.siguiente
			return temporal
		else:
			return Nodo_Cabecera(-1, "")

class Nodo_Lateral():
	def __init__(self, y, let):
		self.y = y
		self.letra = let
		self.Fila = Lista_Horizontal()
		self.siguiente = None
		self.anterior = None

class Laterales():
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def insertar(self, inserta):
		if self.vacia():
			self.primero = inserta
			self.ultimo = inserta
		else:
			if inserta.y < self.primero.y:
				self.insertaFrente(inserta)
			elif inserta.y > self.ultimo.y:
				self.insertaFinal(inserta)
			else:
				self.insertaMedio(inserta)

	def insertaFrente(self,inserta):
		self.primero.anterior = inserta
		inserta.siguiente = self.primero
		self.primero = self.primero.anterior

	def insertaMedio(self, inserta):
		temporal1 = self.primero
		while temporal1.y < inserta.y:
			temporal1 = temporal1.siguiente
		temporal2 = temporal1.anterior
		temporal2.siguiente = inserta
		temporal1.anterior = inserta
		inserta.siguiente = temporal1
		inserta.anterior = temporal2

	def insertaFinal(self, inserta):
		self.ultimo.siguiente = inserta
		inserta.anterior = self.ultimo
		self.ultimo = self.ultimo.siguiente

	def recorrer(self):
		if not self.vacia():
			temporal = self.primero
			while temporal !=None:
				temporal = temporal.siguiente

	def existe(self, y):
		if self.vacia():
			return False
		else:
			temporal = self.primero
			while temporal != None:
				if temporal.y == y:
					return True
				elif temporal.siguiente == None:
					return False
				temporal = temporal.siguiente
		return False

	def busqueda(self, y):
		if self.existe(y):
			temporal = self.primero
			while temporal.y != y:
				temporal = temporal.siguiente
			return temporal
		else:
			return Nodo_Lateral(-1, "")

	def existeSt(self, s):
		if self.vacia():
			return False
		else:
			temporal = self.primero
			while temporal != None:
				if temporal.letra == s:
					return True
				elif temporal.siguiente == None:
					return False
				temporal = temporal.siguiente
		return	False

	def busquedaSt(self, s):
		if self.existeSt(s):
			temporal = self.primero
			while temporal.letra != s:
				temporal = temporal.siguiente
			return temporal
		else:
			return Nodo_Lateral(-1, "")

class matriz_Ortogonal():
	def __init__(self):
		self.c = cabeceras()
		self.l = Laterales()

	def existe(self, x, y):
		nodoCol = self.l.primero
		if nodoCol == None:
			return False
		else:
			while nodoCol != None:
				nodoRow = nodoCol.Fila.primero
				while nodoRow != None:
					if nodoRow.x == x and nodoRow.y == y:
						return True
					nodoRow = nodoRow.derecha
				nodoCol = nodoCol.siguiente
		return False

	def insertar(self, correo):
		auxi = correo.split("@")
		y = ord(correo[0])
		x = 0
		for letter in auxi[1]:
			x += ord(letter)
		if not self.existe(x, y):
			insercion = Nodo_Ortogonal(x, y, 1, auxi[0])
			if self.c.existe(x)==False:
				self.c.insertar(Nodo_Cabecera(x, auxi[1]))
			if self.l.existe(y) == False:
				self.l.insertar(Nodo_Lateral(y, correo[0]))
			cTemporal = self.c.busqueda(x)
			lTemporal = self.l.busqueda(y)
			cTemporal.Columna.insertar(insercion)
			lTemporal.Fila.insertar(insercion)
		else:
			print "Correo ya insertado"

	def toDot(self):
		conexionHeadColumID = "NODOM"
		conexionHeadColumDI = ""
		headColum = "{\nrank=min;\nNODOM[label=\"Matriz de correos\"];\n"
		conexionesVerticalesID = ""
		conexionesVerticalesDI = ""
		bloqueConexVert = ""
		nodoTemp1 = self.l.primero
		while nodoTemp1 != None:
			headColum = headColum + "NODOC" + str(nodoTemp1.y) + "[label=\"Letra: " + str(nodoTemp1.letra) + "\",rankdir=LR];\n"
			conexionHeadColumID = conexionHeadColumID + " -> NODOC" + str(nodoTemp1.y)
			if nodoTemp1.siguiente != None:
				conexionHeadColumDI = " -> NODOC" + str(nodoTemp1.y) + conexionHeadColumDI
			conexionesVerticalesID = "NODOC" + str(nodoTemp1.y)
			conexionesVerticalesDI = "NODOC" + str(nodoTemp1.y)
			nodoTemp2 = nodoTemp1.Fila.primero
			while nodoTemp2 != None:
				conexionesVerticalesID = conexionesVerticalesID + " -> NODO" + str(nodoTemp2.x) + str(nodoTemp1.y)
				conexionesVerticalesDI = "NODO" + str(nodoTemp2.x) + str(nodoTemp1.y) + " -> " + conexionesVerticalesDI
				nodoTemp2 = nodoTemp2.derecha
			conexionesVerticalesID = conexionesVerticalesID + ";\n"
			conexionesVerticalesDI = conexionesVerticalesDI + ";\n"
			bloqueConexVert = bloqueConexVert + conexionesVerticalesID + conexionesVerticalesDI
			conexionesVerticalesID = ""
			conexionesVerticalesDI = ""
			nodoTemp1 = nodoTemp1.siguiente
		nodoFila = self.c.primero
		if nodoFila != None:
			headFila = ""
			conexioHeadFila = ""
			headFilaAnterior = "NODOM"
			nodoAnterior = ""
			etiquetaRank = "\n{\nrank=same;\n"
			bloqueRank = ""
			conexionesHoriz = ""
			bloqueConexHoriz = ""
			esPrimeraFila = True
			while nodoFila != None:
				if esPrimeraFila:
					conexioHeadFila = headFilaAnterior + " -> NODOF" + str(nodoFila.x) + "\n"
					headFilaAnterior = "NODOF" + str(nodoFila.x)
					esPrimeraFila = False
				else:
					conexioHeadFila = conexioHeadFila + headFilaAnterior + " -> NODOF" + str(nodoFila.x) + "[rankdir=UD];\n"
					conexioHeadFila = conexioHeadFila + "NODOF" + str(nodoFila.x) + " -> " + headFilaAnterior + "\n"
					headFilaAnterior = "NODOF" + str(nodoFila.x)
				if nodoFila.siguiente == None:
					etiquetaRank = "\n{\nrank=max;\n"
				nodoAnterior = "NODOF" + str(nodoFila.x)
				headFila = etiquetaRank + "NODOF" + str(nodoFila.x) + "[label=\"Dominio " + str(nodoFila.proveedor) + "\"];\n"
				nodoColum = nodoFila.Columna.primero
				while nodoColum != None:
					if nodoColum.estado > 0:
						headFila = headFila + "NODO" + str(nodoFila.x) + str(nodoColum.y) + "[label=\"Correo: " + str(nodoColum.mail) + "\"];\n"
						conexionesHoriz = conexionesHoriz + nodoAnterior + " -> " + "NODO" + str(nodoFila.x) + str(nodoColum.y) + "[constraint=false];\n"
						conexionesHoriz = conexionesHoriz + "NODO" + str(nodoFila.x) + str(nodoColum.y) + " -> " + nodoAnterior + "[constraint=false];\n"
						nodoAnterior = "NODO" + str(nodoFila.x) + str(nodoColum.y)
					nodoColum = nodoColum.abajo
				bloqueConexHoriz = bloqueConexHoriz + conexionesHoriz + "\n"
				conexionesHoriz = ""
				nodoAnterior = ""
				bloqueRank = bloqueRank + headFila + "}\n"
				headFila = ""
				nodoFila = nodoFila.siguiente
			headColum = headColum + "}\n"
			with open("C:\Users\Carlos\Desktop\matriz.dot", "w") as f:
				f.write("digraph Mat_Orto{\n")
				f.write("rankdir=UD;\n")
				f.write("node[shape = box ]\n")
				f.write(headColum)
				f.write(bloqueRank)
				f.write(conexionHeadColumID + conexionHeadColumDI)
				f.write("\n" + conexioHeadFila)
				f.write(bloqueConexVert + "\n")
				f.write(bloqueConexHoriz)
				f.write("}\n")
			from subprocess import check_call
		check_call(['dot','-Tpng','C:\Users\Carlos\Desktop\matriz.dot','-o','C:\Users\Carlos\Desktop\matriz.png'])





matriz = matriz_Ortogonal()
matriz.insertar("carlospecam@gmail.com")
matriz.insertar("marceperalta@hotmail.com")
matriz.insertar("samyaceituno@gmail.com")
matriz.insertar("meganaceituno@gmail.com")
matriz.insertar("jorgesalguero@hotmail.com")
matriz.insertar("carlospecam@outlook.com")
matriz.toDot()

'''
queue = cola()
queue.encolar(1)
queue.encolar(2)
queue.encolar(3)
queue.encolar(4)
queue.encolar(5)
queue.desencolar()
queue.toDot()

stack = pila()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.toDot()

lista = listaSimple()
lista.insertarFinal("Hola")
lista.insertarFinal("Ciao")
lista.insertarFinal("Jelou")
lista.insertarFinal("Holis")
lista.insertarFinal("Merga")
lista.eliminarNodo("muere")
print lista.buscarNodo("Jelou")
lista.toDot()
'''