import webapp2
import passwords
import MySQLdb
class MainPage(webapp2.RequestHandler):
    def get(self):
        conn = MySQLdb.connect(unix_socket = "/cloudsql/gae-lab-258923\:us-central1\:labdb",
                user = passwords.SQL_USER,
                passwd = passwords.SQL_PASSWD,
                db = "gaedb")
        cursor = conn.cursor()
        cursor.execute("SELECT user FROM *** WHERE session_id=***;")
        results = cursor.fetchall()
        cursor.close()
        conn.commit()
        username = results[0][0]
        if username != "NULL":
            self.response.write("""<form action='/' method='post' id=buttonform'>
            <button type='submit'>Press to increment</button></form>""")
            cursor = conn.cursor()
            cursor.execute("SELECT values FROM *** WHERE user=" + username + ";")
            values = cursor.fetchall()
            cursor.close()
            conn.commit()
            self.response.write("<br>Current value: " + values[0][0])

    def post(self):
        cursor = conn.cursor()
        cursor.execute("SELECT user FROM *** WHERE session_id=***;")
        results = cursor.fetchall()
        cursor.close()
        conn.commit()
        username = results[0][0]
        if username != "NULL":
            cursor = conn.cursor()
            cursor.execute("UPDATE *** SET values=values+1 WHERE user=" + username + ";")
            
            
        


