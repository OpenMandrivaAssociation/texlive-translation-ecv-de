# revision 24754
# category Package
# catalog-ctan /info/translations/ecv/de
# catalog-date 2011-09-15 18:36:27 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-ecv-de
Version:	20110915
Release:	1
Summary:	German version of evc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/ecv/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-ecv-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-ecv-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the ecv documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.pdf
%doc %{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
