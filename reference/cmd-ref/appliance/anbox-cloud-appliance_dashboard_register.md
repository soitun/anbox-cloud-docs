## anbox-cloud-appliance dashboard register

Register a new user for access to the Anbox Cloud dashboard

### Synopsis

Register a new user for access to the Anbox Cloud dashboard

Access to the Anbox Cloud dashboard requires authentication. Authentication
on the dashboard is implemented via single-sign on (SSO).

Currently the only supported SSO provider is Ubuntu (https://login.ubuntu.com/).

To register a new user for access to the dashboard you need their email address
they have configured as the primary email address of their Ubuntu SSO account.
With that you can run the following command to generate a registration URL:

$ sudo anbox-cloud-appliance dashboard register foo@bar.com
Visit https://10.2.9.2/?register=xxx to finish your registration

The registration link will by default expire after one hour.

If you run the command on a non-interactive shell only the URL will
be printed as output. This allows you to do

$ url=$(sudo anbox-cloud-appliance dashboard register foo@bar.com)
$ echo "$url"
https://10.2.9.2/?register=xxx


```
anbox-cloud-appliance dashboard register <email> [flags]
```

### Examples

```
$ anbox-cloud-appliance dashboard register foo@bar.com
```

### Options

```
  -h, --help              help for register
  -e, --validity string   Time for which the registration URL will be valid (valid time units are 'm' (minutes) or 'h' (hours)) (default "1h")
```

### SEE ALSO

* [anbox-cloud-appliance dashboard](anbox-cloud-appliance_dashboard.md)	 - Manage the dashboard of the Anbox Cloud Appliance

