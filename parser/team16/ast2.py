from Instruccion import *
from graphviz import Digraph
from graphviz import escape
from expresiones import *
import interprete as Inter
class Ast2:

    def __init__(self, sentencias):
        self.i = 0
        self.sentencias = sentencias

    def inc(self):
        global i
        self.i += 1

    def crearReporte(self):
        global dot

        dot = Digraph('AST', format='png', filename='c:/source/ast.gv')
        dot.attr('node', shape='box', color='#31CEF0')
        dot.node('Node' + str(self.i), '"AST"')
        dot.edge_attr.update(arrowhead='none')
        self.recorrerInstrucciones(self.sentencias, 'Node' + str(self.i))
        dot.render('AST', format='png', view=True)
        print('Hecho')





    def recorrerInstrucciones(self, sente, padre):
        for i in sente:
            #VIENE UN DROP TABLE
            if isinstance(i, DropTable):
                print("Si es un drop table *")
                self.grafoDropTable(i.id, padre)

            elif isinstance(i, Select):
                print("Es Una Instruccion Select")
                self.GrafoSelect(i.Lista_Campos,i.Nombres_Tablas,i.unionn,padre)

            elif isinstance(i, Select2):
                print("Es Una Instruccion Select2")
                self.GrafoSelect2(i.Lista_Campos,i.Nombres_Tablas,i.Cuerpo,i.unionn,padre)

            elif isinstance(i, Select3):
                print("Es Una Instruccion Select 3 ")
                self.GrafoSelect3(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)

            elif isinstance(i, Select4):
                print("Es Una Instruccion Select 4")
                self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)

            elif isinstance(i, Insert_Datos):
                print("Si es un drop Insert *")
                self.grafoInsert_Data(i.id_table,i.valores, padre)
            #-----------------------------------
            elif isinstance(i, CreateTable):
                self.grafoCreateTable(i.id, i.cuerpo, i.inhe, padre)

            elif isinstance(i, CreateDataBase):
                self.grafoCreateDataBase(i.replace, i.exists, i.idBase, i.idOwner ,i.Modo, padre)

            elif isinstance(i, Delete_Datos):
                print("Es Una Instruccion Delete")
                self.grafoDelete_Data(i.id_table,i.valore_where,padre)

            elif isinstance(i, Update_Datos):
                print("Es Una Instruccion Update")
                self.grafoUpdate__Data(i.id_table,i.valores_set,i.valor_where,padre)

            elif isinstance(i, Alter_COLUMN):
                print("Es Una Instruccion Alter  Column")
                self.grafoAlter_Column(i.idtabla,i.columnas,padre)

            elif isinstance(i, Alter_Table_AddColumn):
                print("Es Una Instruccion Alter Add Column")
                self.grafoAlter_AddColumn(i.id_table, i.id_columnas, padre)

            elif isinstance(i, ShowDatabases):
                print("Es Una Instruccion Showdatabases")
                self.grafoShowDatabases(i.cadenaLike, padre)

            elif isinstance(i, AlterDataBase):
                print("Es Una Instruccion AlterDataBase")
                self.grafoAlterDataBase(i.idDB, i.opcion, padre)

            elif isinstance(i, DropDataBase):
                print("Es Una Instruccion DropDataBase")
                self.grafoDropDataBase(i.id, i.existe, padre)

            elif isinstance(i, SelectExtract):
                print("Es Una Instruccion SelectExtract")
                self.grafoSelectExtract(i.tipoTiempo, i.cadenaFecha, padre)

            elif isinstance(i, SelectDatePart):
                print("Es Una Instruccion SelectDatePart")
                self.grafoSelectDatePart(i.cadena, i.cadenaIntervalo, padre)

            elif isinstance(i, SelectTipoCurrent):
                print("Es Una Instruccion SelectCurrentType")
                self.grafoSelectTipoCurrent(i.tipoCurrent, padre)

            elif isinstance(i, SelectStamp):
                print("Es Una Instruccion SelectTIMESTAMP")
                self.grafoSelectStamp(i.cadena, padre)

            elif isinstance(i, Selectnow):
                print("Es Una Instruccion Select Now")
                self.grafoSelectnow(i.constru, padre)

            elif isinstance(i, CreacionEnum):
                print("Es Una Instruccion CReate Type ENUM")
                self.grafoCreacionEnum(i.listaCadenas, padre)

            elif isinstance(i, Alter_Table_AddColumn):
                self.grafoAlter_AddColumn(i.id_table,i.id_columnas,padre)
            elif isinstance(i, Alter_Table_Drop_Column):
                print("es una instruccion alter drop column")
                self.grafoAlter_DropColumn(i.id_table, i.columnas, padre)
            elif isinstance(i, Alter_Table_Rename_Column):
                self.grafoAlter_RenameColumn(i.id_table, i.old_column, i.new_column, padre)
            elif isinstance(i, Alter_Table_Drop_Constraint):
                self.grafoAlter_DropConstraint(i.id_tabla, i.id_constraint, padre)
            elif isinstance(i, Alter_table_Alter_Column_Set):
                self.grafoAlter_AlterColumnSet(i.id_tabla, i.id_column, padre )
            elif isinstance(i, Alter_table_Add_Foreign_Key):
                self.grafoAlter_AddForeignKey(i.id_table, i.id_column, i.id_column_references, padre)
            elif isinstance(i, Alter_Table_Add_Constraint):
                self.grafoAlter_AddConstraint(i.id_table, i.id_constraint, i.id_column, padre)
            
            else:
                print("No es droptable")





    def RecorrerTipoSelect(self, sente, padre):
        i=sente
        if isinstance(i, Select):
            print("Es Una Instruccion Select ")
            self.GrafoSelect(i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)
        elif isinstance(i, Select2):
            print("Es Una Instruccion Select 2")
            self.GrafoSelect2(i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)

        elif isinstance(i, Select3):
            print("Es Una Instruccion Select 3 ")
            self.GrafoSelect3(i.distinct,i.Lista_Campos, i.Nombres_Tablas, i.unionn, padre)

        elif isinstance(i, Select4):
            print("Es Una Instruccion Select 4")
            self.GrafoSelect4(i.distinct, i.Lista_Campos, i.Nombres_Tablas, i.Cuerpo, i.unionn, padre)
        else:
            print("No hay tipo aun");





    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------
    # INSTRUCCIONES NECESARIAS PARA LOS SELECT
    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------


    # CAMPOS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------

    # Objeto Que Accede A este Tipo "Campo_Accedido"
    # Campos Accedidos Con Lista
    def GrafoCampo_Accedido(self, NombreT, Columna, Lista_Alias, padre):
        global dot
        # NombreT.Campo Lista
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False )):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        # Campo Lista
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False)):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Recorrer la lista de alias
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
        else:
            print("Error Sintactico")


        #Objeto Que Accede A este Tipo "Campo_AccedidoSinLista"
        # Campos Accedidos Sin Lista
    def GrafoCampo_AccedidoSinLista(self, NombreT, Columna, padre):
        global dot
         # NombreT.Campo
        if ((NombreT != "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Campo
        elif ((NombreT == "") and (Columna != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error Sintactico")





    # NOMBRE TABLAS ACCEDIDOS
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoTabla"
    #Nombres Lista Accedidos  Con lista
    def GrafoAccesoTabla(self, NombreT, Lista_Alias, padre):
        global dot
        if ((NombreT != "") and (Lista_Alias != False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # Verificar el Tipo que viene
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))

        else:
            print("Error sintactico")


    #Objeto Que accede "AccesoTablaSinLista"
    #Nombres Lista Accedidos  Sin lista
    def GrafoAccesoTablaSinLista(self, NombreT, padre):
        global dot
        # Nombre
        if ((NombreT != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Nombre_Tabla")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
            print("Error sintactico")




    # Campos Accedidos desde el group By
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoGroupBy"  NombreT,Columna,Estado,Lista_Alias=[]

    #Nombres Lista Accedidos  Con lista
    def GrafoAccesoGroupBy(self, NombreT,Columna, Lista_Alias,Estado, padre):
        global dot

        # Tabla.Columna Alias
        if ((NombreT != "") and (Columna != "") and (Lista_Alias != False ) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Ver tipos de Alias Agregar el de Group By




        # Tabla.Columna
        elif((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))



        #columna Alias
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i),Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Agregar Tipo de Alias de Group by




        #Columna
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado == "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        #Tabla.Columna Alias Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))


            #Recorrer Listado de Estados

        #Tabla.Columna  Estado
        elif ((NombreT != "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i), NombreT + '.' + Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        #Columna Alias Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias != False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))
            self.inc();
            dot.node('Node' + str(self.i),  Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))
            #Agregar el tipo de alias del group by

            # Estado
            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        #Columna  Estado
        elif ((NombreT == "") and (Columna != "") and (Lista_Alias == False) and (Estado != "")):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "ACCESO_CAMPO")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Columna)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Estado
            self.inc();
            dot.node('Node' + str(self.i), Estado)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")



    # Campos Accedidos desde Las Subconsultas
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "AccesoSubConsultas"  AnteQuery=[], Query=[], Lista_Alias=[]
    #Nombres Lista Accedidos  Con Las Subconsultas

    def GrafoAccesoSubConsultas(self, AnteQuery,Query, Lista_Alias, padre):
        print(AnteQuery, Query, Lista_Alias)
        #AnteQuery ( query )
        if  (AnteQuery != False) and  (Query !=False) and  (Lista_Alias ==False):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))


            #Recorrido de las Expresiones Ante Query
            self.inc();
            dot.node('Node' + str(self.i), "AnteQuery")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.Recorrer_Condiciones(AnteQuery, 'Node' + str(self.i))



            #Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query,'Node' + str(self.i) )


        # AnteQuery ( query ) Alias
        elif (AnteQuery != False) and (Query != False) and (Lista_Alias != False):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las Expresiones Ante Query
            self.inc();
            dot.node('Node' + str(self.i), "AnteQuery ")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.Recorrer_Condiciones(AnteQuery, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))


        # ( query )
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias == False):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta ")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))


        # ( query ) Alias
        elif (AnteQuery == False) and (Query != False) and (Lista_Alias != False):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_Subconsulta")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido de las subconsultas
            self.inc();
            dot.node('Node' + str(self.i), "(  SubQuery  )")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaSubconsultas(Query, 'Node' + str(self.i))

            # Recorrido De la Lista de Alias
            self.inc();
            dot.node('Node' + str(self.i), "Lista_Alias")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTiposAlias(Lista_Alias, 'Node' + str(self.i))



    # Campos Accedidos desde La UNION DE CONSULTAS
    # ----------------------------------------------------------------------------------------------------------

    #Objeto Que accede "CamposUnions"  Reservada,Comportamiento,Consulta=[]

    def GrafoAccesoUniones(self, Reservada, Comportamiento, Consulta, padre):


        #Comportamiento Reservada Consulta
        if((Comportamiento!="")and(Reservada!="")and(Consulta==False)):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_UNION")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Reservada)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la de consultas
            self.inc();
            dot.node('Node' + str(self.i), "CONSULTA")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))

        #Comportamiento Consulta
        elif (( Comportamiento!= "") and (Reservada == "") and (Consulta != False)):
            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Acceso_UNION")
            dot.edge(padre, 'Node' + str(self.i))

            # Recorrido De la de consultas
            self.inc();
            dot.node('Node' + str(self.i), "CONSULTA")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerTipoSelect(Consulta, 'Node' + str(self.i))

        # puntocoma
        elif (( Comportamiento == "") and (Reservada != "") and (Consulta == False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Final_Instruccion")
            dot.edge(padre, 'Node' + str(self.i))

            # Punto coma final clausula
            self.inc();
            dot.node('Node' + str(self.i), ";")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sinstacticos")




    # Campos Accedidos por los campos de tipo Cases
    # ----------------------------------------------------------------------------------------------------------

    # Campos Accedidos por  case   : Objeto Accedido "CaseCuerpo"  : Campos  Cuerpo, Lista_When=[]
    def GrafoCampoCasePuro(self,Lista_When,Cuerpo,padre):

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "Acceso_Case")
        dot.edge(padre, 'Node' + str(self.i))


        self.inc();
        dot.node('Node' + str(self.i), "CASE")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Recorrido DE LOS TIPOS DE WHEN
        self.inc();
        dot.node('Node' + str(self.i), "TIPOS_WHEN")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        #Recorrer Lista Case
        self.RecorrerListaWhens(Lista_When,'Node' + str(self.i))


        #FIN CONDICION
        self.inc();
        dot.node('Node' + str(self.i),Cuerpo)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))





    # Campos Accedidos por  Expresion :Objeto Accedido "ExpresionesCase"  : Reservada, ListaExpresiones=[]
    def GrafoExpresionCase(self,Reservada,ListaExpresiones,padre):

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "Acceso_Case_Expresiones")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i),Reservada )
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        # Recorrido lista expresiones
        self.inc();
        dot.node('Node' + str(self.i), "EXPRESIONES")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        # Recorrer la lista de when
        self.Recorrer_Condiciones(ListaExpresiones, 'Node' + str(self.i))




    #Recorriendo tipos de when : Objeto al que Accesa "TiposWhen"  : Campos: Reservada,Reservada2,Reservada3,ListaExpresiones1=[],ListaExpresiones2=[],ListaExpresiones3=[])
    def GrafoTiposWhen(self,Reservada,ListaExpresiones1,Reservada2,ListaExpresiones2,Reservada3,ListaExpresiones3,padre):

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "TIPOS WHEN ENTRADA")
        dot.edge(padre, 'Node' + str(self.i))

        #When ListaExpresiones1 then listaExpresiones3
        if((Reservada!="")and(ListaExpresiones1!=False)and(Reservada2=="")and(ListaExpresiones2==False )and(Reservada3!="")and(ListaExpresiones3!=False)):

            self.inc();
            dot.node('Node' + str(self.i), Reservada)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 1
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES1")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))


            self.inc();
            dot.node('Node' + str(self.i), Reservada3)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


            # Recorrido De la ListaExpresiones 3
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES3")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones3, 'Node' + str(self.i))




        # When ListaExpresiones1 Else listaExpresiones2 then ListaExpresiones3
        if((Reservada!="")and(ListaExpresiones1!=False)and(Reservada2!="")and(ListaExpresiones2!=False )and(Reservada3 !="")and(ListaExpresiones3 !=False)):

            self.inc();
            dot.node('Node' + str(self.i), Reservada)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 1
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES1")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))



            self.inc();
            dot.node('Node' + str(self.i), Reservada2)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 2
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES2")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones2, 'Node' + str(self.i))



            self.inc();
            dot.node('Node' + str(self.i), Reservada3)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


            # Recorrido De la ListaExpresiones 3
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES3")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones3, 'Node' + str(self.i))



        # When ListaExpresiones1
        if((Reservada!="")and(ListaExpresiones1!=False)and(Reservada2=="")and(ListaExpresiones2==False )and(Reservada3 =="")and(ListaExpresiones3 ==False)):

            self.inc();
            dot.node('Node' + str(self.i), Reservada)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 1
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES1")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones1, 'Node' + str(self.i))




        # When ListaExpresiones1 Else listaExpresiones2
        if((Reservada!="")and(ListaExpresiones1!=False)and(Reservada2!="")and(ListaExpresiones2 !=False )and(Reservada3 =="")and(ListaExpresiones3 ==False)):

            self.inc();
            dot.node('Node' + str(self.i), Reservada)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 1
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES1")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones1,'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Reservada2)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            # Recorrido De la ListaExpresiones 2
            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES_EXPRESIONES2")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            # self.RecorrerTipoSelect(Consulta,'Node' + str(self.i))
            self.Recorrer_Condiciones(ListaExpresiones2, 'Node' + str(self.i))










    # ALIAS CAMPOS
    # ----------------------------------------------------------------------------------------------------------


    #Objeto que tiene Acceso "Alias_Campos_ListaCamposSinLista"
    #Acceso a los Campos Sin lista
    def GrafoAlias_Campos_ListaCamposSinLista(self, Alias, padre):
        global dot

        # as Alias
        if ((Alias != "") ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        else:
           print("Verificar Errores Sintacticos")




    # ALIAS Tablas
    # ----------------------------------------------------------------------------------------------------------

    #Objeto que tiene acceso "Alias_Table_ListaTablasSinLista"
    #Acceso a Alias de las Tablas Sin Lista
    def GrafoAlias_Table_ListaTablasSinLista(self, Alias, padre):
        global dot

        # as Alias
        if (Alias != "" ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")






    # ALIAS Group By
    # ----------------------------------------------------------------------------------------------------------

    #Objeto que tiene acceso "Alias_Tablas_GroupSinLista"
    #Acceso a Alias de los Group By

    def GrafoAlias_Tablas_GroupSinLista(self, Alias, padre):
        global dot

        # as Alias
        if (Alias != "" ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")




    # ALIAS  SUB QUERYS
    # ----------------------------------------------------------------------------------------------------------

    #Objeto que tiene acceso "Alias_SubQuerysSinLista"
    #Acceso a Alias de las subconsultas

    def GrafoAlias_SubQuerysSinLista(self, Alias, padre):
        global dot

        # as Alias
        if (Alias != "" ):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "Alias_Produccion")
            dot.edge(padre, 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "As")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), Alias)
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        else:
            print("Verificar Errores Sintacticos")






    # Grafo Where con Expreciones
    # ----------------------------------------------------------------------------------------------------------
    # Where Expreciones
    def GrafoCuerpo_Condiciones(self,Lista,padre):
        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "Cuerpo")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "Where")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.Recorrer_Condiciones(Lista, 'Node' + str(nuevoPadre))



    #Recorremos Expresion y mandamos el nodo aumentando el padre
    def Recorrer_Condiciones(self,Lista,padre):

        # GRAFICANDO EXPRESION===========================
            i = Lista
            self.inc();
            dot.node('Node' + str(self.i), "CONDICION")
            dot.edge(padre, 'Node' + str(self.i))

            # LLAMAMOS A GRAFICAR EXPRESION
            padrenuevo = self.i
            self.graficar_expresion(i)
            self.inc()
            dot.edge('Node' + str(padrenuevo), str(padrenuevo + 1))





    # Recorrido de la lista de Campos
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeCampos(self, Campos, padre):
            for j in Campos:

                if isinstance(j, Campo_AccedidoSinLista):
                    print("Es un Campo Accedido Por la Tabla Sin Lista" + j.NombreT)
                    self.GrafoCampo_AccedidoSinLista(j.NombreT, j.Columna, padre)

                elif isinstance(j, AccesoSubConsultas):
                    print("Es un Acceso a  una subconsulta")
                    self.GrafoAccesoSubConsultas(j.AnteQuery, j.Query, j.Lista_Alias, padre)

                elif isinstance(j,CaseCuerpo):
                    print("Es un Acceso a un Campo CasePuro")
                    self.GrafoCampoCasePuro(j.Lista_When, j.Cuerpo, padre)

                elif isinstance(j,ExpresionesCase ):
                    print("Es un Acceso a  una expresion Case")
                    self.GrafoExpresionCase(j.Reservada, j.ListaExpresiones, padre)

                else:
                    print("No Ningun Tipo  vos ")






    # Recorrido de la lista de Nombres de Tablas
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListadeNombres(self, Nombres, padre):
        for i in Nombres:

            if isinstance(i, AccesoTabla):
                #print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoAccesoTabla(i.NombreT, i.Lista_Alias, padre)

            elif isinstance(i, AccesoTablaSinLista):
                #print("Es un Campo Accedido Por la Tabla" + i.NombreT)
                self.GrafoAccesoTablaSinLista(i.NombreT, padre)

            elif isinstance(i, AccesoSubConsultas):
                print("Es un Acceso a  una subconsulta")
                self.GrafoAccesoSubConsultas(i.AnteQuery, i.Query, i.Lista_Alias, padre)

            else:
                print("No Ningun Tipo")



    # Recorrido a la lista de campos
    # ----------------------------------------------------------------------------------------------------------

    def RecorrerListaCamposGroupBy(self, Lista_Campos, padre):

        for i in Lista_Campos:
            if isinstance(i, AccesoGroupBy):
               # print("Es un Campo Accedido Por la Cuerpo ")
                self.GrafoAccesoGroupBy(i.NombreT,i.Columna,i.Lista_Alias,i.Estado, padre)
            else:
                print("No hay Ningun Tipo")





    # Recorrido a la lista de subconsultas
    # ----------------------------------------------------------------------------------------------------------
    # Solo es uno ya que solo viene una consulta dentro de parentesis
    def RecorrerListaSubconsultas(self, Lista_Subs, padre):

            i = Lista_Subs
            if isinstance(i, SubSelect):
                print("Es un Campo Accedido Por una Subconsulta ")

                self.GrafoSubSelect(i.Lista_Campos,i.Nombres_Tablas, padre)

            elif isinstance(i,SubSelect2):
                print("Es un Campo Accedido Por una Subconsulta 2 ")
                self.GrafoSubSelect2(i.Lista_Campos,i.Nombres_Tablas,i.Cuerpo, padre)


            elif isinstance(i,SubSelect3):
                print("Es un Campo Accedido Por una Subconsulta 3 ")
                self.GrafoSubSelect3(i.Distict,i.Lista_Campos,i.Nombres_Tablas, padre)


            elif isinstance(i,SubSelect4):
                print("Es un Campo Accedido Por una Subconsulta 4 ")
                self.GrafoSubSelect4(i.Distict, i.Lista_Campos,i.Nombres_Tablas,i.Cuerpo, padre)

            else:
                print("No hay Ningun Tipo")



    # Recorrido a al lista de uniones
    # ----------------------------------------------------------------------------------------------------------
    def RecorrerListaUniones(self, Uniones, padre):

        for i in Uniones:
            if isinstance(i, CamposUnions):
                print("Es un Campo Accedido Por una Subconsulta ")
                self.GrafoAccesoUniones(i.Reservada,i.Comportamiento,i.Consulta, padre)
            else:
                print("No hay Ningun Tipo")




    # Recorrido de los Alias
    # ----------------------------------------------------------------------------------------------------------
    def RecorrerTiposAlias(self, Lista_Alias, padre):

        i=Lista_Alias

        # Alias de los Campos Sin Lista
        if isinstance(i, Alias_Campos_ListaCamposSinLista):
           print("Es un Campo Accedido Por la Tabla" + i.Alias)
           self.GrafoAlias_Campos_ListaCamposSinLista(i.Alias, padre)

        #Alias de las Nombres de las Tablas Sin Lista
        elif isinstance(i, Alias_Table_ListaTablasSinLista):
           # print("Es un Campo Accedido Por la Tabla" + i.Alias)
            self.GrafoAlias_Table_ListaTablasSinLista(i.Alias, padre)


        #Alias de los Group By Sin Lista
        elif isinstance(i, Alias_Tablas_GroupSinLista):
          #  print("Es un Campo Accedido Por la Tabla" + i.Alias)
            self.GrafoAlias_Tablas_GroupSinLista(i.Alias, padre)


        #Alias de las Subconsulta sin lista
        elif isinstance(i, Alias_SubQuerysSinLista):
            print("Es un Campo Accedido Por subconsulta sin lista " + i.Alias)
            self.GrafoAlias_SubQuerysSinLista(i.Alias, padre)

        else:
            print("No Ningun Tipo")




    # Recorrido de la lista de de Los Posibles Cuerpos
    # ----------------------------------------------------------------------------------------------------------
    def RecorrerListaCuerpos(self, Groups, padre):
        for i in Groups:
            if isinstance(i, Cuerpo_TipoWhere):
                print("Es un Acceso a Where")
                self.GrafoCuerpo_Condiciones(i.Cuerpo, padre)

            elif isinstance(i, GroupBy):
                print("Es un Campo Accedido Por la Cuerpo ")
                self.GrafoGroupBy(i.Lista_Campos, i.Condiciones, padre)

            elif isinstance(i, AccesoLimit):
                print("Es un Campo Accedido Limit ")
                self.GrafoLimit(i.Reservada, i.Expresion_Numerica, padre)

            elif isinstance(i, AccesoSubConsultas):
                print("Es un Acceso a  una subconsulta")
                self.GrafoAccesoSubConsultas(i.AnteQuery,i.Query,i.Lista_Alias,padre)
            elif isinstance(i, Cuerpo_Condiciones):
                print("Es un acceso a where con condicion de subconsulta")
                self.GrafoCuerpo_Condiciones(i.Cuerpo, padre)
            else:
                print("No Ningun Tipo")


    def RecorrerListaWhens(self, Lista, padre):
        for i in Lista:
            if isinstance(i,TiposWhen):
                print("Es un Acceso A Tipo determinado de When")
                self.GrafoTiposWhen(i.Reservada,i.ListaExpresiones1,i.Reservada2,i.ListaExpresiones2,i.Reservada3,i.ListaExpresiones3,padre)
            else:
                print("No Ningun Tipo")



    # ------------------------------------ FIN DEL ACCESO A LOS CAMPOS DE CADA CUESTION



    # Instruccion SELECT
    # ----------------------------------------------------------------------------------------------------------

    def GrafoSelect(self, ListaCampos, NombresTablas, Uniones, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i),"Uniones")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        #Recorrer lista de uniones
        self.RecorrerListaUniones(Uniones, 'Node' + str(self.i))


    def GrafoSelect2(self,ListaCampos, NombresTablas,cuerpo, Uniones, padre ):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i));

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "CUERPO")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.RecorrerListaCuerpos(cuerpo, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i),"Uniones")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        #Recorrer lista de uniones
        self.RecorrerListaUniones(Uniones, 'Node' + str(self.i))


    def GrafoSelect3(self,Distict, ListaCampos, NombresTablas, Uniones, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        self.inc();
        dot.node('Node' + str(self.i), Distict)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i),"Uniones")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        #Recorrer lista de uniones
        self.RecorrerListaUniones(Uniones, 'Node' + str(self.i))



    def GrafoSelect4(self,Distict,ListaCampos, NombresTablas,cuerpo, Uniones, padre ):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        self.inc();
        dot.node('Node' + str(self.i), Distict)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i));

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "CUERPO")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.RecorrerListaCuerpos(cuerpo, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i),"Uniones")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        #Recorrer lista de uniones
        self.RecorrerListaUniones(Uniones, 'Node' + str(self.i))





    # Instruccion SUB  SELECT
    # ----------------------------------------------------------------------------------------------------------



