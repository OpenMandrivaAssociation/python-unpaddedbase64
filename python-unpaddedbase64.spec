%bcond_with check

%global modname unpaddedbase64

Name:           python-%{modname}
Version:        1.1.0
Release:        1
Summary:        Encode and decode Base64 without "=" padding

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-unpaddedbase64
Source0:        https://github.com/matrix-org/python-unpaddedbase64/archive/v%{version}/%{name}-%{version}.tar.gz

%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%if %{with check}
BuildRequires:  python3dist(pytest)
%endif

BuildArch:      noarch

%description
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes\
using "=" characters. However this conveys no benefit so many protocols\
choose to use Base64 without the "=" padding.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%if %{with check}
%check
py.test-%{python_version} -v
%endif

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{modname}-*.egg-info/
%{python_sitelib}/%{modname}.py
%{python_sitelib}/__pycache__/%{modname}.*
