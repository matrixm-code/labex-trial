# Note

Hi! I'm just an example asset. Don't mind me.

I'm only here because the index.json specified copy over
the contents of the challenge's source /assets/ folder into
the environment's /root/ folder, like so:

```json
"assets": {
    "client": [
        { "file": "*", "target": "~/" }
    ]
}
```

The ~/ just refers to the environment user's home folder.
That user is named "root". Once the environment loads, try
confirming that this example got copied over with:

```bash
$ pwd
/root

$ ls
example-asset.md
```
