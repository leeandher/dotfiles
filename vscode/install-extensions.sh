#!/bin/bash

extensions=(
    alefragnani.project-manager
    christian-kohler.path-intellisense
    CoenraadS.bracket-pair-colorizer-2
    cssho.vscode-svgviewer
    dbaeumer.vscode-eslint
    dsznajder.es7-react-js-snippets
    dzannotti.vscode-babel-coloring
    eamodio.gitlens
    esbenp.prettier-vscode
    jpoissonnier.vscode-styled-components
    ms-azuretools.vscode-docker
    ms-python.python
    ms-vscode.vscode-typescript-tslint-plugin
    naumovs.color-highlight
    PKief.material-icon-theme
    pnp.polacode
    teabyii.ayu
    yzhang.markdown-all-in-one
    ziyasal.vscode-open-in-github
)

for ext in ${extensions[@]}; do
    code --install-extension $ext
done

echo "Completed installations!"