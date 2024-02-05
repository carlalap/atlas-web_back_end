# MySQL advanced

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://devhints.io/mysql" title="MySQL cheatsheet" target="_blank">MySQL cheatsheet</a></li>
<li><a href="https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/" title="MySQL Performance: How To Leverage MySQL Database Indexing" target="_blank">MySQL Performance: How To Leverage MySQL Database Indexing</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-procedure.php" title="Stored Procedure" target="_blank">Stored Procedure</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-triggers.php" title="Triggers" target="_blank">Triggers</a></li>
<li><a href="https://www.w3resource.com/mysql/mysql-views.php" title="Views" target="_blank">Views</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/functions.html" title="Functions and Operators" target="_blank">Functions and Operators</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html" title="Trigger Syntax and Examples" target="_blank">Trigger Syntax and Examples</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-table.html" title="CREATE TABLE Statement" target="_blank">CREATE TABLE Statement</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html" title="CREATE PROCEDURE and CREATE FUNCTION Statements" target="_blank">CREATE PROCEDURE and CREATE FUNCTION Statements</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-index.html" title="CREATE INDEX Statement" target="_blank">CREATE INDEX Statement</a></li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/create-view.html" title="CREATE VIEW Statement" target="_blank">CREATE VIEW Statement</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create tables with constraints</li>
<li>How to optimize queries by adding indexes</li>
<li>What is and how to implement stored procedures and functions in MySQL</li>
<li>What is and how to implement views in MySQL</li>
<li>What is and how to implement triggers in MySQL</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be executed on Ubuntu 18.04 LTS using <code>MySQL 5.7</code> (version 5.7.30)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Use &ldquo;container-on-demand&rdquo; to run MySQL</h3>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - Python 3.7</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p
Enter password: 
$ curl &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo &quot;SELECT * FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

  </div>
</div>

<h2 class="gap">Tasks</h2>
  <div data-role="task19829" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19829">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. We are all unique!
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</em></p>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Jean&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry &#39;bob@dylan.com&#39; for key &#39;email&#39;
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. In and not out
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a SQL script that creates a table <code>users</code> following these requirements:</p>

<ul>
<li>With these attributes:

<ul>
<li><code>id</code>, integer, never null, auto increment and primary key</li>
<li><code>email</code>, string (255 characters), never null and unique</li>
<li><code>name</code>, string (255 characters)</li>
<li><code>country</code>, enumeration of countries: <code>US</code>, <code>CO</code> and <code>TN</code>, never null (= default will be the first element of the enumeration, here <code>US</code>)</li>
</ul></li>
<li>If the table already exists, your script should not fail</li>
<li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table &#39;holberton.users&#39; doesn&#39;t exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;, &quot;US&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, &quot;CO&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name, country) VALUES (&quot;jean@dylan.com&quot;, &quot;Jean&quot;, &quot;FR&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column &#39;country&#39; at row 1
bob@dylan:~$ 
bob@dylan:~$ echo &#39;INSERT INTO users (email, name) VALUES (&quot;john@dylan.com&quot;, &quot;John&quot;);&#39; | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT * FROM users;&quot; | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Best band ever!
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240205T031935Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=929657cd10144ba07c20b163f6dd6910ff7b9c4b041535dec0f17be603ee079b" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>origin</code> and <code>nb_fans</code></li>
<li>Your script can be executed on any database</li>
</ul>

<p><strong>Context:</strong>
<em>Calculate/compute something is always power intensive&hellip; better to distribute the load!</em></p>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton &gt; tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Old school band
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a SQL script that lists all bands with <code>Glam rock</code> as their main style, ranked by their longevity</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240205T031935Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=929657cd10144ba07c20b163f6dd6910ff7b9c4b041535dec0f17be603ee079b" title="metal_bands.sql.zip" target="_blank">metal_bands.sql.zip</a></li>
<li>Column names must be: <code>band_name</code> and <code>lifespan</code> (in years)</li>
<li>You should use attributes <code>formed</code> and <code>split</code> for computing the <code>lifespan</code></li>
<li>Your script can be executed on any database</li>
</ul>

<pre><code>bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Buy buy buy
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
  <p>Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.</p>

<p>Quantity in the table <code>items</code> can be negative.</p>

<p><strong>Context:</strong>
<em>Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc&hellip; to keep your data in a good shape, let MySQL do it for you!</em></p>

<pre><code>bob@dylan:~$ cat 4-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES (&quot;apple&quot;), (&quot;pineapple&quot;), (&quot;pear&quot;);

bob@dylan:~$ 
bob@dylan:~$ cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql
Enter password: 
-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 1);
INSERT INTO orders (item_name, number) VALUES (&#39;apple&#39;, 3);
INSERT INTO orders (item_name, number) VALUES (&#39;pear&#39;, 2);

SELECT &quot;--&quot;;

SELECT * FROM items;
SELECT * FROM orders;

bob@dylan:~$ 
bob@dylan:~$ cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
bob@dylan:~$ 
</code></pre>

  </div>
