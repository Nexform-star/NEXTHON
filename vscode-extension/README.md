# NEXTHON Language Support for VS Code

## Test the extension

1. Open this folder (`nexthon-vscode-extension`) in VS Code.
2. Press F5.
3. A second VS Code window opens (Extension Development Host).
4. In that window, open your NEXTHON project or create a file ending in `.ne`.
5. Check the language mode in the bottom-right: it should say **NEXTHON**.
6. Test snippets by typing `function` or `if` and pressing Tab.

This is a declarative language extension: syntax highlighting, language configuration and snippets. It does not include the NEXTHON interpreter.

## Install locally

Copy this folder to your VS Code extensions directory, or package it later with `vsce`.
