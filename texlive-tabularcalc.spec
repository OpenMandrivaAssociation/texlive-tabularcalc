Name:		texlive-tabularcalc
Version:	15878
Release:	2
Summary:	Calculate formulas in a tabular environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularcalc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Given a list of numbers and one (or more) formulas, the package
offers an easy syntax to build a table of values, i.e., a
tabular in which the first row contains the list of numbers,
and the other rows contain the calculated values of the
formulas for each number of the list. The table may be built
either horizontally or vertically and is fully customizable.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabularcalc/tabularcalc.sty
%doc %{_texmfdistdir}/doc/latex/tabularcalc/README
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_en.tex
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_fr.pdf
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_fr.tex
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_vn.pdf
%doc %{_texmfdistdir}/doc/latex/tabularcalc/tabularcalc_doc_vn.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
