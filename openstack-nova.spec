%global product_name		nova
%global release_name 		folsom
%global _openstack_name		openstack
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

%global pkgname %{_openstack_name}-%{product_name}

Name:             openstack-nova
Version:          2012.2.4
Release:          33%{?dist}.gdc
Summary:          OpenStack Compute (nova)

Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          http://launchpad.net/nova/folsom/%{version}/+download/%{_openstack_name}-%{product_name}-%{version}.tar.gz

Source1:          nova.conf
Source6:          nova.logrotate

Source10:         openstack-nova-api.init
Source100:        openstack-nova-api.upstart
Source11:         openstack-nova-cert.init
Source110:        openstack-nova-cert.upstart
Source12:         openstack-nova-compute.init
Source120:        openstack-nova-compute.upstart
Source13:         openstack-nova-network.init
Source130:        openstack-nova-network.upstart
Source131:        openstack-nova-networkvlan.init
Source132:        nova-networkvlan
Source14:         openstack-nova-objectstore.init
Source140:        openstack-nova-objectstore.upstart
Source15:         openstack-nova-scheduler.init
Source150:        openstack-nova-scheduler.upstart
Source16:         openstack-nova-volume.init
Source160:        openstack-nova-volume.upstart
Source18:         openstack-nova-xvpvncproxy.init
Source180:        openstack-nova-xvpvncproxy.upstart
Source19:         openstack-nova-console.init
Source190:        openstack-nova-console.upstart
Source24:         openstack-nova-consoleauth.init
Source240:        openstack-nova-consoleauth.upstart
Source25:         openstack-nova-metadata-api.init
Source250:        openstack-nova-metadata-api.upstart

Source20:         nova-sudoers
Source21:         nova-polkit.pkla
Source22:         nova-ifc-template

#
# patches_base=2012.2
#

Patch0001: 0001-Ensure-we-don-t-access-the-net-when-building-docs.patch
Patch0002: 0002-update-kwargs-with-args-in-wrap_instance_fault.patch

# backported patches for PCI-3066
Patch0003: 0003-Fixes-a-race-condition-on-updating-security-group-ru.patch
Patch0004: 0004-Update-nova-compute-api-to-handle-instance-as-dict.patch

# This is EPEL specific and not upstream
Patch0500: openstack-nova-newdeps.patch

# GDC patchset
# https://jira.gooddata.com/jira/browse/GD-25782
Patch1002: 1002-Create-a-volume-from-a-snapshot-from-different-avail.patch 
# https://jira.gooddata.com/jira/browse/GD-23657
Patch1004: 1004-force-lvm-snapshot-delete-when-volue-delete.patch
# https://jira.gooddata.com/jira/browse/PCI-141
Patch1005: 1005-use-local-LVM-volume-instead-of-iSCSI-device-on-same.patch
# https://jira.gooddata.com/jira/browse/PCI-156 (PCI-110)
Patch1006: 1006-Setting-promisc-on-VLAN-bridge.patch
# https://bugs.launchpad.net/nova/+bug/1061628
Patch1008: 1008-Workaround-for-bug-1061628.patch
# https://bugs.launchpad.net/nova/+bug/1016633
# not final fix, please update it after the tickets is closed
Patch1009: 1009-Do-not-run-RPC-call-for-simple-db-look-at-fixed_ip-s_v1.patch
# AMI based instance cannot be resized
Patch1012: 1012-Get-size-of-root-block-device-from-mapping-table.patch

# Elastic IPs
Patch1017: 1017-elastic_ip_pool_for_public_ips.patch

# https://bugs.launchpad.net/cinder/+bug/1095633, Netapp Folsom FIX
Patch1018: 1018-Netapp_1095633-Netapp-driver-repeat-DFM-lun-refresh.patch
# https://bugs.launchpad.net/cinder/+bug/1091480, Netapp Folsom FIX
Patch1019: 1019-Netapp_1091480-synchronize-dataset-edit.patch
# https://bugs.launchpad.net/cinder/+bug/1099414, Netapp Folsom FIX
Patch1020: 1020-Netapp_1099414_added-qtree-removal.patch
# https://bugs.launchpad.net/cinder/+bug/1098581, Netapp Folsom FEATURE
Patch1021: 1021-Netapp_1098581_create-volume-from-snapshot-of-smaller-size.patch
# PCI-308, Netapp Folsom driver backport to (GDC) Essex
Patch1024: 1024-Netapp_backport-for-GDC-version-of-driver-API.patch
# https://bugs.launchpad.net/nova/+bug/1112483
Patch1025: 1025-1112483-device-size-mismatch-when-LUN-is-reus.patch
# https://jira.gooddata.com/browse/PCI-437
Patch1026: 1026-Netapp_PCI-437-don-t-resize-parent-volume-for-new-LU.patch

