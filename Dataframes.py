from CargaBD import bdmysql
import pandas as pd



if __name__=="__main__":
    mi_cursor=bdmysql.cursor()
    #_______________Consulta número 3__________________
    sentenciasql3=   "SELECT m.name as 'Movie',\
                        m.year AS 'Year',\
                        d.last_name AS 'Director',\
                        m.ranking AS 'Ranking'\
                        FROM movies_directors AS md\
                        JOIN movies AS m ON m.id = md.movie_id\
                        JOIN directors AS d ON d.id = md.director_id\
                        WHERE m.ranking >8\
                        ORDER BY m.ranking\
                        DESC;"

    mi_cursor.execute(sentenciasql3)
    filas=mi_cursor.fetchall() # Captura las filas consultadas en la tabla users en la base de datos tambien existe fetchmany y fetchone la primera se indica cuantas filas quiere
    print("-------------------Consulta Nº3.3------------------------------")
    lista=[]
    for i in filas: #Posteriormente la recorremos a travez de un loop
        lista.append(i)
        

    df1=pd.DataFrame(lista, columns=["Pelicula","agno","Director","Puntaje"] )
    print(df1)
    df2=df1.loc[:10,["Pelicula","Puntaje"]] 
    print(df2)

    df1=df1.loc[20:50,["Pelicula","agno","Director","Puntaje"]] 
    print(df1)

