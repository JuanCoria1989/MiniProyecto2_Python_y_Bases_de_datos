# importamos la libreria de mysql
import mysql.connector as db
import csv

# creamos una conexión con el la base de datos creada en mysql
bdmysql = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'juan1989',
    database = 'Cine'
)


if __name__ == "__main__":

    #Leyendo el csv actor con las funciones importadas
    with open("actors.csv") as carga_actor:
        leyendoCSV=csv.reader(carga_actor,delimiter=";")
        listaActores=[]
        salto_cabecera=next(leyendoCSV) #Sirver para saltar la cabezera
        for i in leyendoCSV:
            #print("Fila a agregar")
            #print(i)
            listaActores.append(tuple([int(i[0]),i[1],i[2]])) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas


    #Creando cursor para ejecutar query
    mi_cursor= bdmysql.cursor()

    sentenciasql= "INSERT INTO actors (id, first_name, last_name) VALUES (%s, %s, %s)"
    mi_cursor.executemany(sentenciasql,listaActores)
    

    #Leyendo el csv director con las funciones importadas
    with open("directors.csv") as carga_director:
        leyendoCSV=csv.reader(carga_director,delimiter=";")
        listaDirectores=[]
        salto_cabecera=next(leyendoCSV) #Sirver para saltar la cabezera
        for a in leyendoCSV:
            #print("Fila a agregar")
            #print(i)
            listaDirectores.append(tuple([int(a[0]),a[1],a[2]])) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas


    sentenciasql= "INSERT INTO directors (id, first_name, last_name) VALUES (%s, %s, %s)"
    mi_cursor.executemany(sentenciasql,listaDirectores)
    

    #Leyendo el csv movies con las funciones importadas
    with open("movies.csv") as carga_movies:
        leyendoCSV=csv.reader(carga_movies,delimiter=";")
        listaMovies=[]
        salto_cabecera=next(leyendoCSV) #Sirver para saltar la cabezera
        for b in leyendoCSV:
            listaMovies.append([int(b[0]),b[1],b[2],b[3]]) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas      

    #Transformando el ranking en un valor float y poder ser evaluados en las consultas SQL
    ListaMovie2=[]
    for e in listaMovies:
        if e[3]=="NULL":
            e[3]=0
            ListaMovie2.append(tuple([e[0],e[1],e[2],float(e[3])])) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas
        else:
            ListaMovie2.append(tuple([e[0],e[1],e[2],float(e[3])]))
   
    sentenciasql= "INSERT INTO movies (id, name, year, ranking) VALUES (%s, %s, %s, %s)"
    mi_cursor.executemany(sentenciasql,ListaMovie2)

    with open("movies_actors.csv") as carga_movies_actors:
        leyendoCSV=csv.reader(carga_movies_actors,delimiter=';',quoting=csv.QUOTE_NONE) #Elimino las comillas que estaban generando el error de ingreso a la BD
        lista_movies_actors=[]
        salto_cabecera=next(leyendoCSV) #Sirver para saltar la cabezera

        for c in leyendoCSV:
            #print("Fila a agregar")
            #print(i)
            lista_movies_actors.append(tuple([int(c[0]),int(c[1]),c[2]])) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas
        
    sentenciasql= "INSERT INTO movies_actors (actor_id, movie_id, role) VALUES (%s, %s, %s)"
    mi_cursor.executemany(sentenciasql,lista_movies_actors)

    
    with open("movies_directors.csv") as carga_movies_directors:
        leyendoCSV=csv.reader(carga_movies_directors,delimiter=";")
        lista_movies_directors=[]
        salto_cabecera=next(leyendoCSV) #Sirver para saltar la cabezera
        for c in leyendoCSV:
            #print("Fila a agregar")
            #print(i)
            lista_movies_directors.append(tuple([int(c[0]),int(c[1])])) #Recordar siempre que los datos tienen que ser ingresados en una lista de tuplas

    sentenciasql= "INSERT INTO movie_directors (director_id, movie_id) VALUES (%s, %s)"
    mi_cursor.executemany(sentenciasql,lista_movies_directors)

    bdmysql.commit()