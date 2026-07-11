%global tl_name tabularcalc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Calculate formulas in a tabular environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularcalc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Given a list of numbers and one (or more) formulas, the package offers
an easy syntax to build a table of values, i.e., a tabular in which the
first row contains the list of numbers, and the other rows contain the
calculated values of the formulas for each number of the list. The table
may be built either horizontally or vertically and is fully
customizable.

