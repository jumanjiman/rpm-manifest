Name:		rpm-manifest
Version:	0.1
Release:	1%{?dist}
Summary:	creates a hash of all RPMs on a system

Group:		System Environment/Base
License:	GPLv3
URL:		http://github.com/jumanjiman/rpm-manifest
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

Requires:   rpm
Requires:   coreutils
Requires:	crontabs

%description
Generates a single hash value based on the 
name, epoch, version, and release of all every
RPM installed on a system. 

When used in conjunction with ITIL practices,
the manifest can:

* detect unintended change in packages
* validate intended change in packages

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

