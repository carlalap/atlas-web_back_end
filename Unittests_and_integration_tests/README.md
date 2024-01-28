# Unittests and Integration Tests

<p>Unit testing is the process of testing that a particular function returns expected results
for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.</p>

<p>The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?</p>

<p>Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.</p>

<p>Integration tests will test interactions between every part of your code.</p>

<p>Execute your tests with </p>

<pre><code class="bash">$ python -m unittest path/to/test_file.py
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://docs.python.org/3/library/unittest.html" title="unittest — Unit testing framework" target="_blank">unittest — Unit testing framework</a></li>
<li><a href="https://docs.python.org/3/library/unittest.mock.html" title="unittest.mock — mock object library" target="_blank">unittest.mock — mock object library</a></li>
<li><a href="https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock" title="How to mock a readonly property with mock?" target="_blank">How to mock a readonly property with mock?</a></li>
<li><a href="https://pypi.org/project/parameterized/" title="parameterized" target="_blank">parameterized</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memoization" title="Memoization" target="_blank">Memoization</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/AiD51mZh2lZ8stCrg3CjGQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>The difference between unit and integration tests.</li>
<li>Common testing patterns such as mocking, parametrizations and fixtures</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions and coroutines must be type-annotated.</li>
</ul>
