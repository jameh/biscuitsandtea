%%%
#My Python-Markdown + extensions setup

For the basic syntax of the language, see John Gruber's [original post](http://daringfireball.net/projects/markdown/syntax){: title="Original markdown specification at daringfireball.net" }

##Get it
If you don't have [pip](https://pypi.python.org/pypi/pip), or [easy_install](http://pythonhosted.org/distribute/easy_install.html), you're seriously missing out.
```bash
sudo pip install markdown
```
%%%
Alternative installation methods are described [here](http://pythonhosted.org/Markdown/install.html).

##Use it
```python
from markdown import markdown as md
print(md("#Header 1\n##Header 2"))
print(html_content)
<h1>Header 1</h1>
<h2>Header 2</h2>

```

The [Python implementation](http://pythonhosted.org/Markdown/index.html) of markdown is great for a couple of reasons:

1.  Markdown is sublime to write in. (and Python makes it better)
2.  "Safe Mode" which disallows raw html for untrusted users (like in a site's comment section, see [Stack Overflow](http://stackoverflow.com))
3.  Python has extended the markdown syntax with their own [extensions]((http://pythonhosted.org/Markdown/extensions/index.html)){: title="Python Markdown Extensions" }
4.  Python has a [Markdown Extension API](http://pythonhosted.org/Markdown/extensions/api.html) !! So you can customize the syntax to your heart's content.

##Official Extensions

Some of the markdown extensions are so wonderful, that they're all packaged up with your download. These are enumerated [here](http://pythonhosted.org/Markdown/extensions/index.html){: title="Python Markdown Extensions" }

These are the ones I've found a need for are:

*  [Attribute Lists](http://pythonhosted.org/Markdown/extensions/attr_list.html)
*  [Fenced Code Blocks](http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html)
*  [CodeHilite](http://pythonhosted.org/Markdown/extensions/code_hilite.html)

To add them to your markdown parser, pass [their names]() like this:

```python
md(some_markdown_text, ['attr_list', 'fenced_code', 'codehilite'])
```

To add more extensions, just add their keyword to that list. A list of them is [here](http://pythonhosted.org/Markdown/extensions/index.html)

and why they're awesome:
###Attribute Lists
The attribute lists extension lets us add [attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#Attributes "Mozilla HTML Docs <a> tag attributes").
To add attributes, like "width", the syntax is:

```markdown
![A beautiful cat.]({{ url_for('media', filename='beautiful_cat.jpg') }}){: width=200px }
```

To enable, add the keyword attr_list to the second argument of the markdown function (in a list):

```python
from markdown import markdown as md
print(md("![A beautiful cat.]({{ url_for('media', filename='beautiful_cat.jpg') }})\n{: width=200px }",
         ['attr_list']))
<p width="200px"><img alt="A beautiful cat." src="/media/beautiful_cat.jpg" /></p>

```

also, a short form exists for ids and classes:

```markdown
![A beautiful cat.]({{ url_for('media', filename='beautiful_cat.jpg') }}){: #most-beautiful-cat .cat }
```

And the cat:
![A beautiful cat.]({{ url_for('media', filename='beautiful_cat.jpg') }}){: #cat width=200px .floatright }


###Fenced Code Blocks and CodeHilite
You've probably noticed how pretty my code blocks are. That's thanks to these two extensions. 

The syntax I like most for fenced code blocks is Github's triple backticks (ignore the leading spaces):

~~~markdown
```javascript
var i = 0
```
~~~
and \`single ticks\` for `inline code`

[CodeHilite](http://pythonhosted.org/Markdown/extensions/code_hilite.html) uses the [Pygments](http://pygments.org/download/) package to parse the code blocks generating ugly HTML that can be styled with one of [these fantastic CSS sheets](https://github.com/richleland/pygments-css "Pygments CSS on Github"). The one I'm using right now is [monokai.css](https://github.com/richleland/pygments-css/blob/master/monokai.css).

To specify what language to parse the code as, it's this simple (again, ignore leading space before backticks):
~~~markdown
```python
def sing(n=0):
    if n < 3:
        print("row", end="")
    elif n == 3:
        print("your boat", end="")
    elif n == 4:
        print("gently down the stream", end="")
    elif n > 4 and n < 9:
        print("merrily", end="")
    elif n == 9:
        print("life is but a dream", end="")
    
    if n < 2 or (n > 4 and n < 9):
        print(", ", end="")
    elif n == 4:
        print(";")
    elif n == 9:
        print(".")
        return
    else:
        print(" ", end="")
    
    sing(n+1)

sing()
```
~~~

###Third Party Extensions
A list of third party extensions is kept up-to-date [here](https://github.com/waylan/Python-Markdown/wiki/Third-Party-Extensions)

Personally, I am particularly interested in [this LaTeX extension](https://github.com/mayoff/python-markdown-mathjax) that uses mathjax to parse the LaTeX embedded code. And in the [Superscript](https://github.com/sgraber/markdown.superscript) and [Subscript](https://github.com/sgraber/markdown.subscript) extensions by [@sgraber](https://github.com/sgraber "sgraber's Github page").

##That's it
And that's it! just point Python to your markdown file, and get wonderful HTML out.

*[CSS]: Cascading StyleSheets
*[HTML]: Hyper Text Markup Language
