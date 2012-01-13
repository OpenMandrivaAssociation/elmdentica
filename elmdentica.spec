#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/elmdentica elmdentica; \
#cd elmdentica; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "elmdentica" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf elmdentica-$PKG_VERSION.tar.xz elmdentica/ --exclude .svn --exclude .*ignore

%define svnrev	66729

Summary:	A simple Identi.ca client with Elementary UI
Name:		elmdentica
Version:	0.9.10
Release:	0.%{svnrev}.1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	pkgconfig(azy)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(embryo)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(json-glib-1.0)

%description
A simple Identi.ca client with Elementary UI

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
rm -fr %{buildroot}
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/themes/default.edj