Patch1027: 1027-Calculate-with-REAL-free-RAM-in-least_cost.py.patch

# Folsom's issue with naming volumes
Patch1028: 1028-ec2api-blockdevicemapping.patch

Patch1029: 1029-graceful-shutdown-for-poweroff-and-reboot.patch

# E->F migration: fix two tgt entries for same volume
Patch1030: 1030-FIX-attach-premigration-ISCSI.patch
# E->F migration: make existing Essex Netapp volume/snapshots available in Folsom
Patch1031: 1031-Netapp_existing-Essex-volume-snapshots-availab.patch
Patch1032: 1032-fix-describe-instance-attribute-api-call.patch
Patch1033: 1033-simple-sleep-for-bdm.patch
Patch1034: 1034-pae-for-kvm-and-i686.patch
Patch1035: 1035-add_default_flagfile_into_utils.patch
# workaround for SNAT output interface issue
Patch1036: 1036-FIX-switch-back-to-SNAT-rule-to-any-target-if.patch
# PCI-640 - trim firewall log for verbose level
Patch1037: 1037-FIX-PCI-640-trim-firewall-log-for-verbose-level.patch
Patch1038: 1038-FIX-remove-essex-volume.patch
Patch1039: 1039-Enforce-mkfs-at-lvm-ephemerals.patch
# PCI-1069 - add EC2 API authorization layer
Patch1040: 1040-ec2-authorization.patch
# PCI-1466
Patch1041: 1041-hugepages-memory-backend-for-libvirt.patch
# PCI-1523
Patch1042: 1042-Report-free-LVM-volume-group-space.patch
Patch1043: 1043-Report-free-HugeMemory-space-instead-of-free-memory.patch
Patch1044: 1044-LVM-Thin-volumes-support.patch
Patch1045: 1045-FIX-solves-error-in-volume-deleting.patch
Patch1046: 1046-LVM-Thin-nova-volumes-support.patch
Patch1047: 1047-FIX-deleting-volumes-in-error-state.patch
# PCI-1958
Patch1048: 1048-BUGFIX-PCI-1958-zero-out-only-first-1G-during-delete.patch
# PCI-2083
Patch1049: 1049-FEATURE-PCI-2083-Allow-same-net-traffic.patch
Patch1050: 1050-FEATURE-PCI-1711-thin-LVM-support-for-OpenStack-sche.patch
Patch1051: 1051-FEATURE-PCI-2046-RAM-CPU-overcommit-per-compute-node.patch
Patch1052: 1052-BUGFIX-PCI-2025-delete-domain-after-unsuccessful-ins.patch
Patch1053: 1053-FEATURE-PCI-2238-return-host-in-descr.-instances-and.patch
Patch1054: 1054-FEATURE-PCI-2479-EC2-DescribeInstances-API-show-terminated-instances.patch

# PCI-2069, PCI-1286
Patch1055: 1055-CONFIG-PCI-2069-Remove-dnsmasq-strict-order-option.patch
# PCI-3147
Patch1056: 1056-BUGFIX-PCI-3147-create-iptables-for-stopped-instance.patch
# PCI-3186
Patch1057: 1057-FEATURE-PCI-3186-Show-auto-assigned-IP-s-in-floating.patch
# PCI-3231
Patch1058: 1058-BUGFIX-PCI-3231-speed-up-get_floating_ips-nova-API-c.patch

# PCI-3066 backporting fix for 1003 patch
Patch1059: 1059-PCI-3066-backporting-secgroup-patch-to-Folsom.patch

# PCI-3411 fix floating IPs API call
Patch1060: 1060-BUGFIX-PCI-3411-fix-floating-IPs-API-call-to-get-una.patch
Patch1061: 1061-FEATURE-PCI-3639-Allow-change-root-volume-size-via-n.patch

