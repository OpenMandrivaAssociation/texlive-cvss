%global tl_name cvss
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	Compute and display CVSS base scores
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cvss
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cvss.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Common Vulnerability Scoring System (CVSS) is an open framework for
communicating the characteristics and severity of software
vulnerabilities. CVSS consists of three metric groups: Base, Temporal,
and Environmental. This package allows the user to compute CVSS3.1 base
scores and use them in documents, i.e. it only deals with the Base
score. Temporal and Environmental scores will be part of a future
release. More information can be found at
https://www.first.org/cvss/specification-document.

