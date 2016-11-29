# Complete guide to setup Sublime Text 2 as a best MarkDown Editor.
----

Sublime Text is one of a very light-weight, feature heavy, extensible code editor. 

The true power of Sublime Text come from 

1. Package Control provide by wbond, 
2. Not remembering a lot of keystrokes. Only `crtl+shift+p` opens up the command palette where we can just type what we want.
3. Multiple cursor, you can highlight on a word and if you want to select all the matching word and change just keep pressing `ctrl + d`
4. Also you can have the same text editor across all Operating System.

If you want toe use the full power of Sublime Text, TutsPlus have a great course for it you can check it [here](https://tutsplus.com/course/improve-workflow-in-sublime-text-2/)

[Sublime Text 2](http://www.macstories.net/roundups/sublime-text-2-and-markdown-tips-tricks-and-links/)

## Install Sublime Text 2 and Package Control
----

You can install Sublime Text 2 depending on you operating system. There is a previous post from my on this.

1. Ubuntu 14.04
2. Mac OS X (Mavericks)

---

## MarkDown ##
---
As mentioned in Wiki, and i am quoting from there.

> Markdown is a plain text formatting syntax[5] designed so that it can optionally be converted to HTML using a tool by the same name. Markdown is popularly used as format for readme files, or for writing messages in online discussion forums, or in text editors for the quick creation of rich text documents.
> 

You can read the complete article here [MarkDown-wiki](http://en.wikipedia.org/wiki/Markdown).

In fact this complete blog is written in Markdown. To enable markdown in Wordpress blog you can follow the instructions written [here](http://en.support.wordpress.com/markdown/).

For Syntax of Markdown you can visit [Daring FireBall](http://daringfireball.net/projects/markdown/), the site created by the creator of Markdown **John Gruber **.

A very nice Cheat Sheet for Markdown syntax are available at [GitHub](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Install MarkDown Editing Package Control
The detailed process of installing Markdown in Sublime Text 2 is mentioned at [GuidingTech](http://www.guidingtech.com/26607/turn-sublime-text-3-markdown/), But a very simpler version is.

1. Perquisite is to have Package control Installed. 
2. Open **Command Palette** by using the key stroke `Ctrl + shift +p`.
3. Type **MarkDownEditing** and install the package.
4. After this Markdown should be installed.

## Few Modification for Markdown Editing.
The default setting is also great for Markdown, but i guess lot of people does not like the default behavior of anything. So here are few things which you can change.

1. Open any markdown file with **.md** extension.
2. Click `Preferences -> Settings-More -> Syntax Specific-User`. This will open a File for changing some option.
3. First thing we should do after to achieve something different in Markdown is.
    1. Enable Spell Check in Markdown, because you will be writing normal english mostly, by writing the following line.
        1. `"spell_check": true`
    2. Enable Dark Theme for Markdown theme.
        1. `"color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme"`  


----
## Chrome, FireFox, extensions for MarkDown

Now to View Markdown file in browser, you need some browser specific plugins. I have listed down some of the plugins.

----
###Install Markdown Plugin for FireFox
For FireFox the best is MarkDown Viewer by Thiht which you can download from [here](https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer/),There is one issue with this plugin in firefox, it does not displays the *.md* files though it opens other markdown extensions, the bug can be found at  [markdown-viewer](https://github.com/Thiht/markdown-viewer/issues/3)

A possible solution is mentioned in this link, [Ryanchapin](http://www.ryanchapin.com/Home?article_id=737)

Basically you have to edit this file, `~/.mozilla/firefox/*default/mimeTypes.rdf` and add the below code at the end.

````
<RDF:Description RDF:about="urn:mimetype:text/plain"
        NC:value="text/plain"
        NC:fileExtensions="md"
        NC:description="Text Document">
    <NC:handlerProp RDF:resource="urn:mimetype:handler:text/plain"/>
</RDF:Description>
````
###Install Markdown Plugin for Chrome.

For Chrome the best plugin is [Markdown Preview Plus](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl), the benefit of this plugin over others including the one in Firefox is this allows you to add your own custom css for displaying markdown file.

If you are not using apache to see the markdown file using *localhost*, you have to enable `Allow access to file URLs` in `chrome://extensions/` for Markdown Preview Plus.

----
## Live Reload for MarkDown
One very useful feature in markdown is you can have live reload in the browser, so as soon as you save a markdown file in sublime, the changes is reflected in the browser, you do not have to reload the file manually.

###Install Live Reload In Sublime Text

Here are the steps to install Live Reload 

1. Perquisite is to have Package control Installed. 
2. Open **Command Palette** by using the key stroke `Ctrl + shift +p`.
3. Type **Livereload** and install the package.
4. After this LiveReload should be installed.

After you have installed LiveReload Plugin, you have to installed the respective Browser Extensions, 

### Browser Extension of LiveReload for Chrome
You can Install Live Reload for Chrome by following the instruction mentioned here.

1. [LiveReload Extension](http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-)
2. [LiveReload Installation Guide](http://www.ishaanrawat.com/setting-up-livereload-for-sublime-text-2/)

### Browser Extension of LiveReload for  FireFox
You can install Live Reload for Firefox by following the instruction mentioned here.

1. [LiveReload Extension](http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-)

There is a bug in Firefox extension so it may not work, you can install another **.xpi** file mentioned in [StackOverflow](http://stackoverflow.com/questions/8710613/livereload-not-working-guard-firefox/11068251#11068251)

-----

After following all the above steps you will have a very stable Markdown editing plugin for Sublime and also a viewer in Browser, So enjoy writing your content in plain text, and let other bother about converting it into HTML, as it is said in Blogging Content is the King, so focus more on content than presentation.