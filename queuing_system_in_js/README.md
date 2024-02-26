# Queuing System in JS

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://redis.io/docs/install/install-redis/" title="Redis quick start" target="_blank">Redis quick start</a></li>
<li><a href="https://redis.io/docs/connect/cli/" title="Redis client interface" target="_blank">Redis client interface</a></li>
<li><a href="https://github.com/redis/node-redis" title="Redis client for Node JS" target="_blank">Redis client for Node JS</a></li>
<li><a href="https://github.com/Automattic/kue" title="Kue" target="_blank">Kue</a> <em>deprecated but still use in the industry</em></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/KVesHRrG4OE8kHXfVkojZw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to run a Redis server on your machine</li>
<li>How to run simple operations with the Redis client</li>
<li>How to use a Redis client with Node JS for basic operations</li>
<li>How to store hash values in Redis</li>
<li>How to deal with async operations with Redis</li>
<li>How to use Kue as a queue system</li>
<li>How to build a basic Express app interacting with a Redis server</li>
<li>How to the build a basic Express app interacting with a Redis server and queue</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7</li>
<li>All of your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
</ul>

<h2>Required Files for the Project</h2>

<h3><code>package.json</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
<pre>
<code>
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
</code>
</pre>
</details>

<h3><code>.babelrc</code></h3>

<details>
<summary>
Click to show/hide file contents
</summary>
<pre>
<code> 
{
  "presets": [
    "@babel/preset-env"
  ]
}
</code>
</pre>
</details>

<h3>and&hellip;</h3>

<p>Don&rsquo;t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>

  </div>
</div>

<h2 class="gap">Tasks</h2>

    <div data-role="task21792" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-21792">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Install a redis instance
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - <a href="/rltoken/pavamO3EvDlmNlqOmhm4mQ" title="https://redis.io/download/" target="_blank">https://redis.io/download/</a>):</p>

<pre><code>$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
</code></pre>

<ul>
<li>Start Redis in the background with <code>src/redis-server</code></li>
</ul>

<pre><code>$ src/redis-server &amp;
</code></pre>

<ul>
<li>Make sure that the server is working with a ping <code>src/redis-cli ping</code></li>
</ul>

<pre><code>PONG
</code></pre>

<ul>
<li>Using the Redis client again, set the value <code>School</code> for the key <code>Holberton</code></li>
</ul>

<pre><code>127.0.0.1:[Port]&gt; set Holberton School
OK
127.0.0.1:[Port]&gt; get Holberton
&quot;School&quot;
</code></pre>

<ul>
<li>Kill the server with the process id of the redis-server (hint: use <code>ps</code> and <code>grep</code>)</li>
</ul>

<pre><code>$ kill [PID_OF_Redis_Server]
</code></pre>

<p>Copy the <code>dump.rdb</code> from the <code>redis-5.0.7</code> directory into the root of the Queuing project.</p>

<p>Requirements:</p>

<ul>
<li>Running <code>get Holberton</code> in the client, should return <code>School</code></li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Node Redis Client
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
 <p>Install <a href="/rltoken/y1WPXQxH-S7Op_P2bh7dPg" title="node_redis" target="_blank">node_redis</a> using npm</p>

<p>Using Babel and ES6, write a script named <code>0-redis_client.js</code>. It should connect to the Redis server running on your machine:</p>

<ul>
<li>It should log to the console the message <code>Redis client connected to the server</code> when the connection to Redis works correctly</li>
<li>It should log to the console the message <code>Redis client not connected to the server: ERROR_MESSAGE</code> when the connection to Redis does not work</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>To import the library, you need to use the keyword <code>import</code></li>
</ul>

<pre><code>bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;0-redis_client.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server &gt; /dev/null 2&gt;&amp;1 &amp;
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;0-redis_client.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Node Redis client and basic operations
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In a file <code>1-redis_op.js</code>, copy the code you previously wrote (<code>0-redis_client.js</code>). </p>

<p>Add two functions:</p>

<ul>
<li><code>setNewSchool</code>:

<ul>
<li>It accepts two arguments <code>schoolName</code>, and <code>value</code>. </li>
<li>It should set in Redis the value for the key <code>schoolName</code></li>
<li>It should display a confirmation message using <code>redis.print</code></li>
</ul></li>
<li><code>displaySchoolValue</code>:

<ul>
<li>It accepts one argument <code>schoolName</code>. </li>
<li>It should log to the console the value for the key passed as argument</li>
</ul></li>
</ul>

<p>At the end of the file, call:</p>

