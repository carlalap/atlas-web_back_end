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
