from flask import Flask, request, url_for, redirect, render_template
from flask_mysqldb import MySQL
import mysql.connector
import html
import collections
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

@app.route('/')
def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college"
    )
    mycursor = mydb.cursor()
    tables_names = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='college'"
    mycursor.execute(tables_names)
    tables = mycursor.fetchall()
    myresult = []
    columns = []
    for i in tables:
        names = "SELECT * FROM "+i[0]
        mycursor.execute(names)
        myresult.append(mycursor.fetchall())
        names = "SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '" + \
            i[0]+"' ORDER BY ORDINAL_POSITION"
        mycursor.execute(names)
        columns.append(mycursor.fetchall())
    return render_template('index.html', table=tables, column=columns, data=myresult, n=len(tables))

def queries(query):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("start Time =", current_time)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="college"
    )
    mycursor = mydb.cursor()
    try:
        try:
            if(len(query) == 0):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("end Time =", current_time)
                return [0,"Please Enter Query","","",query]
            if(query.split()[0].lower() == 'drop' and query.split()[1].lower() == 'database'):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("end Time =", current_time)
                return [0,"Drop Database Not Allowed...!!!","","",query]
            if(query.split()[0].lower() == 'select'):
                if(query.split()[1] == '*'):
                    mycursor.execute(query)
                    myresult = mycursor.fetchall()
                    if(len(myresult) == 0):
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        print("end Time =", current_time)
                        return [0,"Table is Empty..!!!","","",query]
                    names = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '" + \
                        query.split()[-1] + \
                        "' ORDER BY ORDINAL_POSITION"
                    mycursor.execute(names)
                    columns = mycursor.fetchall()
                    column = []
                    for i in columns:
                        column.append(i[3])
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("end Time =", current_time)
                    return [2,myresult,len(myresult[0]),column,query]
                else:
                    tables_names = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='college'"
                    mycursor.execute(tables_names)
                    tables = mycursor.fetchall()
                    columns = []
                    for i in tables:
                        names = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '" + \
                            i[0]+"' ORDER BY ORDINAL_POSITION"
                        mycursor.execute(names)
                        columns.append(mycursor.fetchall())
                    column = []
                    a = query.lower().index('from')
                    temp = query.lower()[:a]
                    d = dict()
                    for i in columns:
                        for j in i:
                            if j[3].lower() in temp:
                                t = temp.replace(",", " ")
                                t = t.replace(".", " ")
                                if ' as ' in temp:
                                    if (t.split()[t.split().index(j[3])+1].lower() == 'as'):
                                        d[temp.index(j[3])] = t.split()[
                                            t.split().index(j[3])+2]
                                else:
                                    d[temp.index(j[3])] = j[3]
                                temp = temp.replace(
                                    j[3].lower(), " "*len(j[3].lower()), 1)
                    d = dict(collections.OrderedDict(sorted(d.items())))
                    column = list(d.values())
                    mycursor.execute(query)
                    myresult = mycursor.fetchall()
                    if(len(myresult) == 0):
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        print("end Time =", current_time)
                        return [0,"No Data Avaiable...!!!","","",query]
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("end Time =", current_time)
                    return [2,myresult,len(myresult[0]),column,query]
            elif(query.split()[0].lower() == 'show'):
                mycursor.execute(query)
                myresult = mycursor.fetchall()
                if(len(myresult) == 0):
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("end Time =", current_time)
                    return [0,"Table is Empty..!!!","","",query]
                names = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '" + \
                    query.split()[-1]+"' ORDER BY ORDINAL_POSITION"
                mycursor.execute(names)
                columns = mycursor.fetchall()
                column = []
                for i in columns:
                    column.append(i[3])
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("end Time =", current_time)
                return [2,myresult,len(myresult[0]),column,query]
            else:
                mycursor.execute(query)
                mydb.commit()
                tables_names = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='college'"
                mycursor.execute(tables_names)
                tables = mycursor.fetchall()
                myresult = []
                columns = []
                for i in tables:
                    names = "SELECT * FROM "+i[0]
                    mycursor.execute(names)
                    myresult.append(mycursor.fetchall())
                    names = "SELECT Column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME= '" + \
                        i[0]+"' ORDER BY ORDINAL_POSITION"
                    mycursor.execute(names)
                    columns.append(mycursor.fetchall())
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("end Time =", current_time)
                return [1,tables,columns,myresult,query,len(tables)]
        except mysql.connector.Error as e:
            e = str(e)
            html.unescape(e)
            e = e.replace("college.", "")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("end Time =", current_time)
            return [0,e,"","",query]
    except BaseException:
        logging.exception("ERROR")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("end Time =", current_time)
        return [0,"Something Went Wrong...!!!","","",query]

@app.route('/display', methods=['POST', 'GET'])
def display():
    int_features = [x for x in request.form.values()]
    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in int_features:
            processes.append(executor.submit(queries, i))
    results=[]
    for task in as_completed(processes):
        l=task.result()
        results.append(l)
    # print(results)
    return render_template("output.html",results=results)
        # if(l[0]==0):
        #     return render_template("error.html", error=l[1], query="")
        # elif(l[1]==1):
        #     return render_template('index.html', table=l[1], column=l[2], data=l[3], n=l[4])
        # else:
        #     return render_template("output.html", output=l[1], n=l[2], col=l[3], query=l[4])

if __name__ == '__main__':
    app.run(debug=True)
