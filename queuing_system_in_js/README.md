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

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Create the Job creator
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a file named <code>6-job_creator.js</code>:</p>

<ul>
<li>Create a queue with <code>Kue</code></li>
<li>Create an object containing the Job data with the following format:</li>
</ul>

<pre><code>{
  phoneNumber: string,
  message: string,
}
</code></pre>

<ul>
<li>Create a queue named <code>push_notification_code</code>, and create a job with the object created before</li>
<li>When the job is created without error, log to the console <code>Notification job created: JOB ID</code></li>
<li>When the job is completed, log to the console <code>Notification job completed</code></li>
<li>When the job is failing, log to the console <code>Notification job failed</code></li>
</ul>

<pre><code>bob@dylan:~$ npm run dev 6-job_creator.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;6-job_creator.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1

</code></pre>

<p>Nothing else will happen - to process the job, go to the next task!</p>

<p>If you execute multiple time this file, you will see the <code>JOB ID</code> increasing - it means you are storing new job to process&hellip;</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Create the Job processor
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In a file named <code>6-job_processor.js</code>:</p>

<ul>
<li>Create a queue with <code>Kue</code></li>
<li>Create a function named <code>sendNotification</code>:

<ul>
<li>It will take two arguments <code>phoneNumber</code> and <code>message</code></li>
<li>It will log to the console <code>Sending notification to PHONE_NUMBER, with message: MESSAGE</code></li>
</ul></li>
<li>Write the queue process that will listen to new jobs on <code>push_notification_code</code>:

<ul>
<li>Every new job should call the <code>sendNotification</code> function with the phone number and the message contained within the job data</li>
</ul></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
<li>You muse use <code>Kue</code> to set up the queue</li>
</ul>

<p><strong>Terminal 2:</strong></p>

<pre><code>bob@dylan:~$ npm run dev 6-job_processor.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;6-job_processor.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_processor.js`
Sending notification to 4153518780, with message: This is the code to verify your account

</code></pre>

<p><strong>Terminal 1:</strong> let&rsquo;s queue a new job!</p>

<pre><code>bob@dylan:~$ npm run dev 6-job_creator.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;6-job_creator.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 2

</code></pre>

<p><strong>And in the same time in Terminal 2:</strong></p>

<pre><code>Sending notification to 4153518780, with message: This is the code to verify your account
</code></pre>

<p>BOOM! same as <code>5-subscriber.js</code> and <code>5-publisher.js</code> but with a module to manage jobs.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Track progress and errors with Kue: Create the Job creator
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>In a file named <code>7-job_creator.js</code>:</p>

<p>Create an array <code>jobs</code> with the following data inside:</p>

<pre><code>const jobs = [
  {
    phoneNumber: &#39;4153518780&#39;,
    message: &#39;This is the code 1234 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153518781&#39;,
    message: &#39;This is the code 4562 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153518743&#39;,
    message: &#39;This is the code 4321 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153538781&#39;,
    message: &#39;This is the code 4562 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153118782&#39;,
    message: &#39;This is the code 4321 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153718781&#39;,
    message: &#39;This is the code 4562 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4159518782&#39;,
    message: &#39;This is the code 4321 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4158718781&#39;,
    message: &#39;This is the code 4562 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4153818782&#39;,
    message: &#39;This is the code 4321 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4154318781&#39;,
    message: &#39;This is the code 4562 to verify your account&#39;
  },
  {
    phoneNumber: &#39;4151218782&#39;,
    message: &#39;This is the code 4321 to verify your account&#39;
  }
];
</code></pre>

<p>After this array created:</p>

<ul>
<li>Create a queue with <code>Kue</code></li>
<li>Write a loop that will go through the array <code>jobs</code> and for each object:

<ul>
<li>Create a new job to the queue <code>push_notification_code_2</code> with the current object</li>
<li>If there is no error, log to the console <code>Notification job created: JOB_ID</code></li>
<li>On the job completion, log to the console <code>Notification job JOB_ID completed</code></li>
<li>On the job failure, log to the console <code>Notification job JOB_ID failed: ERROR</code></li>
<li>On the job progress, log to the console <code>Notification job JOB_ID PERCENTAGE% complete</code></li>
</ul></li>
</ul>

<p><strong>Terminal 1</strong>:</p>

<pre><code>bob@dylan:~$ npm run dev 7-job_creator.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;7-job_creator.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 39
Notification job created: 40
Notification job created: 41
Notification job created: 42
Notification job created: 43
Notification job created: 44
Notification job created: 45
Notification job created: 46
Notification job created: 47
Notification job created: 48
Notification job created: 49

</code></pre>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Track progress and errors with Kue: Create the Job processor
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a file named <code>7-job_processor.js</code>:</p>

<p>Create an array that will contain the blacklisted phone numbers. Add in it <code>4153518780</code> and <code>4153518781</code> - these 2 numbers will be blacklisted by our jobs processor.</p>

<p>Create a function <code>sendNotification</code> that takes 4 arguments: <code>phoneNumber</code>, <code>message</code>, <code>job</code>, and <code>done</code>:</p>

<ul>
<li>When the function is called, track the progress of the <code>job</code> of <code>0</code> out of <code>100</code></li>
<li>If <code>phoneNumber</code> is included in the &ldquo;blacklisted array&rdquo;, fail the job with an <code>Error</code> object and the message: <code>Phone number PHONE_NUMBER is blacklisted</code></li>
<li>Otherwise:

<ul>
<li>Track the progress to 50%</li>
<li>Log to the console <code>Sending notification to PHONE_NUMBER, with message: MESSAGE</code></li>
</ul></li>
</ul>

<p>Create a queue with <code>Kue</code> that will proceed job of the queue <code>push_notification_code_2</code> with two jobs at a time.</p>

<p><strong>Requirements:</strong></p>

<ul>
<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
<li>You muse use <code>Kue</code> to set up the queue</li>
<li>Executing the jobs list should log to the console the following:</li>
</ul>

<p><strong>Terminal 2:</strong></p>

<pre><code>bob@dylan:~$ npm run dev 7-job_processor.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;7-job_processor.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_processor.js`
Sending notification to 4153518743, with message: This is the code 4321 to verify your account
Sending notification to 4153538781, with message: This is the code 4562 to verify your account
Sending notification to 4153118782, with message: This is the code 4321 to verify your account
Sending notification to 4153718781, with message: This is the code 4562 to verify your account
Sending notification to 4159518782, with message: This is the code 4321 to verify your account
Sending notification to 4158718781, with message: This is the code 4562 to verify your account
Sending notification to 4153818782, with message: This is the code 4321 to verify your account
Sending notification to 4154318781, with message: This is the code 4562 to verify your account
Sending notification to 4151218782, with message: This is the code 4321 to verify your account

