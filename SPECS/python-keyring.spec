%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global upstream_name keyring

Name:           python-keyring
Version:        0.5.1
Release:        2.ius%{?dist}
Summary:        Python library to access the system keyring service

Source0:        http://pypi.python.org/packages/source/k/keyring/%{upstream_name}-%{version}.tar.gz
License:        Python
Group:          Development/Libraries
URL:            http://pypi.python.org/pypi/keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel
Obsoletes:      %{name}-kwallet < %{version}
Obsoletes:      %{name}-gnome < %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      %{name} < %{version}

%description
The Python keyring lib provides a easy way to access the system keyring 
service from python. It can be used in any application that needs safe 
password storage.

This package only provides file-based pseudo-keyrings. To interface with 
gnome-keyring or KWallet, please install one of python-keyring-gnome or 
python-keyring-kwallet.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%doc README.txt demo
%{python_sitelib}/%{upstream_name}

# EL5 does not install EGG
%if (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{python_sitelib}/%{upstream_name}-*.egg-info
%endif

%changelog
* Mon Jun 27 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> 0.5.1-2
- Porting from Fedora Bodhi to IUS

* Mon Jan 10 2011 rtnpro <rtnpro@gmail.com> 0.5.1-1
- Remove a spurious KDE debug message when using KWallet
- Fix a bug that caused an exception if the user canceled the KWallet dialog

* Sun Nov 28 2010 rtnpro <rtnpro@gmail.com> 0.5-2
- Removed sub-packages: gnome and kwallet; removed "Requires: PyKDE4 PyQt4" 

* Mon Nov 22 2010 rtnpro <rtnpro@gmail.com> 0.5-1
- RPM for keyring-0.5

* Mon Nov 01 2010 rtnpro <rtnpro@gmail.com> 0.4-1
- Updated rpm to python-keyring version 0.4

* Sat Oct 30 2010 rtnpro <rtnpro@gmail.com> 0.2-4
- Filtered gnome_keyring.so from the provides list, removed kdelibs-devel

* Sat Oct 02 2010 rtnpro <rtnpro@gmail.com> 0.2-3
- Updated dependencies to kdelibs4-devel, some cleanup

* Tue Aug 24 2010 rtnpro <rtnpro@gmail.com> 0.2-2
- Some updates according to bugzilla reviews

* Sat Jun 26 2010 rtnpro <rtnpro@gmail.com> 0.2-1.3
- Some cleanup

* Sat Jun 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.2
- add KWallet subpackage

* Mon Jun 21 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.1
- add build dependencies
- create subpackage for gnome, disable KWallet for now
- look for files in arch-dependend site-packages

* Tue May 25 2010 rtnpro <rtnpro@gmail.com> 0.2-1
- Incorporated some changes with reference to http://vcrhonek.fedorapeople.org/python-keyring/python-keyring.spec
- Fixed some rpmlint errors

* Wed May 19 2010 rtnpro <rtnpro@gmail.com> 0.2
- Initial RPM package


