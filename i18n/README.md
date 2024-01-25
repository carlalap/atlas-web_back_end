# i18n

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://python-babel.github.io/flask-babel/" title="Flask-Babel" target="_blank">Flask-Babel</a></li>
<li><a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n" title="Flask i18n tutorial" target="_blank">Flask i18n tutorial</a></li>
<li><a href="https://sourceforge.net/directory/software-development/windows/" title="pytz" target="_blank">pytz</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Learn how to parametrize Flask templates to display different languages</li>
<li>Learn how to infer the correct locale based on URL parameters, user settings or request headers</li>
<li>Learn how to localize timestamps</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle style (version 2.5)</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>All your <code>*.py</code> files should be executable</li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions and methods should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions and coroutines must be type-annotated.</li>
</ul>

  </div>
</div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Basic Flask app
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
  <div class="task_progress_score_bar" data-task-id="21884" data-correction-id="707695">
     <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>First you will setup a basic Flask app in <code>0-app.py</code>. Create a single <code>/</code> route and an <code>index.html</code> template that simply outputs &ldquo;Welcome to Holberton&rdquo; as page title (<code>&lt;title&gt;</code>) and &ldquo;Hello world&rdquo; as header (<code>&lt;h1&gt;</code>).</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Basic Babel setup
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21885" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Install the Babel Flask extension:</p>

<pre><code>$ pip3 install flask_babel
</code></pre>

<p>Then instantiate the <code>Babel</code> object in your app. Store it in a module-level variable named <code>babel</code>.</p>

<p>In order to configure available languages in our app, you will create a <code>Config</code> class that has a <code>LANGUAGES</code> class attribute equal to <code>[&quot;en&quot;, &quot;fr&quot;]</code>.</p>

<p>Use <code>Config</code> to set Babel&rsquo;s default locale (<code>&quot;en&quot;</code>) and timezone (<code>&quot;UTC&quot;</code>).</p>

<p>Use that class as config for your Flask app.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Get locale from request
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

  <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21886" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

    <!-- Task Body -->
    <p>Create a <code>get_locale</code> function with the <code>babel.localeselector</code> decorator. Use <code>request.accept_languages</code> to determine the best match with our supported languages.</p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Parametrize templates
    </h3>
</div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21887" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
   <p>Use the <code>_</code> or <code>gettext</code> function to parametrize your templates. Use the message IDs <code>home_title</code> and <code>home_header</code>.</p>

<p>Create a <code>babel.cfg</code> file containing</p>

