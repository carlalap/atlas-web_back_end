# NodeJS Basics

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://nodejs.org/en/learn/getting-started/introduction-to-nodejs" title="Node JS getting started" target="_blank">Node JS getting started</a></li>
<li><a href="https://node.readthedocs.io/en/latest/api/process/" title="Process API doc" target="_blank">Process API doc</a></li>
<li><a href="https://nodejs.org/api/child_process.html" title="Child process" target="_blank">Child process</a></li>
<li><a href="https://expressjs.com/en/starter/installing.html" title="Express getting started" target="_blank">Express getting started</a></li>
<li><a href="https://mochajs.org/" title="Mocha documentation" target="_blank">Mocha documentation</a></li>
<li><a href="https://github.com/remy/nodemon#nodemon" title="Nodemon documentation" target="_blank">Nodemon documentation</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>run javascript using NodeJS</li>
<li>use NodeJS modules</li>
<li>use specific Node JS module to read files</li>
<li>use <code>process</code> to access command line arguments and the environment</li>
<li>create a small HTTP server using Node JS</li>
<li>create a small HTTP server using Express JS</li>
<li>create advanced routes with Express JS</li>
<li>use ES6 with Node JS with Babel-node</li>
<li>use Nodemon to develop faster</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>, <code>Visual Studio Code</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>node</code> (version 12.x.x)</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
<li>Your code will be tested using <code>Jest</code> and the command <code>npm run test</code></li>
<li>Your code will be verified against lint using ESLint</li>
<li>Your code needs to pass all the tests and lint. You can verify the entire project running <code>npm run full-test</code></li>
<li>All of your functions/classes must be exported by using this format: <code>module.exports = myFunction;</code></li>
</ul>

<h2>Provided files</h2>

<h3><code>database.csv</code></h3>

<pre><code>firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
</code></pre>

<h3><code>package.json</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "nodemon": "^2.0.2",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
</code>
</pre>
</details>

<h3><code>babel.config.js</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
</code>
</pre>
</details>

<h3><code>.eslintrc.js</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre>
<code>
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
</code>
</pre>
</details>

<h3>and&hellip;</h3>

<p>Don&rsquo;t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>

  </div>
</div>

 <h2 class="gap">Tasks</h2>

<div data-role="task21735" data-position="1" id="task-num-0">
     <div class="panel panel-default task-card " id="task-21735">
  <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Executing basic javascript with Node JS
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
<p>In the file <code>0-console.js</code>, create a function named <code>displayMessage</code> that prints in <code>STDOUT</code> the string argument.</p>

