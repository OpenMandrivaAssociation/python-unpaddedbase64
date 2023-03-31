%global module unpaddedbase64

%bcond_with check

Name:           python-%{module}
Version:        2.1.0
Release:        3
Summary:        Encode and decode Base64 without "=" padding

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-unpaddedbase64
Source0:        https://files.pythonhosted.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz

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

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-*.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

%if %{with check}
%check
py.test-%{python_version} -v
%endif
