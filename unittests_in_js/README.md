# Unittests in JS

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://mochajs.org/" title="Mocha documentation" target="_blank">Mocha documentation</a></li>
<li><a href="https://www.chaijs.com/api/" title="Chai" target="_blank">Chai</a></li>
<li><a href="https://sinonjs.org/#get-started" title="Sinon" target="_blank">Sinon</a></li>
<li><a href="https://expressjs.com/en/guide/routing.html" title="Express" target="_blank">Express</a></li>
<li><a href="https://www.npmjs.com/package/request" title="Request" target="_blank">Request</a></li>
<li><a href="https://www.digitalocean.com/community" title="How to Test NodeJS Apps using Mocha, Chai and SinonJS" target="_blank">How to Test NodeJS Apps using Mocha, Chai and SinonJS</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/4ZxwXNG7ByKjbq7VcQFc7Q" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to use Mocha to write a test suite</li>

<p>Mocha is a popular JavaScript testing framework that is commonly used with Node.js applications. It provides an easy-to-use interface for writing and running tests, including support for various assertion libraries, test suites, spies, stubs, hooks, and asynchronous functions. Here's a step-by-step guide to using Mocha for testing </p>

## 1. Installing Mocha:

<br>You can install Mocha globally

```sh
npm install --global mocha
```

<br> or locally in your project using npm:

```sh
npm install --save-dev mocha
```

<li>How to use different assertion libraries (Node or Chai)</li>

<p>Mocha works with different assertion libraries like Node's built-in assert module, Chai, or others. To use Chai, install it and require it in your test file: </p>

```sh
npm install --save-dev chai
const expect = require('chai').expect;
```

<li>How to present long test suites</li>
<li>When and how to use spies & stubs</li>

<p>Spies and stubs are used for mocking functions and objects in tests. You can use libraries like Sinon.js with Mocha for this purpose:</p>

```sh
npm install --save-dev sinon
const sinon = require('sinon');
```

<li>What are hooks and when to use them</li>
<p>Hooks are functions that are executed before or after tests. Mocha supports before, beforeEach, after, and afterEach hooks:</p>

<pre><code>
describe('Array', function() {
  let arr;

  beforeEach(function() {
    arr = [1, 2, 3];
  });

  it('should return -1 when the value is not present', function() {
    assert.equal(arr.indexOf(4), -1);
  });
});
</code></pre>

<li>Unit testing with Async functions</li>
<br> To test asynchronous functions, use Mocha's done parameter or return a Promise:
<pre><code>
it('should return a promise', function() {
  return asyncFunction().then(result => {
    assert.equal(result, expected);
  });
});
</code></pre>

<li>How to write integration tests with a small node server</li>
<br>For integration tests, you can use libraries like Supertest to make HTTP requests to your server:
<pre><code>

bob@dylan:~$npm install --save-dev supertest

javascript file:

const request = require('supertest');

describe('GET /users', function() {
it('responds with json', function(done) {
request(app)
.get('/users')
.set('Accept', 'application/json')
.expect('Content-Type', /json/)
.expect(200, done);
});
});

</code></pre>

</ul>

<h2>Requirements</h2>

<ul>
<li>All of your code will be executed on Ubuntu 18.04 using Node 12.x.x</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>, <code>Visual Studio Code</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
<li>When running every test with <code>npm run test *.test.js</code>, everything should pass correctly without any warning or error</li>
</ul>

  </div>
</div>

<h2 class="gap">Tasks</h2>
   <div data-role="task21724" data-position="1" id="task-num-0">
     <div class="panel panel-default task-card " id="task-21724">
 <span id="user_id" data-id="6138"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Basic test with Mocha and Node assertion library
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p><strong>Install Mocha using npm:</strong></p>

<ul>
<li>Set up a scripts in your <code>package.json</code> to quickly run Mocha using <code>npm test</code></li>
<li>You have to use <code>assert</code></li>
</ul>

