# %bcond_without	tests	# do not perform "make test"

%define 	module	bbfreeze
Summary:	Creates stand-alone executables from python scripts
Name:		python-%{module}
Version:	1.0.2
Release:	1
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/bbfreeze/bbfreeze-%{version}.zip
# Source0-md5:	53e74d5ae352541732ef2987ad1f68a6
URL:		http://pypi.python.org/pypi/bbfreeze
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
Requires:	python-modules
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bb-freeze

%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/console.exe
%dir %{py_sitedir}/%{module}/modulegraph
%{py_sitedir}/%{module}/modulegraph/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}*.egg-info
%endif
