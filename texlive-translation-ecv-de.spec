Name:		texlive-translation-ecv-de
Version:	24754
Release:	2
Summary:	German version of evc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/ecv/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-ecv-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-ecv-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the ecv documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.pdf
%doc %{_texmfdistdir}/doc/latex/translation-ecv-de/ecvde.dtx.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
