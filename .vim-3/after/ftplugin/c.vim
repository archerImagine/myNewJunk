" set UTF-8 encoding
" https://gist.github.com/rocarvaj/2513367
" http://vim.wikia.com/wiki/Keep_your_vimrc_file_clean
set enc=utf-8
set fenc=utf-8
set termencoding=utf-8

" use indentation of previous line
set autoindent

" use intelligent indentation for C
set smartindent

" configure tabwidth and insert spaces instead of tabs
set tabstop=4        	" tab width is 4 spaces
set shiftwidth=4     	" indent also with 4 spaces
set expandtab 		" expand tabs to spaces
" wrap lines at 120 chars. 80 is somewaht antiquated with nowadays displays.
set textwidth=120

" turn syntax highlighting on
set t_Co=256
syntax on

" turn line numbers on
set number

" highlight matching braces
set showmatch

" intelligent comments
set comments=sl:/*,mb:\ *,elx:\ */

" set tags+=~/.vim/tags/C

