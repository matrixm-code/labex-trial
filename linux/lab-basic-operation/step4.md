# Copy Files and Directories

`cp` is a command that allows you to copy files and directories.

## Copy Files

The following example shows how to copy the `~/.zshrc` file to the `~/Desktop/zshrc-copy`.

```bash
cp ~/.zshrc ~/Desktop/zshrc-copy
ls -l ~/Desktop
```

![lab-basic-operation-4-1](assets/lab-basic-operation-4-1.png)

## Copy Directories

The following example shows how to copy the `~/Code` directory to the `~/Desktop`.

```bash
cp -r ~/Code ~/Desktop/Code
ls -l ~/Desktop
```

![lab-basic-operation-4-2](assets/lab-basic-operation-4-2.png)

## Copy Files and Directories With Details

The following example shows how to copy the `~/.zshrc` file to the `~/Desktop` directory with details.

```bash
cp -rv ~/.zshrc ~/Desktop/zshrc-copy-new
ls -l ~/Desktop
```

![lab-basic-operation-4-3](assets/lab-basic-operation-4-3.png)
