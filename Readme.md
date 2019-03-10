# Customize Markdown Editor - Sublime Text 2/3

Adds a handy command and menu item to open your current file with the customize markdown editor.

## Installation Instructions

**Package Installer**

* Install [Sublime Package Control](https://packagecontrol.io/)
* Select `Package Control: Add Repository` from the Command Palette (`super+shift+p`)
* Input `https://github.com/maboloshi/CustomizeMarkdownEditor`
* Select `Package Control: Install Package` from the Command Palette (`super+shift+p`)
* Find `CustomizeMarkdownEditor` and select

## Setting
the example markdown editor of `Typora.app`:

### Create/Merge `User/Main.sublime-menu`
```json
[
    {
        "id": "tools",
        "children":
        [
            {
                "caption": "Markdown: Open with Typora.app ...",
                "command": "open_markdown_file"
            }
        ]
    }
]
```
> Note: Don't modify the `command` section

### Create/Merge `User/Main.sublime-commands`
```json
[
    {
        "caption": "Markdown: Open with Typora.app ...",
        "command": "open_markdown_file"
    }
]
```
> Note: Don't modify the `command` section

### Create `User/CustomizeMarkdownEditor(OSX).sublime-settings`
```json
{
    "name": "Typora"
}
```

## Usage

With the view selected containing the file you wish to preview in Marked:

**Command Palette:**

* Select `Markdown: Open with Typora.app ...` from the Command Palette (`super+shift+p`)

**Menus:**

* Select `Tools` → `Markdown: Open with Typora.app ...`

# License
[MIT](http://jbrooksuk.mit-license.org)