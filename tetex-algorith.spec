%define	_short_name 	algorith
Summary:	Set of LaTeX macros for ... physicists
Summary(pl):	Zestaw makr LaTeXa dla ... fizyków
Name:		tetex-algorith
Version:	20050316
Release:	1
License:	LGPL 2.1+
Group:		Applications/Publishing/TeX
# taken from: ftp://ftp.dante.de/pub/tex/macros/latex/contrib/algorithms.tgz
Source0:	algorithms.tgz
# Source0-md5:	b8d41cfe88164385c294329a63dff7cc
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for ... physicists.

%description -l pl
Zestaw makr LaTeXa dla ... fizyków.

%prep
%setup -q -n algorithms

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{_short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name}

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.tex
%{_datadir}/texmf/tex/latex/%{_short_name}/*