# PCI-3773
Patch1062: 1062-FEATURE-PCI-3773-aio-native-and-virtio-blk-dataplane.patch

# PCI-3781
Patch1063: 1063-BUGFIX-PCI-3781-nova-compute-service-is-running-vgs.patch

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-sphinx10
BuildRequires:    python-setuptools
BuildRequires:    python-netaddr
BuildRequires:    openstack-utils
# These are required to build due to the requirements check added
BuildRequires:    python-paste-deploy >= 1.5
BuildRequires:    python-routes1.12
BuildRequires:    python-sqlalchemy0.7
BuildRequires:    python-webob1.0

Requires:         openstack-nova-compute = %{version}-%{release}
Requires:         openstack-nova-cert = %{version}-%{release}
Requires:         openstack-nova-scheduler = %{version}-%{release}
Requires:         openstack-nova-volume = %{version}-%{release}
Requires:         openstack-nova-api = %{version}-%{release}
Requires:         openstack-nova-network = %{version}-%{release}
Requires:         openstack-nova-objectstore = %{version}-%{release}
Requires:         openstack-nova-console = %{version}-%{release}



%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package common
Summary:          Components common to all OpenStack Nova services
Group:            Applications/System

Requires:         openstack-utils
Requires:         python-nova = %{version}-%{release}
Requires:         python-keystone

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(pre):    shadow-utils

Requires:         python-setuptools

%description common
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains scripts, config and dependencies shared
between all the OpenStack nova services.


%package compute
Summary:          OpenStack Nova Virtual Machine control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         curl
Requires:         iscsi-initiator-utils
Requires:         iptables iptables-ipv6
Requires:         vconfig
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl
Requires:         libguestfs-mount >= 1.7.17
# The fuse dependency should be added to libguestfs-mount
Requires:         fuse
Requires:         libvirt >= 0.9.6
Requires:         libvirt-python
Requires:         openssh-clients
Requires:         rsync
Requires(pre):    qemu-kvm

%description compute
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling Virtual Machines.


%package network
Summary:          OpenStack Nova Network control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         vconfig
Requires:         radvd
Requires:         bridge-utils
Requires:         dnsmasq
Requires:         dnsmasq-utils
# tunctl is needed where `ip tuntap` is not available
Requires:         tunctl

%description network
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling networking.


%package volume
Summary:          OpenStack Nova storage volume control service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}
Requires:         lvm2
Requires:         scsi-target-utils

%description volume
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for controlling storage volumes.


%package scheduler
Summary:          OpenStack Nova VM distribution service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description scheduler
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the service for scheduling where
to run Virtual Machines in the cloud.


%package cert
Summary:          OpenStack Nova certificate management service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description cert
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service for managing certificates.


%package api
Summary:          OpenStack Nova API services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description api
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing programmatic access.


%package objectstore
Summary:          OpenStack Nova simple object store service
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description objectstore
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova service providing a simple object store.


%package console
Summary:          OpenStack Nova console access services
Group:            Applications/System

Requires:         openstack-nova-common = %{version}-%{release}

%description console
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

This package contains the Nova services providing
console access services to Virtual Machines.


%package -n       python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         openssl
# Require openssh for ssh-keygen
Requires:         openssh
Requires:         sudo

Requires:         MySQL-python

Requires:         python-paramiko

Requires:         python-qpid
Requires:         python-kombu
Requires:         python-amqplib

Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-iso8601
Requires:         python-netaddr
Requires:         python-lxml
Requires:         python-anyjson
Requires:         python-boto
Requires:         python-cheetah
Requires:         python-ldap

Requires:         python-memcached

Requires:         python-sqlalchemy0.7
Requires:         python-migrate

Requires:         python-paste-deploy >= 1.5
Requires:         python-routes1.12
Requires:         python-webob1.0

Requires:         python-glanceclient >= 1:0
Requires:         python-quantumclient >= 1:2
Requires:         python-novaclient

%description -n   python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    graphviz

# Required to build module documents
BuildRequires:    python-boto
BuildRequires:    python-eventlet
# while not strictly required, quiets the build down when building docs.
BuildRequires:    python-migrate, python-iso8601

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1

# Apply EPEL patch
%patch0500 -p1

