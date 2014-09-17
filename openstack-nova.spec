%global product_name		nova
%global release_name 		folsom
%global _openstack_name		openstack
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

%global pkgname %{_openstack_name}-%{product_name}
%global release_number 36

Name:             openstack-nova
Version:          2012.2.4
Release:          %{release_number}%{?dist}.gdc
Summary:          OpenStack Compute (nova)

Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          openstack-nova.tar.gz

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
%setup -q -n %{_openstack_name}-%{product_name}-%{release_number}


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
* Fri Oct 10 2014 Yury Tsarev <yury.tsarev@gooddata.com> -  2013.2.4-36.gdc
- CONFIG: PCI-4155 Switch to github based builds

* Thu Sep 12 2014 Zdenek Pizl <zdenek.pizl@gooddata.com> -  2013.2.4-35.gdc
- BUGFIX: PCI-3781 correct application of patches related to PCI-3781

* Wed Sep 11 2014 Zdenek Pizl <zdenek.pizl@gooddata.com> -  2013.2.4-34.gdc
- Added test cases for new functionality
- BUGFIX: PCI-3781 missing pool_path variable regression corrected
- Added test cases for new functionality

* Tue Sep 9 2014 Zdenek Pizl <zdenek.pizl@gooddata.com> -  2013.2.4-33.gdc
- BUGFIX: PCI-3781 remove multiple call to external command 'vgs'

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