<pre><code>bob@dylan:~$ cat 0-main.js
const displayMessage = require(&#39;./0-console&#39;);

displayMessage(&quot;Hello NodeJS!&quot;);

bob@dylan:~$ node 0-main.js
Hello NodeJS!
bob@dylan:~$
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Using Process stdin
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a program named <code>1-stdin.js</code> that will be executed through command line:</p>

<ul>
<li>It should display the message <code>Welcome to Holberton School, what is your name?</code> (followed by a new line)</li>
<li>The user should be able to input their name on a new line</li>
<li>The program should display <code>Your name is: INPUT</code></li>
<li>When the user ends the program, it should display <code>This important software is now closing</code> (followed by a new line)</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>Your code will be tested through a child process, make sure you have everything you need for that</li>
</ul>

<pre><code>bob@dylan:~$ node 1-stdin.js 
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
bob@dylan:~$ 
bob@dylan:~$ echo &quot;John&quot; | node 1-stdin.js 
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Reading a file synchronously with Node JS
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Using the database <code>database.csv</code> (provided in project description), create a function <code>countStudents</code> in the file <code>2-read_file.js</code></p>

<ul>
<li>Create a function named <code>countStudents</code>. It should accept a path in argument</li>
<li>The script should attempt to read the database file synchronously</li>
<li>If the database is not available, it should throw an error with the text <code>Cannot load the database</code></li>
<li>If the database is available, it should log the following message to the console <code>Number of students: NUMBER_OF_STUDENTS</code></li>
<li>It should log the number of students in each field, and the list with the following format: <code>Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES</code></li>
<li>CSV file can contain empty lines (at the end) - and they are not a valid student!</li>
</ul>

<pre><code>bob@dylan:~$ cat 2-main_0.js
const countStudents = require(&#39;./2-read_file&#39;);

countStudents(&quot;nope.csv&quot;);

bob@dylan:~$ node 2-main_0.js
2-read_file.js:9
    throw new Error(&#39;Cannot load the database&#39;);
    ^

Error: Cannot load the database
...
bob@dylan:~$
bob@dylan:~$ cat 2-main_1.js
const countStudents = require(&#39;./2-read_file&#39;);

countStudents(&quot;database.csv&quot;);

bob@dylan:~$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$ 
</code></pre>
 </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Reading a file asynchronously with Node JS
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Using the database <code>database.csv</code> (provided in project description), create a function <code>countStudents</code> in the file <code>3-read_file_async.js</code></p>

<ul>
<li>Create a function named <code>countStudents</code>. It should accept a path in argument (same as in <code>2-read_file.js</code>)</li>
<li>The script should attempt to read the database file asynchronously</li>
<li>The function should return a Promise</li>
<li>If the database is not available, it should throw an error with the text <code>Cannot load the database</code></li>
<li>If the database is available, it should log the following message to the console <code>Number of students: NUMBER_OF_STUDENTS</code></li>
<li>It should log the number of students in each field, and the list with the following format: <code>Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES</code></li>
<li>CSV file can contain empty lines (at the end) - and they are not a valid student!</li>
</ul>

<pre><code>bob@dylan:~$ cat 3-main_0.js
const countStudents = require(&#39;./3-read_file_async&#39;);

countStudents(&quot;nope.csv&quot;)
    .then(() =&gt; {
        console.log(&quot;Done!&quot;);
    })
        .catch((error) =&gt; {
        console.log(error);
    });

bob@dylan:~$ node 3-main_0.js
Error: Cannot load the database
...
bob@dylan:~$
bob@dylan:~$ cat 3-main_1.js
const countStudents = require(&#39;./3-read_file_async&#39;);

countStudents(&quot;database.csv&quot;)
    .then(() =&gt; {
        console.log(&quot;Done!&quot;);
    })
        .catch((error) =&gt; {
        console.log(error);
    });
console.log(&quot;After!&quot;);

bob@dylan:~$ node 3-main_1.js
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
bob@dylan:~$ 
</code></pre>

<p><strong>Tips:</strong></p>

<ul>
<li>Using asynchronous callbacks is the preferred way to write code in Node to avoid blocking threads</li>
</ul>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Create a small HTTP server using Node&#39;s HTTP module
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->
<!-- Task Body -->
<p>In a file named <code>4-http.js</code>, create a small HTTP server using the <code>http</code> module:</p>

<ul>
<li>It should be assigned to the variable <code>app</code> and this one must be exported </li>
<li>HTTP server should listen on port 1245</li>
<li>Displays <code>Hello Holberton School!</code> in the page body for any endpoint as plain text</li>
</ul>

<p>In terminal 1:</p>

<pre><code>bob@dylan:~$ node 4-http.js
...
</code></pre>

<p>In terminal 2:</p>

<pre><code>bob@dylan:~$ curl localhost:1245 &amp;&amp; echo &quot;&quot;
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/any_endpoint &amp;&amp; echo &quot;&quot;
Hello Holberton School!
bob@dylan:~$ 
</code></pre>

</div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Create a more complex HTTP server using Node&#39;s HTTP module
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a file named <code>5-http.js</code>, create a small HTTP server using the <code>http</code> module:</p>

<ul>
<li>It should be assigned to the variable app and this one must be exported</li>
<li>HTTP server should listen on port 1245</li>
<li>It should return plain text</li>
<li>When the URL path is <code>/</code>, it should display <code>Hello Holberton School!</code> in the page body</li>
<li>When the URL path is <code>/students</code>, it should display <code>This is the list of our students</code> followed by the same content as the file <code>3-read_file_async.js</code> (with and without the database) - the name of the database must be passed as argument of the file</li>
<li>CSV file can contain empty lines (at the end) - and they are not a valid student!</li>
</ul>

<p>Terminal 1:</p>

<pre><code>bob@dylan:~$ node 5-http.js database.csv
...
</code></pre>

<p>In terminal 2:</p>

<pre><code>bob@dylan:~$ curl localhost:1245 &amp;&amp; echo &quot;&quot;
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/students &amp;&amp; echo &quot;&quot;
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$ 
</code></pre>

  </div>
