# Caching

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p>In this project, you learn different caching algorithms. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29" title="Cache replacement policies - FIFO" target="_blank">Cache replacement policies - FIFO</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29" title="Cache replacement policies - LIFO" target="_blank">Cache replacement policies - LIFO</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29" title="Cache replacement policies - LRU" target="_blank">Cache replacement policies - LRU</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29" title="Cache replacement policies - MRU" target="_blank">Cache replacement policies - MRU</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29" title="Cache replacement policies - LFU" target="_blank">Cache replacement policies - LFU</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/cHhMVpo-XBzdLtk8C42Rrg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What a caching system is</li>
<li>What FIFO means </li>
<li>What LIFO means</li>
<li>What LRU means</li>
<li>What MRU means</li>
<li>What LFU means</li>
<li>What the purpose of a caching system</li>
<li>What limits a caching system have</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h2>More Info</h2>

<h3>Parent class <code>BaseCaching</code></h3>

<p>All your classes must inherit from <code>BaseCaching</code> defined below:</p>

<pre><code>$ cat base_caching.py
#!/usr/bin/python3
&quot;&quot;&quot; BaseCaching module
&quot;&quot;&quot;

class BaseCaching():
    &quot;&quot;&quot; BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    &quot;&quot;&quot;
    MAX_ITEMS = 4

    def __init__(self):
        &quot;&quot;&quot; Initiliaze
        &quot;&quot;&quot;
        self.cache_data = {}

    def print_cache(self):
        &quot;&quot;&quot; Print the cache
        &quot;&quot;&quot;
        print(&quot;Current cache:&quot;)
        for key in sorted(self.cache_data.keys()):
            print(&quot;{}: {}&quot;.format(key, self.cache_data.get(key)))

    def put(self, key, item):
        &quot;&quot;&quot; Add an item in the cache
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;put must be implemented in your cache class&quot;)

    def get(self, key):
        &quot;&quot;&quot; Get an item by key
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;get must be implemented in your cache class&quot;)
</code></pre>

  </div>
</div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Basic dictionary
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a class <code>BasicCache</code> that inherits from <code>BaseCaching</code> and is a caching system:</p>

<ul>
<li>You must use <code>self.cache_data</code> - dictionary from the parent class <code>BaseCaching</code></li>
<li>This caching system doesn&rsquo;t have limit</li>
<li><code>def put(self, key, item):</code>

<ul>
<li>Must assign to the dictionary <code>self.cache_data</code> the <code>item</code> value for the key <code>key</code>.</li>
<li>If <code>key</code> or <code>item</code> is <code>None</code>, this method should not do anything.</li>
</ul></li>
<li><code>def get(self, key):</code>

<ul>
<li>Must return the value in <code>self.cache_data</code> linked to <code>key</code>.</li>
<li>If <code>key</code> is <code>None</code> or if the <code>key</code> doesn&rsquo;t exist in <code>self.cache_data</code>, return <code>None</code>.</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 0-main &quot;&quot;&quot;
BasicCache = __import__(&#39;0-basic_cache&#39;).BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
print(my_cache.get(&quot;D&quot;))
my_cache.print_cache()
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.put(&quot;A&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))

guillaume@ubuntu:~/$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. FIFO caching
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a class <code>FIFOCache</code> that inherits from <code>BaseCaching</code> and is a caching system:</p>

<ul>
<li>You must use <code>self.cache_data</code> - dictionary from the parent class <code>BaseCaching</code></li>
<li>You can overload <code>def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code>super().__init__()</code></li>
<li><code>def put(self, key, item):</code>

<ul>
<li>Must assign to the dictionary <code>self.cache_data</code> the <code>item</code> value for the key <code>key</code>.</li>
<li>If <code>key</code> or <code>item</code> is <code>None</code>, this method should not do anything.</li>
<li>If the number of items in <code>self.cache_data</code> is higher that <code>BaseCaching.MAX_ITEMS</code>:

<ul>
<li>you must discard the first item put in cache (FIFO algorithm)</li>
<li>you must print <code>DISCARD:</code> with the <code>key</code> discarded and following by a new line </li>
</ul></li>
</ul></li>
<li><code>def get(self, key):</code>

