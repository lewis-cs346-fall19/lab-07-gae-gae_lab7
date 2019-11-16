import webapp2
import passwords
import MySQLdb
import random
import cgi
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/html"
        if self.request.cookies.get("visited")==None:
            self.response.write("You will be given a cookiee. <br> Please enter a username:<form action='/' method='post'><input type='text' name='username'><input type='submit' value='Submit'></form>")
        else:
            conn=MySQLdb.connect(unix_socket = passwords.SQL_HOST,
                    user = passwords.SQL_USER,
                    passwd = passwords.SQL_PASS,
                    db = 'Lab7')
            id_checker = self.request.cookies.get("visited")
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM sessions WHERE id='"+id_checker+"'")
            username = cursor.fetchall()
            if username==None:
                self.response.write("You have yet to submit a username associated with your cookie. Click on the button to do so. <br> <form action='/' method='post'><input type='submit' value='Submit'></form>")
            else:
                self.response.write("Click this button to increment your value. <form action='/' method='get'><input type='submit' value='Submit'></form><br> Current value: '"+value+"'<br>")
                cursor.execute("UPDATE Increments SET value=value+1 WHERE user=" + username + ";")
                cursor.commit()
    def post(self):
        username = self.request.POST.get('username')
        self.response.headers["Content-Type"]="text/html"
        conn=MySQLdb.connect(unix_socket=passwords.SQL_HOST,
                user = passwords.SQL_USER,
                passwd = passwords.SQL_PASS,
                db = 'Lab7')
        cursor = conn.cursor()
        random_id = "%032x" % random.getrandbits(128)
        self.response.set_cookie("visited",random_id,max_age=1800)
        cursor.execute("INSERT INTO sessions (id,username) VALUES ('"+random_id+"','"+username+"')")
        cursor.execute("INSERT INTO Increments (username,value) VALUES ('"+username+"',0)")
        conn.commit()
        cursor.close()
        self.response.write("Your username has been added to the database and you have been given a cookie. <br> Please press the button to continue. <form action='/' method='get'><input type='submit' value='Submit'></form>")


app = webapp2.WSGIApplication([("/", MainPage),], debug=True)
