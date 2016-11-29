" http://vimcasts.org/episodes/synchronizing-plugins-with-git-submodules-and-pathogen/
" call pathogen#runtime_append_all_bundles() This doesnot work, used the next link.
call pathogen#helptags()

" https://github.com/tpope/vim-pathogen
execute pathogen#infect()
syntax on
filetype plugin indent on

" https://github.com/altercation/vim-colors-solarized
syntax enable
" set background=dark
colorscheme solarized

" Setting if gui is running or in terminal
if has('gui_running')
    set background=dark
else
    set background=light "Seting light in termial is not working for non-gui
endif

" http://www.alexeyshmalko.com/2014/using-vim-as-c-cpp-ide/
" set indentation rules

set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

" File-type detection
augroup project
    autocmd!
    autocmd BufRead,BufNewFile *.h,*.c set filetype=c.doxygen
augroup END


" Setting path variable
" using the gF command to open File from system.

let &path.="/usr/include/,"

" http://www.alexeyshmalko.com/2014/youcompleteme-ultimate-autocomplete-plugin-for-vim/
" In order to auto-complete source code for C family, you should provide custom .ycm_extra_conf.py file for your project. If you don’t do this, YCM will be unable to use semantic completion.
let g:ycm_global_ycm_extra_conf = "~/.vim/.ycm_extra_conf.py"

"NERDTree plugin configuration.


"open a NERDTree automatically when vim starts up
autocmd vimenter * NERDTree

"open a NERDTree automatically when vim starts up if no files were specified
autocmd vimenter * if !argc() | NERDTree | endif

"map a specific key or shortcut to open NERDTree
map <C-n> :NERDTreeToggle<CR>

"close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
"cursor always starts in the NERDTree window
"http://stackoverflow.com/questions/1447334/how-do-you-add-nerdtree-to-your-vimrc
autocmd VimEnter * wincmd p
"Easy window navigation, Just use CTRL + hjkl for navigation inplace of CTRL + W
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
