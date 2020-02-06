# VSCode Extensions

Listing off the extensions via `code --list-extensions` yields:

```
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
```

Use `code --install-extension $author.$extension` using the above.

Install all these extensions using the `install-extensions.sh` script.
Uninstall every existing extension with the `uninstall-extensions.sh` script.