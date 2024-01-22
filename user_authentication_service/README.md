# User authentication service

<p>In the industry, you should <strong>not</strong> implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-user.readthedocs.io/en/latest/" title="Flask-User" target="_blank">Flask-User</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/" title="Flask documentation" target="_blank">Flask documentation</a></li>
<li><a href="https://requests.kennethreitz.org/en/latest/user/quickstart/" title="Requests module" target="_blank">Requests module</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc9110.html" title="HTTP status codes" target="_blank">HTTP status codes</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/PTIhFapJKLUJ76WnfXonkQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to declare API routes in a Flask app</li>
<li>How to get and set cookies</li>
<li>How to retrieve request form data</li>
<li>How to return various HTTP status codes</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>You should use <code>SQLAlchemy</code> 1.3.x</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions should be type annotated</li>
<li>The flask app should only interact with <code>Auth</code> and never with <code>DB</code> directly.</li>
<li>Only public methods of <code>Auth</code> and <code>DB</code> should be used outside these classes</li>
</ul>

<h2>Setup</h2>

<p>You will need to install <code>bcrypt</code></p>

<pre><code>pip3 install bcrypt
</code></pre>

  </div>
</div>

<h2 class="gap">Tasks</h2>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. User model
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task you will create a SQLAlchemy model named <code>User</code> for a database table named <code>users</code> (by using the <a href="/rltoken/GfLP1eOPDGnc6J9hkw0CeA" title="mapping declaration" target="_blank">mapping declaration</a> of SQLAlchemy). </p>

<p>The model will have the following attributes:</p>

