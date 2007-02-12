%define	_short_name 	algorith
Summary:	Set of LaTeX macros for algorithms
Summary(pl.UTF-8):   Zestaw makr LaTeXa dla algorytmów
Name:		tetex-algorith
Version:	20050316
Release:	2
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
This package provides two environments, algorithmic and algorithm,
which are designed to be used together but may be used separately. The
algorithmic environment provides an environment for describing
algorithms and the algorithm environment provides a "float" wrapper
for algorithms (implemented using algorithmic or some other method at
the author's option). The reason that two environments are provided is
to allow the author maximum flexibility.

%description -l pl.UTF-8
Ten pakiet udostępnia dwa środowiska: algorithmic i algorithm, które
zostały zaprojektowane do wspólnego używania, ale można ich używać
osobno. Środowisko algorithmic umożliwia opisywanie algorytmów, a
algorithm jest "pływającym" środowiskiem do prezentowania algorytmów
(generowanych w środowisku algorithmic lub inną metodą). Powodem
istnienia dwóch środowisk jest pozostawienie autorom maksymalnej
swobody.

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
%{_datadir}/texmf/tex/latex/%{_short_name}