</code></pre>

<p><strong>And in the same time in terminal 1:</strong></p>

<pre><code>...
Notification job #39 0% complete
Notification job #40 0% complete
Notification job #39 failed: Phone number 4153518780 is blacklisted
Notification job #40 failed: Phone number 4153518781 is blacklisted
Notification job #41 0% complete
Notification job #41 50% complete
Notification job #42 0% complete
Notification job #42 50% complete
Notification job #41 completed
Notification job #42 completed
Notification job #43 0% complete
Notification job #43 50% complete
Notification job #44 0% complete
Notification job #44 50% complete
Notification job #43 completed
Notification job #44 completed
Notification job #45 0% complete
Notification job #45 50% complete
Notification job #46 0% complete
Notification job #46 50% complete
Notification job #45 completed
Notification job #46 completed
Notification job #47 0% complete
Notification job #47 50% complete
Notification job #48 0% complete
Notification job #48 50% complete
Notification job #47 completed
Notification job #48 completed
Notification job #49 0% complete
Notification job #49 50% complete
Notification job #49 completed
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Writing the job creation function
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
   <p>In a file named <code>8-job.js</code>, create a function named <code>createPushNotificationsJobs</code>:</p>

<ul>
<li>It takes into argument <code>jobs</code> (array of objects), and <code>queue</code> (<code>Kue</code> queue)</li>
<li>If <code>jobs</code> is not an array, it should throw an <code>Error</code> with message: <code>Jobs is not an array</code></li>
<li>For each job in <code>jobs</code>, create a job in the queue <code>push_notification_code_3</code></li>
<li>When a job is created, it should log to the console <code>Notification job created: JOB_ID</code></li>
<li>When a job is complete, it should log to the console <code>Notification job JOB_ID completed</code></li>
<li>When a job is failed, it should log to the console <code>Notification job JOB_ID failed: ERROR</code></li>
<li>When a job is making progress, it should log to the console <code>Notification job JOB_ID PERCENT% complete</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 8-job-main.js 
import kue from &#39;kue&#39;;

import createPushNotificationsJobs from &#39;./8-job.js&#39;;

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: &#39;4153518780&#39;,
    message: &#39;This is the code 1234 to verify your account&#39;
    }
];
createPushNotificationsJobs(list, queue);

bob@dylan:~$
bob@dylan:~$ npm run dev 8-job-main.js 

