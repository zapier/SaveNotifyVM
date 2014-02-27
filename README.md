This Sublime Text 3 plugin will post file change events against a Vagrant VM so that a script inside the VM can listen for file change events and react accordingly (touch the file, trigger watch scripts, etc.)

This is necessary because most OS' do a terrible job at quickly and reliably sending file change events across VM shared-filesystem bridges like NFS.

Note: this repo does not include a script for actually doing anything with the request that is posted (you are responsible for handling it).


Installation
============
The easiest way to install this plugin is via [Sublime Package Control](http://wbond.net/sublime_packages/package_control) by adding an extra repository.

An other way is by cloning this repository into the package folder of Sublime


Usage
=====
After installing, open up your `Preferences > Package Settings > Save Notify VM > User settings` and paste this config and update is appropriately.

```
{
  "path_to_repo": "/Users/mikeknoop/Code/zapier",
  "vm_ip": "192.168.50.100",
  "vm_port": "3600"
}
```
