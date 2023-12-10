-- Nvim Lazy setup
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"

if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Set up plugins
require('lazy').setup({
	'ellisonleao/gruvbox.nvim',
	'preservim/nerdtree',
	'simrat39/rust-tools.nvim',
	'neovim/nvim-lspconfig',
	'vim-airline/vim-airline',
	'vim-airline/vim-airline-themes',
	'chikko80/error-lens.nvim',
	'nvim-telescope/telescope.nvim',
})

-- setup error lens
require("error-lens").setup(client, {

})

vim.cmd([[
set number

colorscheme gruvbox

AirlineTheme base16_gruvbox_dark_medium
let g:airline_powerline_fonts = 1
]])

-- Setup language servers
local lspconfig = require('lspconfig')

lspconfig.pyright.setup {}
lspconfig.tsserver.setup {}
lspconfig.rust_analyzer.setup {}


