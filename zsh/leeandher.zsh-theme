# leeandher.zsh-theme
PROMPT='[$fg[cyan]%n$reset_color@$fg[blue]%m$reset_color:$fg[magenta]%~$reset_color] $(git_prompt_info)
👉 '

function git_prompt_info() {
   ref=$(git symbolic-ref HEAD 2> /dev/null) || return
   echo "$ZSH_THEME_GIT_PROMPT_PREFIX$(parse_git_dirty)$(current_branch)$ZSH_THEME_GIT_PROMPT_SUFFIX"
}

ZSH_THEME_GIT_PROMPT_PREFIX="("
ZSH_THEME_GIT_PROMPT_SUFFIX="$reset_color)"
ZSH_THEME_GIT_PROMPT_CLEAN="$fg[green]"
ZSH_THEME_GIT_PROMPT_DIRTY="$fg[red]"
