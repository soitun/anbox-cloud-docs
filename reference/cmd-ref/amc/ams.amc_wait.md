## ams.amc wait

Wait for an instance to reach a specific condition

### Synopsis

Wait for an instance to reach a specific condition.

You must specify one or multiple conditions with the '--condition'|'-c' flag.

A condition is of the form 'key=value', where 'key' is a supported attribute
and 'value' defines what to wait on.

Valid attributes:
 - For applications: published, status
 - For application versions: published, status
 - For instances: status

Use '--selector version=<version number>' to wait on an application version.

```
ams.amc wait (<app_id> | <instance_id>) [flags]
```

### Examples

```
Wait for the application to be either ready or in an error state:

$ amc wait bkhk491hpuo2c84rai9g -c status=ready -c status=error

```

### Options

```
  -c, --condition stringArray   Condition of the application or instance to wait for
  -h, --help                    help for wait
  -s, --selector string         Selector to filter the application or instance
  -t, --timeout string          Maximum time to wait for the condition (default "5m")
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client

