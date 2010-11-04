Name:		rpm-manifest
Version:	0.1
Release:	2%{?dist}
Summary:	creates a hash of all RPMs on a system

Group:		System Environment/Base
License:	GPLv3
URL:		http://github.com/jumanjiman/rpm-manifest
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	rpm
Requires:	coreutils
Requires:	crontabs

%description
Generates a single hash value based on the 
name, epoch, version, and release of all every
RPM installed on a system. 

When used in conjunction with ITIL practices,
and with respect to the set of RPMs installed,
the manifest can:

* detect unintended changes
* validate intended changes

%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{name}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -pm 755 src/rpm-manifest %{buildroot}%{_sysconfdir}/cron.daily


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPLv3
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/cron.daily/rpm-manifest



%changelog
* Thu Nov 04 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-2
- cleanup spec (jumanjiman@gmail.com)

* Thu Nov 04 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito


