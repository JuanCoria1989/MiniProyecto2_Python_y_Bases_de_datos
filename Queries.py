from CargaBD import bdmysql #Importo la conexión para que no quede a la vista

#Consultas a BD
if __name__== "__main__":
    #_______________Consulta número 1__________________
    mi_cursor= bdmysql.cursor()
    sentenciasql1=   "SELECT d.last_name,\
                    d.first_name,\
                    COUNT(movie_id) AS 'How Many'\
                    FROM movies_directors AS md\
                    JOIN directors AS d ON d.id = md.director_id\
                    GROUP BY d.last_name, d.first_name\
                    HAVING COUNT(movie_id) >3\
                    ORDER BY COUNT(movie_id) DESC;"

    mi_cursor.execute(sentenciasql1)
    filas=mi_cursor.fetchall() # Captura las filas consultadas en la tabla users en la base de datos tambien existe fetchmany y fetchone la primera se indica cuantas filas quiere
    print("-------------------Consulta Nº1------------------------------")
    for i in filas: #Posteriormente la recorremos a travez de un loop
        print(i)

    #_______________Consulta número 2__________________
    sentenciasql2=   "SELECT a.last_name,\
                    a.first_name,\
                    COUNT(movie_id)\
                    FROM actors AS a\
                    JOIN movies_actors AS ma ON ma.actor_id = a.id\
                    GROUP BY a.last_name, a.first_name\
                    HAVING COUNT(movie_id) >3\
                    ORDER BY a.last_name, a.first_name;"

    mi_cursor.execute(sentenciasql2)
    filas=mi_cursor.fetchall() # Captura las filas consultadas en la tabla users en la base de datos tambien existe fetchmany y fetchone la primera se indica cuantas filas quiere
    print("-------------------Consulta Nº2------------------------------")
    for i in filas: #Posteriormente la recorremos a travez de un loop
        print(i)
    
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
    print("-------------------Consulta Nº3------------------------------")
    for i in filas: #Posteriormente la recorremos a travez de un loop
        print(i)