<p><strong>Create a new file named <code>0-calcul.js</code>:</strong></p>

<ul>
<li>Create a function named <code>calculateNumber</code>. It should accepts two arguments (number) <code>a</code> and <code>b</code></li>
<li>The function should round <code>a</code> and <code>b</code> and return the sum of it </li>
</ul>

<p><strong>Test cases</strong></p>

<ul>
<li>Create a file <code>0-calcul.test.js</code> that contains test cases of this function</li>
<li>You can assume <code>a</code> and <code>b</code> are always number</li>
<li>Tests should be around the &ldquo;rounded&rdquo; part</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>For the sake of the example, this test suite is slightly extreme and probably not needed</li>
<li>However, remember that your tests should not only verify what a function is supposed to do, but also the edge cases</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You have to use <code>assert</code></li>
<li>You should be able to run the test suite using <code>npm test 0-calcul.test.js</code></li>
<li>Every test should pass without any warning</li>
</ul>

<p><strong>Expected output</strong></p>

<pre><code>&gt; const calculateNumber = require(&quot;./0-calcul.js&quot;);
&gt; calculateNumber(1, 3)
4
&gt; calculateNumber(1, 3.7)
5
&gt; calculateNumber(1.2, 3.7)
5
&gt; calculateNumber(1.5, 3.7)
6
&gt; 
</code></pre>

<p><strong>Run test</strong></p>

<pre><code>bob@dylan:~$ npm test 0-calcul.test.js 

&gt; task_0@1.0.0 test /root
&gt; ./node_modules/mocha/bin/mocha &quot;0-calcul.test.js&quot;

  calculateNumber
    ✓ ...
    ✓ ...
    ✓ ...
    ...

  130 passing (35ms)
bob@dylan:~$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Combining descriptions
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->
   <!-- Task Body -->
  <p><strong>Create a new file named <code>1-calcul.js</code>:</strong></p>

<ul>
<li>Upgrade the function you created in the previous task (<code>0-calcul.js</code>)</li>
<li>Add a new argument named <code>type</code> at first argument of the function. <code>type</code> can be <code>SUM</code>, <code>SUBTRACT</code>, or <code>DIVIDE</code> (string)</li>
<li>When type is <code>SUM</code>, round the two numbers, and add <code>a</code> from <code>b</code></li>
<li>When type is <code>SUBTRACT</code>, round the two numbers, and subtract <code>b</code> from <code>a</code></li>
<li>When type is <code>DIVIDE</code>, round the two numbers, and divide <code>a</code> with <code>b</code> - if the rounded value of <code>b</code> is equal to 0, return the string <code>Error</code></li>
</ul>

<p><strong>Test cases</strong></p>

<ul>
<li>Create a file <code>1-calcul.test.js</code> that contains test cases of this function</li>
<li>You can assume <code>a</code> and <code>b</code> are always number</li>
<li>Usage of <code>describe</code> will help you to organize your test cases</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>For the sake of the example, this test suite is slightly extreme and probably not needed</li>
<li>However, remember that your tests should not only verify what a function is supposed to do, but also the edge cases</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You have to use <code>assert</code></li>
<li>You should be able to run the test suite using <code>npm test 1-calcul.test.js</code></li>
<li>Every test should pass without any warning</li>
</ul>

<p><strong>Expected output</strong></p>

