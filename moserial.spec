%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	Serial terminal for the Gnome desktop
Name:		moserial
Version:	3.0.5
Release:	2
Group:		Communications
License:	GPLv3+
URL:		http://live.gnome.org/moserial/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		moserial-3.0.2-str-fmt.patch
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	rarian
Requires:	hicolor-icon-theme
Requires:	yelp

%description
Moserial is a clean, friendly gtk-based serial terminal for the Gnome
desktop. It is written in Vala for extra goodness.

%prep
%setup -q
%patch0 -p0 -b .strfmt

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-gnome

#for omf in %{buildroot}%{_datadir}/omf/*/*-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}.lang
#done

%files -f %{name}.lang
%doc AUTHORS ChangeLog ChangeLog.pre-git MAINTAINERS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Sun Jan 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.5-1
+ Revision: 769649
- imported package moserial

