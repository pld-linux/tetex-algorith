%define	_short_name 	algorith
Summary:	Set of LaTeX macros for algorithms
Summary(pl):	Zestaw makr LaTeXa dla algorytmów
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

%description -l pl
Ten pakiet udostêpnia dwa ¶rodowiska: algorithmic i algorithm, które
zosta³y zaprojektowane do wspólnego u¿ywania, ale mo¿na ich u¿ywaæ
osobno. ¦rodowisko algorithmic umo¿liwia opisywanie algorytmów, a
algorithm jest "p³ywaj±cym" ¶rodowiskiem do prezentowania algorytmów
(generowanych w ¶rodowisku algorithmic lub inn± metod±). Powodem
istnienia dwóch ¶rodowisk jest pozostawienie autorom maksymalnej
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
%{_datadir}/texmf/tex/latex/%{_short_name}/*
