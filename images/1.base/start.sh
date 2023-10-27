#!/bin/bash

#
# Trust all sudoers
#
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

#
# Create the users in /etc/users.*
#
/bin/createusers


service ssh start
jupyterhub --Spawner.default_url=/lab -f /etc/jupyterhub_config.py