<pre><code>[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
</code></pre>

<p>Then initialize your translations with</p>

<pre><code>$ pybabel extract -F babel.cfg -o messages.pot .
</code></pre>

<p>and your two dictionaries with </p>

<pre><code>$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
</code></pre>

<p>Then edit files <code>translations/[en|fr]/LC_MESSAGES/messages.po</code> to provide the correct value for each message ID for each language. Use the following translations:</p>
<table class="hbtn-table"><tr>
<th>msgid</th>
<th>English</th>
<th>French</th>
</tr>
<tr>
<td><code>home_title</code></td>
<td><code>&quot;Welcome to Holberton&quot;</code></td>
<td><code>&quot;Bienvenue chez Holberton&quot;</code></td>
</tr>
<tr>
<td><code>home_header</code></td>
<td><code>&quot;Hello world!&quot;</code></td>
<td><code>&quot;Bonjour monde!&quot;</code></td>
</tr>
</table>
<p>Then compile your dictionaries with</p>

<pre><code>$ pybabel compile -d translations
</code></pre>

<p>Reload the home page of your app and make sure that the correct messages show up.</p>

  </div>

 <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Force locale with URL parameter
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21888" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

   <!-- Task Body -->
   <p>In this task, you will implement a way to force a particular locale by passing the <code>locale=fr</code> parameter to your app&rsquo;s URLs.</p>

<p>In your <code>get_locale</code> function, detect if the incoming request contains <code>locale</code> argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.</p>

<p>Now you should be able to test different translations by visiting <code>http://127.0.0.1:5000?locale=[fr|en]</code>.</p>

<p><strong>Visiting <code>http://127.0.0.1:5000/?locale=fr</code> should display this level 1 heading:</strong>
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240201%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240201T044137Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=510eb9e63568168e77914603d8fdfe8f82ade4ef4066b028c5e2b68dfaa8d62d" alt="" loading='lazy' style="" /></p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Mock logging in
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21889" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in <code>5-app.py</code>.</p>

<pre><code>users = {
    1: {&quot;name&quot;: &quot;Balou&quot;, &quot;locale&quot;: &quot;fr&quot;, &quot;timezone&quot;: &quot;Europe/Paris&quot;},
    2: {&quot;name&quot;: &quot;Beyonce&quot;, &quot;locale&quot;: &quot;en&quot;, &quot;timezone&quot;: &quot;US/Central&quot;},
    3: {&quot;name&quot;: &quot;Spock&quot;, &quot;locale&quot;: &quot;kg&quot;, &quot;timezone&quot;: &quot;Vulcan&quot;},
    4: {&quot;name&quot;: &quot;Teletubby&quot;, &quot;locale&quot;: None, &quot;timezone&quot;: &quot;Europe/London&quot;},
}
</code></pre>

<p>This will mock a database user table. Logging in will be mocked by passing <code>login_as</code> URL parameter containing the user ID to log in as.</p>

<p>Define a <code>get_user</code>  function that returns a user dictionary or <code>None</code> if the ID cannot be found or if <code>login_as</code> was not passed.</p>

<p>Define a <code>before_request</code> function and use the <code>app.before_request</code> decorator to make it be executed before all other functions. <code>before_request</code> should use <code>get_user</code> to find a user if any, and set it as a global on <code>flask.g.user</code>.</p>

<p>In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.</p>
<table class="hbtn-table"><tr>
<th>msgid</th>
<th>English</th>
<th>French</th>
</tr>
<tr>
<td><code>logged_in_as</code></td>
<td><code>&quot;You are logged in as %(username)s.&quot;</code></td>
<td><code>&quot;Vous êtes connecté en tant que %(username)s.&quot;</code></td>
</tr>
<tr>
<td><code>not_logged_in</code></td>
<td><code>&quot;You are not logged in.&quot;</code></td>
<td><code>&quot;Vous n&#39;êtes pas connecté.&quot;</code></td>
</tr>
</table>
<p><strong>Visiting <code>http://127.0.0.1:5000/</code> in your browser should display this:</strong></p>

![Alt Text](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240201%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240201T044137Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c37a9cc1b4b153fa8f63f555db6ffafeffe55b30d639af81d034adbdb68e0b29)

<p><strong>Visiting <code>http://127.0.0.1:5000/?login_as=2</code> in your browser should display this:</strong>
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240201%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240201T044137Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=41a83c4ac1d805e783caf6ce5c5c92f35457d7770403946696213048d7923b4d" alt="" loading='lazy' style="" /></p>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Use user locale
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21890" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
  <p>Change your <code>get_locale</code> function to use a user&rsquo;s preferred local if it is supported.</p>

<p>The order of priority should be</p>

<ol>
<li>Locale from URL parameters</li>
<li>Locale from user settings</li>
<li>Locale from request header</li>
<li>Default locale</li>
</ol>

<p>Test by logging in as different users</p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240201%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240201T044137Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=381a353761b0265336df16bb5ce141d0774a1702c4b1c15a1ea763c1a1491d37" alt="" loading='lazy' style="" /></p>
  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. Infer appropriate time zone
    </h3>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="6138"></span>

   <!-- Progress vs Score -->
   <div class="task_progress_score_bar" data-task-id="21891" data-correction-id="707695">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>
        </div>
        <div class="task_progress_score_text">
          Score: <span class="task_score_value">0%</span> (<span class="task_progress_value">Checks completed: 0%</span>)
        </div>
      </div>

  <!-- Task Body -->
   <p>Define a <code>get_timezone</code> function and use the <code>babel.timezoneselector</code> decorator.</p>

<p>The logic should be the same as <code>get_locale</code>:</p>

<ol>
<li>Find <code>timezone</code> parameter in URL parameters</li>
<li>Find time zone from user settings</li>
<li>Default to UTC</li>
</ol>

<p>Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use <code>pytz.timezone</code> and catch the <code>pytz.exceptions.UnknownTimeZoneError</code> exception.</p>

  </div>