#GRAFO DEL SUB SELECT
    def GrafoSubSelect(self, ListaCampos, NombresTablas, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))




#Grafo Sub Select Con Cuerpo
    def GrafoSubSelect2(self, ListaCampos, NombresTablas, cuerpo, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i));

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "CUERPO")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListaCuerpos(cuerpo, 'Node' + str(self.i))




    def GrafoSubSelect3(self,Distinct,ListaCampos, NombresTablas, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        self.inc();
        dot.node('Node' + str(self.i), Distinct)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))


        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))



        # Grafo Sub Select Con Cuerpo
    def GrafoSubSelect4(self,Distinct,ListaCampos, NombresTablas, cuerpo, padre):
        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION_SELECT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "SELECT")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), Distinct)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_CAMPOS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeCampos(ListaCampos, 'Node' + str(self.i));

        self.inc();
        dot.node('Node' + str(self.i), "FROM")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "LISTA_TABLAS")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListadeNombres(NombresTablas, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), "CUERPO")
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
        self.RecorrerListaCuerpos(cuerpo, 'Node' + str(self.i))






    def GrafoGroupBy(self, Lista_Campos, Condiciones, padre):
        global dot
       #Group by ListaCampos Having Condiciones
        if ((Lista_Campos!=False) and  (Condiciones!=False)):

            self.inc();
            nuevoPadre = self.i
            dot.node('Node' + str(self.i), "INSTRUCCION GROUP BY ")
            dot.edge(padre, 'Node' + str(self.i))


            self.inc();
            dot.node('Node' + str(self.i), "GROUP BY")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "LISTA_CAMPOS")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.RecorrerListaCamposGroupBy(Lista_Campos,'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "HAVING")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

            self.inc();
            dot.node('Node' + str(self.i), "CONDICIONES")
            dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
            self.Recorrer_Condiciones(Condiciones, 'Node' + str(self.i))

       #Group by ListaCampos
        elif ((Lista_Campos != False) and (Condiciones == False)):

           self.inc();
           nuevoPadre = self.i
           dot.node('Node' + str(self.i), "INSTRUCCION GROUP BY ")
           dot.edge(padre, 'Node' + str(self.i))

           self.inc();
           dot.node('Node' + str(self.i), "GROUP BY")
           dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           self.inc();
           dot.node('Node' + str(self.i), "LISTA_CAMPOS")
           dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))
           self.RecorrerListaCamposGroupBy(Lista_Campos,'Node' + str(self.i))