<pre><code>&gt; const calculateNumber = require(&quot;./1-calcul.js&quot;);
&gt; calculateNumber(&#39;SUM&#39;, 1.4, 4.5)
6
&gt; calculateNumber(&#39;SUBTRACT&#39;, 1.4, 4.5)
-4
&gt; calculateNumber(&#39;DIVIDE&#39;, 1.4, 4.5)
0.2
&gt; calculateNumber(&#39;DIVIDE&#39;, 1.4, 0)
&#39;Error&#39;
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Basic test using Chai assertion library
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>While using Node assert library is completely valid, a lot of developers prefer to have a behavior driven development style. This type being easier to read and therefore to maintain.</p>

<p><strong>Let&rsquo;s install Chai with npm:</strong></p>

<ul>
<li>Copy the file <code>1-calcul.js</code> in a new file <code>2-calcul_chai.js</code> (same content, same behavior)</li>
<li>Copy the file <code>1-calcul.test.js</code> in a new file <code>2-calcul_chai.test.js</code></li>
<li>Rewrite the test suite, using <code>expect</code> from <code>Chai</code></li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>Remember that test coverage is always difficult to maintain. Using an easier style for your tests will help you</li>
<li>The easier your tests are to read and understand, the more other engineers will be able to fix them when they are modifying your code</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 2-calcul_chai.test.js</code></li>
<li>Every test should pass without any warning</li>
</ul>
</div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Spies
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Spies are a useful wrapper that will execute the wrapped function, and log useful information (e.g. was it called, with what arguments). Sinon is a library allowing you to create spies.</p>

<p><strong>Let&rsquo;s install Sinon with npm:</strong></p>

<ul>
<li>Create a new file named <code>utils.js</code></li>
<li>Create a new module named <code>Utils</code></li>
<li>Create a property named <code>calculateNumber</code> and paste your previous code in the function</li>
<li>Export the Utils module</li>
</ul>

<p><strong>Create a new file named <code>3-payment.js</code>:</strong></p>

<ul>
<li>Create a new function named <code>sendPaymentRequestToApi</code>. The function takes two argument <code>totalAmount</code>, and <code>totalShipping</code></li>
<li>The function calls the <code>Utils.calculateNumber</code> function with type <code>SUM</code>, <code>totalAmount</code> as <code>a</code>, <code>totalShipping</code> as <code>b</code> and display in the console the message <code>The total is: &lt;result of the sum&gt;</code></li>
</ul>

<p><strong>Create a new file named <code>3-payment.test.js</code> and add a new suite named <code>sendPaymentRequestToApi</code>:</strong></p>

<ul>
<li>By using <code>sinon.spy</code>, make sure the math used for <code>sendPaymentRequestToApi(100, 20)</code> is the same as <code>Utils.calculateNumber(&#39;SUM&#39;, 100, 20)</code> (validate the usage of the <code>Utils</code> function)</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 3-payment.test.js</code></li>
<li>Every test should pass without any warning</li>
<li>You should use a <code>spy</code> to complete this exercise</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>Remember to always restore a spy after using it in a test, it will prevent you from having weird behaviors</li>
<li>Spies are really useful and allow you to focus only on what your code is doing and not the downstream APIs or functions</li>
<li>Remember that integration test is different from unit test. Your unit test should test your code, not the code of a different function</li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Stubs
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

 <!-- Task Body -->
 <p>Stubs are similar to spies. Except that you can provide a different implementation of the function you are wrapping. Sinon can be used as well for stubs.</p>

<p><strong>Create a new file <code>4-payment.js</code>, and copy the code from <code>3-payment.js</code></strong> (same content, same behavior)</p>

<p><strong>Create a new file <code>4-payment.test.js</code>, and copy the code from <code>3-payment.test.js</code></strong></p>

<ul>
<li>Imagine that calling the function <code>Utils.calculateNumber</code> is actually calling an API or a very expensive method. You don&rsquo;t necessarily want to do that on every test run</li>
<li>Stub the function <code>Utils.calculateNumber</code> to always return the same number <code>10</code></li>
<li>Verify that the stub is being called with <code>type = SUM</code>, <code>a = 100</code>, and <code>b = 20</code></li>
<li>Add a spy to verify that <code>console.log</code> is logging the correct message <code>The total is: 10</code></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 4-payment.test.js</code></li>
<li>Every test should pass without any warning</li>
<li>You should use a <code>stub</code> to complete this exercise</li>
<li>Do not forget to restore the spy and the stub</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>Using stubs allows you to greatly speed up your test. When executing thousands of tests, saving a few seconds is important</li>
<li>Using stubs allows you to control specific edge case (e.g a function throwing an error or returning a specific result like a number or a timestamp)</li>
</ul>
</div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Hooks
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Hooks are useful functions that can be called before execute one or all tests in a suite</p>

<p><strong>Copy the code from <code>4-payment.js</code> into a new file <code>5-payment.js</code>:</strong> (same content/same behavior)</p>

<p><strong>Create a new file <code>5-payment.test.js</code>:</strong></p>

<ul>
<li>Inside the same <code>describe</code>, create 2 tests:

<ul>
<li>The first test will call <code>sendPaymentRequestToAPI</code> with 100, and 20:

<ul>
<li>Verify that the console is logging the string <code>The total is: 120</code></li>
<li>Verify that the console is only called once</li>
</ul></li>
<li>The second test will call <code>sendPaymentRequestToAPI</code> with 10, and 10:

<ul>
<li>Verify that the console is logging the string <code>The total is: 20</code></li>
<li>Verify that the console is only called once</li>
</ul></li>
</ul></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 5-payment.test.js</code></li>
<li>Every test should pass without any warning</li>
<li>You should use only one <code>spy</code> to complete this exercise</li>
<li>You should use a <code>beforeEach</code> and a <code>afterEach</code> hooks to complete this exercise</li>
</ul>
</div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Async tests with done
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Look into how to support async testing, for example when waiting for the answer of an API or from a Promise</p>

<p><strong>Create a new file <code>6-payment_token.js</code>:</strong></p>

<ul>
<li>Create a new function named <code>getPaymentTokenFromAPI</code></li>
<li>The function will take an argument called <code>success</code> (boolean)</li>
<li>When <code>success</code> is true, it should return a resolved promise with the object <code>{data: &#39;Successful response from the API&#39; }</code></li>
<li>Otherwise, the function is doing nothing.</li>
</ul>

<p><strong>Create a new file <code>6-payment_token.test.js</code> and write a test suite named <code>getPaymentTokenFromAPI</code></strong></p>

<ul>
<li>How to test the result of <code>getPaymentTokenFromAPI(true)</code>?</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>You should be extremely careful when working with async testing. Without calling <code>done</code> properly, your test could be always passing even if what you are actually testing is never executed</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 6-payment_token.test.js</code></li>
<li>Every test should pass without any warning</li>
<li>You should use the <code>done</code> callback to execute this test</li>
</ul>
  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Skip
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>When you have a long list of tests, and you can&rsquo;t figure out why a test is breaking, avoid commenting out a test, or removing it. <strong>Skip</strong> it instead, and file a ticket to come back to it as soon as possible</p>

<p>You will be using this file, conveniently named <code>7-skip.test.js</code></p>

<pre><code>const { expect } = require(&#39;chai&#39;);

describe(&#39;Testing numbers&#39;, () =&gt; {
  it(&#39;1 is equal to 1&#39;, () =&gt; {
    expect(1 === 1).to.be.true;
  });

  it(&#39;2 is equal to 2&#39;, () =&gt; {
    expect(2 === 2).to.be.true;
  });

  it(&#39;1 is equal to 3&#39;, () =&gt; {
    expect(1 === 3).to.be.true;
  });

  it(&#39;3 is equal to 3&#39;, () =&gt; {
    expect(3 === 3).to.be.true;
  });

  it(&#39;4 is equal to 4&#39;, () =&gt; {
    expect(4 === 4).to.be.true;
  });

  it(&#39;5 is equal to 5&#39;, () =&gt; {
    expect(5 === 5).to.be.true;
  });

  it(&#39;6 is equal to 6&#39;, () =&gt; {
    expect(6 === 6).to.be.true;
  });

  it(&#39;7 is equal to 7&#39;, () =&gt; {
    expect(7 === 7).to.be.true;
  });
});
</code></pre>

