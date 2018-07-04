# %bcond_without	tests	# do not perform "make test"

%define 	module	bbfreeze
Summary:	Creates stand-alone executables from python scripts
Name:		python-%{module}
Version:	1.1.3
Release:	1
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pypi.debian.net/bbfreeze/bbfreeze-%{version}.zip
# Source0-md5:	5c7bf32800376f1a1305176ad396feba
URL:		http://pypi.python.org/pypi/bbfreeze
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbfreeze creates stand-alone executables from python scripts. It's
similar in purpose to the well known py2exe for windows, py2app for OS
X, PyInstaller and cx_Freeze (in fact ancient versions were based on
cx_Freeze. And it uses the modulegraph package, which is also used by
py2app).

%prep
%setup -q -n bbfreeze-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bb-freeze

%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/modulegraph
%{py_sitescriptdir}/%{module}/modulegraph/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}*.egg-info
%endif
