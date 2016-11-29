# CSS and Documents #

----


## Need of CSS ##

The web has a perfect separation of concern today as shown below.

|   Purpose    |  Language  |
|:------------ | :--------- |
| Structure    | HTML       |
| Presentation | CSS        |
| Logic        | JavaScript |

But this was also a case in the beginning, where HTML did not had those dreaded **Table**, **Font** tags.

As a result of the above few things happened.

1. Lot of presentation code came into HTML.
2. Most websites has enormous markup in place of the actual content.
3. Most websites markup consisted of **table** and **font** tags.

### Disadvantages of using presentation HTML ###

1. Unstructured pages make content indexing inordinately difficult.
2. Lack of structure reduces accessibility. 
3. Advanced page presentation is possible only with some sort of document structure.
4. Structured markup is easier to maintain.

## Benefits of CSS ##
Due to mixing of presentation logic inside a structured HTML markup led to the problems listed above. To solve these issues **W3C** came up with CSS specification in 1996.

So here are the benefits of CSS.

*  **Rich Styling**

    CSS allows for richer document appearances than HTML ever allowed. Here are few things which a CSS is capable of doing.
    * Set Color on text and in the background of any element.
    * Creation of border around any elements.
    * Increase/Decrease space between elements.
    * Font related changes. italicized, capitalized, decorated etc.

Sample of these change be checked in [CSSStyling.html](CSSStyling.html)

**Example:-**
````html
<h1 style="color: maroon; 
            font: italic 2em Times, serif; 
            text-decoration: underline;
            background: yellow;">Leaping Above The Water</h1>
