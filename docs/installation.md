# Installation

This guide explains how to install and configure NEXTHON on Windows.

## Requirements

Before installing NEXTHON, make sure you have:

- **Windows 10 or later**
- **Python 3.14.x**
- **Git**

You can download them here:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

During Python installation, make sure to enable **Add Python to PATH**.

## 1. Download NEXTHON

Open PowerShell or Command Prompt and clone the repository:

```powershell
git clone https://github.com/Nexform-star/NEXTHON.git
```

Move into the project directory:

```powershell
cd NEXTHON
```

## 2. Test NEXTHON

Run the following command:

```powershell
.\nexthon.cmd --version
```

Expected output:

```text
NEXTHON 0.1.0
```

You can also run the Hello World example:

```powershell
.\nexthon.cmd examples\hello.ne
```

## 3. Add NEXTHON to PATH

Adding NEXTHON to the Windows PATH allows you to run it from any directory without specifying the full path to `nexthon.cmd`.

1. Open the Windows Start menu.
2. Search for `Edit environment variables for your account`.
3. Open the result.
4. Select the `Path` variable under **User variables**.
5. Click **Edit**.
6. Click **New**.
7. Add the full path to your NEXTHON project directory (the folder containing `nexthon.cmd`).
8. Confirm all windows by clicking **OK**.

**Important:** Close and reopen your terminal after modifying PATH.

### Verify PATH configuration

Open a new terminal and run:

```powershell
nexthon --version
```

If the version is displayed, NEXTHON is correctly configured.

You can now run `.ne` files from any directory:

```powershell
nexthon examples\hello.ne
```

## 4. Visual Studio Code

NEXTHON has a Visual Studio Code extension that provides syntax highlighting and snippets.

You can install it from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nexform.nexthon-language).

After installation, open a `.ne` file in VS Code.

## Next steps

- [Getting Started](getting-started.md)
- [Language Syntax](syntax.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
