%global release_name 		essex
%global _openstack_name		openstack
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

Name:             %{_openstack_name}-%{release_name}-nova
Version:          2012.1
Release:          1%{?dist}.gdc1

#
# - GoodData customization
#

%global _common_python_name	common-python
%global _prefix			/opt/%{_openstack_name}
%global _python_prefix		/opt/%{_common_python_name}
%global _sysconfdir		/etc/opt/%{_openstack_name}
%global _localstatedir		/var/opt/%{_openstack_name}
%global _infodir		%{_prefix}/share/info
%global _mandir			%{_prefix}/share/man
%global _initrddir		/etc/rc.d/init.d
%global _defaultdocdir		%{_prefix}/share/doc

%global _logdir			/var/log/%{_openstack_name}
%global _rundir			/var/run/%{_openstack_name}

# system's Python prefix is /usr change prefix to /opt/common-python
%global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()" | sed "s:/usr:%{_python_prefix}:")
%global pkgname openstack-nova

#
# ------------------------
#

Summary:          OpenStack Compute (nova)
Group:            Applications/System
License:          ASL 2.0
URL:              http://openstack.org/projects/compute/
Source0:          http://launchpad.net/nova/essex/2012.1/+download/nova-2012.1.tar.gz
Source1:          nova.conf
Source6:          nova.logrotate

Source10:         openstack-nova-api.init
Source11:         openstack-nova-cert.init
Source12:         openstack-nova-compute.init
Source13:         openstack-nova-network.init
Source14:         openstack-nova-objectstore.init
Source15:         openstack-nova-scheduler.init
Source16:         openstack-nova-volume.init
Source17:         openstack-nova-direct-api.init
Source19:         openstack-nova-vncproxy.init

Source20:         nova-sudoers
Source21:         nova-polkit.pkla
Source22:         nova-ifc-template

#
# patches_base=2012.1
#
Patch0001: 0001-fix-bug-where-nova-ignores-glance-host-in-imageref.patch
Patch0002: 0002-Stop-libvirt-test-from-deleting-instances-dir.patch
Patch0003: 0003-ensure-atomic-manipulation-of-libvirt-disk-images.patch
Patch0004: 0004-Fixed-bug-962840-added-a-test-case.patch
Patch0005: 0005-Ensure-we-don-t-access-the-net-when-building-docs.patch
Patch0006: 0006-fix-useexisting-deprecation-warnings.patch

Patch100:         openstack-nova-newdeps.patch

BuildArch:        noarch
BuildRequires:    intltool
BuildRequires:    python-setuptools
BuildRequires:    python-distutils-extra >= 2.18
BuildRequires:    python-netaddr
BuildRequires:    python-lockfile

Requires:         common-python-nova = %{version}-%{release}

Requires:         python-paste
Requires:         python-paste-deploy

Requires:         bridge-utils
# Not in EL6
#Requires:         dnsmasq-utils

Requires:         libguestfs-mount >= 1.7.17
# The fuse dependency should be added to libguestfs-mount
Requires:         fuse
Requires:         libvirt-python
Requires:         libvirt >= 0.8.7
Requires:         libxml2-python
Requires:         python-cheetah
Requires:         MySQL-python

Requires:         euca2ools
Requires:         openssl
Requires:         sudo

Requires(post):   chkconfig
Requires(preun):  initscripts
Requires(preun):  chkconfig
Requires(pre):    shadow-utils qemu-kvm

%description
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform. It gives you the
software, control panels, and APIs required to orchestrate a cloud,
including running instances, managing networks, and controlling access
through users and projects. OpenStack Compute strives to be both
hardware and hypervisor agnostic, currently supporting a variety of
standard hardware configurations and seven major hypervisors.

%package -n       common-python-nova
Summary:          Nova Python libraries
Group:            Applications/System