# GDC Patches
%patch1002 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1008 -p1
%patch1009 -p1
%patch1012
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1026 -p1
%patch1024 -p1
%patch1025 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
# quick patch for Essex volumes removal
%patch1038 -p1
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1
%patch1045 -p1
%patch1046 -p1
%patch1047 -p1
%patch1048 -p1
%patch1049 -p1
%patch1050 -p1
%patch1051 -p1
%patch1052 -p1
%patch1053 -p1
%patch1054 -p1
%patch1055 -p1
%patch1056 -p1
%patch1057 -p1
%patch1058 -p1
%patch1059 -p1
%patch1060 -p1
%patch1061 -p1
%patch1062 -p1
%patch1063 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setuptools_git/d' setup.py

sed -i s/LOCALBRANCH:LOCALREVISION/%{release}/ nova/version.py

%build
%{__python} setup.py build

# Move authtoken configuration out of paste.ini
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_tenant_name
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_user
openstack-config --del etc/nova/api-paste.ini filter:authtoken admin_password
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_host
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_port
openstack-config --del etc/nova/api-paste.ini filter:authtoken auth_protocol
openstack-config --del etc/nova/api-paste.ini filter:authtoken signing_dir

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-1.0-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-1.0-build -b man -c source source/man build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/nova

# Setup ghost CA cert
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 755 nova/CA/*.sh %{buildroot}%{_sharedstatedir}/nova/CA
install -p -m 644 nova/CA/openssl.cnf.tmpl %{buildroot}%{_sharedstatedir}/nova/CA
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/CA/{certs,crl,newcerts,projects,reqs}
touch %{buildroot}%{_sharedstatedir}/nova/CA/{cacert.pem,crl.pem,index.txt,openssl.cnf,serial}
install -d -m 750 %{buildroot}%{_sharedstatedir}/nova/CA/private
touch %{buildroot}%{_sharedstatedir}/nova/CA/private/cakey.pem

# Install config files
install -d -m 755 %{buildroot}%{_sysconfdir}/nova
install -p -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/nova/nova.conf
install -d -m 755 %{buildroot}%{_sysconfdir}/nova/volumes
install -p -D -m 640 etc/nova/rootwrap.conf %{buildroot}%{_sysconfdir}/nova/rootwrap.conf
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/openstack-nova-api
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/openstack-nova-cert
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/openstack-nova-compute
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/openstack-nova-network
install -p -D -m 755 %{SOURCE131} %{buildroot}%{_initrddir}/openstack-nova-networkvlan
# install nova-networkvlan too
install -p -D -m 755 %{SOURCE132} %{buildroot}%{_bindir}/nova-networkvlan
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_initrddir}/openstack-nova-objectstore
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_initrddir}/openstack-nova-scheduler
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_initrddir}/openstack-nova-volume
install -p -D -m 755 %{SOURCE18} %{buildroot}%{_initrddir}/openstack-nova-xvpvncproxy
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_initrddir}/openstack-nova-console
install -p -D -m 755 %{SOURCE24} %{buildroot}%{_initrddir}/openstack-nova-consoleauth
install -p -D -m 755 %{SOURCE25} %{buildroot}%{_initrddir}/openstack-nova-metadata-api

# Install sudoers
install -p -D -m 440 %{SOURCE20} %{buildroot}%{_sysconfdir}/sudoers.d/nova

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-nova

# Install pid directory
install -d -m 755 %{buildroot}%{_localstatedir}/run/nova

# Install template files
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

# Install upstart jobs examples
install -p -m 644 %{SOURCE100} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE110} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE120} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE130} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE140} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE150} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE160} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE180} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE190} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE240} %{buildroot}%{_datadir}/nova/
install -p -m 644 %{SOURCE250} %{buildroot}%{_datadir}/nova/

# Install rootwrap files in /usr/share/nova/rootwrap
mkdir -p %{buildroot}%{_datarootdir}/nova/rootwrap/
install -p -D -m 644 etc/nova/rootwrap.d/* %{buildroot}%{_datarootdir}/nova/rootwrap/

install -d -m 755 %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelib}/nova/tests/
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}/usr/share/doc/nova/README*


# We currently use the equivalent file from the novnc package
rm -f %{buildroot}%{_bindir}/nova-novncproxy

%pre common
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
exit 0

%pre compute
usermod -a -G qemu nova
# Add nova to the fuse group (if present) to support guestmount
if getent group fuse >/dev/null; then
  usermod -a -G fuse nova
fi
exit 0

%post compute
/sbin/chkconfig --add openstack-nova-compute
%post network
/sbin/chkconfig --add openstack-nova-network
/sbin/chkconfig --add openstack-nova-networkvlan
%post volume
/sbin/chkconfig --add openstack-nova-volume
%post scheduler
/sbin/chkconfig --add openstack-nova-scheduler
%post cert
/sbin/chkconfig --add openstack-nova-cert
%post api
for svc in api metadata-api; do
    /sbin/chkconfig --add openstack-nova-$svc
done
%post objectstore
/sbin/chkconfig --add openstack-nova-objectstore
%post console
for svc in console consoleauth xvpvncproxy; do
    /sbin/chkconfig --add openstack-nova-$svc
done

%preun compute
if [ $1 -eq 0 ] ; then
    for svc in compute; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun network
if [ $1 -eq 0 ] ; then
    for svc in network networkvlan; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun volume
if [ $1 -eq 0 ] ; then
    for svc in volume; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun scheduler
if [ $1 -eq 0 ] ; then
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun cert
if [ $1 -eq 0 ] ; then
    for svc in cert; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun api
if [ $1 -eq 0 ] ; then
    for svc in api metadata-api; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun objectstore
if [ $1 -eq 0 ] ; then
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi
%preun console
if [ $1 -eq 0 ] ; then
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} stop >/dev/null 2>&1
        /sbin/chkconfig --del openstack-nova-${svc}
    done
fi

%postun compute
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in compute; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun network
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in network networkvlan; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun volume
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in volume; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun scheduler
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in scheduler; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun cert
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in cert; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun api
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api metadata-api; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun objectstore
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in objectstore; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi
%postun console
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in console consoleauth xvpvncproxy; do
        /sbin/service openstack-nova-${svc} condrestart > /dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%{_bindir}/nova-all

%files common
%doc LICENSE
%dir %{_sysconfdir}/nova
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/rootwrap.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-nova
%config(noreplace) %{_sysconfdir}/sudoers.d/nova
%config(noreplace) %{_sysconfdir}/polkit-1/localauthority/50-local.d/50-nova.pkla

%dir %attr(0755, nova, root) %{_localstatedir}/log/nova
%dir %attr(0755, nova, root) %{_localstatedir}/run/nova

%{_bindir}/nova-clear-rabbit-queues
# TODO. zmq-receiver may need its own service?
%{_bindir}/nova-rpc-zmq-receiver
%{_bindir}/nova-manage
%{_bindir}/nova-rootwrap

%exclude %{_datarootdir}/nova/*.upstart
%{_datarootdir}/nova
%{_mandir}/man1/nova*.1.gz

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%files compute
%{_bindir}/nova-compute
%{_initrddir}/openstack-nova-compute
%{_datarootdir}/nova/openstack-nova-compute.upstart
%{_datarootdir}/nova/rootwrap/compute.filters

%files network
%{_bindir}/nova-network
%{_bindir}/nova-networkvlan
%{_bindir}/nova-dhcpbridge
%{_initrddir}/openstack-nova-network
%{_initrddir}/openstack-nova-networkvlan
%{_datarootdir}/nova/openstack-nova-network.upstart
%{_datarootdir}/nova/rootwrap/network.filters

%files volume
%{_bindir}/nova-volume
%{_initrddir}/openstack-nova-volume
%{_bindir}/nova-volume-usage-audit
%{_datarootdir}/nova/openstack-nova-volume.upstart
%{_datarootdir}/nova/rootwrap/volume.filters
%dir %attr(0755, nova, root) %{_sysconfdir}/nova/volumes

%files scheduler
%{_bindir}/nova-scheduler
%{_initrddir}/openstack-nova-scheduler
%{_datarootdir}/nova/openstack-nova-scheduler.upstart

%files cert
%{_bindir}/nova-cert
%{_initrddir}/openstack-nova-cert
%{_datarootdir}/nova/openstack-nova-cert.upstart
%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nova/CA/private/cakey.pem

%files api
%{_bindir}/nova-api*
%{_initrddir}/openstack-nova-*api
%{_datarootdir}/nova/openstack-nova-*api.upstart
%{_datarootdir}/nova/rootwrap/api-metadata.filters

%files objectstore
%{_bindir}/nova-objectstore
%{_initrddir}/openstack-nova-objectstore
%{_datarootdir}/nova/openstack-nova-objectstore.upstart

%files console
%{_bindir}/nova-console*
%{_bindir}/nova-xvpvncproxy
%{_initrddir}/openstack-nova-console*
%{_datarootdir}/nova/openstack-nova-console*.upstart
%{_initrddir}/openstack-nova-xvpvncproxy
%{_datarootdir}/nova/openstack-nova-xvpvncproxy.upstart

%files -n python-nova
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}-*.egg-info

%if 0%{?with_doc}
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Tue Sep 9 2014 Zdenek Pizl <zdenek.pizl@gooddata.com> -  2013.2.4-33.gdc
- BUGFIX: remove multiple call to external command 'vgs'

* Mon May 5 2014 Yury Tsarev <yury.tsarev@gooddata.com> -  2013.2.4-32.gdc
- FEATURE: PCI-3773 aio=native and virtio-blk-dataplane enablement

* Wed Mar 26 2014 Martin Surovcak <martin.surovcak@gooddata.com> -  2013.2.4-31.gdc
- FEATURE: PCI-3639 Allow change root volume size via nova api

* Fri Mar 7 2014 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> -  2013.2.4-30.gdc
- BUGFIX: PCI-3536 EC2 user_data api now returs empty string when None userdata

* Tue Feb 18 2014 Tomas Dubec <tomas.dubec@gooddata.com> - 2013.2.4-29.gdc
- BUGFIX: PCI-3411 fix floating IPs API call to get unassigned addresses

* Wed Feb 12 2014 Branislav Zarnovican <branislav.zarnovican@gooddata.com> -  2013.2.4-28.gdc
- Fix of BUGFIX: PCI-3066 - backported two patches for secgroup issues

* Tue Feb 11 2014 Branislav Zarnovican <branislav.zarnovican@gooddata.com> -  2013.2.4-27.gdc
- BUGFIX: PCI-3066 - backported two patches for secgroup issues

* Tue Feb 4 2014 Tomas Dubec <tomas.dubec@gooddata.com> - 2013.2.4-26.gdc
- BUGFIX: PCI-3231 speed up get_floating_ips nova API call via updating SQL and thus making hundreds of RPCs and SQLs unnecessary

* Tue Jan 21 2014 Martin Surovcak <martin.surovcak@gooddata.com> - 2013.2.4-25.gdc
- FEATURE: PCI-3186 Show auto-assigned IP's in floating-ip-list

* Wed Jan 15 2014 Tomas Dubec <tomas.dubec@gooddata.com> - 2013.2.4-24.gdc
- PCI-3147: create iptables for stopped instances after host boot

* Mon Nov 25 2013 Martin Surovcak <martin.surovcak@gooddata.com> - 2013.2.4-23.gdc
- PCI-2069: Remove dnsmasq strict-order option

* Thu Nov 21 2013 Tomas Dubec <tomas.dubec@gooddata.com> - 2012.2.4-22.gdc
- PCI-2758 - fix init scripts so that openstack services are terminated correctly during shutdown

* Tue Oct 23 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-21.gdc
- PCI-2479 - Extend EC2 DescribeInstances API to show terminated instances (EC2 API)

* Tue Oct 01 2013 Tomas Dubec <tomas.dubec@gooddata.com> - 2012.2.4-20.gdc
- PCI-2238 - allow error volume deletion, return host for instances (EC2 API)

* Thu Sep 26 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-19.gdc
- updated existing 1020 patch, fix for PCI-2092

* Wed Sep 18 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-18.gdc
- PCI-2079 snapshot have to use provider_location instead of hostname

* Tue Sep 03 2013 Tomas Dubec <tomas.dubec@gooddata.com> - 2012.2.4-17.gdc
- PCI-2046 per compute node RAM/CPU overcommit
- PCI-1711 thin LVM support for OpenStack scheduler disk filter
- PCI-2025 delete domain after unsuccessful deployment

* Tue Sep 03 2013 Martin Surovcak <martin.surovcak@gooddatam.com> - 2012.2.4-17.gdc
- PCI-2083 Do not generate per-instance rules when allow_same_net_traffic=True

* Thu Aug 29 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com>
- backported fix for #1067254, masking real stacktraces in wrap_instance_fault

* Mon Aug 19 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-16.gdc
- PCI-1958 - dd with zero only the first 1G of LVM volume

* Thu Aug 15 2013 Radek Smidl <radek.smidl@gooddata.com> - 2012.2.4-15.gdc
- PCI-1802 - volumes in error_deleting state when created from inaccessible NetApp snapshot

* Wed Aug 07 2013 Tomas Dubec <tomas.dubec@gooddata.com> - 2012.2.4-14.gdc
- fix typo in hugepage patch 1041

* Fri Aug 02 2013 Radek Smidl <radek.smidl@gooddata.com> - 2012.2.4-13.gdc
- PCI-1576 solves error in volume deleting when creation was failed
- PCI-1718 LVM Thin volumes support added to nova-volume

* Wed Jul 22 2013 Radek Smidl <radek.smidl@gooddata.com> - 2012.2.4-12.gdc
- Update of PCI-1526 LVM Thin volumes support

* Tue Jul 21 2013 Radek Smidl <radek.smidl@gooddata.com> - 2012.2.4-11.gdc
- PCI-1526 LVM Thin volumes support

* Mon Jul 15 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-10.gdc
- Remove unused patches from spec file
- Integrate PAE for i686 patch

* Thu Jul 11 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-9.gdc
- PCI-1466 optional HugePages memory backend
- PCI-1523 report free HugeMemory space instead of OS free memory when HugePages are enabled
- PCI-1523 report free LVM volume group space when LVM AMI backend is used (https://bugs.launchpad.net/nova/+bug/1198831)

* Thu Jul 11 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-9.gdc
- PCI-1466 optional HugePages memory backend
- PCI-1523 report free HugeMemory space instead of OS free memory when HugePages are enabled
- PCI-1523 report free LVM volume group space when LVM AMI backend is used (https://bugs.launchpad.net/nova/+bug/1198831)

* Tue Jun 25 2013 Tomas Dubec <tomas.dubec@gooddata.com> - 2012.2.4-8.gdc
- add EC2 API authorization layer

* Mon Jun 24 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-7.gdc
- Ephemeral volume at LVM have to be formated like as on qcow2 ephemeral
- ext4 filesystem is a default
- make sure that enforced filesystem is used (default_ephemeral_format)
- add missing dnsmasq-utils package into reuqires

* Fri May 31 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-6.gdc10
- fix 1012-Get-size-of-root-block-device-from-mapping-table.patch

* Wed May 22 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-6.gdc7
- added patch to trim firewall log for verbose level
- fixed tabs/spaces in 1009 patch

* Sat May 18 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-6.gdc5
- added workaround for SNAT output interface issue (patch 1036)

* Fri May 17 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-6.gdc4
- added 1035-add_default_flagfile_into_utils.patch

* Fri May 17 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-6.gdc3
- added 1033-simple-sleep-for-bdm.patch
- included 1034-pae-for-kvm-and-i686.patch but not used for now because of missing testing

* Thu May 16 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-6.gdc2
- added missing 1032-fix-describe-instance-attribute-api-call.patch

* Thu May 16 2013 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> - 2012.2.4-6.gdc1
- added missing 1027-Calculate-with-REAL-free-RAM-in-least_cost.py.patch

* Fri May 10 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-5.gdc6
- removed Netapp's copy-instead-of-clone patch

* Thu May 09 2013 Zdenek Pizl <zdenek.pizl@gooddata.com> - 2012.2.4-5.gdc5
- removed BZA's patch1030 and use another dirty patch instead of it

* Tue May 07 2013 Branislav Zarnovican <branislav.zarnovican@gooddata.com> - 2012.2.4-5.gdc4
- added migration patch for LV volumes
- added migration patch for Netapp volumes

* Tue Mar 26 2013 Zdenek Pizl <zdenek.pizl@gooddata.com> 2012.2.4-1.gdc1
 - Upgrade to Folsom release 2012.2.4 tarball
 - build for default  EL6 directory layout
 - standard naming for packages