`````

<h1 style="color: maroon; 
            font: italic 2em Times, serif; 
            text-decoration: underline;
            background: yellow;">Leaping Above The Water</h1>



*  **Ease of Use**  
Style Sheet helps is centralizing the styles to a central place, so it helps in making changes easy.

Say to change color of `<h2>` tag to purple, in good olden days you will do something like this.

````html
    <h2><font color="purple">This is purple!</font></h2>
````

Now thing of a scene where you have 40 or more `<h2>` tags, you have to add the font tag to so many place, but with css how things become easy.

This will be your HTML,

````html
<h2>This is purple!<h2>
````

And this will be you CSS,
````css
h2 {color: purple;}
````
So if you have to change tomorrow the color to green, you have to just change your css at only one place and all `<h2>` tags will be changed.

*  **Using same style across multiple HTML file**  
Not only we can centralize the css for a file at one place, we can also create a simple css files which can be shared across all html files.

We can add a sample css file into a html document with this code.  
````html
<link rel="stylesheet" type="text/css" href="mystyle.css">
````
So now a simple change in one CSS file will be reflected in multiple HTML files.

*  **Cascading**  
CSS also helps in cascading styles, like say you have 100 of html file where you want to apply one CSS rules, but out of these you want a different style of a particular file, you can just override the default behavior by have a style specific to the files, or add another CSS sheet which is inserted after the default CSS files.  
Also a reader can have its own CSS files in the browser where he is viewing the web page which helps him in customizing the view of a web page as per his needs.  
This is the true power of cascading in CSS.

*  **Compact file size.**  
CSS also help in reducing the file size considerably as you we will not have unnecessary markup in HTML files for presentation.
*  **Preparing for future.**  
With the advent of CSS it is quite possible that most of the presentation tags from HTML will be removed, also we can use XML for content and CSS for styling, in both cases, knowing CSS helps.
## Elements ##  
*Elements* are the basis of document structure. Every single element in a document plays a part in the presentation. Elements can be divided into two groups based on classification.  
1. Elements take two forms.
    1. Replaced Elements.
    2. Non-Replaced Elements.
2. Based on Display roles.
    1. Block-Level elements.
    2. Inline-Level elements.      

### Replaced and Nonreplaced Elements ###
#### Replaced elements ####  
*Replaced elements* are  those where the element's content is replaced by something that is not directly represented by document content.  
The most famous elements in this group is `<img>` tag, as explained in the example below.  
````html
<img src="howdy.gif" />
````  
In the above code, there is no actual content, only a *tag* and *attribute*, the attribute `src=` actually decides what content will be shown.
#### Nonreplaced elements ####  
*Non replaced elements* are those whose content is presented by the user agent (generally a browser) inside a box generated by the element itself.  
Most of HTML elements fall in this group,  
````html
<span>hi there</span>
````
In the above example the text `hi there` is the actual content of the `<span>` tag.
### Element Display Roles ###
#### Block-level elements ####  
*Block-level elements* generate an element box that (by default) fills its parent element’s content area and cannot have other elements at its sides.  
In a much simpler language, they have line break before and after the elements.  
Replaced elements can be block level elements, but generally it is not.  
List items are a special case of block level elements, because of the *bullet* which gets attached to the elements.  
List of block level elements can be found at [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)
#### Inline-level elements ####  
*Inline-level elements* generate an element box within a line of text and do not break up the flow of that line.  
The list of inline level elements can be found at [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elemente)  

**Example:-**
Consider the below mark up, in this markup `<p>` is a block element and `<em>` is an inline element.  
````html
<body>
<p>This is a paragraph with <em>an inline element</em> within it.</p>
</body>
````
it should displayed as below.
<p>This is a paragraph with <em>an inline element</em> within it.</p>
The above behavior of block an inline elements can be changes with the below CSS.  
````css
p {display: inline;}
em {display: block;}
````
The output should look like this.

````html
<p style="display: inline;">This is a paragraph with <em style="display: block;">an inline element</em> within it.</p>
````  

## Bringing CSS and HTML Together ##
Structure is an inherent part of the relationship between HTML and CSS, without the structure there cannot be any relationship. The next section will take inspiration from the page show at [Waffles](Waffles.html).  
Now we will check how CSS and HTML connect together.
### The Link Tag ###
Consider the following code,  
````
<link rel="stylesheet" type="text/css" href="sheet1.css" media="all">
````
The basic purpose of the link tag is to:-  

* Allow HTML authors to associate other documents with the document containing the link tag.
* CSS uses this tag to link style sheet to HTML.

These style sheet which are not part of the HTML document but are still used by it, are referred to as *external style sheet*.  
The link tag should be present in the `<head></head>` tag. There are other places we can have have it, which will be discussed later.  
The external style sheet contains CSS rules, just the difference is that it is saved as a different file, a sample content of the CSS file will look like this:-  
````
h1 {color: red;}
h2 {color: maroon; background: white;}
h3 {color: white; 
    background: black;
    font: medium Helvetica;
    }
````
Care should be taken that CSS does not have any markup when used with `<link rel="stylesheet" type="text/css" href="">` tag. The file name may or may not have the extension of `.css`, but some older browser won't recognize a style sheet if it does not end in `.css`.
#### Attributes ####
All the attributes in the `<link>` tag have a purpose.  

* `rel="stylesheet"` : **rel** stands for relation, in this case it means the relation is a **stylesheet**.
* `type="text/css"` : **type** is always set to **text/css**, this describes the type of data that will be loaded as a '<link>'tag.
* `href="sheet1.css"` : **href** is the URL to the actual file, the URL can be absolute or relative.
* `media="all"` : **media** means the type of media on which this CSS has to be applied, the value **all** actually means all media. The different type of media values are.
  * `all` : Use in all presentation media.
  * `aural` : Use in Speech synthesizers, screen readers, and other audio rendering of the documents.
  * `braille` : Use when rendering the document with a Braille device.
  * `embossed` : Use when printing with a Braille printing device.
  * `handheld` : Use on handheld devices like personal digital assistants or web-enabled cell phones.
  * `print` : Use when printing the document for sighted users and also when displaying a "print preview" of the document.
  * `projection` : Use in a projection medium, such as a digital projector used to present a slideshow when delivering a speech.
  * `screen` : Use when presenting the document in a screen medium like a desktop computer monitor. All web browsers running on such systems are screen-medium user agents.
  * `tty` : Use when delivering the document in a fixed-pitch environment like teletype printers.
  * `tv` : Use when the document is being presented on a television.

The most commonly used value of `media` are `all`,`screen`,`print`.  
You can also use one style sheet for more than one media with the below code.  
````
<link rel="stylesheet" type="text/css" href="visual-sheet.css"
   media="screen, projection" />
````

More than one style sheet can also be used in a HTML document, you can include it in this manner. This will cause both the style sheet to be loaded, rules to be combined, and apply these combined rule to the document.  
````
<link rel="stylesheet" type="text/css" href="basic.css" />
<link rel="stylesheet" type="text/css" href="splash.css" />
````

#### Alternate Style Sheet ####

It is also possible to define *alternate style sheet*. These are defined by using the value of `rel` attribute to `alternate stylesheet`, as shown below:-  
````
<link rel="alternate stylesheet" type="text/css" href="bigtext.css" title="Big Text" />
````
The user can select these style sheet from the browser option, those this feature is not available in chrome.

It is also possible to group *alternate style sheet* together by giving the same `title`. This make it possible for the user's to pick a different presentation for the site in both screen and print medium. Consider the below code.  
````
<link rel="stylesheet" type="text/css" href="sheet1.css" title="Default" media="screen" />
<link rel="stylesheet" type="text/css" href="print-sheet1.css" title="Default" media="print" />
<link rel="alternate stylesheet" type="text/css" href="bigtext.css" title="Big Text" media="screen" />
<link rel="alternate stylesheet" type="text/css" href="print-bigtext.css" title="Big Text" media="print" />
````

In the above code, if the user select **Big Text** as the preferred style sheet from the browser options, then "bigtext.css" is applied in the `screen` medium and "print-bigtext.css" in the `print` medium.

If you do not give a style sheet a title then it becomes a *persistent style sheet* and is always used in the display of the content.

### The Style Element ###

The *style* element is one way to include style sheet, an it appears in the document itself.

````
<style type="text/css">
````

`<style>` should always be used with attribute `type`, also `media` attribute is also supported.
The `<style>` opening and the closing tags enclose the css codes.

The styles between the opening and closing tags are refferred to as *document style sheet* since the style is embedded within the document.

### The @import Directive ###

Consider the following code,

````
@import url(sheet2.css);
````
Just like link, @import can be used to direct the web browser to load an external style sheet and use its styles in the rendering of the HTML document.

Unlike link, however, the style sheets of every @import directive will be loaded and used;

There is no way to designate alternate style sheets with @import.

As with link, you can restrict imported style sheets to one or more media by listing the media to which it should be applied after the style sheet’s URL:
````
@import url(sheet2.css) all;
@import url(blueworld.css) screen;
@import url(zany.css) projection, print;
````

@import can be highly useful if you have an external style sheet that needs to use the styles found in other external style sheets. Since external style sheets cannot contain any document markup, the link element can’t be used but @import can.

````
@import url(http://example.org/library/layout.css);
@import url(basic-text.css);
@import url(printer.css) print;
body {color: red;}
h1 {color: blue;}
````


### The Actual Style Rules ###
#### Backward accessibility ####

For those of you concerned about making your documents accessible to older browsers, there is an important warning to consider.  
If a browser does not recognize <style> and </style>, it will ignore them altogether. However, the declarations within those tags will not necessarily be ignored because they look like ordinary text as far as the browser is concerned.  
To combat this problem, it is recommended that you enclose your declarations in a comment tag.  
````
<style type="text/css"><!--
@import url(sheet2.css);
h1 {color: maroon;}
body {background: yellow;}
--></style>
````  
This should cause older browsers to completely ignore the declarations as well as the style tags because HTML comments are not displayed.

### CSS Comment ###

CSS also allows for comments. These are very similar to C/C++ comments in that they are surrounded by /* and */:

````
/* This is a CSS1 comment */
````  
It's important to remember that CSS comments cannot be nested. 

### Inline Style ###
For cases where you want to simply assign a few styles to one individual element, without the need for embedded or external style sheets, employ the HTML attribute style to set *an inline style*:

````
<p style="color: gray;">The most wonderful of all breakfast foods is
the waffle--a ridged and cratered slab of home-cooked, fluffy goodness...
</p>
````
Some of the primary advantages of CSS—the ability to organize centralized styles that control an entire document's appearance or the appearance of all documents on a web server—are negated when you place styles into a style attribute.