<ul>
<li><code>id</code>, the integer primary key</li>
<li><code>email</code>, a non-nullable string</li>
<li><code>hashed_password</code>, a non-nullable string</li>
<li><code>session_id</code>, a nullable string</li>
<li><code>reset_token</code>, a nullable string</li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print(&quot;{}: {}&quot;.format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. create user
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will complete the <code>DB</code> class provided below to implement the <code>add_user</code> method.</p>

<pre><code class="python">&quot;&quot;&quot;DB module
&quot;&quot;&quot;
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    &quot;&quot;&quot;DB class
    &quot;&quot;&quot;

    def __init__(self) -&gt; None:
        &quot;&quot;&quot;Initialize a new DB instance
        &quot;&quot;&quot;
        self._engine = create_engine(&quot;sqlite:///a.db&quot;, echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -&gt; Session:
        &quot;&quot;&quot;Memoized session object
        &quot;&quot;&quot;
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
</code></pre>

<p>Note that <code>DB._session</code> is a private property and hence should NEVER be used from outside the <code>DB</code> class.</p>

<p>Implement the <code>add_user</code> method, which has two required string arguments: <code>email</code> and <code>hashed_password</code>, and returns a <code>User</code> object. The method should save the user to the database. No validations are required at this stage.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user(&quot;test@test.com&quot;, &quot;SuperHashedPwd&quot;)
print(user_1.id)

user_2 = my_db.add_user(&quot;test1@test.com&quot;, &quot;SuperHashedPwd1&quot;)
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Find user
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task you will implement the <code>DB.find_user_by</code> method. This method takes in arbitrary keyword arguments and returns the first row found in the <code>users</code> table as filtered by the method&rsquo;s input arguments. No validation of input arguments required at this point.</p>

<p>Make sure that SQLAlchemy&rsquo;s <code>NoResultFound</code> and <code>InvalidRequestError</code> are raised when no results are found, or when wrong query arguments are passed, respectively.</p>

<p><strong>Warning:</strong></p>

<ul>
<li> <code>NoResultFound</code> has been moved from <code>sqlalchemy.orm.exc</code> to <code>sqlalchemy.exc</code> between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from <code>sqlalchemy.orm.exc</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user(&quot;test@test.com&quot;, &quot;PwdHashed&quot;)
print(user.id)

find_user = my_db.find_user_by(email=&quot;test@test.com&quot;)
print(find_user.id)

try:
    find_user = my_db.find_user_by(email=&quot;test2@test.com&quot;)
    print(find_user.id)
except NoResultFound:
    print(&quot;Not found&quot;)

try:
    find_user = my_db.find_user_by(no_email=&quot;test@test.com&quot;)
    print(find_user.id)
except InvalidRequestError:
    print(&quot;Invalid&quot;)        

bob@dylan:~$ python3 main.py
1
1
Not found
Invalid
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. update user
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task, you will implement the <code>DB.update_user</code> method that takes as argument a required <code>user_id</code> integer and arbitrary keyword arguments, and returns <code>None</code>.</p>

<p>The method will use <code>find_user_by</code> to locate the user to update, then will update the user&rsquo;s attributes as passed in the method&rsquo;s arguments then commit changes to the database.</p>

<p>If an argument that does not correspond to a user attribute is passed, raise a <code>ValueError</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = &#39;test@test.com&#39;
hashed_password = &quot;hashedPwd&quot;

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password=&#39;NewPwd&#39;)
    print(&quot;Password updated&quot;)
except ValueError:
    print(&quot;Error&quot;)

bob@dylan:~$ python3 main.py
1
Password updated
bob@dylan:~$ 
</code></pre>
  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Hash password
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task you will define a <code>_hash_password</code> method that takes in a <code>password</code> string arguments and returns bytes.</p>

<p>The returned bytes is a salted hash of the input password, hashed with <code>bcrypt.hashpw</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from auth import _hash_password

print(_hash_password(&quot;Hello Holberton&quot;))

bob@dylan:~$ python3 main.py
b&#39;$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2&#39;
bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Register user
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement the <code>Auth.register_user</code> in the <code>Auth</code> class provided below:</p>

<pre><code class="python">from db import DB


class Auth:
    &quot;&quot;&quot;Auth class to interact with the authentication database.
    &quot;&quot;&quot;

    def __init__(self):
        self._db = DB()
</code></pre>

<p>Note that <code>Auth._db</code> is a private property and should NEVER be used from outside the class.</p>

<p><code>Auth.register_user</code> should take mandatory <code>email</code> and <code>password</code> string arguments and return a <code>User</code> object.</p>

<p>If a user already exist with the passed email, raise a <code>ValueError</code> with the message <code>User &lt;user&#39;s email&gt; already exists</code>.</p>

<p>If not, hash the password with <code>_hash_password</code>, save the user to the database using <code>self._db</code> and return the <code>User</code> object.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from auth import Auth

email = &#39;me@me.com&#39;
password = &#39;mySecuredPwd&#39;

auth = Auth()

try:
    user = auth.register_user(email, password)
    print(&quot;successfully created a new user!&quot;)
except ValueError as err:
    print(&quot;could not create a new user: {}&quot;.format(err))

try:
    user = auth.register_user(email, password)
    print(&quot;successfully created a new user!&quot;)
except ValueError as err:
    print(&quot;could not create a new user: {}&quot;.format(err))        

bob@dylan:~$ python3 main.py
successfully created a new user!
could not create a new user: User me@me.com already exists
bob@dylan:~$
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Basic Flask app
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
   <p>In this task, you will set up a basic Flask app.</p>

<p>Create a Flask app that has a single <code>GET</code> route (<code>&quot;/&quot;</code>) and use <code>flask.jsonify</code> to return a JSON payload of the form:</p>

<pre><code class="json">{&quot;message&quot;: &quot;Bienvenue&quot;}
</code></pre>

<p>Add the following code at the end of the module:</p>

<pre><code>if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, port=&quot;5000&quot;)
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Register user
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement the end-point to register a user. Define a <code>users</code> function that implements the <code>POST /users</code> route.</p>

<p>Import the <code>Auth</code> object and instantiate it at the root of the module as such:</p>

<pre><code class="python">from auth import Auth


AUTH = Auth()
</code></pre>

<p>The end-point should expect two form data fields: <code>&quot;email&quot;</code> and <code>&quot;password&quot;</code>. If the user does not exist, the end-point should register it and respond with the following JSON payload:</p>

<pre><code class="json">{&quot;email&quot;: &quot;&lt;registered email&gt;&quot;, &quot;message&quot;: &quot;user created&quot;}
</code></pre>

<p>If the user is already registered, catch the exception and return a JSON payload of the form</p>

<pre><code class="json">{&quot;message&quot;: &quot;email already registered&quot;}
</code></pre>

<p>and return a 400 status code</p>

<p>Remember that you should only use <code>AUTH</code> in this app. <code>DB</code> is a lower abstraction that is proxied by <code>Auth</code>.</p>

<p><em>Terminal 1:</em></p>

<pre><code>bob@dylan:~$ python3 app.py 
* Serving Flask app &quot;app&quot; (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

</code></pre>

<p>Terminal 2:</p>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/users -d &#39;email=bob@me.com&#39; -d &#39;password=mySuperPwd&#39; -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /users HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 40
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 52
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:03:18 GMT
&lt; 
{&quot;email&quot;:&quot;bob@me.com&quot;,&quot;message&quot;:&quot;user created&quot;}

bob@dylan:~$
bob@dylan:~$ curl -XPOST localhost:5000/users -d &#39;email=bob@me.com&#39; -d &#39;password=mySuperPwd&#39; -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /users HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 40
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 400 BAD REQUEST
&lt; Content-Type: application/json
&lt; Content-Length: 39
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:03:33 GMT
&lt; 
{&quot;message&quot;:&quot;email already registered&quot;}
bob@dylan:~$
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Credentials validation
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement the <code>Auth.valid_login</code> method. It should expect <code>email</code> and <code>password</code> required arguments and return a boolean.</p>

<p>Try locating the user by email. If it exists, check the password with <code>bcrypt.checkpw</code>. If it matches return <code>True</code>. In any other case, return <code>False</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from auth import Auth

email = &#39;bob@bob.com&#39;
password = &#39;MyPwdOfBob&#39;
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, &quot;WrongPwd&quot;))

