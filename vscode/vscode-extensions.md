# VSCode Extensions

Listing off the extensions via `code --list-extensions` yields:

```
alefragnani.project-manager
christian-kohler.path-intellisense
dbaeumer.vscode-eslint
dracula-theme.theme-dracula
eamodio.gitlens
esbenp.prettier-vscode
jpoissonnier.vscode-styled-components
ms-vscode.vscode-typescript-tslint-plugin
naumovs.color-highlight
PKief.material-icon-theme
pnp.polacode
tinkertrain.theme-panda
yzhang.markdown-all-in-one
```

Use `code --install-extension $author.$extension` using the above.

To install all of them, copy paste the following batch install script.

Take a look at [this](https://gist.github.com/mdschweda/2311e3f2c7062bf7367e44f8a7aa8b55).

```bash
code --install-extension alefragnani.project-manager christian-kohler.path-intellisense
```