<p><strong>Using the file <code>7-skip.test.js</code>:</strong></p>

<ul>
<li>Make the test suite pass <strong>without</strong> fixing or removing the failing test</li>
<li><code>it</code> description <strong>must stay</strong> the same</li>
</ul>

<p><strong>Tips:</strong></p>

<ul>
<li>Skipping is also very helpful when you only want to execute the test in a particular case (specific environment, or when an API is not behaving correctly)</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test 7-skip.test.js</code></li>
<li>Every test should pass without any warning</li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Basic Integration testing
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a folder <code>8-api</code> located at the root of the project directory, copy this <code>package.json</code> over.</p>

<pre><code>{
  &quot;name&quot;: &quot;8-api&quot;,
  &quot;version&quot;: &quot;1.0.0&quot;,
  &quot;description&quot;: &quot;&quot;,
  &quot;main&quot;: &quot;index.js&quot;,
  &quot;scripts&quot;: {
    &quot;test&quot;: &quot;./node_modules/mocha/bin/mocha&quot;
  },
  &quot;author&quot;: &quot;&quot;,
  &quot;license&quot;: &quot;ISC&quot;,
  &quot;dependencies&quot;: {
    &quot;express&quot;: &quot;^4.17.1&quot;
  },
  &quot;devDependencies&quot;: {
    &quot;chai&quot;: &quot;^4.2.0&quot;,
    &quot;mocha&quot;: &quot;^6.2.2&quot;,
    &quot;request&quot;: &quot;^2.88.0&quot;,
    &quot;sinon&quot;: &quot;^7.5.0&quot;
  }
}
</code></pre>