print(auth.valid_login(&quot;unknown@email&quot;, password))

bob@dylan:~$ python3 main.py
True
False
False
bob@dylan:~$ 
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Generate UUIDs
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task you will implement a <code>_generate_uuid</code> function in the <code>auth</code> module. The function should return a string representation of a new UUID. Use the <code>uuid</code> module.</p>

<p>Note that the method is private to the <code>auth</code> module and should <strong>NOT</strong> be used outside of it.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Get session ID
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task, you will implement the <code>Auth.create_session</code> method. It takes an <code>email</code> string argument and returns the session ID as a string.</p>

<p>The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user&rsquo;s <code>session_id</code>, then return the session ID.</p>

<p>Remember that only public methods of <code>self._db</code> can be used.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from auth import Auth

email = &#39;bob@bob.com&#39;
password = &#39;MyPwdOfBob&#39;
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session(&quot;unknown@email.com&quot;))

bob@dylan:~$ python3 main.py
5a006849-343e-4a48-ba4e-bbd523fcca58
None
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Log in
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement a <code>login</code> function to respond to the <code>POST /sessions</code> route.</p>

<p>The request is expected to contain form data with <code>&quot;email&quot;</code> and a <code>&quot;password&quot;</code> fields.</p>

<p>If the login information is incorrect, use <code>flask.abort</code> to respond with a 401 HTTP status.</p>

<p>Otherwise, create a new session for the user, store it the session ID as a cookie with key <code>&quot;session_id&quot;</code> on the response and return a JSON payload of the form</p>

<pre><code class="json">{&quot;email&quot;: &quot;&lt;user email&gt;&quot;, &quot;message&quot;: &quot;logged in&quot;}
</code></pre>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/users -d &#39;email=bob@bob.com&#39; -d &#39;password=mySuperPwd&#39;
{&quot;email&quot;:&quot;bob@bob.com&quot;,&quot;message&quot;:&quot;user created&quot;}
bob@dylan:~$ 
bob@dylan:~$  curl -XPOST localhost:5000/sessions -d &#39;email=bob@bob.com&#39; -d &#39;password=mySuperPwd&#39; -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 37
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 46
&lt; Set-Cookie: session_id=163fe508-19a2-48ed-a7c8-d9c6e56fabd1; Path=/
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:12:34 GMT
&lt; 
{&quot;email&quot;:&quot;bob@bob.com&quot;,&quot;message&quot;:&quot;logged in&quot;}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl -XPOST localhost:5000/sessions -d &#39;email=bob@bob.com&#39; -d &#39;password=BlaBla&#39; -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 34
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 34 out of 34 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 401 UNAUTHORIZED
&lt; Content-Type: text/html; charset=utf-8
&lt; Content-Length: 338
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:12:45 GMT
&lt; 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;401 Unauthorized&lt;/title&gt;
&lt;h1&gt;Unauthorized&lt;/h1&gt;
&lt;p&gt;The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn&#39;t understand how to supply the credentials required.&lt;/p&gt;
* Closing connection 0
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Find user by session ID
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement the <code>Auth.get_user_from_session_id</code> method. It takes a single <code>session_id</code> string argument and returns the corresponding <code>User</code> or <code>None</code>.</p>