<ul>
<li><code>displaySchoolValue(&#39;Holberton&#39;);</code></li>
<li><code>setNewSchool(&#39;HolbertonSanFrancisco&#39;, &#39;100&#39;);</code></li>
<li><code>displaySchoolValue(&#39;HolbertonSanFrancisco&#39;);</code></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>Use callbacks for any of the operation, we will look at async operations later</li>
</ul>

<pre><code>bob@dylan:~$ npm run dev 1-redis_op.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;1-redis_op.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Node Redis client and basic operations
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In a file <code>1-redis_op.js</code>, copy the code you previously wrote (<code>0-redis_client.js</code>). </p>

<p>Add two functions:</p>

<ul>
<li><code>setNewSchool</code>:

<ul>
<li>It accepts two arguments <code>schoolName</code>, and <code>value</code>. </li>
<li>It should set in Redis the value for the key <code>schoolName</code></li>
<li>It should display a confirmation message using <code>redis.print</code></li>
</ul></li>
<li><code>displaySchoolValue</code>:

<ul>
<li>It accepts one argument <code>schoolName</code>. </li>
<li>It should log to the console the value for the key passed as argument</li>
</ul></li>
</ul>

<p>At the end of the file, call:</p>

<ul>
<li><code>displaySchoolValue(&#39;Holberton&#39;);</code></li>
<li><code>setNewSchool(&#39;HolbertonSanFrancisco&#39;, &#39;100&#39;);</code></li>
<li><code>displaySchoolValue(&#39;HolbertonSanFrancisco&#39;);</code></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>Use callbacks for any of the operation, we will look at async operations later</li>
</ul>

<pre><code>bob@dylan:~$ npm run dev 1-redis_op.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;1-redis_op.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Node Redis client and async operations
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

<!-- Task Body -->
<p>In a file <code>2-redis_op_async.js</code>, let&rsquo;s copy the code from the previous exercise (<code>1-redis_op.js</code>)</p>

<p>Using <code>promisify</code>, modify the function <code>displaySchoolValue</code> to use ES6 <code>async / await</code></p>

<p>Same result as <code>1-redis_op.js</code></p>

<pre><code>bob@dylan:~$ npm run dev 2-redis_op_async.js

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;2-redis_op_async.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Node Redis client and advanced operations
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In a file named <code>4-redis_advanced_op.js</code>, let&rsquo;s use the client to store a hash value</p>

<h4>Create Hash:</h4>

<p>Using <code>hset</code>, let&rsquo;s store the following:</p>

<ul>
<li>The key of the hash should be <code>HolbertonSchools</code></li>
<li>It should have a value for:

<ul>
<li><code>Portland=50</code></li>
<li><code>Seattle=80</code></li>
<li><code>New York=20</code></li>
<li><code>Bogota=20</code></li>
<li><code>Cali=40</code></li>
<li><code>Paris=2</code></li>
</ul></li>
<li>Make sure you use <code>redis.print</code> for each <code>hset</code></li>
</ul>

<h4>Display Hash:</h4>

<p>Using <code>hgetall</code>, display the object stored in Redis. It should return the following:</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>Use callbacks for any of the operation, we will look at async operations later</li>
</ul>

<pre><code>bob@dylan:~$ npm run dev 4-redis_advanced_op.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;4-redis_advanced_op.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: &#39;50&#39;,
  Seattle: &#39;80&#39;,
  &#39;New York&#39;: &#39;20&#39;,
  Bogota: &#39;20&#39;,
  Cali: &#39;40&#39;,
  Paris: &#39;2&#39;
}
^C
bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Node Redis client publisher and subscriber
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->
   <!-- Task Body -->
   <p>In a file named <code>5-subscriber.js</code>, create a redis client:</p>

<ul>
<li>On connect, it should log the message <code>Redis client connected to the server</code></li>
<li>On error, it should log the message <code>Redis client not connected to the server: ERROR MESSAGE</code></li>
<li>It should subscribe to the channel <code>holberton school channel</code></li>
<li>When it receives message on the channel <code>holberton school channel</code>, it should log the message to the console</li>
<li>When the message is <code>KILL_SERVER</code>, it should unsubscribe and quit</li>
</ul>

<p>In a file named <code>5-publisher.js</code>, create a redis client:</p>

<ul>
<li>On connect, it should log the message <code>Redis client connected to the server</code></li>
<li>On error, it should log the message <code>Redis client not connected to the server: ERROR MESSAGE</code></li>
<li>Write a function named <code>publishMessage</code>:

<ul>
<li>It will take two arguments: <code>message</code> (string), and <code>time</code> (integer - in ms)</li>
<li>After <code>time</code> millisecond:

<ul>
<li>The function should log to the console <code>About to send MESSAGE</code></li>
<li>The function should publish to the channel <code>holberton school channel</code>, the message passed in argument after the time passed in arguments</li>
</ul></li>
</ul></li>
<li>At the end of the file, call:</li>
</ul>

<pre><code>publishMessage(&quot;Holberton Student #1 starts course&quot;, 100);
publishMessage(&quot;Holberton Student #2 starts course&quot;, 200);
publishMessage(&quot;KILL_SERVER&quot;, 300);
publishMessage(&quot;Holberton Student #3 starts course&quot;, 400);
</code></pre>

<p><strong>Requirements:</strong></p>

<ul>
<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
</ul>

<p><strong>Terminal 1:</strong></p>

<pre><code>bob@dylan:~$ npm run dev 5-subscriber.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;5-subscriber.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
</code></pre>

<p><strong>Terminal 2:</strong></p>

<pre><code>bob@dylan:~$ npm run dev 5-publisher.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;5-publisher.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$ 
</code></pre>

<p><strong>And in the same time in Terminal 1:</strong></p>

<pre><code>Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$ 
</code></pre>

<p>Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call &ldquo;background workers&rdquo;.</p>

  </div>