Requires:         vconfig
Requires:         PyXML
Requires:         curl
Requires:         m2crypto
Requires:         libvirt-python
Requires:         python-anyjson
Requires:         python-IPy
Requires:         python-qpid
Requires:         python-carrot
Requires:         python-kombu
Requires:         python-amqplib
Requires:         python-daemon
Requires:         python-eventlet
Requires:         python-greenlet
Requires:         python-gflags
Requires:         python-iso8601
Requires:         python-lockfile
Requires:         python-lxml
Requires:         python-mox
Requires:         python-redis
Requires:         python-routes
Requires:         python-tornado
Requires:         python-twisted-core
Requires:         python-twisted-web
Requires:         python-netaddr
Requires:         python-paste-deploy
Requires:         python-migrate
Requires:         python-ldap
Requires:         radvd
Requires:         iptables iptables-ipv6
Requires:         iscsi-initiator-utils
Requires:         scsi-target-utils
Requires:         lvm2
Requires:         socat
Requires:         coreutils

Requires:         python-sqlalchemy0.7
Requires:         python-webob1.0

Requires:         common-python-boto
Requires:         common-python-glance
Requires:         common-python-novaclient

%description -n   common-python-nova
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains the nova Python library.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Compute
Group:            Documentation

Requires:         %{name} = %{version}-%{release}

BuildRequires:    python-sphinx
BuildRequires:    graphviz
BuildRequires:    python-distutils-extra

BuildRequires:    python-nose
BuildRequires:    python-IPy
BuildRequires:    python-eventlet
BuildRequires:    python-gflags
BuildRequires:    python-routes
BuildRequires:    python-tornado
BuildRequires:    python-twisted-core
BuildRequires:    python-twisted-web
BuildRequires:    python-webob1.0
BuildRequires:    python-sqlalchemy0.7
BuildRequires:    python-carrot, python-mox, python-suds, m2crypto, bpython, python-memcached, python-migrate, python-iso8601

BuildRequires:    common-python-boto

%description      doc
OpenStack Compute (codename Nova) is open source software designed to
provision and manage large networks of virtual machines, creating a
redundant and scalable cloud computing platform.

This package contains documentation files for nova.
%endif

%prep
%setup -q -n nova-%{version}

%patch100 -p1
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find nova -name \*.py -exec sed -i '/\/usr\/bin\/env python/d' {} \;

%build
. /etc/opt/common-python/profile.d/common-python-boto.sh
. /etc/opt/common-python/profile.d/common-python-glance.sh
. /etc/opt/common-python/profile.d/common-python-novaclient.sh
%{__python} setup.py build

%install
. /etc/opt/common-python/profile.d/common-python-boto.sh
. /etc/opt/common-python/profile.d/common-python-glance.sh
. /etc/opt/common-python/profile.d/common-python-novaclient.sh
%{__python} setup.py install \
	--prefix=%{_prefix} \
	--install-lib=%{python_sitelib} \
	-O1 --skip-build --root %{buildroot}

# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

# TODO: possibly remove call to
# manually auto-generate to work around sphinx-build segfault
# This was not required on python-sphinx-1.0.7 at least
# but it's relatively quick at least
doc/generate_autodoc_index.sh

pushd doc

%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif

# Create dir link to avoid a sphinx-build exception
mkdir -p build/man/.doctrees/
ln -s .  build/man/.doctrees/man
SPHINX_DEBUG=1 sphinx-build -b man -c source source/man build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 build/man/*.1 %{buildroot}%{_mandir}/man1/

popd

# Give stack, instance-usage-audit and clear_rabbit_queues a reasonable prefix
mv %{buildroot}%{_bindir}/stack %{buildroot}%{_bindir}/nova-stack
mv %{buildroot}%{_bindir}/instance-usage-audit %{buildroot}%{_bindir}/nova-instance-usage-audit
mv %{buildroot}%{_bindir}/clear_rabbit_queues %{buildroot}%{_bindir}/nova-clear-rabbit-queues

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/buckets
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/images
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/instances
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/keys
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/networks
install -d -m 755 %{buildroot}%{_sharedstatedir}/nova/tmp
install -d -m 755 %{buildroot}%{_logdir}/nova

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
install -p -D -m 640 etc/nova/api-paste.ini %{buildroot}%{_sysconfdir}/nova/api-paste.ini
install -p -D -m 640 etc/nova/policy.json %{buildroot}%{_sysconfdir}/nova/policy.json

# Install initscripts for Nova services
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_initrddir}/%{name}-api
install -p -D -m 755 %{SOURCE11} %{buildroot}%{_initrddir}/%{name}-cert
install -p -D -m 755 %{SOURCE12} %{buildroot}%{_initrddir}/%{name}-compute
install -p -D -m 755 %{SOURCE13} %{buildroot}%{_initrddir}/%{name}-network
install -p -D -m 755 %{SOURCE14} %{buildroot}%{_initrddir}/%{name}-objectstore
install -p -D -m 755 %{SOURCE15} %{buildroot}%{_initrddir}/%{name}-scheduler
install -p -D -m 755 %{SOURCE16} %{buildroot}%{_initrddir}/%{name}-volume
install -p -D -m 755 %{SOURCE17} %{buildroot}%{_initrddir}/%{name}-direct-api
install -p -D -m 755 %{SOURCE19} %{buildroot}%{_initrddir}/%{name}-nova-vncproxy

# Install sudoers
install -p -D -m 440 %{SOURCE20} %{buildroot}/etc/sudoers.d/%{name}

# Install logrotate
install -p -D -m 644 %{SOURCE6} %{buildroot}/etc/logrotate.d/%{name}

# Install pid directory
install -d -m 755 %{buildroot}%{_rundir}/nova

# Install template files
install -p -D -m 644 nova/auth/novarc.template %{buildroot}%{_datarootdir}/nova/novarc.template
install -p -D -m 644 nova/cloudpipe/client.ovpn.template %{buildroot}%{_datarootdir}/nova/client.ovpn.template
install -p -D -m 644 nova/virt/libvirt.xml.template %{buildroot}%{_datarootdir}/nova/libvirt.xml.template
install -p -D -m 644 nova/virt/interfaces.template %{buildroot}%{_datarootdir}/nova/interfaces.template
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_datarootdir}/nova/interfaces.template

install -d -m 755 %{buildroot}/etc/polkit-1/localauthority/50-local.d
install -p -D -m 644 %{SOURCE21} %{buildroot}/etc/polkit-1/localauthority/50-local.d/50-%{name}.pkla

# Remove unneeded in production stuff
rm -f %{buildroot}%{_bindir}/nova-debug
rm -fr %{buildroot}%{python_sitelib}/nova/tests/
rm -fr %{buildroot}%{python_sitelib}/run_tests.*
rm -f %{buildroot}%{_bindir}/nova-combined
rm -f %{buildroot}%{_prefix}/share/doc/nova/README*

# Profile into /etc/profile.d/
mkdir -p $RPM_BUILD_ROOT/etc/profile.d/
cat > $RPM_BUILD_ROOT/etc/profile.d/%{name}.sh <<EOF
PATH=%{_bindir}:\${PATH}
PYTHONPATH=%{python_sitelib}:\${PYTHONPATH}
export PATH PYTHONPATH
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/profile.d/%{name}.sh

mkdir -p $RPM_BUILD_ROOT/etc/%{_python_prefix}/profile.d/
cat > $RPM_BUILD_ROOT/etc/%{_python_prefix}/profile.d/common-python-nova.sh <<EOF
export PYTHONPATH=%{python_sitelib}:\${PYTHONPATH}
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/%{_python_prefix}/profile.d/common-python-nova.sh

# Replace ~[^~]\+~ in configuration templates
for file in `find %{buildroot} -type f -print0 | xargs -0 grep -l '~[^~]\+~'`; do
	echo "Modify file: '$file'"
	sed -i \
		-e 's:~bindir~:%{_bindir}:g' \
		-e 's:~prefix~:%{_prefix}:g' \
		-e 's:~sysconfdir~:%{_sysconfdir}:g' \
		-e 's:~name~:%{_openstack_name}:g' \
		-e 's:~release~:%{release_name}:g' \
		-e 's:~rundir~:%{_rundir}:g' \
		-e 's:~logdir~:%{_logdir}:g' \
		-e 's:~localstatedir~:%{_localstatedir}:g' \
		$file
done

%pre
getent group nova >/dev/null || groupadd -r nova --gid 162
if ! getent passwd nova >/dev/null; then
  useradd -u 162 -r -g nova -G nova,nobody,qemu -d %{_sharedstatedir}/nova -s /sbin/nologin -c "OpenStack Nova Daemons" nova
fi
# Add nova to the fuse group (if present) to support guestmount
if getent group fuse >/dev/null; then
  usermod -a -G fuse nova
fi
exit 0

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    for svc in api cert compute network objectstore scheduler volume direct-api vncproxy; do
        /sbin/chkconfig --add %{name}-${svc} > /dev/null 2>&1 || :
    done
fi

%preun
if [ $1 -eq 0 ] ; then
    for svc in api cert compute network objectstore scheduler volume direct-api vncproxy; do
        /sbin/service %{name}-${svc} stop > /dev/null 2>&1 || :
        /sbin/chkconfig --del %{name}-${svc} > /dev/null 2>&1 || :
    done
fi

%postun
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    for svc in api cert compute network objectstore scheduler volume direct-api vncproxy; do
        /sbin/service %{name}-${svc} condrestart >/dev/null 2>&1 || :
    done
fi

%files
%doc LICENSE
%dir %{_sysconfdir}/nova
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/nova.conf
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/api-paste.ini
%config(noreplace) %attr(-, root, nova) %{_sysconfdir}/nova/policy.json
%config(noreplace) /etc/logrotate.d/%{name}
%config(noreplace) /etc/sudoers.d/%{name}
%config(noreplace) /etc/polkit-1/localauthority/50-local.d/50-%{name}.pkla

%dir %attr(0755, nova, root) %{_logdir}/nova
%dir %attr(0755, nova, root) %{_rundir}/nova

%{_bindir}/nova-*
%{_initrddir}/%{name}-*
%{_datarootdir}/nova
%{_mandir}/man1/nova*

%defattr(-, nova, nova, -)
%dir %{_sharedstatedir}/nova
%dir %{_sharedstatedir}/nova/buckets
%dir %{_sharedstatedir}/nova/images
%dir %{_sharedstatedir}/nova/instances
%dir %{_sharedstatedir}/nova/keys
%dir %{_sharedstatedir}/nova/networks
%dir %{_sharedstatedir}/nova/tmp

%dir %{_sharedstatedir}/nova/CA/
%dir %{_sharedstatedir}/nova/CA/certs
%dir %{_sharedstatedir}/nova/CA/crl
%dir %{_sharedstatedir}/nova/CA/newcerts
%dir %{_sharedstatedir}/nova/CA/projects
%dir %{_sharedstatedir}/nova/CA/reqs
%{_sharedstatedir}/nova/CA/*.sh
%{_sharedstatedir}/nova/CA/openssl.cnf.tmpl
%ghost %config(noreplace) %attr(-, root, nova) %{_sharedstatedir}/nova/CA/cacert.pem
%ghost %config(noreplace) %attr(-, root, nova) %{_sharedstatedir}/nova/CA/crl.pem
%ghost %config(noreplace) %attr(-, root, nova) %{_sharedstatedir}/nova/CA/index.txt
%ghost %config(noreplace) %attr(-, root, nova) %{_sharedstatedir}/nova/CA/openssl.cnf
%ghost %config(noreplace) %attr(-, root, nova) %{_sharedstatedir}/nova/CA/serial
%dir %attr(0750, -, -) %{_sharedstatedir}/nova/CA/private
%ghost %config(noreplace) %attr(-, root, nova)  %{_sharedstatedir}/nova/CA/private/cakey.pem
%config(noreplace) /etc/profile.d/%{name}.sh

%files -n common-python-nova
%defattr(-,root,root,-)
#%doc LICENSE
%{python_sitelib}/nova
%{python_sitelib}/nova-%{version}-*.egg-info
%config(noreplace) /etc/%{_python_prefix}/profile.d/common-python-nova.sh

%if 0%{?with_doc}
%files doc
#%doc LICENSE doc/build/html
%endif

%changelog
* Wed Apr 18 2012 Jaroslav Pulchart <jaroslav.pulchart@gooddata.com> 2012.1-1
- Initial import based on F17 openstack-nova 2012.1-1
- Change prefix to /opt/openstack
