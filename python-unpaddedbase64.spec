%bcond_without check

%global modname unpaddedbase64

Name:           python-%{modname}
Version:        1.1.0
Release:        14%{?dist}
Summary:        Encode and decode Base64 without "=" padding

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-unpaddedbase64
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes\
using "=" characters. However this conveys no benefit so many protocols\
choose to use Base64 without the "=" padding.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with check}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
py.test-%{python3_version} -v
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*
