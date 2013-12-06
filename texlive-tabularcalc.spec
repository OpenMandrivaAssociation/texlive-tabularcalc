# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tabularcalc
# catalog-date 2009-04-22 00:12:47 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-tabularcalc
Version:	0.2
Release:	3
Summary:	Calculate formulas in a tabular environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabularcalc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularcalc.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 756439
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719646
- texlive-tabularcalc
- texlive-tabularcalc
- texlive-tabularcalc

