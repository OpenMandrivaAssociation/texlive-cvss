Name:		texlive-cvss
Version:	64985
Release:	2
Summary:	Compute and display CVSS base scores
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cvss
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Common Vulnerability Scoring System (CVSS) is an open
framework for communicating the characteristics and severity of
software vulnerabilities. CVSS consists of three metric groups:
Base, Temporal, and Environmental. This package allows the user
to compute CVSS3.1 base scores and use them in documents, i.e.
it only deals with the Base score. Temporal and Environental
scores will be part of a future release. More information can
be found at https://www.first.org/cvss/specification-document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cvss
%{_texmfdistdir}/tex/latex/cvss
%doc %{_texmfdistdir}/doc/latex/cvss

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