&gt; queuing_system_in_js@1.0.0 dev /root
&gt; nodemon --exec babel-node --presets @babel/preset-env &quot;8-job-main.js&quot;

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 8-job-main.js`
Notification job created: 51

</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Writing the test for job creation
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Now that you created a job creator, let&rsquo;s add tests:</p>

<ul>
<li>Import the function <code>createPushNotificationsJobs</code></li>
<li>Create a queue with <code>Kue</code></li>
<li>Write a test suite for the <code>createPushNotificationsJobs</code> function:

<ul>
<li>Use <code>queue.testMode</code> to validate which jobs are inside the queue</li>
<li>etc.</li>
</ul></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>Make sure to enter the test mode without processing the jobs before executing the tests</li>
<li>Make sure to clear the queue and exit the test mode after executing the tests</li>
</ul>

<pre><code>bob@dylan:~$ npm test 8-job.test.js 

&gt; queuing_system_in_js@1.0.0 test /root
&gt; mocha --require @babel/register --exit &quot;8-job.test.js&quot;



  createPushNotificationsJobs
    ✓ display a error message if jobs is not an array
Notification job created: 1
Notification job created: 2
    ✓ create two new jobs to the queue
...

  123 passing (417ms)

</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. In stock?
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <h4>Data</h4>

<p>Create an array <code>listProducts</code> containing the list of the following products:</p>

<ul>
<li>Id: 1, name: <code>Suitcase 250</code>, price: 50, stock: 4</li>
<li>Id: 2, name: <code>Suitcase 450</code>, price: 100, stock: 10</li>
<li>Id: 3, name: <code>Suitcase 650</code>, price: 350, stock: 2</li>
<li>Id: 4, name: <code>Suitcase 1050</code>, price: 550, stock: 5</li>
</ul>

<h4>Data access</h4>

<p>Create a function named <code>getItemById</code>:</p>

<ul>
<li>It will take <code>id</code> as argument</li>
<li>It will return the item from <code>listProducts</code> with the same id</li>
</ul>

<h4>Server</h4>

<p>Create an <code>express</code> server listening on the port 1245. (You will start it via: <code>npm run dev 9-stock.js</code>)</p>

<h4>Products</h4>

<p>Create the route <code>GET /list_products</code> that will return the list of every available product with the following JSON format:</p>

<pre><code>bob@dylan:~$ curl localhost:1245/list_products ; echo &quot;&quot;
[{&quot;itemId&quot;:1,&quot;itemName&quot;:&quot;Suitcase 250&quot;,&quot;price&quot;:50,&quot;initialAvailableQuantity&quot;:4},{&quot;itemId&quot;:2,&quot;itemName&quot;:&quot;Suitcase 450&quot;,&quot;price&quot;:100,&quot;initialAvailableQuantity&quot;:10},{&quot;itemId&quot;:3,&quot;itemName&quot;:&quot;Suitcase 650&quot;,&quot;price&quot;:350,&quot;initialAvailableQuantity&quot;:2},{&quot;itemId&quot;:4,&quot;itemName&quot;:&quot;Suitcase 1050&quot;,&quot;price&quot;:550,&quot;initialAvailableQuantity&quot;:5}]
bob@dylan:~$ 
</code></pre>

<h4>In stock in Redis</h4>

<p>Create a client to connect to the Redis server:</p>

<ul>
<li>Write a function <code>reserveStockById</code> that will take <code>itemId</code> and <code>stock</code> as arguments:

<ul>
<li>It will set in Redis the stock for the key <code>item.ITEM_ID</code></li>
</ul></li>
<li>Write an async function <code>getCurrentReservedStockById</code>, that will take <code>itemId</code> as an argument:

<ul>
<li>It will return the reserved stock for a specific item</li>
</ul></li>
</ul>

<h4>Product detail</h4>

<p>Create the route <code>GET /list_products/:itemId</code>, that will return the current product and the current available stock (by using <code>getCurrentReservedStockById</code>) with the following JSON format:</p>

<pre><code>bob@dylan:~$ curl localhost:1245/list_products/1 ; echo &quot;&quot;
{&quot;itemId&quot;:1,&quot;itemName&quot;:&quot;Suitcase 250&quot;,&quot;price&quot;:50,&quot;initialAvailableQuantity&quot;:4,&quot;currentQuantity&quot;:4}
bob@dylan:~$ 
</code></pre>

<p>If the item does not exist, it should return:</p>

<pre><code>bob@dylan:~$ curl localhost:1245/list_products/12 ; echo &quot;&quot;
{&quot;status&quot;:&quot;Product not found&quot;}
bob@dylan:~$ 
</code></pre>

<h4>Reserve a product</h4>

<p>Create the route <code>GET /reserve_product/:itemId</code>:</p>

<ul>
<li>If the item does not exist, it should return:</li>
</ul>

<pre><code>bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo &quot;&quot;
{&quot;status&quot;:&quot;Product not found&quot;}
bob@dylan:~$ 
</code></pre>

<ul>
<li>If the item exists, it should check that there is at least one stock available. If not it should return:</li>
</ul>

<pre><code>bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo &quot;&quot;
{&quot;status&quot;:&quot;Not enough stock available&quot;,&quot;itemId&quot;:1}
bob@dylan:~$ 
</code></pre>

<ul>
<li>If there is enough stock available, it should reserve one item (by using <code>reserveStockById</code>), and return:</li>
</ul>

<pre><code>bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo &quot;&quot;
{&quot;status&quot;:&quot;Reservation confirmed&quot;,&quot;itemId&quot;:1}
bob@dylan:~$ 
</code></pre>

<p><strong>Requirements:</strong></p>

<ul>
<li>Make sure to use <code>promisify</code> with Redis</li>
<li>Make sure to use the <code>await</code>/<code>async</code> keyword to get the value from Redis</li>
<li>Make sure the format returned by the web application is always JSON and not text</li>
</ul>

  </div>
