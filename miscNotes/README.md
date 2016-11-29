# miscNotes
Scratchpad for all little details which I will find from various source.

# VIM #

* [Synchronizing plugins with git submodules and pathogen](http://vimcasts.org/episodes/synchronizing-plugins-with-git-submodules-and-pathogen/)

````
./configure --with-features=huge \
            --enable-multibyte \
            --enable-rubyinterp \
            --enable-pythoninterp \
            --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ \
            --enable-perlinterp \
            --enable-luainterp \
            --enable-gui=gtk2 --enable-cscope --prefix=/usr \
            --prefix=/home/animeshkbhadra/myBin

sudo update-alternatives --install /usr/bin/editor editor /home/animeshkbhadra/myBin/bin/vim 1
sudo update-alternatives --set editor /home/animeshkbhadra/myBin/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /home/animeshkbhadra/myBin/bin/vim 1
sudo update-alternatives --set vi /home/animeshkbhadra/myBin/bin/vim          

sudo update-alternatives --install /usr/bin/vim vim /home/animeshkbhadra/myBin/bin/vim 1
sudo update-alternatives --set vim /home/animeshkbhadra/myBin/bin/vim          
````

## Vim Plugin ##

* [nerdtree](https://github.com/scrooloose/nerdtree)


