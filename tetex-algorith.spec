%define	short_name 	algorith
Summary:	Set of LaTeX macros for algorithms
Summary(pl.UTF-8):	Zestaw makr LaTeXa dla algorytmów
Name:		tetex-algorith
Version:	20060603
Release:	1
License:	LGPL 2.1+
Group:		Applications/Publishing/TeX
Source0:	http://www.ctan.org/get/macros/latex/contrib/algorithms.zip
# Source0-md5:	1491fc0eacc3fb3653d1ef4b6f7fc796
BuildRequires:	tetex-latex
BuildRequires:	unzip
%requires_eq	tetex
%requires_eq	tetex-latex
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
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.tex *.pdf
%{_datadir}/texmf/tex/latex/%{short_name}