<p>If the session ID is <code>None</code> or no user is found, return <code>None</code>. Otherwise return the corresponding user.</p>

<p>Remember to only use public methods of <code>self._db</code>.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      13. Destroy session
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement <code>Auth.destroy_session</code>. The method takes a single <code>user_id</code> integer argument and returns <code>None</code>.</p>

<p>The method updates the corresponding user&rsquo;s session ID to <code>None</code>.</p>

<p>Remember to only use public methods of <code>self._db</code>.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      14. Log out
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In this task, you will implement a <code>logout</code> function to respond to the <code>DELETE /sessions</code> route.</p>

<p>The request is expected to contain the session ID as a cookie with key <code>&quot;session_id&quot;</code>.</p>

<p>Find the user with the requested session ID. If the user exists destroy the session and redirect the user to <code>GET /</code>. If the user does not exist, respond with a 403 HTTP status.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      15. User profile
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
  <p>In this task, you will implement a <code>profile</code> function to respond to the <code>GET /profile</code> route.</p>

<p>The request is expected to contain a <code>session_id</code> cookie. Use it to find the user. If the user exist, respond with a 200 HTTP status and the following JSON payload:</p>

<pre><code class="json">{&quot;email&quot;: &quot;&lt;user email&gt;&quot;}
</code></pre>

<p>If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.</p>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/sessions -d &#39;email=bob@bob.com&#39; -d &#39;password=mySuperPwd&#39; -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 37
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 46
&lt; Set-Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a1; Path=/
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:15:57 GMT
&lt; 
{&quot;email&quot;:&quot;bob@bob.com&quot;,&quot;message&quot;:&quot;logged in&quot;}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl -XGET localhost:5000/profile -b &quot;session_id=75c89af8-1729-44d9-a592-41b5e59de9a1&quot;
{&quot;email&quot;: &quot;bob@bob.com&quot;}
bob@dylan:~$ 
bob@dylan:~$ curl -XGET localhost:5000/profile -b &quot;session_id=nope&quot; -v
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; GET /profile HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 403 FORBIDDEN
&lt; Content-Type: text/html; charset=utf-8
&lt; Content-Length: 234
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:16:43 GMT
&lt; 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;403 Forbidden&lt;/title&gt;
&lt;h1&gt;Forbidden&lt;/h1&gt;
&lt;p&gt;You don&#39;t have the permission to access the requested resource. It is either read-protected or not readable by the server.&lt;/p&gt;
* Closing connection 0

bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      16. Generate reset password token
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task, you will implement the <code>Auth.get_reset_password_token</code> method. It take an <code>email</code> string argument and returns a string.</p>

<p>Find the user corresponding to the email. If the user does not exist, raise a <code>ValueError</code> exception. If it exists, generate a UUID and update the user&rsquo;s <code>reset_token</code> database field. Return the token.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      17. Get reset password token
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task, you will implement a <code>get_reset_password_token</code> function to respond to the <code>POST /reset_password</code> route.</p>

<p>The request is expected to contain form data with the <code>&quot;email&quot;</code> field.</p>

<p>If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:</p>

<pre><code class="json">{&quot;email&quot;: &quot;&lt;user email&gt;&quot;, &quot;reset_token&quot;: &quot;&lt;reset token&gt;&quot;}
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      18. Update password
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task, you will implement the <code>Auth.update_password</code> method. It takes <code>reset_token</code> string argument and a <code>password</code> string argument and returns <code>None</code>.</p>

<p>Use the <code>reset_token</code> to find the corresponding user. If it does not exist, raise a <code>ValueError</code> exception.</p>

<p>Otherwise, hash the password and update the user&rsquo;s <code>hashed_password</code> field with the new hashed password and the <code>reset_token</code> field to <code>None</code>.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      19. Update password end-point
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In this task you will implement the <code>update_password</code> function in the <code>app</code> module to respond to the <code>PUT /reset_password</code> route.</p>

<p>The request is expected to contain form data with fields <code>&quot;email&quot;</code>, <code>&quot;reset_token&quot;</code> and <code>&quot;new_password&quot;</code>.</p>

<p>Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code.</p>

<p>If the token is valid, respond with a 200 HTTP code and the following JSON payload:</p>

<pre><code class="json">{&quot;email&quot;: &quot;&lt;user email&gt;&quot;, &quot;message&quot;: &quot;Password updated&quot;}
</code></pre>

  </div>