<p><strong>Create a new file <code>api.js</code>:</strong></p>

<ul>
<li>By using <code>express</code>, create an instance of <code>express</code> called <code>app</code></li>
<li>Listen to port 7865 and log <code>API available on localhost port 7865</code> to the browser console when the <code>express</code> server is started</li>
<li>For the route <code>GET /</code>, return the message <code>Welcome to the payment system</code></li>
</ul>

<p><strong>Create a new file <code>api.test.js</code>:</strong></p>

<ul>
<li>Create one suite for the index page:

<ul>
<li>Correct status code?</li>
<li>Correct result?</li>
<li>Other?</li>
</ul></li>
</ul>

<p><strong>Server</strong></p>

<p>Terminal 1</p>

<pre><code>bob@dylan:~/8-api$  node api.js
API available on localhost port 7865
</code></pre>

<p>Terminal 2</p>

<pre><code>bob@dylan:~/8-api$  curl http://localhost:7865 ; echo &quot;&quot;
Welcome to the payment system
bob@dylan:~/8-api$  
bob@dylan:~/8-api$ npm test api.test.js

&gt; 8-api@1.0.0 test /root/8-api
&gt; ./node_modules/mocha/bin/mocha &quot;api.test.js&quot;



  Index page
    ✓ ...
    ✓ ...
    ...

  23 passing (256ms)

bob@dylan:~/8-api$
</code></pre>

<p><strong>Tips:</strong></p>

<ul>
<li>Since this is an integration test, you will need to have your node server running for the test to pass</li>
<li>You can use the module <code>request</code></li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test api.test.js</code></li>
<li>Every test should pass without any warnings</li>
</ul>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Regex integration testing
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a folder <code>9-api</code>, reusing the previous project in <code>8-api</code> (<code>package.json</code>, <code>api.js</code> and <code>api.test.js</code>)</p>

<p><strong>Modify the file <code>api.js</code>:</strong></p>

<ul>
<li>Add a new endpoint: <code>GET /cart/:id</code></li>
<li><code>:id</code> must be only a number (validation must be in the route definition)</li>
<li>When access, the endpoint should return <code>Payment methods for cart :id</code></li>
</ul>