<ul>
<li>Must return the value in <code>self.cache_data</code> linked to <code>key</code>.</li>
<li>If <code>key</code> is <code>None</code> or if the <code>key</code> doesn&rsquo;t exist in <code>self.cache_data</code>, return <code>None</code>.</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 1-main &quot;&quot;&quot;
FIFOCache = __import__(&#39;1-fifo_cache&#39;).FIFOCache

my_cache = FIFOCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. LIFO Caching
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a class <code>LIFOCache</code> that inherits from <code>BaseCaching</code> and is a caching system:</p>

<ul>
<li>You must use <code>self.cache_data</code> - dictionary from the parent class <code>BaseCaching</code></li>
<li>You can overload <code>def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code>super().__init__()</code></li>
<li><code>def put(self, key, item):</code>

<ul>
<li>Must assign to the dictionary <code>self.cache_data</code> the <code>item</code> value for the key <code>key</code>.</li>
<li>If <code>key</code> or <code>item</code> is <code>None</code>, this method should not do anything.</li>
<li>If the number of items in <code>self.cache_data</code> is higher that <code>BaseCaching.MAX_ITEMS</code>:

<ul>
<li>you must discard the last item put in cache (LIFO algorithm)</li>
<li>you must print <code>DISCARD:</code> with the <code>key</code> discarded and following by a new line </li>
</ul></li>
</ul></li>
<li><code>def get(self, key):</code>

<ul>
<li>Must return the value in <code>self.cache_data</code> linked to <code>key</code>.</li>
<li>If <code>key</code> is <code>None</code> or if the <code>key</code> doesn&rsquo;t exist in <code>self.cache_data</code>, return <code>None</code>.</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 2-main &quot;&quot;&quot;
LIFOCache = __import__(&#39;2-lifo_cache&#39;).LIFOCache

my_cache = LIFOCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. LRU Caching
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a class <code>LRUCache</code> that inherits from <code>BaseCaching</code> and is a caching system:</p>

<ul>
<li>You must use <code>self.cache_data</code> - dictionary from the parent class <code>BaseCaching</code></li>
<li>You can overload <code>def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code>super().__init__()</code></li>
<li><code>def put(self, key, item):</code>

<ul>
<li>Must assign to the dictionary <code>self.cache_data</code> the <code>item</code> value for the key <code>key</code>.</li>
<li>If <code>key</code> or <code>item</code> is <code>None</code>, this method should not do anything.</li>
<li>If the number of items in <code>self.cache_data</code> is higher that <code>BaseCaching.MAX_ITEMS</code>:

<ul>
<li>you must discard the least recently used item (LRU algorithm)</li>
<li>you must print <code>DISCARD:</code> with the <code>key</code> discarded and following by a new line </li>
</ul></li>
</ul></li>
<li><code>def get(self, key):</code>

<ul>
<li>Must return the value in <code>self.cache_data</code> linked to <code>key</code>.</li>
<li>If <code>key</code> is <code>None</code> or if the <code>key</code> doesn&rsquo;t exist in <code>self.cache_data</code>, return <code>None</code>.</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 3-main &quot;&quot;&quot;
LRUCache = __import__(&#39;3-lru_cache&#39;).LRUCache

my_cache = LRUCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;B&quot;))
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()
my_cache.put(&quot;H&quot;, &quot;H&quot;)
my_cache.print_cache()
my_cache.put(&quot;I&quot;, &quot;I&quot;)
my_cache.print_cache()
my_cache.put(&quot;J&quot;, &quot;J&quot;)
my_cache.print_cache()
my_cache.put(&quot;K&quot;, &quot;K&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. MRU Caching
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

<!-- Progress vs Score -->

   <!-- Task Body -->
   <p>Create a class <code>MRUCache</code> that inherits from <code>BaseCaching</code> and is a caching system:</p>

<ul>
<li>You must use <code>self.cache_data</code> - dictionary from the parent class <code>BaseCaching</code></li>
<li>You can overload <code>def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code>super().__init__()</code></li>
<li><code>def put(self, key, item):</code>

<ul>
<li>Must assign to the dictionary <code>self.cache_data</code> the <code>item</code> value for the key <code>key</code>.</li>
<li>If <code>key</code> or <code>item</code> is <code>None</code>, this method should not do anything.</li>
<li>If the number of items in <code>self.cache_data</code> is higher that <code>BaseCaching.MAX_ITEMS</code>:

<ul>
<li>you must discard the most recently used item (MRU algorithm)</li>
<li>you must print <code>DISCARD:</code> with the <code>key</code> discarded and following by a new line </li>
</ul></li>
</ul></li>
<li><code>def get(self, key):</code>

<ul>
<li>Must return the value in <code>self.cache_data</code> linked to <code>key</code>.</li>
<li>If <code>key</code> is <code>None</code> or if the <code>key</code> doesn&rsquo;t exist in <code>self.cache_data</code>, return <code>None</code>.</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 4-main &quot;&quot;&quot;
MRUCache = __import__(&#39;4-mru_cache&#39;).MRUCache

my_cache = MRUCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;B&quot;))
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()
my_cache.put(&quot;H&quot;, &quot;H&quot;)
my_cache.print_cache()
my_cache.put(&quot;I&quot;, &quot;I&quot;)
my_cache.print_cache()
my_cache.put(&quot;J&quot;, &quot;J&quot;)
my_cache.print_cache()
my_cache.put(&quot;K&quot;, &quot;K&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/$ 
</code></pre>

  </div>
