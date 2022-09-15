# Character Encoding
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# React Native Code Editor
export REACT_EDITOR=code

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=13

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
HIST_STAMPS="yyyy-mm-dd"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
alias edit="open ~/.zshrc"
alias refresh="source ~/.zshrc"
alias gc="gitmoji -c"
alias np="nodemon -e py -x"
alias npt="nodemon -e py -x pytest"
alias penv="source .venv/bin/activate"
alias whport='f() { lsof -i tcp:$1 };f'

# Sentry-specific aliases
alias sd_c="SENTRY_SILO_MODE=CONTROL sentry devserver"
alias sd_r="SENTRY_DEVSERVER_BIND=localhost:8002 SENTRY_SILO_MODE=REGION sentry devserver"
alias sd="sentry devserver"
alias sdw="sentry devserver --workers "
alias sdu="sentry devservices up"
alias sdd="sentry devservices down"
alias gsd="getsentry devserver"
alias gsdw="getsentry devserver --workers"
alias gsdu="getsentry devservices up"
alias gsdd="getsentry devservices down"

# Constants
export GPG_TTY=$(tty)
export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"

# Evals
eval "$(starship init zsh)"
eval "$(direnv hook zsh)"

# Allow autocomplete for git branches
autoload -Uz compinit && compinit