#Grafo de los Limit
    def GrafoLimit(self,Reservada, Expresion_Numerica,padre):

        global dot

        self.inc();
        nuevoPadre = self.i
        dot.node('Node' + str(self.i), "INSTRUCCION LIMIT")
        dot.edge(padre, 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), Reservada)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))

        self.inc();
        dot.node('Node' + str(self.i), Expresion_Numerica)
        dot.edge('Node' + str(nuevoPadre), 'Node' + str(self.i))







    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------
    # FIN DE INSTRUCCIONES NECESARIAS PARA LOS SELECT
    # ----------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------








# ----------------------------------------------------------------------------------------------------------
# ----------------------- GRAFO DROP TABLE-------------------------------------------------------------------
    def grafoDropTable(self, id, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"DROP_TABLE")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        for i in id:
            self.inc();
            dot.node('Node'+  str(self.i), i.val)
            dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))



#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR INSERTAR-------------------------------------------------------------------
    def grafoInsert_Data(self, id, valores, padre):
        global  dot,tag,i

        self.inc()
        nuevoPadre=self.i
        dot.node('Node'+str(self.i),"INSERT")
        dot.edge(padre,'Node'+str(self.i))

        self.inc();
        nuevoPadre2 = self.i
        dot.node('Node'+str(self.i),"ID TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))

        for i in id:
            self.inc();
            dot.node('Node'+  str(self.i), i.val)
            dot.edge('Node' + str(nuevoPadre2),'Node'+str(self.i))

        self.inc();
        nuevoPadre3 = self.i
        dot.node('Node'+str(self.i),"VALORES TABLA")
        dot.edge('Node' + str(nuevoPadre),'Node'+str(self.i))


       #GRAFICANDO EXPRESION===========================
        for i in valores:
            self.inc();
            dot.node('Node'+  str(self.i), "VALOR NUEVO")
            dot.edge('Node' + str(nuevoPadre3),'Node'+str(self.i))
            #LLAMAMOS A GRAFICAR EXPRESION
            padrenuevo4 = self.i
            self.graficar_expresion(i)
            Respuesta = Inter.procesar_expresion(i,None)
            print("RESPUESTA DE EXPRESION-----")
            print(Respuesta)
            self.inc()

            dot.edge('Node'+str(padrenuevo4),str(padrenuevo4+1))


#----------------------------------------------------------------------------------------------------------
#-----------------------GRAFICAR EXPRESION-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

    def graficar_expresion(self, expresiones):
        global  dot,tag,i

        if isinstance(expresiones,ExpresionAritmetica):
            self.graficar_arit_log_rel_bb(expresiones,"Aritmetica")
        elif isinstance(expresiones,ExpresionRelacional) :
            self.graficar_arit_log_rel_bb(expresiones,"Relacional")
        elif isinstance(expresiones,ExpresionLogica) :
            self.graficar_arit_log_rel_bb(expresiones,"Logica")
        elif isinstance(expresiones,UnitariaNegAritmetica) :
            self.graficarUnaria(expresiones,"NegAritmetica")
        elif isinstance(expresiones,UnitariaLogicaNOT) :
            self.graficarUnaria(expresiones,"LogicaNOT")
        elif isinstance(expresiones,UnitariaNotBB) :
            self.graficarUnaria(expresiones,"NotBB")
        elif isinstance(expresiones, ExpresionFuncion):
            self.graficarExpresionFuncion(expresiones, "FUNCION NATIVA")
        elif isinstance(expresiones, UnitariaAritmetica):
            self.graficarUnitariaAritmetica(expresiones, "UnitariaAritmetica")
        #NUEVAS UNITARIAS

        #----------------------------------------
        elif isinstance(expresiones,ExpresionValor) :
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'ExpresionValor')
            dot.edge(str(padreID),str(padreID+1))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),str(expresiones.val))
        elif isinstance(expresiones, UnariaReferencia) :
            self.inc()
            padreID=self.i
            dot.node(str(padreID),' ExpresionReferencia')
            dot.edge(str(padreID),str(padreID+1))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),expresiones.tipoVar.id)
        elif isinstance(expresiones,Absoluto):
            self.inc()
            padreID=self.i
            dot.node(str(padreID),' ( Expresion )')
            dot.edge(str(padreID),str(padreID+1))
            self.graficar_expresion(expresiones.variable)
        elif isinstance(expresiones, ExpresionCondicionalSubquery):
            self.inc()
            padreID = self.i
            dot.node(str(padreID), self.getVar(expresiones.val))
            # dot.edge(str(padreID), str(padreID + 1))
            # self.graficar_expresion(expresiones.variable) CAMPO_TABLA_ID_PUNTO_ID
        elif isinstance(expresiones, AccesoSubConsultas):
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'Subconsulta')
            self.GrafoAccesoSubConsultas(expresiones.AnteQuery, expresiones.Query, expresiones.Lista_Alias, str(padreID))
        elif isinstance(expresiones,CAMPO_TABLA_ID_PUNTO_ID) :
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'ExpresionValor ID punto ID')
            dot.edge(str(padreID),str(padreID+1))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),str(expresiones.tablaid)+"."+str(expresiones.campoid))

    def graficar_arit_log_rel_bb(self,expresion,tipo_exp="") :
        global  dot,tag,i
        if expresion.exp1 and expresion.exp2:
            self.inc()
            padreID=self.i
            padre=padreID
            dot.node(str(padreID),'Expresion'+tipo_exp)
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'exp1')
            dot.edge(str(padre),str(padreID))
            dot.edge(str(padreID),str(padreID+1))
            self.graficar_expresion(expresion.exp1)
            self.inc()
            padreID=self.i
            dot.node(str(padreID),self.getVar(expresion.operador))
            dot.edge(str(padre),str(padreID))
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'exp2')
            dot.edge(str(padre),str(padreID))
            dot.edge(str(padreID),str(padreID+1))
            self.graficar_expresion(expresion.exp2)
        elif expresion.exp1 == None and expresion.exp2 == None:
            self.inc()
            padreID=self.i
            padre=padreID
            dot.node(str(padreID), self.getVar(expresion.operador))
        elif  expresion.exp2 == None:
            self.inc()
            padreID=self.i
            padre=padreID
            dot.node(str(padreID),'Expresion'+tipo_exp)
            self.inc()
            padreID=self.i
            dot.node(str(padreID),'exp1')
            dot.edge(str(padre),str(padreID))
            dot.edge(str(padreID),str(padreID+1))
            self.graficar_expresion(expresion.exp1)
            self.inc()
            padreID=self.i
            dot.node(str(padreID),self.getVar(expresion.operador))
            dot.edge(str(padre),str(padreID))


    def graficarUnaria(self,expresion,tipo_exp=""):
        self.inc()
        padreID=self.i
        dot.node(str(padreID),'Expresion'+tipo_exp)
        dot.edge(str(padreID),str(padreID+1))
        if isinstance(expresion,UnitariaNegAritmetica):
            self.graficar_expresion(expresion.exp)
        else:
            self.graficar_expresion(expresion.expresion)

    def getVar(self, padreID):
        if padreID==OPERACION_ARITMETICA.MAS:
            return '+'
        elif padreID==OPERACION_ARITMETICA.MENOS:
            return '-'
        elif padreID==OPERACION_ARITMETICA.MULTI:
            return '*'
        elif padreID==OPERACION_ARITMETICA.DIVIDIDO:
            return '/'
        elif padreID==OPERACION_ARITMETICA.RESIDUO:
            return '%'
        elif padreID==OPERACION_LOGICA.AND:
            return 'AND'
        elif padreID==OPERACION_LOGICA.OR:
            return 'OR'
        elif padreID==OPERACION_RELACIONAL.IGUALQUE:
            return '=='
        elif padreID==OPERACION_RELACIONAL.DISTINTO:
            return '!='
        elif padreID==OPERACION_RELACIONAL.MAYORIGUAL:
            return '>='
        elif padreID==OPERACION_RELACIONAL.MENORIGUAL:
            return '!='
        elif padreID==OPERACION_RELACIONAL.MAYORQUE:
            return '>'
        elif padreID==OPERACION_RELACIONAL.MENORQUE:
            return '<'
        #NUEVAS COSAS
        elif padreID==OPERACION_LOGICA.IS_NOT_NULL:
            return 'IS_NOT_NULL'
        elif padreID==OPERACION_LOGICA.IS_NOT_TRUE:
            return 'IS_NOT_TRUE'
        elif padreID==OPERACION_LOGICA.IS_NOT_FALSE:
            return 'IS_NOT_FALSE'
        elif padreID==OPERACION_LOGICA.IS_NOT_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID==OPERACION_LOGICA.IS_NULL:
            return 'IS_NULL'
        elif padreID==OPERACION_LOGICA.IS_TRUE:
            return 'IS_TRUE'
        elif padreID==OPERACION_LOGICA.IS_FALSE:
            return 'IS_FALSE'
        elif padreID==OPERACION_LOGICA.IS_UNKNOWN:
            return 'IS_NOT_UNKNOWN'
        elif padreID==OPERACION_LOGICA.IS_NOT_DISTINCT:
            return 'IS_NOT_DISTINCT'
        elif padreID==OPERACION_LOGICA.IS_DISTINCT:
            return 'IS_DISTINCT'
        elif padreID==OPERACION_LOGICA.EXISTS:
            return 'EXISTS'
        elif padreID==OPERACION_LOGICA.NOT_EXIST:
            return 'NOT_EXISTS'
        elif padreID==OPERACION_LOGICA.IN:
            return 'IN'
        elif padreID==OPERACION_LOGICA.NOT_IN:
            return 'NOT_IN'
        elif padreID==FUNCION_NATIVA.ABS:
            return 'ABS'
        elif padreID==FUNCION_NATIVA.CBRT:
            return 'CBRT'
        elif padreID==FUNCION_NATIVA.CEIL:
            return 'CEIL'
        elif padreID==FUNCION_NATIVA.CEILING:
            return 'CEILING'
        elif padreID==FUNCION_NATIVA.DEGREES:
            return 'DEGREES'
        elif padreID==FUNCION_NATIVA.EXP:
            return 'EXP'
        elif padreID==FUNCION_NATIVA.FACTORIAL:
            return 'FACTORIAL'
        elif padreID==FUNCION_NATIVA.FLOOR:
            return 'FLOOR'
        elif padreID==FUNCION_NATIVA.LN:
            return 'LN'
        elif padreID==FUNCION_NATIVA.LOG:
            return 'LOG'
        elif padreID==FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID==FUNCION_NATIVA.RADIANS:
            return 'RADIANS'
        elif padreID==FUNCION_NATIVA.ROUND:
            return 'ROUND'
        elif padreID==FUNCION_NATIVA.SIGN:
            return 'SIGN'
        elif padreID==FUNCION_NATIVA.SQRT:
            return 'SQRT'
        elif padreID==FUNCION_NATIVA.TRUNC:
            return 'TRUNC'
        elif padreID==FUNCION_NATIVA.ACOS:
            return 'ACOS'
        elif padreID==FUNCION_NATIVA.ACOSD:
            return 'ACOSD'
        elif padreID==FUNCION_NATIVA.ASIN:
            return 'ASIN'
        elif padreID==FUNCION_NATIVA.ASIND:
            return 'ASIND'
        elif padreID==FUNCION_NATIVA.ATAN:
            return 'ATAN'
        elif padreID==FUNCION_NATIVA.ATAND:
            return 'ATAND'
        elif padreID==FUNCION_NATIVA.COS:
            return 'COS'
        elif padreID==FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID==FUNCION_NATIVA.COT:
            return 'COT'
        elif padreID==FUNCION_NATIVA.COTD:
            return 'COTD'
        elif padreID==FUNCION_NATIVA.COSD:
            return 'COSD'
        elif padreID==FUNCION_NATIVA.SIN:
            return 'SIN'
        elif padreID==FUNCION_NATIVA.SIND:
            return 'SIND'
        elif padreID==FUNCION_NATIVA.TAN:
            return 'TAN'
        elif padreID==FUNCION_NATIVA.TAND:
            return 'TAND'
        elif padreID==FUNCION_NATIVA.SINH:
            return 'SINH'
        elif padreID==FUNCION_NATIVA.COSH:
            return 'COSH'
        elif padreID==FUNCION_NATIVA.TANH:
            return 'TANH'
        elif padreID==FUNCION_NATIVA.ASINH:
            return 'ASINH'
        elif padreID==FUNCION_NATIVA.ACOSH:
            return 'ACOSH'
        elif padreID==FUNCION_NATIVA.ATANH:
            return 'ATANH'
        elif padreID==FUNCION_NATIVA.LENGTH:
            return 'LENGTH'
        elif padreID==FUNCION_NATIVA.TRIM:
            return 'TRIM'
        elif padreID==FUNCION_NATIVA.MD5:
            return 'MD5'
        elif padreID==FUNCION_NATIVA.SHA256:
            return 'SHA256'
        elif padreID==FUNCION_NATIVA.DIV:
            return 'DIV'
        elif padreID==FUNCION_NATIVA.GCD:
            return 'GCD'
        elif padreID==FUNCION_NATIVA.MOD:
            return 'MOD'
        elif padreID==FUNCION_NATIVA.POWER:
            return 'POWER'
        elif padreID==FUNCION_NATIVA.ATAN2:
            return 'ATAN2'
        elif padreID==FUNCION_NATIVA.ATAN2D:
            return 'ATAN2D'
        elif padreID==FUNCION_NATIVA.GET_BYTE:
            return 'GET_BYTE'
        elif padreID==FUNCION_NATIVA.ENCODE:
            return 'ENCODE'
        elif padreID==FUNCION_NATIVA.DECODE:
            return 'DECODE'
        elif padreID==CONDICIONAL_SUBQUERY.ANY:
            return 'ANY'
        elif padreID==CONDICIONAL_SUBQUERY.ALL:
            return 'ALL'
        elif padreID==CONDICIONAL_SUBQUERY.SOME:
            return 'SOME'
        elif padreID==FUNCION_NATIVA.SUBSTRING:
            return 'SUBSTRING'
        elif padreID==FUNCION_NATIVA.SUBSTR:
            return 'SUBSTR'
        elif padreID==FUNCION_NATIVA.SET_BYTE:
            return 'SET_BYTE'
        elif padreID==FUNCION_NATIVA.WIDTH_BUCKET:
            return 'WIDTH_BUCKET'
        elif padreID == OPERACION_ARITMETICA.CUBICA:
            return '||'
        elif padreID==OPERACION_ARITMETICA.CUADRATICA:
            return '|'
        elif padreID==OPERACION_ARITMETICA.POTENCIA:
            return '^'
        else:
            return 'op'