<p><strong>Modify the file <code>api.test.js</code>:</strong></p>

<ul>
<li>Add a new test suite for the cart page:

<ul>
<li>Correct status code when <code>:id</code> is a number?</li>
<li>Correct status code when <code>:id</code> is NOT a number (=&gt; 404)?</li>
<li>etc.</li>
</ul></li>
</ul>

<p><strong>Server</strong></p>

<p>Terminal 1</p>

<pre><code>bob@dylan:~$ node api.js
API available on localhost port 7865
</code></pre>

<p>Terminal 2</p>

<pre><code>bob@dylan:~$ curl http://localhost:7865/cart/12 ; echo &quot;&quot;
Payment methods for cart 12
bob@dylan:~$ 
bob@dylan:~$ curl http://localhost:7865/cart/hello -v
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 7865 (#0)
&gt; GET /cart/hello HTTP/1.1
&gt; Host: localhost:7865
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; 
&lt; HTTP/1.1 404 Not Found
&lt; X-Powered-By: Express
&lt; Content-Security-Policy: default-src &#39;none&#39;
&lt; X-Content-Type-Options: nosniff
&lt; Content-Type: text/html; charset=utf-8
&lt; Content-Length: 149
&lt; Date: Wed, 15 Jul 2020 08:33:44 GMT
&lt; Connection: keep-alive
&lt; 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;title&gt;Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;pre&gt;Cannot GET /cart/hello&lt;/pre&gt;
&lt;/body&gt;
&lt;/html&gt;
* Connection #0 to host localhost left intact
bob@dylan:~$ 
</code></pre>

<p><strong>Tips:</strong></p>

<ul>
<li>You will need to add a small regex in your path to support the usecase</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test api.test.js</code></li>
<li>Every test should pass without any warning</li>
</ul>
  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Deep equality &amp; Post integration testing
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>In a folder <code>10-api</code>, reusing the previous project in <code>9-api</code> (<code>package.json</code>, <code>api.js</code> and <code>api.test.js</code>)</p>

<p><strong>Modify the file <code>api.js</code>:</strong></p>

<ul>
<li>Add an endpoint <code>GET /available_payments</code> that returns an object with the following structure:</li>
</ul>

<pre><code>{
  payment_methods: {
    credit_cards: true,
    paypal: false
  }
}
</code></pre>

<ul>
<li>Add an endpoint <code>POST /login</code> that returns the message <code>Welcome :username</code> where <code>:username</code> is the value of the body variable <code>userName</code>.</li>
</ul>

<p><strong>Modify the file <code>api.test.js</code>:</strong></p>

<ul>
<li>Add a test suite for the <code>/login</code> endpoint</li>
<li>Add a test suite for the <code>/available_payments</code> endpoint</li>
</ul>

<p><strong>Server</strong></p>

<p>Terminal 1</p>

<pre><code>bob@dylan:~$ node api.js
API available on localhost port 7865
</code></pre>

<p>Terminal 2</p>

<pre><code>bob@dylan:~$ curl http://localhost:7865/available_payments ; echo &quot;&quot;
{&quot;payment_methods&quot;:{&quot;credit_cards&quot;:true,&quot;paypal&quot;:false}}
bob@dylan:~$ 
bob@dylan:~$ curl -XPOST http://localhost:7865/login -d &#39;{ &quot;userName&quot;: &quot;Betty&quot; }&#39; -H &#39;Content-Type: application/json&#39; ; echo &quot;&quot;
Welcome Betty
bob@dylan:~$ 
</code></pre>

<p><strong>Tips:</strong></p>

<ul>
<li>Look at deep equality to compare objects</li>
</ul>

<p><strong>Requirements:</strong></p>

<ul>
<li>You should be able to run the test suite using <code>npm test api.test.js</code></li>
<li>Every test should pass without any warning</li>
<li>Your server should not display any error</li>
</ul>

  </div>
