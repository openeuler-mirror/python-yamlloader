%global _empty_manifest_terminate_build 0
Name:           python-yamlloader
Version:        1.0.0
Release:        1
Summary:        Ordered YAML loader and dumper for PyYAML.
License:        MIT
URL:            https://github.com/Phynix/yamlloader
Source0:        yamlloader-1.0.0.tar.gz
BuildArch:      noarch
%description
This module provides loaders and dumpers for PyYAML.

%package -n python3-yamlloader
Summary:        Ordered YAML loader and dumper for PyYAML.
Provides:       python-yamlloader
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-pyyaml
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
# General requires
Requires:       python3-pyyaml
Requires:       python3-pytest
Requires:       python3-hypothesis
%description -n python3-yamlloader
This module provides loaders and dumpers for PyYAML.

%package help
Summary:        Ordered YAML loader and dumper for PyYAML.
Provides:       python3-yamlloader-doc
%description help
This module provides loaders and dumpers for PyYAML.

%prep
%autosetup -n yamlloader-1.0.0 -S git

%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} -m pytest



%files -n python3-yamlloader -f filelist.lst
%dir %{python3_sitelib}/*


%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Jul 19 2021 OpenStack_SIG <openstack@openeuler.org> - 1.0.0-1
- Package Spec generate
