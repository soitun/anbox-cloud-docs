## ams.amc addon delete

Delete an existing addon

### Synopsis

Delete an existing addon.

Non-interactive deletion can be achieved with the '--yes'/'-y' flag.


```
ams.amc addon delete <name> [flags]
```

### Examples

```
$ amc addon delete foo
The following addon will be REMOVED:
  - foo
Do you want to continue? [Y/n]: Y

```

### Options

```
  -h, --help             help for delete
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -v, --version int      Version of the application to delete. If not specified, all versions are deleted.
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

### SEE ALSO

* [ams.amc addon](ams.amc_addon.md)	 - Manage addons

