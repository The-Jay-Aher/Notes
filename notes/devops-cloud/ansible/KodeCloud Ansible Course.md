# Intro to Ansible
Quick to pickup: readable YAML, no programming
simple for everyone in IT, not just developers
Powerful at scale, handles complex deployments

#  Configurations and Basic Concept's
## Ansible's default config
location: /etc/ansible/ansible.cfg

The config file is split into sections:
1. defaults
2. inventory
3. priviledge_escalation
4. ssh_connection
5. colours

This a config full of setting, we can tune

So we can also use other files, as configs, are per requirement, we don't need to follow a single ansible script
To do that,
```shell
ANSIBLE_CONFIG=/opt/ansible-config.cfg ansible-playbook site.yml
# Here we are using a differnt config than the default one
```

Order of Precedence (for ansible configs):
1. Environment Variable (ANSIBLE_CONFIG)
2. Current Directory (./ansible.cfg)
3. Default Location (./.ansible.cfg)
4. Default Location (/etc/ansible/ansible.cfg)

Overriding Parameters
So let's say we a ansible config, and we need to override a single change, 
steps:
a. get the variable name
b. change it to `ANSIBLE_<ENVNAME>`
c. export ANSILBE_<ENVNAME>=explicit

A value set this way takes the highest priority as we are setting up an env variable

There are 3 ways you can pass on a parameter,
1. During command line,
```shell
ANSIBLE_GATHERING=explicit ansible-playbook site.yml
```
2. export the parameter
```shell
export ANSIBLE_GATHERING=explicit
```
3. Create a ansible.cfg in our current directory
```shell
cat ansible.cfg
[defaults]
gathering = explicit
```

### Inspect current ansible config
1. `ansible-config list`: Shows every option, with its default value
2. `ansible-config view`: Shows the config file which is getting used now
3. `ansible-config dump`: Shows the current config, and their source

