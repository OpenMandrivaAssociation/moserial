%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Serial terminal for the Gnome desktop
Name:		moserial
Version:	3.0.20
Release:	1
Group:		Communications
License:	GPLv3+
URL:		http://live.gnome.org/moserial/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		moserial-3.0.2-str-fmt.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	rarian
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
Requires:	hicolor-icon-theme
Requires:	yelp

%description
Moserial is a clean, friendly gtk-based serial terminal for the Gnome
desktop. It is written in Vala for extra goodness.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog ChangeLog.pre-git NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/moserial.svg
%{_mandir}/man1/%{name}*
%{_datadir}/metainfo/moserial.appdata.xml
