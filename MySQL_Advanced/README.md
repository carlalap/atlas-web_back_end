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

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Email validation to sent
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
  <div class="task_progress_score_bar" data-task-id="19834" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Write a SQL script that creates a trigger that resets the attribute <code>valid_email</code> only when the <code>email</code> has been changed.</p>

<p><strong>Context:</strong>
<em>Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!</em></p>

<pre><code>bob@dylan:~$ cat 5-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES (&quot;bob@dylan.com&quot;, &quot;Bob&quot;);
INSERT INTO users (email, name, valid_email) VALUES (&quot;sylvie@dylan.com&quot;, &quot;Sylvie&quot;, 1);
INSERT INTO users (email, name, valid_email) VALUES (&quot;jeanne@dylan.com&quot;, &quot;Jeanne&quot;, 1);

bob@dylan:~$ 
bob@dylan:~$ cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql
Enter password: 
-- Show users and update (or not) email
SELECT * FROM users;

UPDATE users SET valid_email = 1 WHERE email = &quot;bob@dylan.com&quot;;
UPDATE users SET email = &quot;sylvie+new@dylan.com&quot; WHERE email = &quot;sylvie@dylan.com&quot;;
UPDATE users SET name = &quot;Jannis&quot; WHERE email = &quot;jeanne@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT * FROM users;

UPDATE users SET email = &quot;bob@dylan.com&quot; WHERE email = &quot;bob@dylan.com&quot;;

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Add bonus
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
  <div class="task_progress_score_bar" data-task-id="19835" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Write a SQL script that creates a stored procedure <code>AddBonus</code> that adds a new correction for a student.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>AddBonus</code> is taking 3 inputs (in this order):

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
<li><code>project_name</code>, a new or already exists <code>projects</code> - if no <code>projects.name</code> found in the table, you should create it</li>
<li><code>score</code>, the score value for the correction</li>
</ul></li>
</ul>

<p><strong>Context:</strong>
<em>Write code in SQL is a nice level up!</em></p>

<pre><code>bob@dylan:~$ cat 6-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 6-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql
Enter password: 
-- Show and add bonus correction
SELECT * FROM projects;
SELECT * FROM corrections;

SELECT &quot;--&quot;;

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Python is cool&quot;, 100);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;Bonus project&quot;, 100);
CALL AddBonus((SELECT id FROM users WHERE name = &quot;Bob&quot;), &quot;Bonus project&quot;, 10);

CALL AddBonus((SELECT id FROM users WHERE name = &quot;Jeanne&quot;), &quot;New bonus&quot;, 90);

SELECT &quot;--&quot;;

SELECT * FROM projects;
SELECT * FROM corrections;

bob@dylan:~$ 
bob@dylan:~$ cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Average score
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="19836" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Write a SQL script that creates a stored procedure <code>ComputeAverageScoreForUser</code> that computes and store the average score for a student.
Note: An average score can be a decimal</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Procedure <code>ComputeAverageScoreForUser</code> is taking 1 input:

<ul>
<li><code>user_id</code>, a <code>users.id</code> value (you can assume <code>user_id</code> is linked to an existing <code>users</code>)</li>
</ul></li>
</ul>

<pre><code>bob@dylan:~$ cat 7-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES (&quot;Bob&quot;);
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES (&quot;Jeanne&quot;);
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;C is fun&quot;);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES (&quot;Python is cool&quot;);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 7-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-average_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql
-- Show and compute average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT &quot;--&quot;;
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = &quot;Jeanne&quot;));

SELECT &quot;--&quot;;
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 7-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$ 
</code></pre>
</div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Optimize simple search
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="19837" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Write a SQL script that creates an index <code>idx_name_first</code> on the table <code>names</code> and the first letter of <code>name</code>.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip" title="names.sql.zip" target="_blank">names.sql.zip</a></li>
<li>Only the first letter of <code>name</code> must be indexed</li>
</ul>

<p><strong>Context:</strong>
<em>Index is not the solution for any performance issue, but well used, it&rsquo;s really powerful!</em></p>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39;;
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Optimize search and score
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="19838" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
   <p>Write a SQL script that creates an index <code>idx_name_first_score</code> on the table <code>names</code> and the first letter of <code>name</code> and the <code>score</code>.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Import this table dump: <a href="https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip" title="names.sql.zip" target="_blank">names.sql.zip</a></li>
<li>Only the first letter of <code>name</code> AND <code>score</code> must be indexed</li>
</ul>

<pre><code>bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 9-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql&gt; SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql&gt; 
mysql&gt; SELECT COUNT(name) FROM names WHERE name LIKE &#39;a%&#39; AND score &lt; 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql&gt; 
mysql&gt; exit
bye
bob@dylan:~$ 
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Safe divide
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
  <div class="task_progress_score_bar" data-task-id="19839" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Write a SQL script that creates a function <code>SafeDiv</code> that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>You must create a function</li>
<li>The function <code>SafeDiv</code> takes 2 arguments:

<ul>
<li><code>a</code>, INT</li>
<li><code>b</code>, INT</li>
</ul></li>
<li>And returns <code>a / b</code> or 0 if <code>b == 0</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 10-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 10-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 10-div.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT (a / b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT SafeDiv(a, b) FROM numbers;&quot; | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. No table for a meeting
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="19840" data-correction-id="707751">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Write a SQL script that creates a view <code>need_meeting</code> that lists all students that have a score under 80 (strict) and no <code>last_meeting</code> or more than 1 month.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>The view <code>need_meeting</code> should return all students name when:

<ul>
<li>They score are under (strict) to 80</li>
<li><strong>AND</strong> no <code>last_meeting</code> date <strong>OR</strong> more than a month</li>
</ul></li>
</ul>

<pre><code>bob@dylan:~$ cat 11-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES (&quot;Bob&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Sylvia&quot;, 120);
INSERT INTO students (name, score) VALUES (&quot;Jean&quot;, 60);
INSERT INTO students (name, score) VALUES (&quot;Steeve&quot;, 50);
INSERT INTO students (name, score) VALUES (&quot;Camilia&quot;, 80);
INSERT INTO students (name, score) VALUES (&quot;Alexa&quot;, 130);

bob@dylan:~$ cat 11-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql
-- Test view
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 40 WHERE name = &#39;Bob&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET score = 80 WHERE name = &#39;Steeve&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = CURDATE() WHERE name = &#39;Jean&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = &#39;Jean&#39;;
SELECT * FROM need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE need_meeting;

SELECT &quot;--&quot;;

SHOW CREATE TABLE students;

bob@dylan:~$ 
bob@dylan:~$ cat 11-main.sql | mysql -uroot -p holberton
Enter password: 
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character_set_client    collation_connection
XXXXXX&lt;yes, here it will display the View SQL statement :-) &gt;XXXXXX
--
--
Table   Create Table
students    CREATE TABLE `students` (\n  `name` varchar(255) NOT NULL,\n  `score` int(11) DEFAULT &#39;0&#39;,\n  `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$ 
</code></pre>

  </div>
